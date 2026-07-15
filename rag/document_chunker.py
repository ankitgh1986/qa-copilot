"""Document chunking using LangChain."""

from __future__ import annotations

import logging
from typing import List

from langchain_text_splitters import RecursiveCharacterTextSplitter
from config.settings import CHUNK_SIZE, CHUNK_OVERLAP

logger = logging.getLogger(__name__)


class DocumentChunker:
    """
    Splits requirement documents into overlapping chunks suitable
    for embedding generation and RAG retrieval.
    """

    def __init__(
        self,
        chunk_size: int = CHUNK_SIZE,
        chunk_overlap: int = CHUNK_OVERLAP
    ) -> None:
        """
        Initialize the document chunker.

        Args:
            chunk_size:
                Maximum characters per chunk.

            chunk_overlap:
                Number of overlapping characters between chunks.
        """

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
    ) -> List[str]:
        """
        Split a document into chunks.

        Args:
            text:
                Requirement document text.

        Returns:
            List of document chunks.
        """

        if not isinstance(text, str) or not text.strip():
            raise ValueError(
                "Input text must be a non-empty string."
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