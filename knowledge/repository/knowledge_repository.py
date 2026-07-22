"""Abstract repository for managing knowledge documents."""

from __future__ import annotations

from abc import ABC, abstractmethod

from knowledge.knowledge_document import KnowledgeDocument


class KnowledgeRepository(ABC):
    """
    Defines the contract for storing and retrieving knowledge documents.

    Implementations may use in-memory storage, databases,
    vector databases, cloud storage, etc.
    """

    @abstractmethod
    def add(self, document: KnowledgeDocument) -> None:
        """
        Adds a knowledge document to the repository.
        """

    @abstractmethod
    def get(self, document_id: str) -> KnowledgeDocument | None:
        """
        Retrieves a document by its unique identifier.
        """

    @abstractmethod
    def list(self) -> list[KnowledgeDocument]:
        """
        Returns all knowledge documents.
        """

    @abstractmethod
    def remove(self, document_id: str) -> bool:
        """
        Removes a document from the repository.

        Returns:
            True if the document was removed.
            False if it was not found.
        """

    @abstractmethod
    def exists(self, document_id: str) -> bool:
        """
        Checks whether a document exists.
        """

    @abstractmethod
    def count(self) -> int:
        """
        Returns the total number of documents.
        """

    @abstractmethod
    def clear(self) -> None:
        """
        Removes all documents from the repository.
        """