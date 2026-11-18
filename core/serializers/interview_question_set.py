
from rest_framework import serializers

from ..models import InterviewQuestionSet


class InterviewQuestionSetSerializer(
    serializers.ModelSerializer[InterviewQuestionSet]
):
    technical_questions = serializers.ListField(
        child=serializers.CharField(),
        read_only=True,
    )

    behavioral_questions = serializers.ListField(
        child=serializers.CharField(),
        read_only=True,
    )

    follow_up_questions = serializers.ListField(
        child=serializers.CharField(),
        read_only=True,
    )

    class Meta:  # pyright: ignore[reportIncompatibleVariableOverride]
        model = InterviewQuestionSet
        fields = "__all__"
        read_only_fields = (
            "id",
            "candidate",
            "job_position",
            "screening_result",
            "technical_questions",
            "behavioral_questions",
            "follow_up_questions",
            "generated_at",
        )
