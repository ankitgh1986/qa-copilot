"""AI agent responsible for generating Acceptance Criteria."""

from __future__ import annotations

import logging

from agents.base_agent import BaseAgent
from models.acceptance_criteria import AcceptanceCriteria
from models.requirement_context import RequirementContext
from prompts.acceptance_criteria_prompt import (
    get_acceptance_criteria_prompt,
)
from utils.acceptance_criteria_parser import (
    AcceptanceCriteriaParser,
)

logger = logging.getLogger(__name__)


class AcceptanceCriteriaAgent(BaseAgent):
    """Generate acceptance criteria from a RequirementContext."""

    def generate(
        self,
        context: RequirementContext,
    ) -> AcceptanceCriteria:
        """Generate acceptance criteria."""

        logger.info(
            "Starting acceptance criteria generation "
            "(input_length=%d).",
            len(context.short_summary),
        )

        prompt = get_acceptance_criteria_prompt(
            context.short_summary,
        )

        logger.info(
            "Acceptance Criteria prompt generated successfully "
            "(prompt_length=%d).",
            len(prompt),
        )

        response = self._generate(
            prompt,
        )

        logger.info(
            "Acceptance Criteria received from LLM "
            "(response_length=%d).",
            len(response),
        )

        criteria = AcceptanceCriteriaParser.parse(
            response,
        )

        logger.info(
            "Acceptance Criteria parsed successfully."
        )

        return criteria


__all__ = [
    "AcceptanceCriteriaAgent",
]