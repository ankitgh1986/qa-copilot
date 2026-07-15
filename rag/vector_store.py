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

        self._index = None

        self._embeddings: List[EmbeddingVector] = []

        logger.info(
            "VectorStore initialized."
        )

    def add(
        self,
        embeddings: List[EmbeddingVector],
    ) -> None:
        """
        Add embeddings to the FAISS index.
        """

        if not embeddings:
            raise ValueError(
                "Embeddings cannot be empty."
            )

        dimension = len(
            embeddings[0].vector
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
            [e.vector for e in embeddings],
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
        Search similar embeddings.
        """

        if self._index is None:

            raise RuntimeError(
                "VectorStore is empty."
            )

        query = np.array(
            [query_vector],
            dtype=np.float32,
        )

        _, indices = self._index.search(
            query,
            top_k,
        )

        results: List[
            EmbeddingVector
        ] = []

        for idx in indices[0]:

            if idx != -1:

                results.append(
                    self._embeddings[idx]
                )

        logger.info(
            "Retrieved %d similar chunks.",
            len(results),
        )

        return results


__all__ = [
    "VectorStore",
]