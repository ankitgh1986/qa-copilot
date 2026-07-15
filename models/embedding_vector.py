"""Embedding vector model."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass(slots=True)
class EmbeddingVector:
    """Represents an embedding generated for a document chunk."""

    chunk_id: int

    text: str

    vector: List[float]


__all__ = [
    "EmbeddingVector",
]