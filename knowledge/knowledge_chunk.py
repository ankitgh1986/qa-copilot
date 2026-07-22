"""Knowledge chunk domain model."""

from __future__ import annotations

from dataclasses import dataclass, field

from knowledge.knowledge_document import KnowledgeDocument


@dataclass(slots=True)
class KnowledgeChunk:
    """
    Represents a retrievable chunk extracted from a knowledge document.
    """

    id: str

    document: KnowledgeDocument

    chunk_index: int

    content: str

    section: str | None = None

    metadata: dict[str, str] = field(default_factory=dict)