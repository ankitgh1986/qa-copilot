"""Domain model representing requirement improvement recommendations."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class ImprovementAssessment:
    """Represents improvement recommendations for a software requirement."""

    priority_improvements: list[str] = field(default_factory=list)

    requirement_updates: list[str] = field(default_factory=list)

    expected_impact: list[str] = field(default_factory=list)

    overall_recommendation: str = ""