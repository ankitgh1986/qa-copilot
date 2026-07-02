"""Standalone tester for the RequirementQualityAgent."""

from __future__ import annotations

import logging

from agents.requirement_quality_agent import RequirementQualityAgent
from agents.requirement_summary_agent import RequirementSummaryAgent
from utils.file_reader import FileReader

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
)

logger = logging.getLogger(__name__)


def _print_list(title: str, items: list[str]) -> None:
    """Print a titled list section."""

    print("=" * 40)
    print(title)
    print("=" * 40)

    if not items:
        print("Information not provided.")
    else:
        for item in items:
            print(f"- {item}")

    print()


def main() -> None:
    """Run the Requirement Quality Agent."""

    try:
        file_path = input(
            "Enter the requirement document path: "
        ).strip()

        if not file_path:
            print("No file path entered.")
            return

        logger.info("Reading requirement document.")

        document = FileReader().read(file_path)

        logger.info("Generating requirement summary.")

        summary_agent = RequirementSummaryAgent()

        context = summary_agent.summarize(document)

        logger.info("Evaluating requirement quality.")

        quality_agent = RequirementQualityAgent()

        assessment = quality_agent.evaluate(
            context
        )

        print()
        print("=" * 50)
        print("QUALITY ASSESSMENT")
        print("=" * 50)

        print(f"Overall Score       : {assessment.overall_score}")
        print(f"Completeness Score  : {assessment.completeness_score}")
        print(f"Clarity Score       : {assessment.clarity_score}")
        print(f"Testability Score   : {assessment.testability_score}")
        print(f"Consistency Score   : {assessment.consistency_score}")
        print(f"Risk Coverage Score : {assessment.risk_coverage_score}")

        print()

        _print_list("STRENGTHS", assessment.strengths)

        _print_list("WEAKNESSES", assessment.weaknesses)

        print("=" * 40)
        print("VERDICT")
        print("=" * 40)

        print(assessment.verdict)

    except Exception as exc:
        logger.exception("Quality agent execution failed.")
        print(f"\nError: {exc}")


if __name__ == "__main__":
    main()