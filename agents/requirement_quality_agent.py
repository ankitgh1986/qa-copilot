"""Requirement quality assessment agent for QA Copilot."""

from __future__ import annotations

import logging

from agents.base_agent import BaseAgent
from models.quality_assessment import QualityAssessment
from models.requirement_context import RequirementContext
from prompts.quality_prompt import get_requirement_quality_prompt
from utils.quality_parser import QualityParser

logger = logging.getLogger(__name__)


class RequirementQualityAgent(BaseAgent):
    """Evaluate the quality of a software requirement.

    This agent evaluates the quality of a structured requirement
    summary and returns a populated QualityAssessment object.
    """

    def evaluate(
        self,
        context: RequirementContext,
    ) -> QualityAssessment:
        """Evaluate the quality of a requirement.

        Args:
            context:
                RequirementContext produced by the
                RequirementSummaryAgent.

        Returns:
            A populated QualityAssessment object.

        Raises:
            ValueError:
                If the requirement summary is empty.

            RuntimeError:
                If quality evaluation fails.
        """

        summary = context.short_summary

        self._validate_input(summary)

        logger.info(
            "Starting requirement quality evaluation (input_length=%d).",
            len(summary),
        )

        prompt = get_requirement_quality_prompt(summary)

        logger.info(
            "Quality prompt generated successfully (prompt_length=%d).",
            len(prompt),
        )

        try:
            response = self._generate(prompt)

            logger.info(
                "Quality assessment received from LLM (response_length=%d).",
                len(response),
            )

            assessment = QualityParser.parse(response)

            logger.info(
                "Quality assessment parsed successfully."
            )

            return assessment

        except Exception as exc:
            logger.exception(
                "Requirement quality evaluation failed."
            )

            raise RuntimeError(
                "Failed to evaluate requirement quality."
            ) from exc


__all__ = ["RequirementQualityAgent"]