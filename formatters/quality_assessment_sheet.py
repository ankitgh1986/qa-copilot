"""Quality Assessment worksheet."""

from __future__ import annotations

from openpyxl.styles import Alignment, Font
from openpyxl.worksheet.worksheet import Worksheet

from .worksheet_base import WorksheetBase


class QualityAssessmentSheet(WorksheetBase):
    """Creates the Quality Assessment worksheet."""

    def generate(self, sheet: Worksheet, result) -> None:
        """Populate the Quality Assessment worksheet."""

        self.write_title(sheet)

        quality = result.quality_assessment

        row = 4

        # -------------------------------------------------------------
        # Overall Metrics
        # -------------------------------------------------------------

        sheet.cell(row=row, column=1).value = "Quality Metrics"
        sheet.cell(row=row, column=1).font = self.SECTION_FONT
        row += 1

        self.write_table_header(sheet, row)
        row += 1

        metrics = [
            ("Overall Score", quality.overall_score),
            ("Completeness Score", quality.completeness_score),
            ("Clarity Score", quality.clarity_score),
            ("Testability Score", quality.testability_score),
            ("Consistency Score", quality.consistency_score),
            ("Risk Coverage Score", quality.risk_coverage_score),
            ("Overall Verdict", quality.verdict),
        ]

        for key, value in metrics:
            self.write_metric(sheet, row, key, value)
            row += 1

        row += 2

        # -------------------------------------------------------------
        # Strengths
        # -------------------------------------------------------------

        row = self.write_section(
            sheet,
            row,
            "Strengths",
            quality.strengths,
        )

        # -------------------------------------------------------------
        # Weaknesses
        # -------------------------------------------------------------

        self.write_section(
            sheet,
            row,
            "Weaknesses",
            quality.weaknesses,
        )

        sheet.freeze_panes = "A5"

        self.auto_fit_columns(sheet)