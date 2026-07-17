"""Standalone test for TestDesignParser."""

from __future__ import annotations

from parsers.test_design_parser import TestDesignParser


def main() -> None:
    """Run standalone parser test."""

    response = """
{
    "domain": "Banking",
    "feature_name": "Internal Fund Transfer",
    "business_goal": "Enable customers to transfer funds.",

    "actors": [
        "Customer"
    ],

    "business_workflow": [
        "Select Source Account",
        "Select Destination Account"
    ],

    "business_rules": [
        "Amount should be positive"
    ],

    "dependencies": [
        "OTP Service"
    ],

    "integration_points": [
        "Account Service"
    ],

    "assumptions": [
        "Customer is authenticated"
    ],

    "test_objectives": [
        "Validate transfer"
    ],

    "quality_attributes": [
        "Security",
        "Performance"
    ],

    "identified_risks": [
        {
            "risk": "OTP Bypass",
            "category": "Security",
            "impact": "High",
            "recommended_testing": [
                "Security Testing"
            ]
        }
    ],

    "functional_areas": [
        "Fund Transfer"
    ],

    "applicable_test_types": [
        "Functional Testing"
    ],

    "coverage_strategy": [
        "Happy Path"
    ],

    "test_data_requirements": [
        "Valid User"
    ],

    "automation_candidates": [
        "API"
    ],

    "automation_strategy": [
        "API Automation"
    ]
}
"""

    parser = TestDesignParser()

    design = parser.parse(response)

    print("\n" + "=" * 80)
    print("TEST DESIGN PARSER")
    print("=" * 80)

    print(f"Domain              : {design.domain}")
    print(f"Feature             : {design.feature_name}")
    print(f"Business Goal       : {design.business_goal}")
    print(f"Actors              : {design.actors}")
    print(f"Objectives          : {design.test_objectives}")
    print(f"Quality Attributes  : {design.quality_attributes}")
    print(f"Number of Risks     : {len(design.identified_risks)}")

    print("\nFirst Risk")
    print("-" * 80)

    risk = design.identified_risks[0]

    print(f"Risk      : {risk['risk']}")
    print(f"Category  : {risk['category']}")
    print(f"Impact    : {risk['impact']}")

    #
    # Assertions
    #
    assert design.domain == "Banking"
    assert design.feature_name == "Internal Fund Transfer"
    assert (
        design.business_goal
        == "Enable customers to transfer funds."
    )

    assert len(design.actors) == 1
    assert len(design.business_workflow) == 2
    assert len(design.business_rules) == 1
    assert len(design.dependencies) == 1
    assert len(design.integration_points) == 1
    assert len(design.assumptions) == 1

    assert len(design.test_objectives) == 1
    assert len(design.quality_attributes) == 2
    assert len(design.identified_risks) == 1
    assert len(design.functional_areas) == 1
    assert len(design.applicable_test_types) == 1
    assert len(design.coverage_strategy) == 1
    assert len(design.test_data_requirements) == 1
    assert len(design.automation_candidates) == 1
    assert len(design.automation_strategy) == 1

    assert design.identified_risks[0]["risk"] == "OTP Bypass"
    assert design.identified_risks[0]["category"] == "Security"
    assert design.identified_risks[0]["impact"] == "High"

    print("\n✅ All parser assertions passed.")
    print("=" * 80)


if __name__ == "__main__":
    main()