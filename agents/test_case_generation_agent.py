"""Test Case Generation Agent."""

from __future__ import annotations

import logging
from urllib import response

from agents.base_agent import BaseAgent
from models.test_case import TestCaseSuite
from parsers.test_case_parser import TestCaseParser
from prompts.test_case_prompt import TEST_CASE_PROMPT

logger = logging.getLogger(__name__)


class TestCaseGenerationAgent(BaseAgent):
    """Generates software test cases from requirements."""

    def __init__(self) -> None:
        """Initialize the Test Case Generation Agent."""

        super().__init__()
        self._parser = TestCaseParser()

    def analyze(
        self,
        requirement: str,
    ) -> TestCaseSuite:
        """
        Generate software test cases.

        Args:
            requirement: Requirement text.

        Returns:
            Generated TestCaseSuite.
        """

        logger.info("Generating software test cases.")

        prompt = TEST_CASE_PROMPT.format(
            requirement=requirement,
        )

        # Use the same provider method used by your existing agents.
        response = self._generate(
            prompt,
        )
        print("=" * 80)
        print("TEST CASE AGENT RAW RESPONSE")
        print("=" * 80)
        print(repr(response))
        print("=" * 80)
        logger.info("Parsing generated test cases.")

        suite = self._parser.parse(response)

        logger.info(
            "Generated %s test cases for feature '%s'.",
            suite.total_test_cases,
            suite.feature_name,
        )

        return suite