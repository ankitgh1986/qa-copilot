"""Data models for QA Copilot Test Case Generator."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


@dataclass(slots=True)
class TestStep:
    """Represents a single test execution step."""

    step_number: int
    action: str
    expected_result: str


@dataclass(slots=True)
class TestCase:
    """Represents a single software test case."""

    test_case_id: str

    title: str
    objective: str

    module: str
    feature: str

    requirement_reference: str

    priority: str
    severity: str
    risk: str

    test_type: str
    execution_type: str

    automation_candidate: bool
    automation_layer: str

    acceptance_criteria_reference: List[str] = field(default_factory=list)
    business_rule_reference: List[str] = field(default_factory=list)

    preconditions: List[str] = field(default_factory=list)
    test_data: List[str] = field(default_factory=list)

    test_steps: List[TestStep] = field(default_factory=list)

    postconditions: List[str] = field(default_factory=list)

    tags: List[str] = field(default_factory=list)


@dataclass(slots=True)
class TestCaseSuite:
    """Collection of generated test cases."""

    feature_name: str
    total_test_cases: int

    test_cases: List[TestCase] = field(default_factory=list)