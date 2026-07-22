"""Knowledge source interface."""

from __future__ import annotations

from abc import ABC, abstractmethod

from knowledge.knowledge_document import KnowledgeDocument


class KnowledgeSource(ABC):
    """
    Base interface for all knowledge sources.

    A knowledge source provides one or more KnowledgeDocument
    objects to the QA Copilot knowledge repository.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Returns the display name of the knowledge source.
        """
        raise NotImplementedError

    @abstractmethod
    def load(self) -> list[KnowledgeDocument]:
        """
        Loads all knowledge documents from the source.

        Returns:
            A list of KnowledgeDocument instances.
        """
        raise NotImplementedError

    @abstractmethod
    def supports(self, query: str) -> bool:
        """
        Determines whether this knowledge source is relevant
        for the supplied query.

        Args:
            query: User query or requirement.

        Returns:
            True if the source should participate in retrieval.
        """
        raise NotImplementedError