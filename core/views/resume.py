
from typing import Any, cast

from drf_spectacular.utils import OpenApiRequest, extend_schema
from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers import ResumeSerializer


class ResumeUploadAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    @extend_schema(
        request=OpenApiRequest(
            request=ResumeSerializer,
            encoding={
                "file": {
                    "contentType": "application/pdf, application/vnd.openxmlformats-officedocument.wordprocessingml.document, text/plain",
                },
            },
        ),
        responses={201: ResumeSerializer},
    )
    def post(self, request: Request) -> Response:
        serializer = ResumeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        response_data = cast(dict[str, Any], cast(Any, serializer).data)

        return Response(
            response_data,
            status=status.HTTP_201_CREATED,
        )
