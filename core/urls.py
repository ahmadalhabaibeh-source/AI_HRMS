from django.urls import path
from .views.department import DepartmentCreateAPIView
from .views.job_position import JobPositionCreateAPIView
from .views.candidate import CandidateCreateAPIView
from .views.resume import ResumeUploadAPIView
from .views.screening_result import ScreeningResultDetailAPIView
from .views.interview_question_set import InterviewQuestionSetDetailAPIView
urlpatterns = [
    path( 'departments/',DepartmentCreateAPIView.as_view(),name='department-create' ),
    path('job-positions/',JobPositionCreateAPIView.as_view(),name='job-position-create'),
    path('candidates/',CandidateCreateAPIView.as_view(),name='candidate-create'),
    path('resumes/',ResumeUploadAPIView.as_view(),name='resume-upload'),
    path('screening-results/<int:pk>/',ScreeningResultDetailAPIView.as_view(),name='screening-result-detail'),
path('interview-question-sets/<int:pk>/',InterviewQuestionSetDetailAPIView.as_view(),name='interview-question-set-detail'),
]