
from rest_framework import serializers

from ..models import Candidate


class CandidateSerializer(serializers.ModelSerializer[Candidate]):
    class Meta:
        model = Candidate
        fields = "__all__"
        read_only_fields = ("id", "created_at")
