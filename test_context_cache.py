"""Standalone tester for the RequirementContext cache."""

from __future__ import annotations

import logging

from agents.requirement_summary_agent import RequirementSummaryAgent
from core.context_cache import ContextCache
from utils.file_reader import FileReader

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
)

logger = logging.getLogger(__name__)


def main() -> None:
    """Generate and cache a RequirementContext."""

    try:

        file_path = input(
            "Enter the requirement document path: "
        ).strip()

        if not file_path:
            print("No file path entered.")
            return

        logger.info(
            "Reading requirement document."
        )

        document = FileReader().read(
            file_path
        )

        logger.info(
            "Generating RequirementContext."
        )

        summary_agent = RequirementSummaryAgent()

        context = summary_agent.summarize(
            document
        )

        logger.info(
            "Saving RequirementContext."
        )

        ContextCache.save(
            context
        )

        print()
        print("=" * 50)
        print("CONTEXT CACHE")
        print("=" * 50)

        print("RequirementContext saved successfully.")

        print(
            f"Cache Exists : {ContextCache.exists()}"
        )

        print()

        logger.info(
            "Loading RequirementContext."
        )

        cached_context = ContextCache.load()

        print(
            "RequirementContext loaded successfully."
        )

        print()

        print("=" * 50)
        print("SHORT SUMMARY")
        print("=" * 50)

        print(
            cached_context.short_summary
        )

    except Exception as exc:

        logger.exception(
            "Context cache test failed."
        )

        print(f"\nError: {exc}")


if __name__ == "__main__":
    main()