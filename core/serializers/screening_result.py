
from dataclasses import fields

from ..models import ScreeningResult
from rest_framework import serializers

class ScreeningResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScreeningResult
        fields = [
            'candidate',
            'job_position',
            'score',
            'generated_at',
            'raw_report',
            'summary',
            'missing_skills',
            'strengths',
            'recommendation',
            'id',
    
        ]
        read_only_fields = fields
