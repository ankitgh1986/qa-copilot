"""Requirement ambiguity assessment agent for QA Copilot."""

from __future__ import annotations

import logging

from agents.base_agent import BaseAgent
from models.ambiguity_assessment import AmbiguityAssessment
from models.requirement_context import RequirementContext
from prompts.ambiguity_prompt import (
    get_requirement_ambiguity_prompt,
)
from utils.ambiguity_parser import AmbiguityParser

logger = logging.getLogger(__name__)


class AmbiguityAgent(BaseAgent):
    """Identify ambiguities in a software requirement."""

    def evaluate(
        self,
        context: RequirementContext,
    ) -> AmbiguityAssessment:
        """Evaluate requirement ambiguity.

        Args:
            context:
                RequirementContext produced by the
                RequirementSummaryAgent.

        Returns:
            A populated AmbiguityAssessment object.

        Raises:
            ValueError:
                If the requirement summary is empty.

            RuntimeError:
                If ambiguity evaluation fails.
        """

        summary = context.short_summary

        self._validate_input(summary)

        logger.info(
            "Starting ambiguity evaluation (input_length=%d).",
            len(summary),
        )

        prompt = get_requirement_ambiguity_prompt(summary)

        logger.info(
            "Ambiguity prompt generated successfully "
            "(prompt_length=%d).",
            len(prompt),
        )

        try:

            response = self._generate(prompt)

            logger.info(
                "Ambiguity assessment received from LLM "
                "(response_length=%d).",
                len(response),
            )

            assessment = AmbiguityParser.parse(response)

            logger.info(
                "Ambiguity assessment parsed successfully."
            )

            return assessment

        except Exception as exc:

            logger.exception(
                "Requirement ambiguity evaluation failed."
            )

            raise RuntimeError(
                "Failed to evaluate requirement ambiguity."
            ) from exc


__all__ = ["AmbiguityAgent"]