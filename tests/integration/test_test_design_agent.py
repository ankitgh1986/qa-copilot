"""Integration test for TestDesignAgent."""

from __future__ import annotations

from agents.test_design_agent import TestDesignAgent
from providers.llm.gemini_provider import GeminiProvider
from utils.file_reader import FileReader


def test_test_design_agent() -> None:
    """Verify that TestDesignAgent generates a valid TestDesign."""

    # Read requirement document
    reader = FileReader()
    requirement = reader.read("sample_inputs/bank_transfer_requirement.docx")

    assert requirement.strip(), "Requirement file is empty."

    # Initialize AI components
    agent = TestDesignAgent()

    # Generate test design
    design = agent.analyze(requirement)

    print("=" * 80)
    print("AI TEST DESIGN")
    print("=" * 80)

    print(f"Domain                 : {design.domain}")
    print(f"Feature                : {design.feature_name}")
    print(f"Business Goal          : {design.business_goal}")

    print("\nActors")
    print("-" * 80)
    for actor in design.actors:
        print(f"- {actor}")

    print("\nBusiness Workflow")
    print("-" * 80)
    for step in design.business_workflow:
        print(f"- {step}")

    print("\nBusiness Rules")
    print("-" * 80)
    for rule in design.business_rules:
        print(f"- {rule}")

    print("\nTest Objectives")
    print("-" * 80)
    for objective in design.test_objectives:
        print(f"- {objective}")

    print("\nQuality Attributes")
    print("-" * 80)
    for attribute in design.quality_attributes:
        print(f"- {attribute}")

    print("\nIdentified Risks")
    print("-" * 80)
    for risk in design.identified_risks:
        print(f"Risk      : {risk.risk}")
        print(f"Category  : {risk.category}")
        print(f"Impact    : {risk.impact}")
        print()

    print("\nAutomation Candidates")
    print("-" * 80)

    print(
        f"- API Automation Candidates: "
        f"{', '.join(design.automation_candidates.api_automation)}"
    )
    print(
        f"- UI Automation Candidates: "
        f"{', '.join(design.automation_candidates.ui_automation)}"
    )
    print(
        f"- Performance Automation Candidates: "
        f"{', '.join(design.automation_candidates.performance_automation)}"
    )
    print(
        f"- Manual Exploratory Areas: "
        f"{', '.join(design.automation_candidates.manual_exploratory)}"
    )

    print("\nAutomation Strategy")
    print("-" * 80)
    for strategy in design.automation_strategy:
        print(f"- {strategy}")

    # Assertions
    assert design.domain
    assert design.feature_name
    assert design.business_goal
    assert design.actors
    assert design.business_workflow
    assert design.business_rules
    assert design.test_objectives
    assert design.quality_attributes
    assert design.identified_risks
    assert design.automation_candidates
    assert design.automation_strategy

    print("\n✅ All TestDesignAgent assertions passed.")
    print("=" * 80)


if __name__ == "__main__":
    test_test_design_agent()