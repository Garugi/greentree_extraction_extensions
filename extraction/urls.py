from django.urls import path
from .views import (HealthCheckView,StartScanView,JobStatusView,JobResultView,CancelJobView,RemoveJobView,JobListView,JobStatisticsView,)

urlpatterns = [
    path("health", HealthCheckView.as_view(), name="health"),
    path("scan/start", StartScanView.as_view(), name="start-scan"),
    path("scan/status/<uuid:job_id>", JobStatusView.as_view(), name="job-status"),
    path("scan/result/<uuid:job_id>", JobResultView.as_view(), name="job-result"),
    path("scan/cancel/<uuid:job_id>", CancelJobView.as_view(), name="cancel-job"),
    path("scan/remove/<uuid:job_id>", RemoveJobView.as_view(), name="remove-job"),
    path("jobs/jobs", JobListView.as_view(), name="job-list"),
    path("jobs/statistics", JobStatisticsView.as_view(), name="job-statistics"),
]
