"""Standalone tester for the RiskAgent."""

from __future__ import annotations

import logging

from agents.requirement_summary_agent import RequirementSummaryAgent
from agents.risk_agent import RiskAgent
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
    """Run the Risk Agent."""

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

        logger.info(
            "Evaluating requirement risks."
        )

        risk_agent = RiskAgent()

        assessment = risk_agent.evaluate(
            context
        )

        print()
        print("=" * 50)
        print("RISK ASSESSMENT")
        print("=" * 50)

        _print_list(
            "HIGH RISKS",
            assessment.high_risks,
        )

        _print_list(
            "MEDIUM RISKS",
            assessment.medium_risks,
        )

        _print_list(
            "LOW RISKS",
            assessment.low_risks,
        )

        _print_list(
            "TESTING FOCUS AREAS",
            assessment.testing_focus_areas,
        )

        _print_list(
            "MITIGATION RECOMMENDATIONS",
            assessment.mitigation_recommendations,
        )

        print("=" * 40)
        print("OVERALL RISK LEVEL")
        print("=" * 40)

        print(
            assessment.overall_risk_level
        )

    except Exception as exc:

        logger.exception(
            "Risk agent execution failed."
        )

        print(f"\nError: {exc}")


if __name__ == "__main__":
    main()