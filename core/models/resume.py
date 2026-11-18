
from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from django.db import models

if TYPE_CHECKING:
    from .candidate import Candidate


class Resume(models.Model):
    candidate: models.ForeignKey[Candidate, Candidate] = models.ForeignKey(
        "core.Candidate",
        on_delete=models.CASCADE,
        related_name="resumes",
    )

    file: models.FileField = models.FileField(
        upload_to="resumes/",
    )

    uploaded_at: models.DateTimeField[datetime, datetime] = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ("-uploaded_at",)
        verbose_name = "Resume"
        verbose_name_plural = "Resumes"

    def __str__(self) -> str:
        return f"Resume - {self.candidate.full_name}"
