"""Reusable Gemini-based LLM client for the QA Copilot project."""

from __future__ import annotations

import logging
from typing import Optional

from google import genai
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

from config.settings import (
    GEMINI_API_KEY,
    MODEL_NAME,
    TEMPERATURE,
)
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
        """Initialize Gemini client."""

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

            self._client = genai.Client(
                api_key=self.api_key,
            )

            logger.info(
                "Gemini client initialized successfully."
            )

        except Exception as exc:

            logger.exception(
                "Failed to initialize Gemini."
            )

            raise RuntimeError(
                "Failed to initialize Gemini."
            ) from exc

    @retry(
        retry=retry_if_exception_type(Exception),
        wait=wait_exponential(
            multiplier=2,
            min=2,
            max=20,
        ),
        stop=stop_after_attempt(5),
        reraise=True,
    )
    def _call_gemini(
        self,
        prompt: str,
    ):
        """
        Internal Gemini API call with retry.
        """

        logger.info(
            "Calling Gemini (model=%s)...",
            self.model_name,
        )

        return self._client.models.generate_content(
            model=self.model_name,
            contents=prompt,
            config={
                "temperature": self.temperature,
            },
        )

    def generate(
        self,
        prompt: str,
    ) -> str:
        """
        Generate response from Gemini.

        Uses local cache to avoid repeated API calls.
        """

        if (
            not isinstance(prompt, str)
            or not prompt.strip()
        ):
            raise ValueError(
                "Prompt must be a non-empty string."
            )

        cached = LLMCache.get(prompt)

        if cached is not None:

            logger.info(
                "LLM Cache HIT."
            )

            return cached

        logger.info(
            "LLM Cache MISS."
        )

        try:

            response = self._call_gemini(
                prompt
            )

            response_text = (
                response.text.strip()
            )

            if not response_text:

                raise RuntimeError(
                    "Gemini returned empty response."
                )

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