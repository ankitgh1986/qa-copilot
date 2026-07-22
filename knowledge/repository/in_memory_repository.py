"""Abstract repository for managing knowledge documents."""

from __future__ import annotations

from abc import ABC, abstractmethod

from knowledge.knowledge_document import KnowledgeDocument


class KnowledgeRepository(ABC):
    """
    Defines the contract for storing and retrieving knowledge
    documents.

    Concrete implementations may store documents in memory,
    databases, cloud storage, or vector databases.
    """

    @abstractmethod
    def add(self, document: KnowledgeDocument) -> None:
        """
        Adds a knowledge document to the repository.

        Args:
            document: Knowledge document to store.
        """

    @abstractmethod
    def get(self, document_id: str) -> KnowledgeDocument | None:
        """
        Retrieves a document by its unique identifier.

        Args:
            document_id: Unique document identifier.

        Returns:
            The matching KnowledgeDocument if found,
            otherwise None.
        """

    @abstractmethod
    def list(self) -> list[KnowledgeDocument]:
        """
        Returns all stored knowledge documents.

        Returns:
            List of KnowledgeDocument objects.
        """

    @abstractmethod
    def remove(self, document_id: str) -> bool:
        """
        Removes a document from the repository.

        Args:
            document_id: Unique document identifier.

        Returns:
            True if removed successfully,
            otherwise False.
        """

    @abstractmethod
    def exists(self, document_id: str) -> bool:
        """
        Checks whether a document exists.

        Args:
            document_id: Unique document identifier.

        Returns:
            True if the document exists.
        """

    @abstractmethod
    def count(self) -> int:
        """
        Returns the total number of stored documents.

        Returns:
            Number of documents.
        """

    @abstractmethod
    def clear(self) -> None:
        """
        Removes all documents from the repository.
        """