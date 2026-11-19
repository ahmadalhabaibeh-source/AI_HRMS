
from ..models import JobPosition
from rest_framework import serializers
class JobPositionSerializer(serializers.ModelSerializer):

    department_name = serializers.CharField(
        source='department.name',
        read_only=True
    )

    class Meta:
        model = JobPosition
        fields = [
            'id',
            'department',
            'department_name',
            'title',
            'description',
            'required_skills',
            'created_at',
        ]

        read_only_fields = ['id', 'created_at']