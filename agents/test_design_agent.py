"""AI Test Design Agent."""

from __future__ import annotations

import logging

from agents.base_agent import BaseAgent
from models.test_design import TestDesign
from parsers.test_design_parser import TestDesignParser
from prompts.test_design_prompt import get_test_design_prompt

logger = logging.getLogger(__name__)


class TestDesignAgent(BaseAgent):
    """
    AI agent responsible for generating a Test Design
    from a software requirement.
    """

    def __init__(self) -> None:
        """Initialize the Test Design Agent."""

        super().__init__()
        self._parser = TestDesignParser()

    def analyze(
        self,
        requirement: str,
    ) -> TestDesign:
        """
        Generate the Test Design for a requirement.

        Args:
            requirement:
                Software requirement.

        Returns:
            Parsed TestDesign object.
        """

        self._validate_input(requirement)

        logger.info("Generating Test Design...")

        prompt = get_test_design_prompt(requirement)

        # Use BaseAgent's protected method
        response = self._generate(prompt)

        design = self._parser.parse(response)

        logger.info("Test Design generated successfully.")

        return design