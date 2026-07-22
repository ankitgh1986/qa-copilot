"""Console report formatter for QA Copilot."""

from __future__ import annotations

import logging
from typing import Iterable

from core.requirement_analyzer import (
    RequirementAnalysisResult,
)

logger = logging.getLogger(__name__)


class ConsoleReportFormatter:
    """Render RequirementAnalysisResult to the console."""

    MAIN_SEPARATOR = "=" * 50
    SECTION_SEPARATOR = "=" * 40

    def format(
        self,
        result: RequirementAnalysisResult,
    ) -> None:
        """Print the complete requirement analysis report."""

        logger.info(
            "Formatting requirement analysis report."
        )

        try:

            self._print_header()

            self._print_requirement_summary(
                result
            )

            self._print_quality(
                result
            )

            self._print_ambiguity(
                result
            )

            self._print_improvement(
                result
            )

            self._print_risk(
                result
            )

            self._print_acceptance_criteria(
                result
            )

            self._print_test_design(
                result
            )

            self._print_test_cases(
                result
            )

            logger.info(
                "Console report generated successfully."
            )

        except Exception:

            logger.exception(
                "Failed to generate console report."
            )

            raise

    @staticmethod
    def _print_header() -> None:
        """Print report header."""

        print()
        print(
            ConsoleReportFormatter.MAIN_SEPARATOR
        )
        print(
            "QA COPILOT REQUIREMENT ANALYSIS"
        )
        print(
            ConsoleReportFormatter.MAIN_SEPARATOR
        )
        print()

    @staticmethod
    def _print_section(
        title: str,
    ) -> None:
        """Print a section heading."""

        print(
            ConsoleReportFormatter.SECTION_SEPARATOR
        )
        print(title)
        print(
            ConsoleReportFormatter.SECTION_SEPARATOR
        )

    @staticmethod
    def _print_list(
        items: Iterable[str],
    ) -> None:
        """Print a bullet list."""

        items = list(items)

        if not items:

            print(
                "Information not provided."
            )
            print()

            return

        for item in items:

            print(f"- {item}")

        print()

    def _print_requirement_summary(
        self,
        result: RequirementAnalysisResult,
    ) -> None:
        """Print requirement summary."""

        self._print_section(
            "REQUIREMENT SUMMARY"
        )

        print(
            result.context.short_summary
        )

        print()

    def _print_quality(
        self,
        result: RequirementAnalysisResult,
    ) -> None:
        """Print quality assessment."""

        qa = result.quality_assessment

        self._print_section(
            "QUALITY ASSESSMENT"
        )

        print(
            f"Overall Score       : {qa.overall_score}"
        )

        print(
            f"Completeness Score  : "
            f"{qa.completeness_score}"
        )

        print(
            f"Clarity Score       : "
            f"{qa.clarity_score}"
        )

        print(
            f"Testability Score   : "
            f"{qa.testability_score}"
        )

        print(
            f"Consistency Score   : "
            f"{qa.consistency_score}"
        )

        print(
            f"Risk Coverage Score : "
            f"{qa.risk_coverage_score}"
        )

        print()

        self._print_section(
            "STRENGTHS"
        )

        self._print_list(
            qa.strengths
        )

        self._print_section(
            "WEAKNESSES"
        )

        self._print_list(
            qa.weaknesses
        )

        self._print_section(
            "VERDICT"
        )

        print(
            qa.verdict.value
        )

        print()
    def _print_ambiguity(
        self,
        result: RequirementAnalysisResult,
    ) -> None:
        """Print ambiguity assessment."""

        aa = result.ambiguity_assessment

        self._print_section(
            "AMBIGUITY ASSESSMENT"
        )

        print(
            f"Ambiguity Score : {aa.ambiguity_score}"
        )

        level = aa.ambiguity_level

        if hasattr(
            level,
            "value",
        ):
            level = level.value

        print(
            f"Ambiguity Level : {level}"
        )

        print()

        self._print_section(
            "AMBIGUOUS TERMS"
        )

        self._print_list(
            aa.ambiguous_terms
        )

        self._print_section(
            "MISSING INFORMATION"
        )

        self._print_list(
            aa.missing_information
        )

        self._print_section(
            "UNDEFINED BUSINESS RULES"
        )

        self._print_list(
            aa.undefined_business_rules
        )

        self._print_section(
            "ASSUMPTIONS"
        )

        self._print_list(
            aa.assumptions
        )

        self._print_section(
            "CONFLICTING STATEMENTS"
        )

        self._print_list(
            aa.conflicting_statements
        )

        self._print_section(
            "SUMMARY"
        )

        print(
            aa.summary
        )

        print()

    def _print_improvement(
        self,
        result: RequirementAnalysisResult,
    ) -> None:
        """Print improvement assessment."""

        ia = result.improvement_assessment

        self._print_section(
            "IMPROVEMENT ASSESSMENT"
        )

        self._print_section(
            "PRIORITY IMPROVEMENTS"
        )

        self._print_list(
            ia.priority_improvements
        )

        self._print_section(
            "RECOMMENDED REQUIREMENT UPDATES"
        )

        self._print_list(
            ia.requirement_updates
        )

        self._print_section(
            "EXPECTED IMPACT"
        )

        self._print_list(
            ia.expected_impact
        )

        self._print_section(
            "OVERALL RECOMMENDATION"
        )

        print(
            ia.overall_recommendation
        )

        print()

    def _print_risk(
        self,
        result: RequirementAnalysisResult,
    ) -> None:
        """Print risk assessment."""

        ra = result.risk_assessment

        self._print_section(
            "RISK ASSESSMENT"
        )

        self._print_section(
            "HIGH RISKS"
        )

        self._print_list(
            ra.high_risks
        )

        self._print_section(
            "MEDIUM RISKS"
        )

        self._print_list(
            ra.medium_risks
        )

        self._print_section(
            "LOW RISKS"
        )

        self._print_list(
            ra.low_risks
        )

        self._print_section(
            "TESTING FOCUS AREAS"
        )

        self._print_list(
            ra.testing_focus_areas
        )

        self._print_section(
            "MITIGATION RECOMMENDATIONS"
        )

        self._print_list(
            ra.mitigation_recommendations
        )

        self._print_section(
            "OVERALL RISK LEVEL"
        )

        print(
            ra.overall_risk_level
        )

        print()

    def _print_acceptance_criteria(
        self,
        result: RequirementAnalysisResult,
    ) -> None:
        """Print generated acceptance criteria."""

        ac = result.acceptance_criteria

        self._print_section(
            "ACCEPTANCE CRITERIA"
        )

        if not ac.criteria:

            print(
                "Information not provided."
            )

            print()

            return

        for index, criterion in enumerate(
            ac.criteria,
            start=1,
        ):

            print(
                f"AC-{index:03d}"
            )

            print(
                criterion
            )

            print()


    def _print_test_design(
        self,
        result: RequirementAnalysisResult,
    ) -> None:
        """Print generated test design."""

        td = result.test_design

        self._print_section(
            "TEST DESIGN"
        )

        fields = [
            ("Domain", td.domain),
            ("Feature Name", td.feature_name),
            ("Business Goal", td.business_goal),
            ("Business Workflow", td.business_workflow),
            ("Coverage Strategy", td.coverage_strategy),
            ("Automation Strategy", td.automation_strategy),
        ]

        for label, value in fields:
            print(f"{label}:")
            print(value if value else "Information not provided.")
            print()

        sections = [
            ("Actors", td.actors),
            ("Business Rules", td.business_rules),
            ("Dependencies", td.dependencies),
            ("Integration Points", td.integration_points),
            ("Assumptions", td.assumptions),
            ("Test Objectives", td.test_objectives),
            ("Quality Attributes", td.quality_attributes),
            ("Functional Areas", td.functional_areas),
            ("Applicable Test Types", td.applicable_test_types),
            ("Test Data Requirements", td.test_data_requirements),
        ]

        for title, items in sections:
            self._print_section(title)
            self._print_list(items)

        self._print_section("IDENTIFIED RISKS")
        if not td.identified_risks:
            print("Information not provided.\n")
        else:
            for risk in td.identified_risks:
                print(f"Risk     : {risk.risk}")
                print(f"Category : {risk.category}")
                print(f"Impact   : {risk.impact}")
                print()

        self._print_section("AUTOMATION CANDIDATES")
        ac = td.automation_candidates

        self._print_section("API AUTOMATION")
        self._print_list(ac.api_automation)

        self._print_section("UI AUTOMATION")
        self._print_list(ac.ui_automation)

        self._print_section("PERFORMANCE AUTOMATION")
        self._print_list(ac.performance_automation)

        self._print_section("MANUAL EXPLORATORY")
        self._print_list(ac.manual_exploratory)



    def _print_test_cases(
        self,
        result: RequirementAnalysisResult,
    ) -> None:
        """Print generated test cases."""

        suite = result.test_cases

        self._print_section(
            "GENERATED TEST CASES"
        )

        print(
            f"Feature Name     : {suite.feature_name}"
        )
        print(
            f"Total Test Cases : {suite.total_test_cases}"
        )
        print()

        if not suite.test_cases:
            print(
                "Information not provided."
            )
            print()
            return

        for test_case in suite.test_cases:
            self._print_section(
                test_case.test_case_id
                or "TEST CASE"
            )

            print(
                f"Title                : {test_case.title}"
            )
            print(
                f"Objective            : {test_case.objective}"
            )
            print(
                f"Module               : {test_case.module}"
            )
            print(
                f"Feature              : {test_case.feature}"
            )
            print(
                "Requirement Reference: "
                f"{test_case.requirement_reference}"
            )
            print(
                f"Priority             : {test_case.priority}"
            )
            print(
                f"Severity             : {test_case.severity}"
            )
            print(
                f"Risk                 : {test_case.risk}"
            )
            print(
                f"Test Type            : {test_case.test_type}"
            )
            print(
                f"Execution Type       : {test_case.execution_type}"
            )
            print(
                "Automation Candidate : "
                f"{test_case.automation_candidate}"
            )
            print(
                "Automation Layer     : "
                f"{test_case.automation_layer}"
            )
            print()

            print("Acceptance Criteria References:")
            self._print_list(
                test_case.acceptance_criteria_reference
            )

            print("Business Rule References:")
            self._print_list(
                test_case.business_rule_reference
            )

            print("Preconditions:")
            self._print_list(
                test_case.preconditions
            )

            print("Test Data:")
            self._print_list(
                test_case.test_data
            )

            print("Test Steps:")

            if not test_case.test_steps:
                print(
                    "Information not provided."
                )
                print()
            else:
                for step in test_case.test_steps:
                    print(
                        f"{step.step_number}. "
                        f"{step.action}"
                    )
                    print(
                        "   Expected Result: "
                        f"{step.expected_result}"
                    )
                print()

            print("Postconditions:")
            self._print_list(
                test_case.postconditions
            )

            print("Tags:")
            self._print_list(
                test_case.tags
            )


__all__ = [
    "ConsoleReportFormatter",
]    