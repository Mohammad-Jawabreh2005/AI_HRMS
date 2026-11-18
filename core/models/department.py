
from __future__ import annotations

from datetime import datetime

from django.db import models


class Department(models.Model):
    name: models.CharField[str, str] = models.CharField(
        max_length=150,
        unique=True,
    )

    description: models.TextField[str, str] = models.TextField(
        blank=True,
    )

    created_at: models.DateTimeField[datetime, datetime] = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ("name",)
        verbose_name = "Department"
        verbose_name_plural = "Departments"

    def __str__(self) -> str:
        return self.name
