"""Standalone tester for the ImprovementAgent."""

from __future__ import annotations

import logging

from agents.improvement_agent import ImprovementAgent
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
    """Run the Improvement Agent."""

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
            "Generating improvement recommendations."
        )

        improvement_agent = ImprovementAgent()

        assessment = improvement_agent.evaluate(
            context
        )

        print()
        print("=" * 50)
        print("IMPROVEMENT ASSESSMENT")
        print("=" * 50)

        _print_list(
            "PRIORITY IMPROVEMENTS",
            assessment.priority_improvements,
        )

        _print_list(
            "RECOMMENDED REQUIREMENT UPDATES",
            assessment.requirement_updates,
        )

        _print_list(
            "EXPECTED IMPACT",
            assessment.expected_impact,
        )

        print("=" * 40)
        print("OVERALL RECOMMENDATION")
        print("=" * 40)

        print(
            assessment.overall_recommendation
        )

    except Exception as exc:

        logger.exception(
            "Improvement agent execution failed."
        )

        print(f"\nError: {exc}")


if __name__ == "__main__":
    main()