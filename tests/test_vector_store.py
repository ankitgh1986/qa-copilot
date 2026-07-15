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


def main():

    reader = FileReader()

    text = reader.read(
        "sample_inputs/bank_transfer_requirement.docx"
    )

    chunker = DocumentChunker()

    chunks = chunker.split(
        text
    )

    embedding_service = (
        EmbeddingService()
    )

    embeddings = (
        embedding_service.generate_embeddings(
            chunks
        )
    )

    store = VectorStore()

    store.add(
        embeddings
    )

    query = (
        embedding_service
        ._provider
        .generate_embedding(
            "OTP verification"
        )
    )

    results = store.search(
        query_vector=query,
        top_k=3,
    )

    print("=" * 60)

    print(
        f"Retrieved {len(results)} chunks"
    )

    print("=" * 60)

    for result in results:

        print()

        print(
            f"Chunk ID : {result.chunk_id}"
        )

        print(result.text)

        print("-" * 60)


if __name__ == "__main__":
    main()