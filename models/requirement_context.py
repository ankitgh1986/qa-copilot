"""Data model for requirement context in QA Copilot."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from models.acceptance_criteria import AcceptanceCriteria
from models.ambiguity_assessment import AmbiguityAssessment
from models.improvement_assessment import ImprovementAssessment
from models.quality_assessment import QualityAssessment
from models.risk_assessment import RiskAssessment
from models.test_design import TestDesign
from models.test_case import TestCaseSuite


@dataclass(slots=True)
class RequirementContext:
    """
    Shared context exchanged between AI agents.

    The context is progressively enriched by each agent in the
    pipeline. Every downstream agent has access to both the
    original requirement document and the outputs of previous
    agents.
    """

    # ======================================================
    # Source Information
    # ======================================================

    source_document: str = ""

    requirement_text: str = ""

    # ======================================================
    # Requirement Summary
    # ======================================================

    business_goal: str = ""

    primary_actor: str = ""

    supporting_actors: list[str] = field(default_factory=list)

    main_features: list[str] = field(default_factory=list)

    business_constraints: list[str] = field(default_factory=list)

    external_dependencies: list[str] = field(default_factory=list)

    short_summary: str = ""

    # ======================================================
    # AI Analysis Results
    # ======================================================

    quality_assessment: Optional[
        QualityAssessment
    ] = None

    ambiguity_assessment: Optional[
        AmbiguityAssessment
    ] = None

    improvement_assessment: Optional[
        ImprovementAssessment
    ] = None

    risk_assessment: Optional[
        RiskAssessment
    ] = None

    acceptance_criteria: Optional[
        AcceptanceCriteria
    ] = None

    test_design: Optional[
        TestDesign
    ] = None

    test_cases: Optional[
        TestCaseSuite
    ] = None


__all__ = [
    "RequirementContext",
]