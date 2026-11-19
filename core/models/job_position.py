

from django.db import models


class JobPosition(models.Model):
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    required_skills = models.JSONField(default=list)  # A list of skills
    created_at = models.DateTimeField(auto_now_add=True)
