
from typing import Any, cast

from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers import JobPositionSerializer


class JobPositionCreateAPIView(APIView):

    @extend_schema(
        request=JobPositionSerializer,
        responses={201: JobPositionSerializer},
    )
    def post(self, request: Request) -> Response:
        serializer = JobPositionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        response_data = cast(dict[str, Any], cast(Any, serializer).data)

        return Response(
            response_data,
            status=status.HTTP_201_CREATED,
        )
