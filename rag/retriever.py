"""Semantic retriever for QA Copilot."""

from __future__ import annotations

import logging
from typing import List

from models.embedding_vector import EmbeddingVector
from rag.embedding_service import EmbeddingService
from rag.vector_store import VectorStore

logger = logging.getLogger(__name__)


class Retriever:
    """Retrieve the most relevant embeddings."""

    def __init__(
        self,
        embedding_service: EmbeddingService,
        vector_store: VectorStore,
    ) -> None:
        """
        Initialize the retriever.

        Args:
            embedding_service:
                Service used to generate query embeddings.

            vector_store:
                Vector store used for semantic search.
        """

        self._embedding_service = (
            embedding_service
        )

        self._vector_store = (
            vector_store
        )

        logger.info(
            "Retriever initialized."
        )

    def retrieve(
        self,
        query: str,
        top_k: int = 3,
    ) -> List[EmbeddingVector]:
        """
        Retrieve the most relevant embeddings.

        Args:
            query:
                User query.

            top_k:
                Number of embeddings to retrieve.

        Returns:
            Matching embedding vectors.
        """

        if not query.strip():
            raise ValueError(
                "Query cannot be empty."
            )

        if top_k <= 0:
            raise ValueError(
                "top_k must be greater than zero."
            )

        query_vector = (
            self._embedding_service
            .generate_query_embedding(
                query
            )
        )

        results = (
            self._vector_store.search(
                query_vector=query_vector,
                top_k=top_k,
            )
        )

        logger.info(
            "Retrieved %d embeddings.",
            len(results),
        )

        return results


__all__ = [
    "Retriever",
]