"""Simple file-based cache for LLM responses."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


class LLMCache:

    CACHE_DIR = Path(".cache")

    @classmethod
    def _file_path(cls, prompt: str) -> Path:
        cls.CACHE_DIR.mkdir(exist_ok=True)

        prompt_hash = hashlib.sha256(
            prompt.encode("utf-8")
        ).hexdigest()

        return cls.CACHE_DIR / f"{prompt_hash}.json"

    @classmethod
    def get(cls, prompt: str):

        file = cls._file_path(prompt)

        if not file.exists():
            return None

        with open(file, "r", encoding="utf-8") as f:
            return json.load(f)["response"]

    @classmethod
    def put(
        cls,
        prompt: str,
        response: str,
    ) -> None:

        file = cls._file_path(prompt)

        with open(file, "w", encoding="utf-8") as f:
            json.dump(
                {"response": response},
                f,
                indent=2,
            )