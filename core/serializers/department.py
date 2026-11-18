
from rest_framework import serializers

from ..models import Department


class DepartmentSerializer(serializers.ModelSerializer[Department]):
    class Meta:
        model = Department
        fields = "__all__"
        read_only_fields = ("id", "created_at")
