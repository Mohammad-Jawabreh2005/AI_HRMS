
from django.contrib import admin

from .models import (
    Candidate,
    Department,
    InterviewQuestionSet,
    JobPosition,
    Resume,
    ScreeningResult,
)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):  # pyright: ignore[reportMissingTypeArgument]
    list_display = ("name", "created_at")
    search_fields = ("name",)


@admin.register(JobPosition)
class JobPositionAdmin(admin.ModelAdmin):  # pyright: ignore[reportMissingTypeArgument]
    list_display = ("title", "department", "created_at")
    list_filter = ("department",)
    search_fields = ("title", "department__name")


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):  # pyright: ignore[reportMissingTypeArgument]
    list_display = ("full_name", "email", "phone", "created_at")
    search_fields = ("full_name", "email", "phone")


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):  # pyright: ignore[reportMissingTypeArgument]
    list_display = ("candidate", "file", "uploaded_at")
    list_filter = ("uploaded_at",)
    search_fields = ("candidate__full_name", "candidate__email")


@admin.register(ScreeningResult)
class ScreeningResultAdmin(admin.ModelAdmin):  # pyright: ignore[reportMissingTypeArgument]
    list_display = (
        "candidate",
        "job_position",
        "score",
        "recommendation",
        "generated_at",
    )
    list_filter = ("recommendation", "job_position")
    search_fields = ("candidate__full_name", "job_position__title")


@admin.register(InterviewQuestionSet)
class InterviewQuestionSetAdmin(admin.ModelAdmin):  # pyright: ignore[reportMissingTypeArgument]
    list_display = (
        "candidate",
        "job_position",
        "screening_result",
        "generated_at",
    )
    list_filter = ("job_position",)
    search_fields = ("candidate__full_name", "job_position__title")
