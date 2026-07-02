"""Domain model representing requirement quality assessment."""

from __future__ import annotations

from dataclasses import dataclass, field

from models.enums import RequirementVerdict


@dataclass(slots=True)
class QualityAssessment:
    """Represents the quality assessment of a software requirement."""

    overall_score: int
    completeness_score: int
    clarity_score: int
    testability_score: int
    consistency_score: int
    risk_coverage_score: int

    verdict: RequirementVerdict

    strengths: list[str] = field(default_factory=list)
    weaknesses: list[str] = field(default_factory=list)