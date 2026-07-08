"""Standalone tester for the RequirementQualityAgent."""

from __future__ import annotations

import logging

from agents.requirement_quality_agent import RequirementQualityAgent
from agents.requirement_summary_agent import RequirementSummaryAgent
from core.context_cache import ContextCache
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

        if ContextCache.exists():

            logger.info(
                "Loading RequirementContext from cache."
            )

            context = ContextCache.load()

        else:

            logger.info(
                "Generating RequirementContext."
            )

            summary_agent = RequirementSummaryAgent()

            context = summary_agent.summarize(
                document
            )

            ContextCache.save(
                context
            )

        logger.info(
            "Evaluating requirement quality."
        )

        quality_agent = RequirementQualityAgent()

        assessment = quality_agent.evaluate(
            context
        )

        print()
        print("=" * 50)
        print("QUALITY ASSESSMENT")
        print("=" * 50)

        print(
            f"Overall Score       : "
            f"{assessment.overall_score}"
        )

        print(
            f"Completeness Score  : "
            f"{assessment.completeness_score}"
        )

        print(
            f"Clarity Score       : "
            f"{assessment.clarity_score}"
        )

        print(
            f"Testability Score   : "
            f"{assessment.testability_score}"
        )

        print(
            f"Consistency Score   : "
            f"{assessment.consistency_score}"
        )

        print(
            f"Risk Coverage Score : "
            f"{assessment.risk_coverage_score}"
        )

        print()

        _print_list(
            "STRENGTHS",
            assessment.strengths,
        )

        _print_list(
            "WEAKNESSES",
            assessment.weaknesses,
        )

        print("=" * 40)
        print("VERDICT")
        print("=" * 40)

        print(
            assessment.verdict.value
        )

    except Exception as exc:

        logger.exception(
            "Quality agent execution failed."
        )

        print(f"\nError: {exc}")


if __name__ == "__main__":
    main()