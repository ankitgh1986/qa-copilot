"""Standalone test for VectorStore."""

from rag.document_chunker import (
    DocumentChunker,
)
from rag.embedding_service import (
    EmbeddingService,
)
from rag.vector_store import (
    VectorStore,
)
from utils.file_reader import (
    FileReader,
)


def main() -> None:
    """Run the VectorStore test."""

    reader = FileReader()

    text = reader.read(
        "sample_inputs/bank_transfer_requirement.docx"
    )

    # Chunk document
    chunker = DocumentChunker()

    chunks = chunker.split(
        text
    )

    # Generate embeddings
    embedding_service = (
        EmbeddingService()
    )

    embeddings = (
        embedding_service.generate_embeddings(
            chunks
        )
    )

    # Create and populate vector store
    store = VectorStore()

    store.add(
        embeddings
    )

    # Generate query embedding
    query = (
        embedding_service.generate_query_embedding(
            "OTP verification"
        )
    )

    # Search similar embeddings
    results = store.search(
        query_vector=query,
        top_k=3,
    )

    print("=" * 60)
    print("VECTOR STORE TEST")
    print("=" * 60)
    print(
        f"Stored Embeddings : {store.count}"
    )
    print(
        f"Retrieved Results : {len(results)}"
    )
    print("=" * 60)

    for index, result in enumerate(
        results,
        start=1,
    ):

        print()

        print("-" * 60)
        print(f"Result {index}")
        print("-" * 60)

        print(
            f"Chunk ID    : {result.chunk_id}"
        )

        print(
            f"Text Length : {len(result.text)}"
        )

        print(result.text)

    print()
    print("=" * 60)
    print("Verification")
    print("=" * 60)

    assert (
        store.count
        == len(embeddings)
    )

    assert len(results) > 0

    print(
        "✅ VectorStore verification passed."
    )


if __name__ == "__main__":
    main()