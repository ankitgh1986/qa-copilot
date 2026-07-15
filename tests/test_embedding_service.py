"""Standalone test for EmbeddingService."""

from rag.document_chunker import DocumentChunker
from rag.embedding_service import EmbeddingService
from utils.file_reader import FileReader


def main():

    reader = FileReader()

    text = reader.read(
        "sample_inputs/bank_transfer_requirement.docx"
    )

    chunker = DocumentChunker()

    chunks = chunker.split(text)

    service = EmbeddingService()

    embeddings = service.generate_embeddings(
        chunks
    )

    print("=" * 60)

    print(f"Chunks      : {len(chunks)}")
    print(f"Embeddings  : {len(embeddings)}")

    print("=" * 60)

    print()

    print(
        "Embedding Dimension:",
        len(embeddings[0].vector),
    )


if __name__ == "__main__":
    main()