"""Standalone test for EmbeddingService."""

from rag.document_chunker import DocumentChunker
from rag.embedding_service import EmbeddingService
from utils.file_reader import FileReader


def main() -> None:
    """Run the EmbeddingService test."""

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
    print("EMBEDDING SERVICE TEST")
    print("=" * 60)

    print(f"Chunks      : {len(chunks)}")
    print(f"Embeddings  : {len(embeddings)}")

    print("=" * 60)

    for index, embedding in enumerate(embeddings, start=1):

        print(f"\nEmbedding {index}")
        print("-" * 60)
        print(f"Chunk ID         : {embedding.chunk_id}")
        print(f"Text Length      : {len(embedding.text)}")
        print(f"Vector Dimension : {len(embedding.vector)}")
        print(f"First 5 Values   : {embedding.vector[:5]}")

    print("\n")
    print("=" * 60)
    print("Verification")
    print("=" * 60)

    assert len(embeddings) == len(chunks)
    assert all(len(e.vector) > 0 for e in embeddings)

    print("✅ All embedding checks passed.")


if __name__ == "__main__":
    main()