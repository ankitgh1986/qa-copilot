"""Prompt builder for requirement summaries in QA Copilot."""

from __future__ import annotations


def get_requirement_summary_prompt(requirement: str) -> str:
    """Build a concise summary prompt for a requirement.

    Args:
        requirement: The requirement text to summarize.

    Returns:
        A prompt string instructing the AI to summarize the requirement.
    """
    return f"""
You are a Business Analyst. Your only responsibility is to summarize the provided requirement.
Do not score the requirement, identify risks, identify ambiguities, recommend improvements,
or generate test cases.
Summarize only what is explicitly present.
If any information is unavailable, respond with: Information not provided.
Avoid hallucination. Do not infer information.Do not assume missing details.; do not invent information.

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

Return plain text.

Do not use Markdown.

Do not use bullet points unless the section explicitly requires a list.

Do not include explanations outside the requested sections.
"""