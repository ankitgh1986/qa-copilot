"""Requirement risk assessment agent for QA Copilot."""

from __future__ import annotations

import logging

from agents.base_agent import BaseAgent
from models.requirement_context import RequirementContext
from models.risk_assessment import RiskAssessment
from prompts.risk_prompt import (
    get_requirement_risk_prompt,
)
from utils.risk_parser import RiskParser

logger = logging.getLogger(__name__)


class RiskAgent(BaseAgent):
    """Identify testing and implementation risks in a software requirement."""

    def evaluate(
        self,
        context: RequirementContext,
    ) -> RiskAssessment:
        """Evaluate the risks in a software requirement.

        Args:
            context:
                RequirementContext produced by the
                RequirementSummaryAgent.

        Returns:
            A populated RiskAssessment object.

        Raises:
            ValueError:
                If the requirement summary is empty.

            RuntimeError:
                If risk assessment fails.
        """

        summary = context.short_summary

        self._validate_input(summary)

        logger.info(
            "Starting requirement risk assessment "
            "(input_length=%d).",
            len(summary),
        )

        prompt = get_requirement_risk_prompt(
            summary,
        )

        logger.info(
            "Risk prompt generated successfully "
            "(prompt_length=%d).",
            len(prompt),
        )

        try:

            response = self._generate(prompt)

            logger.info(
                "Risk assessment received from LLM "
                "(response_length=%d).",
                len(response),
            )

            assessment = RiskParser.parse(
                response,
            )

            logger.info(
                "Risk assessment parsed successfully."
            )

            return assessment

        except Exception as exc:

            logger.exception(
                "Requirement risk assessment failed."
            )

            raise RuntimeError(
                "Failed to evaluate requirement risks."
            ) from exc


__all__ = ["RiskAgent"]