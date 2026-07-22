"""Standalone test for DocumentChunker."""

from pathlib import Path

from knowledge.ingestion.pdf_ingestor import PDFIngestor
from rag.document_chunker import DocumentChunker


def main() -> None:
    """Run the DocumentChunker test."""

    project_root = Path(__file__).resolve().parent.parent

    pdf_path = (
        project_root
        / "knowledge"
        / "ISTQB_CTFL_Syllabus_v4.0.1.pdf"
    )

    ingestor = PDFIngestor()
    document = ingestor.ingest(pdf_path)[0]

    text = document.content

    chunker = DocumentChunker()

    chunks = chunker.split(text)

    print("=" * 60)
    print(f"Document Title : {document.title}")
    print(f"Document Size  : {len(text):,} characters")
    print(f"Total Chunks   : {len(chunks)}")
    print("=" * 60)

    # Print first 5 chunks only
    for index, chunk in enumerate(chunks[:5], start=1):

        print(f"\nChunk {index}")
        print("-" * 60)
        print(chunk)
        print("-" * 60)
        print(f"Length : {len(chunk)}")

    if len(chunks) > 5:
        print("\n...")
        print(f"... {len(chunks) - 5} more chunks not displayed.")
        print("...")

    # -----------------------------
    # Chunk Statistics
    # -----------------------------
    chunk_lengths = [len(chunk) for chunk in chunks]

    print("\n")
    print("=" * 60)
    print("Chunk Statistics")
    print("=" * 60)
    print(f"Min Chunk Size : {min(chunk_lengths)}")
    print(f"Max Chunk Size : {max(chunk_lengths)}")
    print(f"Avg Chunk Size : {sum(chunk_lengths) // len(chunk_lengths)}")

    total_chars = sum(chunk_lengths)
    print(f"Original Size : {len(text):,}")
    print(f"Chunked Size  : {total_chars:,}")


if __name__ == "__main__":
    main()