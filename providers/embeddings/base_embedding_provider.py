"""Abstract base class for embedding providers."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List


class BaseEmbeddingProvider(ABC):
    """Abstract interface for embedding providers."""

    @abstractmethod
    def generate_embedding(
        self,
        text: str,
    ) -> List[float]:
        """
        Generate an embedding vector for the supplied text.

        Args:
            text:
                Input text.

        Returns:
            Embedding vector.
        """
        raise NotImplementedError