
from django.urls import path

from core.views.candidate import CandidateCreateAPIView
from core.views.department import DepartmentCreateAPIView
from core.views.interview_question_set import (
    InterviewQuestionSetDetailAPIView,
)
from core.views.job_position import JobPositionCreateAPIView
from core.views.resume import ResumeUploadAPIView
from core.views.screening_result import ScreeningResultDetailAPIView

app_name = "core_api"

urlpatterns = [
    path(
        "departments/",
        DepartmentCreateAPIView.as_view(),
        name="department-create",
    ),
    path(
        "job-positions/",
        JobPositionCreateAPIView.as_view(),
        name="job-position-create",
    ),
    path(
        "candidates/",
        CandidateCreateAPIView.as_view(),
        name="candidate-create",
    ),
    path(
        "resumes/",
        ResumeUploadAPIView.as_view(),
        name="resume-upload",
    ),
    path(
        "screening-results/<int:pk>/",
        ScreeningResultDetailAPIView.as_view(),
        name="screening-result-detail",
    ),
    path(
        "interview-question-sets/<int:pk>/",
        InterviewQuestionSetDetailAPIView.as_view(),
        name="interview-question-set-detail",
    ),
]
