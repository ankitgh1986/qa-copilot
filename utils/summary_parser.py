"""Parse structured requirement summaries into a RequirementContext.

This module contains the SummaryParser which converts the plain-text output
produced by the RequirementSummaryAgent into a structured
:class:`models.requirement_context.RequirementContext` instance.

The parser is defensive: it returns empty strings or empty lists when the
agent explicitly states "Information not provided." and raises RuntimeError
for unexpected failures.
"""

from __future__ import annotations

import logging
import re

from models.requirement_context import RequirementContext

logger = logging.getLogger(__name__)

# Canonical section names mapped to RequirementContext fields
_SECTION_TO_FIELD = {
    "business goal": "business_goal",
    "primary actor": "primary_actor",
    "supporting actors": "supporting_actors",
    "main features": "main_features",
    "business constraints": "business_constraints",
    "external dependencies": "external_dependencies",
    "short summary": "short_summary",
}

# Regex to detect a section heading line
_HEADING_RE = re.compile(
    r"^\s*(?:\d+\.|)\s*(?P<head>Business Goal|Primary Actor|Supporting Actors|"
    r"Main Features|Business Constraints|External Dependencies|Short Summary)\s*:?\s*$",
    flags=re.IGNORECASE,
)

_MISSING_TOKEN = "information not provided."


class SummaryParser:
    """Parser for structured requirement summaries."""

    @staticmethod
    def parse(summary: str) -> RequirementContext:
        """Parse the textual summary into a RequirementContext.

        Args:
            summary: Structured plain-text summary produced by the
                RequirementSummaryAgent.

        Returns:
            A populated RequirementContext.

        Raises:
            RuntimeError: If an unexpected parsing error occurs.
        """
        logger.info("Parsing requirement summary.")

        try:
            sections = SummaryParser._split_into_sections(summary)

            context_data: dict[str, object] = {}

            for section_name, field_name in _SECTION_TO_FIELD.items():
                content = sections.get(section_name, "")

                if field_name in {
                    "supporting_actors",
                    "main_features",
                    "business_constraints",
                    "external_dependencies",
                }:
                    context_data[field_name] = SummaryParser._parse_list_field(
                        content
                    )
                else:
                    context_data[field_name] = SummaryParser._parse_text_field(
                        content
                    )

            context = RequirementContext(
                business_goal=context_data.get("business_goal", ""),
                primary_actor=context_data.get("primary_actor", ""),
                supporting_actors=context_data.get("supporting_actors", []),
                main_features=context_data.get("main_features", []),
                business_constraints=context_data.get(
                    "business_constraints", []
                ),
                external_dependencies=context_data.get(
                    "external_dependencies", []
                ),
                short_summary=context_data.get("short_summary", ""),
            )

            logger.info("Requirement summary parsed successfully.")
            return context

        except Exception as exc:
            logger.exception("Failed to parse requirement summary.")
            raise RuntimeError(
                "Failed to parse requirement summary."
            ) from exc

    @staticmethod
    def _split_into_sections(text: str) -> dict[str, str]:
        """Split summary text into named sections."""
        lines = text.splitlines()

        sections: dict[str, str] = {}

        current_section: str | None = None
        buffer: list[str] = []

        for raw_line in lines:
            line = raw_line.strip()

            if not line:
                if current_section and buffer and buffer[-1] != "":
                    buffer.append("")
                continue

            match = _HEADING_RE.match(line)

            if match:
                if current_section is not None:
                    sections[current_section] = "\n".join(buffer).strip()

                current_section = match.group("head").lower()
                buffer = []
                continue

            if current_section is None:
                continue

            buffer.append(raw_line)

        if current_section is not None:
            sections[current_section] = "\n".join(buffer).strip()

        return sections

    @staticmethod
    def _parse_text_field(content: str) -> str:
        """Parse a text field."""
        if not content:
            return ""

        normalized = content.strip()

        if normalized.casefold() == _MISSING_TOKEN:
            return ""

        return " ".join(
            line.strip()
            for line in normalized.splitlines()
            if line.strip()
        )

    @staticmethod
    def _parse_list_field(content: str) -> list[str]:
        """Parse a list field."""
        if not content:
            return []

        normalized = content.strip()

        if normalized.casefold() == _MISSING_TOKEN:
            return []

        items: list[str] = []

        for raw_line in normalized.splitlines():
            line = raw_line.strip()

            if not line:
                continue

            line = re.sub(r"^[\-\*\u2022]\s+", "", line)
            line = re.sub(r"^[0-9]+[.)]\s+", "", line)
            line = re.sub(r"^[a-zA-Z]+[.)]\s+", "", line)

            if line:
                items.append(line)

        return items


__all__ = ["SummaryParser"]