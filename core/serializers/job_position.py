
from rest_framework import serializers

from ..models import JobPosition


class JobPositionSerializer(serializers.ModelSerializer[JobPosition]):
    department_name = serializers.CharField(
        source="department.name",
        read_only=True,
    )

    required_skills = serializers.ListField(
        child=serializers.CharField(
            allow_blank=False,
            trim_whitespace=True,
        ),
        required=False,
        allow_empty=True,
    )

    class Meta:  # pyright: ignore[reportIncompatibleVariableOverride]
        model = JobPosition
        fields = (
            "id",
            "department",
            "department_name",
            "title",
            "description",
            "required_skills",
            "created_at",
        )
        read_only_fields = ("id", "created_at")
