"""Factory for creating KnowledgeDocument instances."""

from __future__ import annotations

from datetime import datetime

from knowledge.enums import (
    Domain,
    KnowledgeCategory,
    KnowledgeSource,
    KnowledgeStatus,
    Technology,
)
from knowledge.knowledge_document import KnowledgeDocument


class KnowledgeDocumentFactory:
    """Creates KnowledgeDocument objects."""

    @staticmethod
    def create(
        *,
        title: str,
        content: str,
        category: KnowledgeCategory,
        source: KnowledgeSource,
        domains: list[Domain] | None = None,
        technologies: list[Technology] | None = None,
        tags: list[str] | None = None,
        author: str | None = None,
        version: str = "1.0",
        status: KnowledgeStatus = KnowledgeStatus.ACTIVE,
        metadata: dict[str, str] | None = None,
    ) -> KnowledgeDocument:
        """
        Creates a KnowledgeDocument with sensible defaults.
        """

        now = datetime.utcnow()

        return KnowledgeDocument(
            id=f"{title.lower().replace(' ', '_')}_{int(now.timestamp())}",
            title=title,
            content=content,
            category=category,
            source=source,
            domains=domains or [],
            technologies=technologies or [],
            tags=tags or [],
            author=author,
            version=version,
            status=status,
            created_at=now,
            updated_at=now,
            metadata=metadata or {},
        )