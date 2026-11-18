
from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from django.db import models

if TYPE_CHECKING:
    from .department import Department


class JobPosition(models.Model):
    department: models.ForeignKey[Department, Department] = models.ForeignKey(
        "core.Department",
        on_delete=models.PROTECT,
        related_name="job_positions",
    )

    title: models.CharField[str, str] = models.CharField(
        max_length=200,
    )

    description: models.TextField[str, str] = models.TextField(
        blank=True,
    )

    required_skills: models.JSONField = models.JSONField(
        default=list,
        blank=True,
    )

    created_at: models.DateTimeField[datetime, datetime] = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ("title",)
        verbose_name = "Job Position"
        verbose_name_plural = "Job Positions"

    def __str__(self) -> str:
        return self.title
