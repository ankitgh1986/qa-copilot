"""RAG pipeline for QA Copilot."""

from __future__ import annotations

import logging
from typing import Optional

from providers.llm.base_provider import BaseLLMProvider
from providers.llm.gemini_provider import GeminiProvider
from rag.prompt_builder import PromptBuilder
from rag.retriever import Retriever

logger = logging.getLogger(__name__)


class RAGPipeline:
    """
    Retrieval-Augmented Generation pipeline.

    Responsible for:
        - Retrieving relevant knowledge
        - Building the final prompt
        - Sending the prompt to the LLM
    """

    def __init__(
        self,
        retriever: Retriever,
        llm_provider: Optional[BaseLLMProvider] = None,
    ) -> None:
        """
        Initialize the RAG pipeline.

        Args:
            retriever:
                Retriever used to fetch relevant chunks.

            llm_provider:
                LLM provider implementation.
        """

        self._retriever = retriever

        self._llm_provider = (
            llm_provider
            or GeminiProvider()
        )

        logger.info(
            "RAGPipeline initialized."
        )

    def generate(
        self,
        task: str,
        top_k: int = 3,
    ) -> str:
        """
        Generate an answer using RAG.

        Args:
            task:
                User task or question.

            top_k:
                Number of relevant chunks to retrieve.

        Returns:
            Generated response.
        """

        if not task.strip():
            raise ValueError(
                "Task cannot be empty."
            )

        logger.info(
            "Retrieving relevant context."
        )

        context = self._retriever.retrieve(
            query=task,
            top_k=top_k,
        )

        logger.info(
            "Building RAG prompt."
        )

        prompt = PromptBuilder.build(
            task=task,
            context=context,
        )

        logger.info(
            "Generating response using LLM."
        )

        response = self._llm_provider.generate(
            prompt
        )

        logger.info(
            "RAG pipeline completed successfully."
        )

        return response


__all__ = [
    "RAGPipeline",
]