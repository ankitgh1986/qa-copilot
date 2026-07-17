"""Test suite model."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List

from models.test_case import TestCase


@dataclass(slots=True)
class TestSuite:
    """
    Represents a collection of generated test cases.
    """

    title: str

    generated_by: str = "QA Copilot"

    requirement_name: str = ""

    total_test_cases: int = 0

    functional_count: int = 0

    negative_count: int = 0

    boundary_count: int = 0

    security_count: int = 0

    performance_count: int = 0

    api_count: int = 0

    ui_count: int = 0

    automation_candidates: int = 0

    test_cases: List[TestCase] = field(
        default_factory=list
    )


__all__ = [
    "TestSuite",
]