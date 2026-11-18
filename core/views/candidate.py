
from typing import Any, cast

from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers import CandidateSerializer


class CandidateCreateAPIView(APIView):

    @extend_schema(
        request=CandidateSerializer,
        responses={201: CandidateSerializer},
    )
    def post(self, request: Request) -> Response:
        serializer = CandidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        response_data = cast(dict[str, Any], cast(Any, serializer).data)

        return Response(
            response_data,
            status=status.HTTP_201_CREATED,
        )
