# QA Copilot Excel Report Architecture Analysis

## Architecture Summary

- `main.py` is the application entrypoint.
  - It runs `RequirementAnalyzer.analyze(document_path)` to get a `RequirementAnalysisResult`.
  - It formats the report to the console via `ConsoleReportFormatter`.
  - It writes the Excel report via `ExcelReportFormatter`.

- `RequirementAnalyzer` orchestrates the pipeline and produces `RequirementAnalysisResult`.
  - The result includes:
    - `context: RequirementContext`
    - `quality_assessment: QualityAssessment`
    - `ambiguity_assessment: AmbiguityAssessment`
    - `improvement_assessment: ImprovementAssessment`
    - `risk_assessment: RiskAssessment`
    - `acceptance_criteria: AcceptanceCriteria`
    - `test_design: TestDesign`
    - `test_cases: TestCaseSuite`

- `RequirementContext` stores shared metadata and summary information.
  - source document metadata and text
  - business goal, primary/supporting actors, main features, constraints, dependencies
  - `short_summary`
  - optional nested assessment objects for quality, ambiguity, improvement, risk, acceptance criteria, test design, and test cases

- Excel output is modeled as a set of sheet generator classes in `formatters/`.
  - `WorksheetBase` provides shared styling and helper methods.
  - Specific sheet classes each implement `.generate(sheet, result)`.

- The sheet classes currently implemented are:
  - `ExecutiveSummarySheet`
  - `RequirementSummarySheet`
  - `QualityAssessmentSheet`
  - `AmbiguityAssessmentSheet`
  - `RiskAssessmentSheet`
  - `AcceptanceCriteriaSheet`
  - `TestDesignSheet`
  - `TestCasesSheet`

- `WorksheetBase` provides reusable workbook helpers:
  - `write_title`
  - `write_table_header`
  - `write_metric`
  - `write_section`
  - `auto_fit_columns`
  - shared OpenPyXL styling constants and utility imports

- The current implementation gap:
  - `ImprovementAssessment` is in the data model but has no dedicated Excel sheet class.

## Worksheet Plan

1. `Executive Summary`
   - overall quality score and component scores
   - overall verdict
   - strengths and weaknesses

2. `Requirement Summary`
   - document metadata (source file, type, language, pages, words)
   - short requirement summary
   - functional areas
   - business objectives
   - key features
   - stakeholders
   - assumptions

3. `Quality Assessment`
   - quality metrics: overall, completeness, clarity, testability, consistency, risk coverage
   - overall verdict
   - strengths
   - weaknesses

4. `Ambiguity Assessment`
   - ambiguity score
   - ambiguity level
   - ambiguous terms
   - missing information
   - undefined business rules
   - assumptions
   - conflicting statements
   - summary

5. `Risk Assessment`
   - overall risk level
   - high risks
   - medium risks
   - low risks
   - testing focus areas
   - mitigation recommendations

6. `Acceptance Criteria`
   - numbered list of acceptance criteria items

7. `Test Design`
   - domain, feature, business goal
   - actors and workflows
   - business rules, dependencies, integration points, assumptions
   - test objectives, quality attributes, functional areas, test types, coverage strategy, test data requirements
   - identified risks table
   - automation candidates by API/UI/performance/manual
   - automation strategy

8. `Test Cases`
   - one section for each generated test case
   - test case metadata: title, objective, priority, severity, risk, automation candidate, automation layer
   - preconditions
   - test data
   - tags
   - test steps table

## Implementation Strategy

- `ExcelReportFormatter` should orchestrate workbook creation and sheet generation.
  - create an `openpyxl.Workbook` instance
  - remove the default sheet if needed
  - instantiate and generate each sheet in order
  - save the workbook to the provided `output_path`

- Each sheet class should be responsible for its own layout and data subset.
  - use `.generate(sheet, result)` to render one worksheet.
  - rely on `WorksheetBase` for repeated Excel operations and styling.

- Shared workbook helper responsibilities:
  - consistent title/subtitle rendering on each worksheet
  - table header styling and borders
  - metric row rendering and wrapped text alignment
  - section headers and bulleted item rendering
  - automatic column width adjustment via `get_column_letter`

- Data flow:
  - `RequirementAnalyzer` returns a fully populated `RequirementAnalysisResult`.
  - `ExcelReportFormatter` reads from the result and passes it to each sheet generator.
  - If the report should include `ImprovementAssessment`, add an `ImprovementAssessmentSheet` and include it in the workbook flow.

- Required models for Excel generation:
  - `RequirementAnalysisResult`
  - `RequirementContext`
  - `QualityAssessment`
  - `AmbiguityAssessment`
  - `RiskAssessment`
  - `AcceptanceCriteria`
  - `TestDesign` and nested `Risk` / `AutomationCandidates`
  - `TestCaseSuite`, `TestCase`, `TestStep`

- Styling / utilities should remain centralized in `WorksheetBase`.
  - avoid duplicating border, font, and alignment setup across sheets
  - keep layout logic in each worksheet class and styling logic in the base helper
