"""Standalone test for AcceptanceCriteriaAgent."""

from __future__ import annotations

import logging

from agents.acceptance_criteria_agent import (
    AcceptanceCriteriaAgent,
)
from core.context_cache import ContextCache

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
)

logger = logging.getLogger(__name__)


def main() -> None:
    """Execute Acceptance Criteria generation."""

    print("=" * 50)
    print("ACCEPTANCE CRITERIA GENERATION")
    print("=" * 50)

    logger.info(
        "Loading RequirementContext."
    )

    context = ContextCache.load()

    agent = AcceptanceCriteriaAgent()

    result = agent.generate(
        context,
    )

    print()

    if not result.criteria:

        print("No Acceptance Criteria generated.")
        return

    for index, criterion in enumerate(
        result.criteria,
        start=1,
    ):

        print(f"AC-{index:03d}")
        print(criterion)
        print()


if __name__ == "__main__":
    main()