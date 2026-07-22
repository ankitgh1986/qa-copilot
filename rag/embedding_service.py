"""Embedding service for QA Copilot."""

from __future__ import annotations

import logging
from typing import List, Optional

from models.embedding_vector import EmbeddingVector
from providers.embeddings.base_embedding_provider import (
    BaseEmbeddingProvider,
)
from providers.embeddings.gemini_embedding_provider import (
    GeminiEmbeddingProvider,
)

logger = logging.getLogger(__name__)


class EmbeddingService:
    """Generates embeddings for document chunks."""

    def __init__(
        self,
        provider: Optional[BaseEmbeddingProvider] = None,
    ) -> None:
        """
        Initialize the embedding service.

        Args:
            provider:
                Embedding provider implementation.
        """

        self._provider = (
            provider
            or GeminiEmbeddingProvider()
        )

        logger.info(
            "EmbeddingService initialized using %s.",
            self._provider.__class__.__name__,
        )

    def generate_query_embedding(
        self,
        query: str,
    ) -> List[float]:
        """
        Generate an embedding for a user query.

        Args:
            query:
                User search query.

        Returns:
            Query embedding vector.
        """

        if not isinstance(query, str):
            raise TypeError(
                "Query must be a string."
            )

        query = query.strip()

        if not query:
            raise ValueError(
                "Query cannot be empty."
            )

        return self._provider.generate_embedding(
            query
        )

    def generate_embeddings(
        self,
        chunks: List[str],
    ) -> List[EmbeddingVector]:
        """
        Generate embeddings for document chunks.

        Args:
            chunks:
                List of document chunks.

        Returns:
            List of EmbeddingVector objects.
        """

        if not chunks:
            raise ValueError(
                "Chunks cannot be empty."
            )

        if any(
            not isinstance(chunk, str) or not chunk.strip()
            for chunk in chunks
        ):
            raise ValueError(
                "Chunks cannot contain empty text."
            )

        embeddings: List[EmbeddingVector] = []

        for index, chunk in enumerate(chunks):

            vector = self._provider.generate_embedding(
                chunk
            )

            embeddings.append(
                EmbeddingVector(
                    # TODO:
                    # Replace index with KnowledgeChunk.id
                    # once KnowledgeChunkFactory is integrated.
                    chunk_id=index,
                    text=chunk,
                    vector=vector,
                )
            )

        logger.info(
            "Generated %d embedding vectors using %s.",
            len(embeddings),
            self._provider.__class__.__name__,
        )

        return embeddings


__all__ = [
    "EmbeddingService",
]