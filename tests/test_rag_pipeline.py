"""Standalone test for the RAG pipeline."""

from rag.document_chunker import DocumentChunker
from rag.embedding_service import EmbeddingService
from rag.rag_pipeline import RAGPipeline
from rag.retriever import Retriever
from rag.vector_store import VectorStore
from utils.file_reader import FileReader


def main() -> None:

    reader = FileReader()

    text = reader.read(
        "sample_inputs/bank_transfer_requirement.docx"
    )

    chunker = DocumentChunker()

    chunks = chunker.split(text)

    embedding_service = EmbeddingService()

    embeddings = (
        embedding_service.generate_embeddings(
            chunks
        )
    )

    vector_store = VectorStore()

    vector_store.add(
        embeddings
    )

    retriever = Retriever(
        embedding_service=embedding_service,
        vector_store=vector_store,
    )

    rag = RAGPipeline(
        retriever=retriever,
    )

    response = rag.generate(
        task="Generate acceptance criteria for this requirement.",
        top_k=3,
    )

    print("=" * 80)
    print("RAG RESPONSE")
    print("=" * 80)
    print(response)
    print("=" * 80)


if __name__ == "__main__":
    main()