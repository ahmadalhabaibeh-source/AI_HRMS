
from django.contrib import admin

from .models import (
    Department,
    JobPosition,
    Candidate,
    Resume,
    ScreeningResult,
    InterviewQuestionSet,
)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)
    ordering = ('name',)


@admin.register(JobPosition)
class JobPositionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'department',
        'title',
        'description',
        'required_skills',
        'created_at',
    )
    list_filter = ('department',)
    search_fields = ('title', 'department__name')
    ordering = ('title',)


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email', 'phone', 'created_at')
    search_fields = ('full_name', 'email', 'phone')
    ordering = ('full_name',)


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('id', 'candidate', 'file', 'uploaded_at')
    search_fields = ('candidate__full_name', 'candidate__email')
    list_filter = ('uploaded_at',)
    ordering = ('-uploaded_at',)


@admin.register(ScreeningResult)
class ScreeningResultAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'candidate',
        'job_position',
        'score',
        'recommendation',
        'generated_at',
    )
    search_fields = (
        'candidate__full_name',
        'candidate__email',
        'job_position__title',
    )
    list_filter = ('recommendation', 'generated_at')
    ordering = ('-generated_at',)


@admin.register(InterviewQuestionSet)
class InterviewQuestionSetAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'candidate',
        'job_position',
        'screening_result',
        'generated_at',
    )
    search_fields = (
        'candidate__full_name',
        'candidate__email',
        'job_position__title',
    )
    list_filter = ('generated_at',)
    ordering = ('-generated_at',)
