"""Abstract base class for knowledge ingestors."""

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path

from knowledge.knowledge_document import KnowledgeDocument


class KnowledgeIngestor(ABC):
    """Base class for all knowledge ingestors."""

    @property
    @abstractmethod
    def supported_extensions(self) -> tuple[str, ...]:
        """
        Returns the file extensions supported by this ingestor.
        Example: (".pdf",)
        """

    def can_ingest(self, file_path: Path) -> bool:
        """
        Returns True if this ingestor supports the given file.
        """
        return file_path.suffix.lower() in self.supported_extensions

    @abstractmethod
    def ingest(self, file_path: Path) -> list[KnowledgeDocument]:
        """
        Reads the file and returns one or more KnowledgeDocument objects.
        """