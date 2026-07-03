"""Common parsing utilities for QA Copilot parsers."""

from __future__ import annotations

import re


_MISSING_TOKEN = "information not provided."


def extract_score(
    text: str,
    section: str,
) -> int:
    """Extract a numeric score from a named section.

    Args:
        text:
            Complete LLM response.

        section:
            Section name.

    Returns:
        Extracted integer score or zero if not found.
    """

    pattern = rf"{re.escape(section)}\s*:?\s*(\d+)"

    match = re.search(
        pattern,
        text,
        flags=re.IGNORECASE,
    )

    if match:
        return int(match.group(1))

    return 0


def extract_text(
    text: str,
    section: str,
) -> str:
    """Extract a single-line text value from a named section.

    Args:
        text:
            Complete LLM response.

        section:
            Section name.

    Returns:
        Extracted text or an empty string.
    """

    pattern = rf"{re.escape(section)}\s*:?\s*(.+)"

    match = re.search(
        pattern,
        text,
        flags=re.IGNORECASE,
    )

    if not match:
        return ""

    value = match.group(1).strip()

    if value.casefold() == _MISSING_TOKEN:
        return ""

    return value


def extract_list(
    text: str,
    start_section: str,
    end_section: str,
) -> list[str]:
    """Extract a bullet list between two sections.

    Args:
        text:
            Complete LLM response.

        start_section:
            Starting section name.

        end_section:
            Ending section name.

    Returns:
        List of extracted items.
    """

    pattern = (
        rf"{re.escape(start_section)}\s*:?"
        rf"(.*?)"
        rf"{re.escape(end_section)}"
    )

    match = re.search(
        pattern,
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )

    if not match:
        return []

    block = match.group(1).strip()

    if (
        not block
        or block.casefold() == _MISSING_TOKEN
        or block.casefold() == "none"
    ):
        return []

    items: list[str] = []

    for line in block.splitlines():

        line = line.strip()

        if not line:
            continue

        line = re.sub(
            r"^[\-\*\u2022]\s*",
            "",
            line,
        )

        line = re.sub(
            r"^\d+[.)]\s*",
            "",
            line,
        )

        if line.casefold() == "none":
            continue

        if line:
            items.append(line)

    return items


__all__ = [
    "extract_score",
    "extract_text",
    "extract_list",
]