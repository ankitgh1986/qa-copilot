"""Data model for requirement context in QA Copilot."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class RequirementContext:
    """Structured representation of a software requirement.

    This model captures the essential business information extracted from a
    requirement document. It serves as the shared data model exchanged between
    AI agents within QA Copilot.

    The class intentionally contains no business logic and can be extended
    as additional agents are introduced.
    """

    business_goal: str = ""
    primary_actor: str = ""
    supporting_actors: list[str] = field(default_factory=list)
    main_features: list[str] = field(default_factory=list)
    business_constraints: list[str] = field(default_factory=list)
    external_dependencies: list[str] = field(default_factory=list)
    short_summary: str = ""