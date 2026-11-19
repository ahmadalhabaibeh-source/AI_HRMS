from django.db import models

class InterviewQuestionSet(models.Model):

    candidate = models.ForeignKey('Candidate', on_delete=models.CASCADE)
    job_position = models.ForeignKey('JobPosition', on_delete=models.CASCADE)
    screening_result = models.ForeignKey('ScreeningResult',on_delete=models.CASCADE)    
    technical_questions = models.JSONField(default=list)
    behavioral_questions = models.JSONField(default=list)
    follow_up_questions = models.JSONField(default=list)
    generated_at = models.DateTimeField(auto_now_add=True)
    