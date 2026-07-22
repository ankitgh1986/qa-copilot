"""Parser for Test Case Generator responses."""

from __future__ import annotations

import json
import logging
from typing import Any

from models.test_case import TestCase
from models.test_case import TestCaseSuite
from models.test_case import TestStep

logger = logging.getLogger(__name__)


class TestCaseParser:
    """Parses LLM JSON response into TestCaseSuite."""

    def parse(self, response: str) -> TestCaseSuite:
        """
        Parse LLM response.

        Args:
            response: Raw JSON response from the LLM.

        Returns:
            Parsed TestCaseSuite object.

        Raises:
            ValueError: If parsing fails.
        """

        try:
            response = response.strip()

            # Remove Markdown code fences if the LLM wrapped the JSON.
            if response.startswith("```json"):
                response = response[7:]
            elif response.startswith("```"):
                response = response[3:]

            if response.endswith("```"):
                response = response[:-3]

            response = response.strip()

            data = json.loads(response)

            test_cases = []

            for tc in data.get("test_cases", []):

                steps = [
                    TestStep(
                        step_number=step.get("step_number", 0),
                        action=step.get("action", ""),
                        expected_result=step.get(
                            "expected_result",
                            "",
                        ),
                    )
                    for step in tc.get("test_steps", [])
                ]

                test_case = TestCase(
                    test_case_id=tc.get("test_case_id", ""),

                    title=tc.get("title", ""),
                    objective=tc.get("objective", ""),

                    module=tc.get("module", ""),
                    feature=tc.get("feature", ""),

                    requirement_reference=tc.get(
                        "requirement_reference",
                        "",
                    ),

                    acceptance_criteria_reference=tc.get(
                        "acceptance_criteria_reference",
                        [],
                    ),

                    business_rule_reference=tc.get(
                        "business_rule_reference",
                        [],
                    ),

                    priority=tc.get("priority", ""),
                    severity=tc.get("severity", ""),
                    risk=tc.get("risk", ""),

                    test_type=tc.get("test_type", ""),
                    execution_type=tc.get(
                        "execution_type",
                        "",
                    ),

                    automation_candidate=tc.get(
                        "automation_candidate",
                        False,
                    ),

                    automation_layer=tc.get(
                        "automation_layer",
                        "",
                    ),

                    preconditions=tc.get(
                        "preconditions",
                        [],
                    ),

                    test_data=tc.get(
                        "test_data",
                        [],
                    ),

                    test_steps=steps,

                    postconditions=tc.get(
                        "postconditions",
                        [],
                    ),

                    tags=tc.get(
                        "tags",
                        [],
                    ),
                )

                test_cases.append(test_case)

            return TestCaseSuite(
                feature_name=data.get(
                    "feature_name",
                    "",
                ),
                total_test_cases=data.get(
                    "total_test_cases",
                    len(test_cases),
                ),
                test_cases=test_cases,
            )

        except json.JSONDecodeError as exc:
            logger.exception("Invalid JSON returned by LLM.")
            raise ValueError(
                "LLM returned invalid JSON."
            ) from exc

        except Exception as exc:
            logger.exception(
                "Failed to parse test case response."
            )
            raise ValueError(
                "Unable to parse Test Case response."
            ) from exc
        