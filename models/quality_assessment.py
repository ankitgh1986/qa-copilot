"""Data model representing the quality assessment of a software requirement."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class QualityAssessment:
    """Represents the quality evaluation of a software requirement.

    This model captures the structured output produced by the
    RequirementQualityAgent. It is intentionally free of business
    logic and serves as a domain object exchanged between AI agents.
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

    def is_ready_for_test_design(self) -> bool:
        """Return True if the requirement is ready for test design."""
        return self.verdict.upper() == "READY FOR TEST DESIGN"

    def __str__(self) -> str:
        """Return a readable string representation of the assessment."""
        return (
            f"Overall Score: {self.overall_score}\n"
            f"Completeness: {self.completeness_score}/30\n"
            f"Clarity: {self.clarity_score}/20\n"
            f"Testability: {self.testability_score}/20\n"
            f"Consistency: {self.consistency_score}/15\n"
            f"Risk Coverage: {self.risk_coverage_score}/15\n"
            f"Verdict: {self.verdict}"
        )