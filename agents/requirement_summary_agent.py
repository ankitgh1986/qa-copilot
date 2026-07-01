"""Requirement summary agent for QA Copilot."""

from __future__ import annotations

import logging
from typing import Optional

from agents.base_agent import BaseAgent
from models.requirement_context import RequirementContext
from prompts.summary_prompt import get_requirement_summary_prompt
from utils.summary_parser import SummaryParser

logger = logging.getLogger(__name__)


class RequirementSummaryAgent(BaseAgent):
    """Generate concise requirement summaries using an LLM."""

    def __init__(self, llm_client: Optional[LLMClient] = None) -> None:
        """Initialize the summary agent.

        Args:
            llm_client: Optional injected LLM client. If omitted, a new
                LLMClient instance is created.
        """
        super().__init__(llm_client=llm_client)

    def summarize(self, requirement: str) -> RequirementContext:
        """Generate a summary for the provided requirement.

        Args:
            requirement: The requirement text to summarize.

        Returns:
            A :class:`RequirementContext` populated from the LLM summary.

        Raises:
            ValueError: If the requirement is empty or whitespace.
            RuntimeError: If summary generation fails.
        """
        self._validate_input(requirement)
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
            summary = self._generate(prompt)
            logger.info(
                "Summary received from LLM (response_length=%d).",
                len(summary),
            )

            context: RequirementContext = SummaryParser.parse(summary)
            logger.info("Summary parsed successfully.")
            logger.info("RequirementContext created successfully.")

            return context
        except Exception as exc:
            logger.exception("Unexpected error during requirement summary generation.")
            raise RuntimeError("Failed to generate requirement summary.") from exc


__all__ = ["RequirementSummaryAgent"]
