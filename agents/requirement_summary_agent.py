"""Requirement summary agent for QA Copilot."""

from __future__ import annotations

import logging
from typing import Optional

from core.llm_client import LLMClient
from prompts.summary_prompt import get_requirement_summary_prompt

logger = logging.getLogger(__name__)


class RequirementSummaryAgent:
    """Generate concise requirement summaries using an LLM."""

    def __init__(self, llm_client: Optional[LLMClient] = None) -> None:
        """Initialize the summary agent.

        Args:
            llm_client: Optional injected LLM client. If omitted, a new
                LLMClient instance is created.
        """
        self._llm_client = llm_client or LLMClient()
        logger.info("RequirementSummaryAgent initialized successfully.")

    def summarize(self, requirement: str) -> str:
        """Generate a summary for the provided requirement.

        Args:
            requirement: The requirement text to summarize.

        Returns:
            The generated summary text.

        Raises:
            ValueError: If the requirement is empty or whitespace.
            RuntimeError: If summary generation fails.
        """
        if not isinstance(requirement, str) or not requirement.strip():
            logger.error("Requirement summary validation failed: input was empty.")
            raise ValueError("Requirement must be a non-empty string.")

        logger.info(
            "Generating requirement summary for input length=%d.",
            len(requirement),
        )

        prompt = get_requirement_summary_prompt(requirement)
        logger.info(
            "Summary prompt generated successfully (prompt_length=%d).",
            len(prompt),
        )

        try:
            logger.info("Sending prompt to LLM for requirement summary generation.")
            summary = self._llm_client.generate(prompt)
            logger.info(
                "Requirement summary received successfully (response_length=%d).",
                len(summary),
            )
            return summary
        except Exception as exc:
            logger.exception("Unexpected error during requirement summary generation.")
            raise RuntimeError("Failed to generate requirement summary.") from exc


__all__ = ["RequirementSummaryAgent"]
