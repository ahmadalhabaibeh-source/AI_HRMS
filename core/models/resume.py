from django.db import models
class Resume(models.Model):
    candidate = models.ForeignKey('Candidate', on_delete=models.CASCADE)
    file = models.FileField(upload_to='resumes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)