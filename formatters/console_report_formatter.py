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

            self._print_requirement_summary(result)

            self._print_quality(result)

            self._print_ambiguity(result)

            self._print_improvement(result)

            self._print_risk(result)

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
        print(ConsoleReportFormatter.MAIN_SEPARATOR)
        print("QA COPILOT REQUIREMENT ANALYSIS")
        print(ConsoleReportFormatter.MAIN_SEPARATOR)
        print()

    @staticmethod
    def _print_section(
        title: str,
    ) -> None:
        """Print a section heading."""

        print(ConsoleReportFormatter.SECTION_SEPARATOR)
        print(title)
        print(ConsoleReportFormatter.SECTION_SEPARATOR)

    @staticmethod
    def _print_list(
        items: Iterable[str],
    ) -> None:
        """Print a bullet list."""

        items = list(items)

        if not items:

            print("Information not provided.")
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

        print(qa.verdict.value)
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

        if hasattr(level, "value"):
            level = level.value

        print(f"Ambiguity Level : {level}")

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


__all__ = [
    "ConsoleReportFormatter",
]