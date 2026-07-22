"""Orchestrate the requirement analysis pipeline for QA Copilot."""

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import Optional

from agents.acceptance_criteria_agent import AcceptanceCriteriaAgent
from agents.ambiguity_agent import AmbiguityAgent
from agents.improvement_agent import ImprovementAgent
from agents.requirement_quality_agent import RequirementQualityAgent
from agents.requirement_summary_agent import RequirementSummaryAgent
from agents.risk_agent import RiskAgent
from agents.test_design_agent import TestDesignAgent
from agents.test_case_generation_agent import (
    TestCaseGenerationAgent,
)
from core.context_cache import ContextCache
from models.acceptance_criteria import AcceptanceCriteria
from models.ambiguity_assessment import AmbiguityAssessment
from models.improvement_assessment import ImprovementAssessment
from models.quality_assessment import QualityAssessment
from models.requirement_context import RequirementContext
from models.risk_assessment import RiskAssessment
from models.test_design import TestDesign
from models.test_case import TestCaseSuite
from utils.file_reader import FileReader

logger = logging.getLogger(__name__)


@dataclass(slots=True)
class RequirementAnalysisResult:
    """Structured result of the requirement analysis pipeline."""

    context: RequirementContext
    quality_assessment: QualityAssessment
    ambiguity_assessment: AmbiguityAssessment
    improvement_assessment: ImprovementAssessment
    risk_assessment: RiskAssessment
    acceptance_criteria: AcceptanceCriteria
    test_design: TestDesign
    test_cases: TestCaseSuite


class RequirementAnalyzer:
    """Service that orchestrates the full requirement analysis pipeline."""

    def __init__(
        self,
        summary_agent: Optional[RequirementSummaryAgent] = None,
        quality_agent: Optional[RequirementQualityAgent] = None,
        ambiguity_agent: Optional[AmbiguityAgent] = None,
        improvement_agent: Optional[ImprovementAgent] = None,
        risk_agent: Optional[RiskAgent] = None,
        acceptance_criteria_agent: Optional[
            AcceptanceCriteriaAgent
        ] = None,
        test_design_agent: Optional[TestDesignAgent] = None,
        test_case_generation_agent: Optional[
            TestCaseGenerationAgent
        ] = None,
    ) -> None:
        """Initialize the RequirementAnalyzer service."""

        self._summary_agent = summary_agent or RequirementSummaryAgent()
        self._quality_agent = quality_agent or RequirementQualityAgent()
        self._ambiguity_agent = ambiguity_agent or AmbiguityAgent()
        self._improvement_agent = improvement_agent or ImprovementAgent()
        self._risk_agent = risk_agent or RiskAgent()
        self._acceptance_criteria_agent = (
            acceptance_criteria_agent
            or AcceptanceCriteriaAgent()
        )
        self._test_design_agent = (
            test_design_agent
            or TestDesignAgent()
        )

        self._test_case_generation_agent = (
            test_case_generation_agent
            or TestCaseGenerationAgent()
        )

        self._file_reader = FileReader()

        logger.info(
            "RequirementAnalyzer initialized successfully."
        )

    def analyze(
        self,
        document_path: str,
    ) -> RequirementAnalysisResult:
        """Execute the requirement analysis pipeline."""

        logger.info(
            "Starting requirement analysis for document: %s",
            document_path,
        )

        try:

            context = self._load_or_create_context(
                document_path
            )

            result = self._execute_agents(
                context
            )

            logger.info(
                "Requirement analysis pipeline completed successfully."
            )

            return result

        except Exception as exc:

            logger.exception(
                "Requirement analysis pipeline failed."
            )

            raise RuntimeError(
                "Requirement analysis failed."
            ) from exc

    def _load_or_create_context(
        self,
        document_path: str,
    ) -> RequirementContext:
        """Load cached RequirementContext or create one."""

        if ContextCache.exists():

            logger.info(
                "Loading cached RequirementContext."
            )

            return ContextCache.load()

        logger.info(
            "Cached RequirementContext not available. Reading document."
        )

        requirement_text = self._read_document(
            document_path
        )

        context = self._summary_agent.summarize(
            requirement_text
        )

        context.source_document = document_path
        context.requirement_text = requirement_text

        ContextCache.save(
            context
        )

        return context

    def _read_document(
        self,
        document_path: str,
    ) -> str:
        """Read the requirement document."""

        logger.info(
            "Reading requirement document from path: %s",
            document_path,
        )

        return self._file_reader.read(
            document_path
        )

    def _execute_agents(
        self,
        context: RequirementContext,
    ) -> RequirementAnalysisResult:
        """Execute all analysis agents."""

        logger.info(
            "Executing Quality Agent"
        )

        quality_assessment = (
            self._quality_agent.evaluate(
                context
            )
        )

        logger.info(
            "Executing Ambiguity Agent"
        )

        ambiguity_assessment = (
            self._ambiguity_agent.evaluate(
                context
            )
        )

        logger.info(
            "Executing Improvement Agent"
        )

        improvement_assessment = (
            self._improvement_agent.evaluate(
                context
            )
        )

        logger.info(
            "Executing Risk Agent"
        )

        risk_assessment = (
            self._risk_agent.evaluate(
                context
            )
        )

        logger.info(
            "Executing Acceptance Criteria Agent"
        )

        acceptance_criteria = (
            self._acceptance_criteria_agent.generate(
                context
            )
        )

        logger.info(
            "Executing Test Design Agent"
        )

        test_design = self._test_design_agent.analyze(
            context.requirement_text
        )

        context.test_design = test_design

        logger.info(
            "Executing Test Case Generation Agent"
        )

        test_cases = (
            self._test_case_generation_agent.analyze(
                context.requirement_text
            )
        )

        context.test_cases = test_cases

        return RequirementAnalysisResult(
            context=context,
            quality_assessment=quality_assessment,
            ambiguity_assessment=ambiguity_assessment,
            improvement_assessment=improvement_assessment,
            risk_assessment=risk_assessment,
            acceptance_criteria=acceptance_criteria,
            test_design=test_design,
            test_cases=test_cases,
        )


__all__ = [
    "RequirementAnalyzer",
    "RequirementAnalysisResult",
]