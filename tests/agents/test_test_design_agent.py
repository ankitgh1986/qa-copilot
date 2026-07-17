"""Standalone test for TestDesignAgent."""

from __future__ import annotations

from agents.test_design_agent import TestDesignAgent


def main() -> None:
    """Run Test Design Agent test."""

    requirement = """
Feature: Internal Fund Transfer

Business Requirement:
A customer should be able to transfer funds between
their own accounts after successful authentication.

Business Rules:
1. Transfer amount must be greater than zero.
2. Source and destination accounts cannot be the same.
3. Daily transfer limit is ₹1,00,000.
4. OTP verification is mandatory.
5. Transfer should fail if balance is insufficient.
"""

    agent = TestDesignAgent()

    design = agent.analyze(requirement)

    print("\n" + "=" * 80)
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
        print(f"Risk      : {risk.get('risk')}")
        print(f"Category  : {risk.get('category')}")
        print(f"Impact    : {risk.get('impact')}")
        print()

    print("\nAutomation Candidates")
    print("-" * 80)
    for candidate in design.automation_candidates:
        print(f"- {candidate}")

    print("\nAutomation Strategy")
    print("-" * 80)
    for strategy in design.automation_strategy:
        print(f"- {strategy}")

    #
    # Basic validation
    #
    assert design.domain
    assert design.feature_name
    assert design.business_goal

    assert len(design.actors) > 0
    assert len(design.business_rules) > 0
    assert len(design.test_objectives) > 0
    assert len(design.quality_attributes) > 0
    assert len(design.identified_risks) > 0
    assert len(design.automation_candidates) > 0
    assert len(design.automation_strategy) > 0

    print("\n✅ All TestDesignAgent assertions passed.")
    print("=" * 80)


if __name__ == "__main__":
    main()