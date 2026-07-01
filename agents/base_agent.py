"""Abstract base class for QA Copilot AI agents."""

from __future__ import annotations

import logging
from abc import ABC
from typing import Optional

from core.llm_client import LLMClient

logger = logging.getLogger(__name__)


class BaseAgent(ABC):
    """Base class providing common functionality for all AI agents.

    This class centralizes LLM initialization, input validation,
    and communication with the language model. Concrete agents
    inherit from this class and implement their own business logic.
    """

    def __init__(self, llm_client: Optional[LLMClient] = None) -> None:
        """Initialize the base agent.

        Args:
            llm_client: Optional injected LLM client. If omitted,
                a new LLMClient instance is created.
        """
        self._llm_client = llm_client or LLMClient()
        logger.info("%s initialized successfully.", self.__class__.__name__)

    def _validate_input(self, text: str) -> None:
        """Validate that the supplied input is a non-empty string.

        Args:
            text: Input text to validate.

        Raises:
            ValueError: If the input is empty or invalid.
        """
        if not isinstance(text, str) or not text.strip():
            logger.error("Input validation failed.")
            raise ValueError("Input must be a non-empty string.")

    def _generate(self, prompt: str) -> str:
        """Generate a response from the configured LLM.

        Args:
            prompt: Prompt to send to the language model.

        Returns:
            Generated response.

        Raises:
            RuntimeError: If LLM generation fails.
        """
        self._validate_input(prompt)

        logger.info(
            "Sending prompt to LLM (length=%d).",
            len(prompt),
        )

        try:
            response = self._llm_client.generate(prompt)

            logger.info(
                "Received LLM response (length=%d).",
                len(response),
            )

            return response

        except Exception as exc:
            logger.exception("LLM generation failed.")
            raise RuntimeError(
                "Failed to generate response from LLM."
            ) from exc


__all__ = ["BaseAgent"]