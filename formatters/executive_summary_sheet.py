"""Executive Summary worksheet."""

from __future__ import annotations

from openpyxl.worksheet.worksheet import Worksheet

from .worksheet_base import WorksheetBase


class ExecutiveSummarySheet(WorksheetBase):
    """Creates the Executive Summary worksheet."""

    def generate(self, sheet: Worksheet, result) -> None:
        """Populate the Executive Summary worksheet."""

        self.write_title(sheet)

        row = 4

        self.write_table_header(sheet, row)
        row += 1

        quality = result.quality_assessment

        # Display enum values in a user-friendly format
        verdict = quality.verdict
        if hasattr(verdict, "name"):
            verdict = verdict.name.replace("_", " ").title()
        elif hasattr(verdict, "value"):
            verdict = verdict.value

        metrics = [
            ("Overall Score", quality.overall_score),
            ("Completeness", quality.completeness_score),
            ("Clarity", quality.clarity_score),
            ("Testability", quality.testability_score),
            ("Consistency", quality.consistency_score),
            ("Risk Coverage", quality.risk_coverage_score),
            ("Verdict", verdict),
        ]

        for key, value in metrics:
            self.write_metric(sheet, row, key, value)
            row += 1

        row += 1

        row = self.write_section(
            sheet,
            row,
            "Strengths",
            quality.strengths,
        )

        row = self.write_section(
            sheet,
            row,
            "Weaknesses",
            quality.weaknesses,
        )

        sheet.freeze_panes = "A5"

        self.auto_fit_columns(sheet)