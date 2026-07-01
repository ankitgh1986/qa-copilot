"""Standalone tester for the RequirementSummaryAgent."""

from __future__ import annotations

import logging

from agents.requirement_summary_agent import RequirementSummaryAgent
from utils.file_reader import FileReader

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
)
logger = logging.getLogger(__name__)


def main() -> None:
    """Run an independent test of the RequirementSummaryAgent."""
    try:
        file_path = input("Enter the requirement document path: ").strip()
        if not file_path:
            logger.warning("No file path entered.")
            print("No file path entered. Exiting.")
            return

        logger.info("Reading requirement document from %s.", file_path)
        document_text = FileReader().read(file_path)

        logger.info("Generating requirement summary.")
        agent = RequirementSummaryAgent()
        context = agent.summarize(document_text)

        def print_list(title: str, items: list[str]) -> None:
            print("========================================")
            print(title)
            print("========================================")
            if not items:
                print("Information not provided.")
            else:
                for it in items:
                    print(f"- {it}")

        print("========================================")
        print("BUSINESS GOAL")
        print("========================================")
        print(context.business_goal or "Information not provided.")

        print("========================================")
        print("PRIMARY ACTOR")
        print("========================================")
        print(context.primary_actor or "Information not provided.")

        print_list("SUPPORTING ACTORS", context.supporting_actors)
        print_list("MAIN FEATURES", context.main_features)
        print_list("BUSINESS CONSTRAINTS", context.business_constraints)
        print_list("EXTERNAL DEPENDENCIES", context.external_dependencies)

        print("========================================")
        print("SHORT SUMMARY")
        print("========================================")
        print(context.short_summary or "Information not provided.")

    except FileNotFoundError as exc:
        logger.exception("Requirement document not found.")
        print(f"Error: {exc}")
    except ValueError as exc:
        logger.exception("Invalid requirement input.")
        print(f"Error: {exc}")
    except RuntimeError as exc:
        logger.exception("Summary generation failed.")
        print(f"Error: {exc}")
    except Exception as exc:
        logger.exception("Unexpected error occurred.")
        print(f"Unexpected error: {exc}")


if __name__ == "__main__":
    main()
