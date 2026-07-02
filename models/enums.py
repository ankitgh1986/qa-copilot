"""Common enumerations used across QA Copilot."""

from __future__ import annotations

from enum import Enum


class RequirementVerdict(str, Enum):
    """Overall requirement quality verdict."""

    READY_FOR_TEST_DESIGN = "READY FOR TEST DESIGN"
    NEEDS_CLARIFICATION = "NEEDS CLARIFICATION"


class AmbiguityLevel(str, Enum):
    """Overall ambiguity level."""

    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


__all__ = [
    "RequirementVerdict",
    "AmbiguityLevel",
]