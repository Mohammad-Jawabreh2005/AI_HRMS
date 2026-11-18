
from __future__ import annotations

from io import BytesIO
from pathlib import Path
from typing import Any
from zipfile import BadZipFile, ZipFile

from django.core.files.uploadedfile import UploadedFile
from rest_framework import serializers

from ..models import Resume

MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB

ALLOWED_EXTENSIONS = {
    ".pdf",
    ".docx",
    ".txt",
}


class ResumeSerializer(serializers.ModelSerializer[Resume]):
    class Meta:  # pyright: ignore[reportIncompatibleVariableOverride]
        model = Resume
        fields = "__all__"
        read_only_fields = ("id", "uploaded_at")

    def validate_file(
        self,
        value: UploadedFile[Any],
    ) -> UploadedFile[Any]:

        # 1. Validate filename
        if not value.name:
            raise serializers.ValidationError(
                "The uploaded file must have a name."
            )

        extension = Path(value.name).suffix.lower()

        if extension not in ALLOWED_EXTENSIONS:
            raise serializers.ValidationError(
                "Only PDF, DOCX, and TXT files are allowed."
            )

        # 2. Validate file size
        if value.size == 0:
            raise serializers.ValidationError(
                "The uploaded file cannot be empty."
            )

        if value.size > MAX_FILE_SIZE:
            raise serializers.ValidationError(
                "File size must not exceed 10 MB."
            )

        # 3. Read file content
        try:
            content = value.read()
        except OSError as exc:
            raise serializers.ValidationError(
                "Unable to read the uploaded file."
            ) from exc
        finally:
            value.seek(0)

        # 4. Validate actual content
        if extension == ".pdf":
            self._validate_pdf(content)

        elif extension == ".docx":
            self._validate_docx(content)

        elif extension == ".txt":
            self._validate_txt(content)

        return value

    @staticmethod
    def _validate_pdf(content: bytes) -> None:
        if b"%PDF-" not in content[:1024]:
            raise serializers.ValidationError(
                "The uploaded file is not a valid PDF file."
            )

    @staticmethod
    def _validate_docx(content: bytes) -> None:
        try:
            with ZipFile(BytesIO(content)) as archive:
                required_files = {
                    "[Content_Types].xml",
                    "word/document.xml",
                }

                if not required_files.issubset(archive.namelist()):
                    raise serializers.ValidationError(
                        "The uploaded file is not a valid DOCX document."
                    )

                if archive.testzip() is not None:
                    raise serializers.ValidationError(
                        "The DOCX file is corrupted."
                    )

        except BadZipFile as exc:
            raise serializers.ValidationError(
                "The uploaded file is not a valid DOCX document."
            ) from exc

    @staticmethod
    def _validate_txt(content: bytes) -> None:
        try:
            content.decode("utf-8-sig")
        except UnicodeDecodeError as exc:
            raise serializers.ValidationError(
                "The TXT file must contain valid UTF-8 text."
            ) from exc
