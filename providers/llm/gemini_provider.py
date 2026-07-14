"""Reusable Gemini-based LLM client for the QA Copilot project."""

from __future__ import annotations

import logging
from typing import Optional

import google.generativeai as genai

from config.settings import GEMINI_API_KEY, MODEL_NAME, TEMPERATURE
from core.cache.llm_cache import LLMCache
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

        self.model_name = (
            model_name
            or MODEL_NAME
            or "gemini-2.5-flash"
        )

        self.temperature = (
            temperature
            if temperature is not None
            else TEMPERATURE
        )

        logger.info(
            "Initializing Gemini model '%s'.",
            self.model_name,
        )

        if not self.api_key:
            raise ValueError(
                "GEMINI_API_KEY is not configured."
            )

        try:

            genai.configure(
                api_key=self.api_key,
            )

            self._model = genai.GenerativeModel(
                model_name=self.model_name,
            )

            logger.info(
                "Gemini model initialized successfully."
            )

        except Exception as exc:

            logger.exception(
                "Failed to initialize Gemini."
            )

            raise RuntimeError(
                "Failed to initialize Gemini."
            ) from exc

    def generate(
        self,
        prompt: str,
    ) -> str:
        """
        Generate response from Gemini.

        Uses a local cache to avoid repeated API
        calls for identical prompts.
        """

        if (
            not isinstance(prompt, str)
            or not prompt.strip()
        ):
            raise ValueError(
                "Prompt must be a non-empty string."
            )

        # ----------------------------------
        # Check Cache
        # ----------------------------------

        cached = LLMCache.get(prompt)

        if cached is not None:

            logger.info(
                "LLM Cache HIT."
            )

            return cached

        logger.info(
            "LLM Cache MISS."
        )

        logger.info(
            "Calling Gemini (model=%s)...",
            self.model_name,
        )

        try:

            response = self._model.generate_content(
                prompt,
                generation_config={
                    "temperature": self.temperature,
                },
            )

            response_text = response.text.strip()

            if not response_text:

                raise RuntimeError(
                    "Gemini returned empty response."
                )

            # -------------------------------
            # Save response into cache
            # -------------------------------

            LLMCache.put(
                prompt,
                response_text,
            )

            logger.info(
                "Response cached successfully."
            )

            return response_text

        except Exception as exc:

            logger.exception(
                "Gemini request failed."
            )

            raise RuntimeError(
                f"Failed to generate content from Gemini: {exc}"
            ) from exc


__all__ = [
    "GeminiProvider",
]