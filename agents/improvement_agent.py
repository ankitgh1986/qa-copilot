"""Requirement improvement recommendation agent for QA Copilot."""

from __future__ import annotations

import logging

from agents.base_agent import BaseAgent
from models.improvement_assessment import ImprovementAssessment
from models.requirement_context import RequirementContext
from prompts.improvement_prompt import (
    get_requirement_improvement_prompt,
)
from utils.improvement_parser import ImprovementParser

logger = logging.getLogger(__name__)


class ImprovementAgent(BaseAgent):
    """Recommend improvements for a software requirement."""

    def evaluate(
        self,
        context: RequirementContext,
    ) -> ImprovementAssessment:
        """Generate improvement recommendations.

        Args:
            context:
                RequirementContext produced by the
                RequirementSummaryAgent.

        Returns:
            A populated ImprovementAssessment object.

        Raises:
            ValueError:
                If the requirement summary is empty.

            RuntimeError:
                If improvement generation fails.
        """

        summary = context.short_summary

        self._validate_input(summary)

        logger.info(
            "Starting improvement recommendation (input_length=%d).",
            len(summary),
        )

        prompt = get_requirement_improvement_prompt(
            summary
        )

        logger.info(
            "Improvement prompt generated successfully "
            "(prompt_length=%d).",
            len(prompt),
        )

        try:

            response = self._generate(prompt)

            logger.info(
                "Improvement recommendations received from LLM "
                "(response_length=%d).",
                len(response),
            )

            assessment = ImprovementParser.parse(
                response
            )

            logger.info(
                "Improvement recommendations parsed successfully."
            )

            return assessment

        except Exception as exc:

            logger.exception(
                "Requirement improvement generation failed."
            )

            raise RuntimeError(
                "Failed to generate improvement recommendations."
            ) from exc


__all__ = ["ImprovementAgent"]