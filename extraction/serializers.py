from rest_framework import serializers
from .models import ExtractionJob, ExtractionResult


class ExtractionResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtractionResult
        fields = ['id', 'external_id', 'data', 'created_at']


class ExtractionJobSerializer(serializers.ModelSerializer):
    results = ExtractionResultSerializer(many=True, read_only=True)
    class Meta:
        model = ExtractionJob
        fields = [
            'id',
            'status',
            'record_count',
            'start_time',
            'end_time',
            'error_message',
            'created_at',
            'results',
        ]
