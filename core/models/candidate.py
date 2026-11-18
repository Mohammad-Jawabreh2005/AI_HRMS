
from __future__ import annotations

from datetime import datetime

from django.db import models


class Candidate(models.Model):
    full_name: models.CharField[str, str] = models.CharField(
        max_length=200,
    )

    email: models.EmailField[str, str] = models.EmailField(
        unique=True,
    )

    phone: models.CharField[str, str] = models.CharField(
        max_length=20,
        blank=True,
    )

    created_at: models.DateTimeField[datetime, datetime] = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ("full_name",)
        verbose_name = "Candidate"
        verbose_name_plural = "Candidates"

    def __str__(self) -> str:
        return self.full_name
