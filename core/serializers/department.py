from rest_framework import serializers
from ..models import Department
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields= [
            'name',
            'created_at',
             'id',
            'description',
        ]
        read_only_fields = ['created_at' ,'id']
