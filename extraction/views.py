from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.utils import timezone

from .models import ExtractionJob, ExtractionResult
from .serializers import ExtractionJobSerializer, ExtractionResultSerializer
from django.db.models import Count, Avg, DurationField, F, ExpressionWrapper

# Health Check
class HealthCheckView(APIView):
    def get(self, request):
        return Response({"status": "ok"}, status=status.HTTP_200_OK)


# Start Extraction Job
class StartScanView(APIView):
    def post(self, request):
        job = ExtractionJob.objects.create(
            status="PENDING",
            start_time=timezone.now()
        )
        return Response({"job_id": str(job.id)}, status=status.HTTP_202_ACCEPTED)


# Check Job Status
class JobStatusView(APIView):
    def get(self, request, job_id):
        job = get_object_or_404(ExtractionJob, id=job_id)
        serializer = ExtractionJobSerializer(job)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Get Job Results 
class JobResultView(APIView):
    def get(self, request, job_id):
        job = get_object_or_404(ExtractionJob, id=job_id)

        if job.status != "COMPLETED":
            return Response(
                {"detail": "Job not completed yet."},
                status=status.HTTP_409_CONFLICT
            )

        # Pagination
        limit = int(request.GET.get("limit", 20))
        offset = int(request.GET.get("offset", 0))

        results = job.results.all()[offset: offset + limit]
        serializer = ExtractionResultSerializer(results, many=True)

        return Response({
            "job_id": str(job.id),
            "count": job.results.count(),
            "results": serializer.data,
            "next_offset": offset + limit if offset + limit < job.results.count() else None
        })

class CancelJobView(APIView):
    def post(self, request, job_id):
        job = get_object_or_404(ExtractionJob, id=job_id)

        if job.status in ["COMPLETED", "FAILED", "CANCELLED"]:
            return Response(
                {"detail": "Job cannot be cancelled in its current state."},
                status=status.HTTP_409_CONFLICT
            )

        job.status = "CANCELLED"
        job.end_time = timezone.now()
        job.save()

        return Response(
            {"job_id": str(job.id), "status": "CANCELLED"},
            status=status.HTTP_200_OK
        )

class RemoveJobView(APIView):
    def delete(self, request, job_id):
        job = ExtractionJob.objects.filter(id=job_id).first()

        if not job:
            return Response(
                {"detail": "Job not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        job.results.all().delete()   # delete related results
        job.delete()                 # delete job itself

        return Response(status=status.HTTP_204_NO_CONTENT)
    
class JobListView(APIView):
    def get(self, request):
        limit = int(request.GET.get("limit", 20))
        offset = int(request.GET.get("offset", 0))

        jobs = ExtractionJob.objects.all().order_by("-created_at")
        total = jobs.count()

        serializer = ExtractionJobSerializer(jobs[offset:offset+limit], many=True)

        return Response({
            "count": total,
            "limit": limit,
            "offset": offset,
            "next_offset": offset + limit if offset + limit < total else None,
            "jobs": serializer.data
        })

class JobStatisticsView(APIView):
    def get(self, request):
        jobs = ExtractionJob.objects.all()

        stats = {
            "total_jobs": jobs.count(),
            "pending": jobs.filter(status="PENDING").count(),
            "in_progress": jobs.filter(status="IN_PROGRESS").count(),
            "completed": jobs.filter(status="COMPLETED").count(),
            "cancelled": jobs.filter(status="CANCELLED").count(),
            "failed": jobs.filter(status="FAILED").count(),
        }

        return Response(stats, status=status.HTTP_200_OK)
