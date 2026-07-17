"""Prompt template for AI-powered Test Case Generation."""

from __future__ import annotations


def get_testcase_generation_prompt(
    requirement: str,
    test_design: str,
) -> str:
    """
    Build the prompt for generating detailed
    software test cases.

    Args:
        requirement:
            Original software requirement.

        test_design:
            AI generated Test Design.

    Returns:
        Prompt for the LLM.
    """

    return f"""
You are an experienced Senior Software Test Engineer.

The Test Design has already been completed by a QA Architect.

DO NOT perform business analysis again.

DO NOT identify risks again.

DO NOT redesign the test strategy.

Your responsibility is ONLY to convert the supplied Test Design
into detailed, high-quality software test cases.

===========================================================
Requirement
===========================================================

{requirement}

===========================================================
Approved Test Design
===========================================================

{test_design}

===========================================================
Instructions
===========================================================

Generate comprehensive test cases based ONLY on the
provided Test Design.

For every identified functional area and coverage strategy,
generate detailed software test cases.

Include

• Functional Test Cases

• Negative Test Cases

• Boundary Value Test Cases

• Equivalence Partition Test Cases

• Security Test Cases (if applicable)

• Performance Test Cases (if applicable)

• API Test Cases (if applicable)

• UI Test Cases (if applicable)

Generate multiple test cases wherever required.

===========================================================
Each Test Case Must Include
===========================================================

• Test Case ID

• Title

• Objective

• Priority (High / Medium / Low)

• Category

• Preconditions

• Test Steps

• Expected Result

• Automation Candidate (true / false)

===========================================================
Quality Guidelines
===========================================================

Every test case should

✓ Be atomic

✓ Test only one objective

✓ Have clear execution steps

✓ Have measurable expected results

✓ Be independent

✓ Be reusable

✓ Be automation friendly

===========================================================
Output Format
===========================================================

Return ONLY valid JSON.

Use the following structure.

{{
    "test_cases":
    [
        {{
            "test_case_id": "TC001",
            "title": "",
            "objective": "",
            "priority": "High",
            "category": "Functional",
            "automation_candidate": true,
            "preconditions": [],
            "test_steps": [],
            "expected_result": ""
        }}
    ]
}}

"""