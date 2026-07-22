"""Improvement Assessment worksheet for Excel report generation."""

from __future__ import annotations

import logging

from openpyxl.worksheet.worksheet import Worksheet

from core.requirement_analyzer import RequirementAnalysisResult
from .worksheet_base import WorksheetBase

logger = logging.getLogger(__name__)


class ImprovementAssessmentSheet(WorksheetBase):
    """Generate the Improvement Assessment worksheet."""

    def generate(
        self,
        sheet: Worksheet,
        result: RequirementAnalysisResult,
    ) -> None:
        """Populate the worksheet with improvement recommendations."""

        logger.info("Generating Improvement Assessment worksheet.")

        self.write_title(sheet)

        assessment = result.improvement_assessment

        row = 4

        self.write_table_header(sheet, row)
        row += 1

        self.write_metric(
            sheet,
            row,
            "Overall Recommendation",
            assessment.overall_recommendation,
        )
        row += 2

        row = self.write_section(
            sheet,
            row,
            "Priority Improvements",
            assessment.priority_improvements,
        )

        row = self.write_section(
            sheet,
            row,
            "Requirement Updates",
            assessment.requirement_updates,
        )

        row = self.write_section(
            sheet,
            row,
            "Expected Impact",
            assessment.expected_impact,
        )

        self.auto_fit_columns(sheet)

        logger.info("Improvement Assessment worksheet generated successfully.")