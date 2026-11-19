from rest_framework import serializers
from ..models import Candidate
class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = [
        'full_name',
         'created_at',
         'email',
        'phone',
        'id',
        ]
        read_only_fields = ['created_at', 'id']