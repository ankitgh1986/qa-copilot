"""Prompt builder for summarizing requirements in QA Copilot."""

from __future__ import annotations


def get_requirement_summary_prompt(requirement: str) -> str:
    """Build a concise requirement summary prompt.

    Args:
        requirement: The requirement text to summarize.

    Returns:
        A prompt string instructing the AI to summarize the requirement.
    """
    return f"""
You are a Business Analyst. Your only responsibility is to summarize the provided requirement.
Do not score the requirement, identify risks, identify ambiguities, recommend improvements,
or generate test cases. Summarize only what is explicitly present.
If any information is unavailable, respond with: Information not provided.
Avoid hallucination and do not invent information.

Requirement:
{requirement}

Return only the following sections:
1. Business Goal
2. Primary Actor
3. Supporting Actors
4. Main Features
5. Business Constraints
6. External Dependencies
7. Short Summary
"""