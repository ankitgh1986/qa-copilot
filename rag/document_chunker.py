"""Document chunking using LangChain."""

from __future__ import annotations

import logging

from langchain_text_splitters import RecursiveCharacterTextSplitter

from config.settings import CHUNK_OVERLAP
from config.settings import CHUNK_SIZE

logger = logging.getLogger(__name__)


class DocumentChunker:
    """
    Splits text into overlapping chunks suitable for embedding generation
    and Retrieval-Augmented Generation (RAG).

    This class is generic and can be used for requirement documents,
    PDFs, markdown files, knowledge documents, or any textual content.
    """

    def __init__(
        self,
        chunk_size: int = CHUNK_SIZE,
        chunk_overlap: int = CHUNK_OVERLAP,
    ) -> None:
        """Initialize the document chunker."""

        self._splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                "",
            ],
        )

        logger.info(
            "DocumentChunker initialized "
            "(chunk_size=%d, overlap=%d).",
            chunk_size,
            chunk_overlap,
        )

    def split(
        self,
        text: str,
    ) -> list[str]:
        """
        Split text into chunks.

        Args:
            text:
                Input text.

        Returns:
            List of text chunks.
        """

        if not isinstance(text, str):
            raise TypeError(
                "Input text must be a string."
            )

        text = text.strip()

        if not text:
            raise ValueError(
                "Input text cannot be empty."
            )

        chunks = self._splitter.split_text(text)

        logger.info(
            "Document split into %d chunks.",
            len(chunks),
        )

        return chunks


__all__ = [
    "DocumentChunker",
]