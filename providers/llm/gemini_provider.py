"""Reusable Gemini-based LLM client for the QA Copilot project."""

from __future__ import annotations

import logging
from typing import Optional

import google.generativeai as genai

from config.settings import GEMINI_API_KEY, MODEL_NAME, TEMPERATURE
from providers.llm.base_provider import BaseLLMProvider

logger = logging.getLogger(__name__)


class GeminiProvider(BaseLLMProvider):
    """Reusable wrapper around Google's Gemini API."""

    def __init__(
        self,
        api_key: Optional[str] = None,
        model_name: Optional[str] = None,
        temperature: Optional[float] = None,
    ) -> None:
        """
        Initialize the Gemini client.

        Args:
            api_key: Optional API key override.
            model_name: Optional model name override.
            temperature: Optional temperature override.

        Raises:
            ValueError: If the API key is missing.
            RuntimeError: If Gemini initialization fails.
        """

        self.api_key = api_key or GEMINI_API_KEY
        self.model_name = model_name or MODEL_NAME or "gemini-2.5-flash"
        self.temperature = (
            temperature if temperature is not None else TEMPERATURE
        )

        logger.info(
            "Initializing LLM client for model '%s'.",
            self.model_name,
        )

        if not self.api_key:
            logger.error(
                "Missing API key while initializing LLM client."
            )
            raise ValueError("GEMINI_API_KEY is not configured.")

        try:
            genai.configure(api_key=self.api_key)
            logger.info("Gemini API configured successfully.")

            self._model = genai.GenerativeModel(
                model_name=self.model_name
            )

            logger.info(
                "Gemini model '%s' initialized successfully.",
                self.model_name,
            )

        except Exception as exc:
            logger.exception(
                "Failed to initialize Gemini model '%s'.",
                self.model_name,
            )
            raise RuntimeError(
                f"Failed to initialize Gemini model '{self.model_name}'."
            ) from exc

    def generate(self, prompt: str) -> str:
        """
        Generate a response from Gemini.

        Args:
            prompt: Prompt to send to Gemini.

        Returns:
            Generated text response.

        Raises:
            ValueError: If the prompt is empty.
            RuntimeError: If Gemini generation fails.
        """

        if not isinstance(prompt, str) or not prompt.strip():
            logger.error(
                "Prompt validation failed. Prompt must be a non-empty string."
            )
            raise ValueError("Prompt must be a non-empty string.")

        logger.info(
            "Sending prompt to Gemini (model='%s', length=%d).",
            self.model_name,
            len(prompt),
        )

        try:
            response = self._model.generate_content(
                prompt,
                generation_config={
                    "temperature": self.temperature,
                },
            )

        except Exception as exc:
            logger.exception(
                "Gemini generation failed for model '%s'.",
                self.model_name,
            )
            raise RuntimeError(
                f"Failed to generate content from Gemini: {exc}"
            ) from exc

        try:
            response_text = response.text.strip()

            if not response_text:
                logger.error(
                    "Gemini returned an empty response for model '%s'.",
                    self.model_name,
                )
                raise RuntimeError(
                    "Gemini returned no usable text content."
                )

            logger.info(
                "Received Gemini response successfully (length=%d).",
                len(response_text),
            )

            return response_text

        except Exception as exc:
            logger.exception(
                "Failed to parse Gemini response for model '%s'.",
                self.model_name,
            )
            raise RuntimeError(
                "Gemini returned no usable text content."
            ) from exc


__all__ = ["GeminiProvider"]