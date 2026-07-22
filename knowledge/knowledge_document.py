"""Knowledge document domain model."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime

from knowledge.enums import (
    Domain,
    KnowledgeCategory,
    KnowledgeSource,
    KnowledgeStatus,
    Technology,
)


@dataclass(slots=True)
class KnowledgeDocument:
    """
    Represents a knowledge document stored in the QA Copilot
    knowledge repository.
    """

    id: str
    title: str
    content: str

    category: KnowledgeCategory
    source: KnowledgeSource

    domains: list[Domain] = field(default_factory=list)
    technologies: list[Technology] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)

    author: str | None = None
    version: str = "1.0"

    status: KnowledgeStatus = KnowledgeStatus.ACTIVE

    created_at: datetime | None = None
    updated_at: datetime | None = None

    metadata: dict[str, str] = field(default_factory=dict)