
from typing import Any, cast

from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import InterviewQuestionSet
from ..serializers import InterviewQuestionSetSerializer


class InterviewQuestionSetDetailAPIView(APIView):

    @extend_schema(
        responses={200: InterviewQuestionSetSerializer},
    )
    def get(self, request: Request, pk: int) -> Response:
        question_set = get_object_or_404(
            InterviewQuestionSet,
            pk=pk,
        )

        serializer = InterviewQuestionSetSerializer(question_set)

        response_data = cast(
            dict[str, Any],
            cast(Any, serializer).data,
        )

        return Response(
            response_data,
            status=status.HTTP_200_OK,
        )
