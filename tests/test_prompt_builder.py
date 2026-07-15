"""Standalone test for PromptBuilder."""

from models.embedding_vector import EmbeddingVector
from rag.prompt_builder import PromptBuilder


def main():

    chunks = [
        EmbeddingVector(
            chunk_id=0,
            text="Transfers above ₹1 lakh require OTP.",
            vector=[],
        ),
        EmbeddingVector(
            chunk_id=1,
            text="Every transfer must be audited.",
            vector=[],
        ),
    ]

    prompt = PromptBuilder.build(
        task="Generate Acceptance Criteria",
        context=chunks,
    )

    print(prompt)


if __name__ == "__main__":
    main()