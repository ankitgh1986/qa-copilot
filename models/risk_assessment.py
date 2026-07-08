"""Domain model representing requirement risk assessment."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class RiskAssessment:
    """Represents the risk assessment of a software requirement."""

    high_risks: list[str] = field(default_factory=list)

    medium_risks: list[str] = field(default_factory=list)

    low_risks: list[str] = field(default_factory=list)

    testing_focus_areas: list[str] = field(default_factory=list)

    mitigation_recommendations: list[str] = field(default_factory=list)

    overall_risk_level: str = ""