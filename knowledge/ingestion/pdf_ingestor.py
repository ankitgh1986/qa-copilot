"""PDF knowledge ingestor."""

from __future__ import annotations

from pathlib import Path

from pypdf import PdfReader

from knowledge.enums import (
    Domain,
    KnowledgeCategory,
    KnowledgeSource,
    Technology,
)
from knowledge.factories.knowledge_document_factory import (
    KnowledgeDocumentFactory,
)
from knowledge.ingestion.knowledge_ingestor import KnowledgeIngestor


class PDFIngestor(KnowledgeIngestor):
    """Ingests PDF documents into the knowledge repository."""

    @property
    def supported_extensions(self) -> tuple[str, ...]:
        return (".pdf",)

    def ingest(self, file_path: Path):
        """
        Reads a PDF file and converts it into a KnowledgeDocument.
        """

        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        if not self.can_ingest(file_path):
            raise ValueError(
                f"Unsupported file type: {file_path.suffix}"
            )

        text = self._extract_text(file_path)

        document = KnowledgeDocumentFactory.create(
            title=file_path.stem,
            content=text,
            category=KnowledgeCategory.TESTING_TECHNIQUE,
            source=KnowledgeSource.EXTERNAL,
            domains=[Domain.UNIVERSAL],
            technologies=[Technology.GENERIC],
            metadata={
                "file_name": file_path.name,
                "file_path": str(file_path),
            },
        )

        return [document]

    @staticmethod
    def _extract_text(file_path: Path) -> str:
        """
        Extracts all text from the PDF.
        """
        reader = PdfReader(file_path)

        pages = []

        for page in reader.pages:
            text = page.extract_text() or ""
            pages.append(text)

        return "\n".join(pages)