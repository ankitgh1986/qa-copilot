"""Cache management for RequirementContext objects."""

from __future__ import annotations

import logging
import pickle
from pathlib import Path

from models.requirement_context import RequirementContext

logger = logging.getLogger(__name__)


class ContextCache:
    """Persist and retrieve RequirementContext objects."""

    _CACHE_DIR = Path("sample_outputs")
    _CACHE_FILE = _CACHE_DIR / "requirement_context.pkl"

    @classmethod
    def save(
        cls,
        context: RequirementContext,
    ) -> None:
        """Save a RequirementContext to the cache.

        Args:
            context:
                RequirementContext to cache.

        Raises:
            RuntimeError:
                If saving fails.
        """

        logger.info(
            "Saving RequirementContext to cache."
        )

        try:

            cls._CACHE_DIR.mkdir(
                parents=True,
                exist_ok=True,
            )

            with cls._CACHE_FILE.open("wb") as file:

                pickle.dump(
                    context,
                    file,
                )

            logger.info(
                "RequirementContext cached successfully."
            )

        except Exception as exc:

            logger.exception(
                "Failed to save RequirementContext."
            )

            raise RuntimeError(
                "Failed to save RequirementContext."
            ) from exc

    @classmethod
    def load(
        cls,
    ) -> RequirementContext:
        """Load the cached RequirementContext.

        Returns:
            Cached RequirementContext.

        Raises:
            RuntimeError:
                If loading fails.
        """

        logger.info(
            "Loading RequirementContext from cache."
        )

        try:

            with cls._CACHE_FILE.open("rb") as file:

                context = pickle.load(file)

            logger.info(
                "RequirementContext loaded successfully."
            )

            return context

        except Exception as exc:

            logger.exception(
                "Failed to load RequirementContext."
            )

            raise RuntimeError(
                "Failed to load RequirementContext."
            ) from exc

    @classmethod
    def exists(
        cls,
    ) -> bool:
        """Return whether the cache exists."""

        return cls._CACHE_FILE.exists()

    @classmethod
    def clear(
        cls,
    ) -> None:
        """Delete the cached RequirementContext."""

        if cls._CACHE_FILE.exists():

            cls._CACHE_FILE.unlink()

            logger.info(
                "RequirementContext cache cleared."
            )


__all__ = ["ContextCache"]