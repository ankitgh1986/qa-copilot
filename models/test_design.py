"""Test design model."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


@dataclass(slots=True)
class TestDesign:
    """
    Represents the complete QA reasoning for a software
    requirement. This acts as the blueprint for all downstream
    AI generators.
    """

    # ======================================================
    # Requirement Understanding
    # ======================================================

    domain: str = ""

    feature_name: str = ""

    business_goal: str = ""

    actors: List[str] = field(default_factory=list)

    business_workflow: List[str] = field(default_factory=list)

    business_rules: List[str] = field(default_factory=list)

    dependencies: List[str] = field(default_factory=list)

    integration_points: List[str] = field(default_factory=list)

    assumptions: List[str] = field(default_factory=list)

    # ======================================================
    # QA Analysis
    # ======================================================

    test_objectives: List[str] = field(default_factory=list)

    quality_attributes: List[str] = field(default_factory=list)

    identified_risks: List[str] = field(default_factory=list)

    functional_areas: List[str] = field(default_factory=list)

    applicable_test_types: List[str] = field(default_factory=list)

    coverage_strategy: List[str] = field(default_factory=list)

    test_data_requirements: List[str] = field(default_factory=list)

    # ======================================================
    # Automation Strategy
    # ======================================================

    automation_candidates: List[str] = field(default_factory=list)

    automation_strategy: List[str] = field(default_factory=list)


__all__ = [
    "TestDesign",
]