"""Entry point for the QA Copilot application."""

from __future__ import annotations

import logging

from agents.requirement_reviewer import RequirementReviewer
from utils.file_reader import FileReader

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
)
logger = logging.getLogger(__name__)


def main() -> None:
    """Run the QA Copilot workflow for reviewing a requirement document."""
    print("=========================================")
    print("QA COPILOT v1.0")
    print("AI Assistant for Software Test Engineers")
    print("=========================================")

    logger.info("QA Copilot application started.")

    file_path = input("Enter the requirement document path: ").strip()
    if not file_path:
        logger.warning("No file path provided by the user.")
        print("No file path provided. Exiting.")
        return

    try:
        logger.info("Initializing file reader and reviewer.")
        file_reader = FileReader()
        reviewer = RequirementReviewer()

        print("\nReading document...")
        requirement_text = file_reader.read(file_path)

        print("\nGenerating AI review...")
        review = reviewer.review(requirement_text)

        print("\nReview completed successfully.")
        print("\nGenerated Review:\n")
        print(review)

    except FileNotFoundError as exc:
        logger.exception("File could not be found.")
        print(f"Error: {exc}")
    except ValueError as exc:
        logger.exception("Invalid input provided.")
        print(f"Error: {exc}")
    except RuntimeError as exc:
        logger.exception("Runtime error while processing the requirement.")
        print(f"Error: {exc}")
    except Exception as exc:
        logger.exception("Unexpected error occurred.")
        print(f"Unexpected error: {exc}")


if __name__ == "__main__":
    main()
