"""Domain model representing requirement ambiguity assessment."""

from __future__ import annotations

from dataclasses import dataclass, field

from models.enums import AmbiguityLevel


@dataclass(slots=True)
class AmbiguityAssessment:
    """Represents the ambiguity assessment of a software requirement.

    Attributes:
        ambiguity_score:
            Overall ambiguity score ranging from 0 to 100.

        ambiguity_level:
            Overall ambiguity level.

        ambiguous_terms:
            Terms or phrases that are vague or open to interpretation.

        missing_information:
            Information required to fully understand or validate
            the requirement.

        undefined_business_rules:
            Business rules that are referenced but not sufficiently
            defined.

        assumptions:
            Implicit assumptions identified in the requirement.

        conflicting_statements:
            Statements that contradict one another.

        summary:
            Brief overall assessment of requirement ambiguity.
    """

    ambiguity_score: int

    ambiguity_level: AmbiguityLevel

    ambiguous_terms: list[str] = field(default_factory=list)

    missing_information: list[str] = field(default_factory=list)

    undefined_business_rules: list[str] = field(default_factory=list)

    assumptions: list[str] = field(default_factory=list)

    conflicting_statements: list[str] = field(default_factory=list)

    summary: str = ""