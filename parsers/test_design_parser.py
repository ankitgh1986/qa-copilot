"""Parser for AI-generated Test Design."""

from __future__ import annotations

import json
import logging

from models.test_design import (
    AutomationCandidates,
    Risk,
    TestDesign,
)

logger = logging.getLogger(__name__)


class TestDesignParser:
    """Parses AI generated Test Design JSON into TestDesign model."""

    def parse(
        self,
        response: str,
    ) -> TestDesign:
        """
        Parse LLM response into a TestDesign object.

        Args:
            response:
                Raw JSON response returned by the LLM.

        Returns:
            Parsed TestDesign.
        """

        if not response.strip():
            raise ValueError("Response cannot be empty.")

        try:
            cleaned = (
                response.replace("```json", "")
                .replace("```", "")
                .strip()
            )

            data = json.loads(cleaned)
            

            logger.info("Successfully parsed Test Design JSON.")

            # -----------------------------
            # Parse Risks
            # -----------------------------
            risks = [
                Risk(
                    risk=item.get("risk", ""),
                    category=item.get("category", ""),
                    impact=item.get("impact", ""),
                )
                for item in data.get("identified_risks", [])
            ]

            # -----------------------------
            # Parse Automation Candidates
            # -----------------------------
            automation = data.get("automation_candidates", {})

            automation_candidates = AutomationCandidates(
                api_automation=automation.get(
                    "api_automation_candidates",
                    automation.get("api_automation", []),
                ),
                ui_automation=automation.get(
                    "ui_automation_candidates",
                    automation.get("ui_automation", []),
                ),
                performance_automation=automation.get(
                    "performance_automation_candidates",
                    automation.get("performance_automation", []),
                ),
                manual_exploratory=automation.get(
                    "manual_exploratory_areas",
                    automation.get("manual_exploratory", []),
                ),
            )

            return TestDesign(
                domain=data.get("domain", ""),
                feature_name=data.get("feature_name", ""),
                business_goal=data.get("business_goal", ""),
                actors=data.get("actors", []),
                business_workflow=data.get("business_workflow", []),
                business_rules=data.get("business_rules", []),
                dependencies=data.get("dependencies", []),
                integration_points=data.get(
                    "integration_points",
                    [],
                ),
                assumptions=data.get("assumptions", []),
                test_objectives=data.get(
                    "test_objectives",
                    [],
                ),
                quality_attributes=data.get(
                    "quality_attributes",
                    [],
                ),
                identified_risks=risks,
                functional_areas=data.get(
                    "functional_areas",
                    [],
                ),
                applicable_test_types=data.get(
                    "applicable_test_types",
                    [],
                ),
                coverage_strategy=data.get(
                    "coverage_strategy",
                    [],
                ),
                test_data_requirements=data.get(
                    "test_data_requirements",
                    [],
                ),
                automation_candidates=automation_candidates,
                automation_strategy=data.get(
                    "automation_strategy",
                    [],
                ),
            )

        except json.JSONDecodeError as exc:
            logger.exception("Failed to parse Test Design JSON.")

            raise ValueError(
                "Invalid JSON returned by LLM."
            ) from exc