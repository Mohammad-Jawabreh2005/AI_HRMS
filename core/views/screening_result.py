
from typing import Any, cast

from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import ScreeningResult
from ..serializers import ScreeningResultSerializer


class ScreeningResultDetailAPIView(APIView):

    @extend_schema(
        responses={200: ScreeningResultSerializer},
    )
    def get(self, request: Request, pk: int) -> Response:
        screening_result = get_object_or_404(
            ScreeningResult,
            pk=pk,
        )

        serializer = ScreeningResultSerializer(screening_result)

        response_data = cast(dict[str, Any], cast(Any, serializer).data)

        return Response(
            response_data,
            status=status.HTTP_200_OK,
        )
