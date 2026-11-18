from typing import Any, cast

from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers import DepartmentSerializer


class DepartmentCreateAPIView(APIView):

    @extend_schema(
        request=DepartmentSerializer,
        responses={201: DepartmentSerializer},
    )
    def post(self, request: Request) -> Response:
        serializer = DepartmentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        response_data = cast(dict[str, Any], cast(Any, serializer).data)

        return Response(
            response_data,
            status=status.HTTP_201_CREATED,
        )