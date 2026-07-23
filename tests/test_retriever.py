"""Standalone test for Retriever."""

from rag.document_chunker import (
    DocumentChunker,
)
from rag.embedding_service import (
    EmbeddingService,
)
from rag.retriever import (
    Retriever,
)
from rag.vector_store import (
    VectorStore,
)
from utils.file_reader import (
    FileReader,
)


def main() -> None:
    """Run the Retriever test."""

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

    # Create vector store
    store = VectorStore()

    store.add(
        embeddings
    )

    # Create retriever
    retriever = Retriever(
        embedding_service=embedding_service,
        vector_store=store,
    )

    query = "OTP verification"

    results = retriever.retrieve(
        query=query,
        top_k=3,
    )

    print("=" * 60)
    print("RETRIEVER TEST")
    print("=" * 60)
    print(
        f"Query              : {query}"
    )
    print(
        f"Retrieved Results  : {len(results)}"
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

    assert len(results) > 0

    print(
        "✅ Retriever verification passed."
    )


if __name__ == "__main__":
    main()