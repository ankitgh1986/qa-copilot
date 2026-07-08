"""Entry point for the QA Copilot application."""

from __future__ import annotations

import logging

from core.requirement_analyzer import RequirementAnalyzer
from formatters.console_report_formatter import (
    ConsoleReportFormatter,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
)

logger = logging.getLogger(__name__)


def main() -> None:
    """Run the QA Copilot application."""

    print("=" * 50)
    print("QA COPILOT")
    print("AI Assistant for Software Test Engineers")
    print("=" * 50)

    logger.info(
        "QA Copilot application started."
    )

    document_path = input(
        "Enter the requirement document path: "
    ).strip()

    if not document_path:

        logger.warning(
            "No document path provided."
        )

        print(
            "No document path provided."
        )

        return

    try:

        analyzer = RequirementAnalyzer()

        result = analyzer.analyze(
            document_path
        )

        formatter = ConsoleReportFormatter()

        formatter.format(result)

    except FileNotFoundError as exc:

        logger.exception(
            "Requirement document not found."
        )

        print(f"\nError: {exc}")

    except ValueError as exc:

        logger.exception(
            "Invalid input."
        )

        print(f"\nError: {exc}")

    except RuntimeError as exc:

        logger.exception(
            "Requirement analysis failed."
        )

        print(f"\nError: {exc}")

    except Exception as exc:

        logger.exception(
            "Unexpected application error."
        )

        print(f"\nUnexpected Error: {exc}")


if __name__ == "__main__":
    main()