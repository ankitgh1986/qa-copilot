"""Prompt builder for RAG."""

from __future__ import annotations

from typing import List

from models.embedding_vector import EmbeddingVector
from rag.prompt_templates import (
    QUALITY_ANALYSIS_TEMPLATE,
)


class PromptBuilder:
    """Build prompts using retrieved context."""

    @staticmethod
    def build(
        task: str,
        context: List[EmbeddingVector],
    ) -> str:
        """
        Build a RAG prompt.

        Args:
            task:
                User task.

            context:
                Retrieved document chunks.

        Returns:
            Final prompt.
        """

        combined_context = "\n\n".join(
            chunk.text
            for chunk in context
        )

        return QUALITY_ANALYSIS_TEMPLATE.format(
            context=combined_context,
            task=task,
        )


__all__ = [
    "PromptBuilder",
]