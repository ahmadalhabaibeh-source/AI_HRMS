from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class ScreeningResult(models.Model):
    candidate = models.ForeignKey('Candidate', on_delete=models.CASCADE)
    job_position = models.ForeignKey('Jobposition', on_delete=models.CASCADE)
    strengths = models.TextField(blank=True, null=True)
    missing_skills = models.TextField(blank=True, null=True)
    recommendation = models.CharField(max_length=10, choices=[('proceed', 'Proceed'), ('hold', 'Hold'), ('reject', 'Reject')])
    summary = models.TextField(blank=True, null=True)
    raw_report = models.TextField(blank=True, null=True)
    generated_at = models.DateTimeField(auto_now_add=True)
    score = models.PositiveSmallIntegerField(
    validators=[MinValueValidator(0), MaxValueValidator(100)])