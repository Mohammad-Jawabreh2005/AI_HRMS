
from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from django.db import models
from django.db.models import Q

if TYPE_CHECKING:
    from .candidate import Candidate
    from .job_position import JobPosition


class ScreeningResult(models.Model):

    class Recommendation(models.TextChoices):
        PROCEED = "proceed", "Proceed"
        HOLD = "hold", "Hold"
        REJECT = "reject", "Reject"

    candidate: models.ForeignKey[Candidate, Candidate] = models.ForeignKey(
        "core.Candidate",
        on_delete=models.CASCADE,
        related_name="screening_results",
    )

    job_position: models.ForeignKey[JobPosition, JobPosition] = models.ForeignKey(
        "core.JobPosition",
        on_delete=models.PROTECT,
        related_name="screening_results",
    )

    score: models.PositiveSmallIntegerField[int, int] = (
        models.PositiveSmallIntegerField()
    )

    strengths: models.JSONField = models.JSONField(
        default=list,
        blank=True,
    )

    missing_skills: models.JSONField = models.JSONField(
        default=list,
        blank=True,
    )

    recommendation: models.CharField[str, str] = models.CharField(
        max_length=10,
        choices=Recommendation.choices,
    )

    summary: models.TextField[str, str] = models.TextField(
        blank=True,
    )

    raw_report: models.JSONField = models.JSONField(
        default=dict,
        blank=True,
    )

    generated_at: models.DateTimeField[datetime, datetime] = (
        models.DateTimeField(auto_now_add=True)
    )

    class Meta:
        ordering = ("-generated_at",)
        verbose_name = "Screening Result"
        verbose_name_plural = "Screening Results"
        constraints = (
            models.CheckConstraint(
                condition=Q(score__gte=0) & Q(score__lte=100),
                name="screening_score_between_0_and_100",
            ),
        )

    def __str__(self) -> str:
        return f"{self.candidate.full_name} - {self.score}"
