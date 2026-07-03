"""Standalone tester for the AmbiguityAgent."""

from __future__ import annotations

import logging

from agents.ambiguity_agent import AmbiguityAgent
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
    """Run the Ambiguity Agent."""

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

        logger.info("Evaluating requirement ambiguity.")

        ambiguity_agent = AmbiguityAgent()

        assessment = ambiguity_agent.evaluate(
            context
        )

        print()
        print("=" * 50)
        print("AMBIGUITY ASSESSMENT")
        print("=" * 50)

        print(
            f"Ambiguity Score : "
            f"{assessment.ambiguity_score}"
        )

        print(
            f"Ambiguity Level : "
            f"{assessment.ambiguity_level.value}"
        )

        print()

        _print_list(
            "AMBIGUOUS TERMS",
            assessment.ambiguous_terms,
        )

        _print_list(
            "MISSING INFORMATION",
            assessment.missing_information,
        )

        _print_list(
            "UNDEFINED BUSINESS RULES",
            assessment.undefined_business_rules,
        )

        _print_list(
            "ASSUMPTIONS",
            assessment.assumptions,
        )

        _print_list(
            "CONFLICTING STATEMENTS",
            assessment.conflicting_statements,
        )

        print("=" * 40)
        print("SUMMARY")
        print("=" * 40)

        print(assessment.summary)

    except Exception as exc:
        logger.exception(
            "Ambiguity agent execution failed."
        )

        print(f"\nError: {exc}")


if __name__ == "__main__":
    main()