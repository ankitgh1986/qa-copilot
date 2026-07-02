"""Data model representing the quality assessment of a software requirement."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class QualityAssessment:
    """Represents the quality evaluation of a requirement.

    This model captures the output of the RequirementQualityAgent.
    It is intentionally free of business logic and serves as a
    structured object exchanged between AI agents.
    """

    overall_score: int = 0
    completeness_score: int = 0
    clarity_score: int = 0
    testability_score: int = 0
    consistency_score: int = 0
    risk_coverage_score: int = 0

    strengths: list[str] = field(default_factory=list)
    weaknesses: list[str] = field(default_factory=list)

    verdict: str = ""