"""Excel report formatter for QA Copilot."""

from __future__ import annotations

import logging
from datetime import datetime

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.worksheet import Worksheet

from core.requirement_analyzer import RequirementAnalysisResult

logger = logging.getLogger(__name__)


class ExcelReportFormatter:
    """Generate Excel reports for QA Copilot."""

    REPORT_TITLE = "QA COPILOT"
    REPORT_SUBTITLE = "Requirement Analysis Report"
    VERSION = "v1.7.0"

    SHEETS = [
        "Executive Summary",
        "Requirement Summary",
        "Quality Assessment",
        "Ambiguity Assessment",
        "Improvement Assessment",
        "Risk Assessment",
        "Acceptance Criteria",
    ]

    HEADER_FILL = PatternFill(fill_type="solid", fgColor="1F4E78")
    HEADER_FONT = Font(bold=True, color="FFFFFF")
    TITLE_FONT = Font(bold=True, size=20)
    SUBTITLE_FONT = Font(italic=True, size=11)
    SECTION_FONT = Font(bold=True, size=14)

    THIN_BORDER = Border(
        left=Side(style="thin"),
        right=Side(style="thin"),
        top=Side(style="thin"),
        bottom=Side(style="thin"),
    )

    def format(
        self,
        result: RequirementAnalysisResult,
        output_path: str,
    ) -> None:

        workbook = Workbook()
        workbook.remove(workbook.active)

        for sheet_name in self.SHEETS:
            workbook.create_sheet(title=sheet_name)

        self._create_executive_summary_sheet(workbook, result)
        self._create_requirement_summary_sheet(workbook, result)

        workbook.save(output_path)

    def _create_executive_summary_sheet(
        self,
        workbook: Workbook,
        result: RequirementAnalysisResult,
    ) -> None:

        sheet = workbook["Executive Summary"]

        self._write_title(sheet)
        self._write_table_header(sheet, 6)

        verdict = getattr(result.quality_assessment.verdict, "value",
                          result.quality_assessment.verdict)
        ambiguity = getattr(
            result.ambiguity_assessment.ambiguity_level,
            "value",
            result.ambiguity_assessment.ambiguity_level,
        )

        metrics = [
            ("Generated On", datetime.now().strftime("%d-%b-%Y %H:%M")),
            ("Version", self.VERSION),
            ("Overall Quality Score", result.quality_assessment.overall_score),
            ("Quality Verdict", verdict),
            ("Ambiguity Level", ambiguity),
            ("Overall Risk Level", result.risk_assessment.overall_risk_level),
            ("Acceptance Criteria", len(result.acceptance_criteria.criteria)),
        ]

        row = 7
        for k, v in metrics:
            self._write_metric(sheet, row, k, v)
            row += 1

        self._auto_fit_columns(sheet)
        sheet.freeze_panes = "A7"

    def _create_requirement_summary_sheet(
        self,
        workbook: Workbook,
        result: RequirementAnalysisResult,
    ) -> None:

        sheet = workbook["Requirement Summary"]

        self._write_title(sheet)

        sheet["A4"] = "REQUIREMENT SUMMARY"
        sheet["A4"].font = self.SECTION_FONT

        sheet.merge_cells("A6:B18")
        cell = sheet["A6"]
        cell.value = result.context.short_summary
        cell.alignment = Alignment(
            wrap_text=True,
            vertical="top",
        )

        self._auto_fit_columns(sheet)
        sheet.row_dimensions[6].height = 180

    def _write_title(self, sheet: Worksheet) -> None:
        sheet.merge_cells("A1:B1")
        sheet["A1"] = self.REPORT_TITLE
        sheet["A1"].font = self.TITLE_FONT
        sheet["A1"].alignment = Alignment(horizontal="center")

        sheet.merge_cells("A2:B2")
        sheet["A2"] = self.REPORT_SUBTITLE
        sheet["A2"].font = self.SUBTITLE_FONT
        sheet["A2"].alignment = Alignment(horizontal="center")

    def _write_table_header(self, sheet: Worksheet, row: int) -> None:
        for col, value in enumerate(("Metric", "Value"), start=1):
            cell = sheet.cell(row=row, column=col)
            cell.value = value
            cell.font = self.HEADER_FONT
            cell.fill = self.HEADER_FILL
            cell.border = self.THIN_BORDER
            cell.alignment = Alignment(horizontal="center")

    def _write_metric(self, sheet: Worksheet, row: int, key: str, value: object) -> None:
        a = sheet.cell(row=row, column=1)
        a.value = key
        a.font = Font(bold=True)
        a.border = self.THIN_BORDER

        b = sheet.cell(row=row, column=2)
        b.value = value
        b.border = self.THIN_BORDER

    def _auto_fit_columns(self, sheet: Worksheet) -> None:
        for column in range(1, sheet.max_column + 1):
            letter = get_column_letter(column)
            max_len = 0
            for row in range(1, sheet.max_row + 1):
                value = sheet.cell(row=row, column=column).value
                if value:
                    max_len = max(max_len, len(str(value)))
            sheet.column_dimensions[letter].width = max_len + 5


__all__ = ["ExcelReportFormatter"]
