"""Common enumerations used across the QA Copilot domain models."""

from __future__ import annotations

from enum import Enum


class AmbiguityLevel(str, Enum):
    """Represents the ambiguity level of a requirement."""

    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


class RequirementVerdict(str, Enum):
    """Represents the overall requirement quality verdict."""

    READY_FOR_TEST_DESIGN = "READY FOR TEST DESIGN"
    NEEDS_CLARIFICATION = "NEEDS CLARIFICATION"


__all__ = [
    "AmbiguityLevel",
    "RequirementVerdict",
]