"""Gemini embedding provider."""

from __future__ import annotations

import logging
from typing import List, Optional

from google import genai

from config.settings import GEMINI_API_KEY
from providers.embeddings.base_embedding_provider import (
    BaseEmbeddingProvider,
)

logger = logging.getLogger(__name__)


class GeminiEmbeddingProvider(BaseEmbeddingProvider):
    """Embedding provider backed by Google's Gemini Embedding API."""

    def __init__(
        self,
        api_key: Optional[str] = None,
        model_name: str = "gemini-embedding-2",
    ) -> None:
        """
        Initialize the Gemini embedding provider.

        Args:
            api_key:
                Optional API key override.

            model_name:
                Gemini embedding model.
        """

        self._api_key = api_key or GEMINI_API_KEY

        if not self._api_key:
            raise ValueError(
                "GEMINI_API_KEY is not configured."
            )

        self._client = genai.Client(
            api_key=self._api_key,
        )

        self._model_name = model_name

        logger.info(
            "GeminiEmbeddingProvider initialized "
            "(model=%s).",
            self._model_name,
        )

    def generate_embedding(
        self,
        text: str,
    ) -> List[float]:
        """
        Generate an embedding for a text.

        Args:
            text:
                Input text.

        Returns:
            Embedding vector.
        """

        if not text.strip():
            raise ValueError(
                "Text must not be empty."
            )

        response = self._client.models.embed_content(
            model=self._model_name,
            contents=text,
        )

        return list(
            response.embeddings[0].values
        )