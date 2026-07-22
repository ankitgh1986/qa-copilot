"""Risk Assessment worksheet."""

from __future__ import annotations

from openpyxl.styles import Alignment
from openpyxl.worksheet.worksheet import Worksheet

from .worksheet_base import WorksheetBase


class RiskAssessmentSheet(WorksheetBase):
    """Creates the Risk Assessment worksheet."""

    def generate(self, sheet: Worksheet, result) -> None:
        """Populate the Risk Assessment worksheet."""

        self.write_title(sheet)

        risk = result.risk_assessment

        row = 4

        # ---------------------------------------------------------
        # Overall Risk Level
        # ---------------------------------------------------------

        sheet.cell(row=row, column=1).value = "Overall Risk Level"
        sheet.cell(row=row, column=1).font = self.SECTION_FONT
        row += 1

        self.write_table_header(sheet, row)
        row += 1

        self.write_metric(
            sheet,
            row,
            "Risk Level",
            risk.overall_risk_level,
        )

        row += 3

        # ---------------------------------------------------------
        # High Risks
        # ---------------------------------------------------------

        row = self.write_section(
            sheet,
            row,
            "High Risks",
            risk.high_risks,
        )

        # ---------------------------------------------------------
        # Medium Risks
        # ---------------------------------------------------------

        row = self.write_section(
            sheet,
            row,
            "Medium Risks",
            risk.medium_risks,
        )

        # ---------------------------------------------------------
        # Low Risks
        # ---------------------------------------------------------

        row = self.write_section(
            sheet,
            row,
            "Low Risks",
            risk.low_risks,
        )

        # ---------------------------------------------------------
        # Testing Focus Areas
        # ---------------------------------------------------------

        row = self.write_section(
            sheet,
            row,
            "Testing Focus Areas",
            risk.testing_focus_areas,
        )

        # ---------------------------------------------------------
        # Mitigation Recommendations
        # ---------------------------------------------------------

        row = self.write_section(
            sheet,
            row,
            "Mitigation Recommendations",
            risk.mitigation_recommendations,
        )

        sheet.freeze_panes = "A5"

        self.auto_fit_columns(sheet)