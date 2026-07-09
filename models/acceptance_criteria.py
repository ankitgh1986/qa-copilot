"""Domain model representing generated acceptance criteria."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class AcceptanceCriteria:
    """Acceptance criteria generated from a requirement."""

    criteria: list[str] = field(default_factory=list)


__all__ = [
    "AcceptanceCriteria",
]