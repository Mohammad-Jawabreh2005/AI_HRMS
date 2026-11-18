
from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from django.db import models

if TYPE_CHECKING:
    from .candidate import Candidate
    from .job_position import JobPosition
    from .screening_result import ScreeningResult


class InterviewQuestionSet(models.Model):

    candidate: models.ForeignKey[Candidate, Candidate] = models.ForeignKey(
        "core.Candidate",
        on_delete=models.CASCADE,
        related_name="interview_question_sets",
    )

    job_position: models.ForeignKey[JobPosition, JobPosition] = models.ForeignKey(
        "core.JobPosition",
        on_delete=models.PROTECT,
        related_name="interview_question_sets",
    )

    screening_result: models.ForeignKey[
        ScreeningResult, ScreeningResult
    ] = models.ForeignKey(
        "core.ScreeningResult",
        on_delete=models.PROTECT,
        related_name="interview_question_sets",
    )

    technical_questions: models.JSONField = models.JSONField(
        default=list,
        blank=True,
    )

    behavioral_questions: models.JSONField = models.JSONField(
        default=list,
        blank=True,
    )

    follow_up_questions: models.JSONField = models.JSONField(
        default=list,
        blank=True,
    )

    generated_at: models.DateTimeField[datetime, datetime] = (
        models.DateTimeField(auto_now_add=True)
    )

    class Meta:
        ordering = ("-generated_at",)
        verbose_name = "Interview Question Set"
        verbose_name_plural = "Interview Question Sets"

    def __str__(self) -> str:
        return f"Interview Questions - {self.candidate.full_name}"
