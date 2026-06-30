"""Utility for reading requirement documents and extracting plain text."""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Final

from docx import Document
from pypdf import PdfReader

logger = logging.getLogger(__name__)

SUPPORTED_EXTENSIONS: Final[set[str]] = {".txt", ".md", ".docx", ".pdf"}


class FileReader:
    """Read text-based requirement documents from supported file formats."""

    def __init__(self) -> None:
        """Initialize the file reader."""
        self.logger = logger
        self.logger.info("FileReader initialized successfully.")

    def read(self, file_path: str) -> str:
        """Read text from a supported file and return the extracted content.

        Args:
            file_path: Path to the file to read.

        Returns:
            The extracted text content as a string.

        Raises:
            FileNotFoundError: If the file does not exist.
            ValueError: If the file extension is not supported.
        """
        path = Path(file_path)
        self.logger.info("File selected for reading: %s", path)

        if not path.exists():
            logger.error("File not found: %s", path)
            raise FileNotFoundError(f"File not found: {path}")

        if not path.is_file():
            logger.error("Path is not a file: %s", path)
            raise FileNotFoundError(f"Path is not a file: {path}")

        extension = path.suffix.lower()
        if extension not in SUPPORTED_EXTENSIONS:
            logger.error("Unsupported file extension: %s", extension)
            raise ValueError(f"Unsupported file extension: {extension}")

        self.logger.info("Detected file type: %s", extension)

        try:
            if extension == ".txt":
                text = self._read_txt(path)
            elif extension == ".md":
                text = self._read_md(path)
            elif extension == ".docx":
                text = self._read_docx(path)
            else:
                text = self._read_pdf(path)
        except Exception as exc:
            self.logger.exception("Failed to extract text from file: %s", path)
            raise RuntimeError(f"Failed to extract text from file: {path}") from exc

        cleaned_text = "\n".join(part.strip() for part in text.splitlines() if part.strip())
        self.logger.info("Successfully extracted text from file: %s", path)
        return cleaned_text

    def _read_txt(self, path: Path) -> str:
        """Read plain text from a .txt file."""
        with path.open("r", encoding="utf-8") as file_handle:
            return file_handle.read()

    def _read_md(self, path: Path) -> str:
        """Read plain text from a Markdown file."""
        with path.open("r", encoding="utf-8") as file_handle:
            return file_handle.read()

    def _read_docx(self, path: Path) -> str:
        """Read plain text from a DOCX file."""
        document = Document(path)
        paragraphs = [paragraph.text for paragraph in document.paragraphs]
        return "\n".join(paragraphs)

    def _read_pdf(self, path: Path) -> str:
        """Read plain text from a PDF file."""
        reader = PdfReader(str(path))
        pages = [page.extract_text() or "" for page in reader.pages]
        return "\n".join(pages)


__all__ = ["FileReader"]
