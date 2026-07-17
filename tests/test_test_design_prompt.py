"""Standalone test for the Test Design prompt."""

from __future__ import annotations

from providers.llm.gemini_provider import GeminiProvider
from prompts.test_design_prompt import (
    get_test_design_prompt,
)
from utils.file_reader import FileReader


def main() -> None:
    """Execute the Test Design prompt."""

    reader = FileReader()

    requirement = reader.read(
        "sample_inputs/bank_transfer_requirement.docx"
    )

    prompt = get_test_design_prompt(
        requirement=requirement,
    )

    llm = GeminiProvider()

    response = llm.generate(
        prompt
    )

    print("=" * 100)
    print("AI TEST DESIGN")
    print("=" * 100)
    print(response)
    print("=" * 100)


if __name__ == "__main__":
    main()