"""FAISS vector store for QA Copilot."""

from __future__ import annotations

import logging
from typing import List

import faiss
import numpy as np

from models.embedding_vector import EmbeddingVector

logger = logging.getLogger(__name__)


class VectorStore:
    """
    In-memory FAISS vector store.
    """

    def __init__(self) -> None:
        """Initialize the vector store."""

        self._index = None
        self._embeddings: List[EmbeddingVector] = []

        logger.info(
            "VectorStore initialized."
        )

    @property
    def count(self) -> int:
        """
        Return the number of stored embeddings.
        """

        return len(self._embeddings)

    def clear(self) -> None:
        """
        Clear the vector store.
        """

        self._index = None
        self._embeddings.clear()

        logger.info(
            "VectorStore cleared."
        )

    def add(
        self,
        embeddings: List[EmbeddingVector],
    ) -> None:
        """
        Add embeddings to the FAISS index.

        Args:
            embeddings:
                Embedding vectors to store.
        """

        if not embeddings:
            raise ValueError(
                "Embeddings cannot be empty."
            )

        if any(
            not embedding.vector
            for embedding in embeddings
        ):
            raise ValueError(
                "Embedding vectors cannot be empty."
            )

        dimension = len(
            embeddings[0].vector
        )

        if any(
            len(embedding.vector) != dimension
            for embedding in embeddings
        ):
            raise ValueError(
                "All embeddings must have the same dimension."
            )

        if self._index is None:

            self._index = faiss.IndexFlatL2(
                dimension
            )

            logger.info(
                "Created FAISS index (dimension=%d).",
                dimension,
            )

        vectors = np.array(
            [embedding.vector for embedding in embeddings],
            dtype=np.float32,
        )

        self._index.add(
            vectors,
        )

        self._embeddings.extend(
            embeddings,
        )

        logger.info(
            "Added %d embeddings to FAISS.",
            len(embeddings),
        )

    def search(
        self,
        query_vector: List[float],
        top_k: int = 3,
    ) -> List[EmbeddingVector]:
        """
        Search for similar embeddings.

        Args:
            query_vector:
                Query embedding vector.

            top_k:
                Number of results to retrieve.

        Returns:
            List of similar embedding vectors.
        """

        if self._index is None:
            raise RuntimeError(
                "VectorStore is empty."
            )

        if not query_vector:
            raise ValueError(
                "Query vector cannot be empty."
            )

        if top_k <= 0:
            raise ValueError(
                "top_k must be greater than zero."
            )

        query = np.array(
            [query_vector],
            dtype=np.float32,
        )

        _, indices = self._index.search(
            query,
            top_k,
        )

        results: List[EmbeddingVector] = []

        for idx in indices[0]:

            if idx != -1:

                results.append(
                    self._embeddings[idx]
                )

        logger.info(
            "Retrieved %d similar embeddings.",
            len(results),
        )

        return results


__all__ = [
    "VectorStore",
]