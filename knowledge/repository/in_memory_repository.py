"""In-memory implementation of the Knowledge Repository."""

from __future__ import annotations

from knowledge.knowledge_document import KnowledgeDocument
from knowledge.repository.knowledge_repository import KnowledgeRepository


class InMemoryKnowledgeRepository(KnowledgeRepository):
    """
    Stores knowledge documents in memory.

    This implementation is intended for development,
    testing, and prototyping.
    """

    def __init__(self) -> None:
        self._documents: dict[str, KnowledgeDocument] = {}

    def add(self, document: KnowledgeDocument) -> None:
        """
        Adds or updates a knowledge document.
        """
        self._documents[document.id] = document

    def get(self, document_id: str) -> KnowledgeDocument | None:
        """
        Retrieves a document by ID.
        """
        return self._documents.get(document_id)

    def list(self) -> list[KnowledgeDocument]:
        """
        Returns all stored documents.
        """
        return list(self._documents.values())

    def remove(self, document_id: str) -> bool:
        """
        Removes a document by ID.
        """
        if document_id not in self._documents:
            return False

        del self._documents[document_id]
        return True

    def exists(self, document_id: str) -> bool:
        """
        Checks whether a document exists.
        """
        return document_id in self._documents

    def count(self) -> int:
        """
        Returns the total number of documents.
        """
        return len(self._documents)

    def clear(self) -> None:
        """
        Removes all documents.
        """
        self._documents.clear()