"""Test script for PDFIngestor."""

from pathlib import Path

from knowledge.ingestion.pdf_ingestor import PDFIngestor


def main():
    """Run the PDF ingestor test."""

    # Project root (QA_COPILOT)
    project_root = Path(__file__).resolve().parent.parent

    # ISTQB PDF location
    pdf_path = (
        project_root
        / "knowledge"
        / "ISTQB_CTFL_Syllabus_v4.0.1.pdf"
    )

    print("=" * 80)
    print("PDF INGESTOR TEST")
    print("=" * 80)
    print(f"PDF Path : {pdf_path}")
    print(f"Exists   : {pdf_path.exists()}")

    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    ingestor = PDFIngestor()

    documents = ingestor.ingest(pdf_path)

    print("\n" + "=" * 80)
    print(f"Documents Created : {len(documents)}")
    print("=" * 80)

    document = documents[0]

    print(f"Title        : {document.title}")
    print(f"ID           : {document.id}")
    print(f"Category     : {document.category.name}")
    print(f"Source       : {document.source.name}")
    print(f"Status       : {document.status.name}")
    print(f"Domains      : {[domain.name for domain in document.domains]}")
    print(
        f"Technologies : {[tech.name for tech in document.technologies]}"
    )
    print(f"Metadata     : {document.metadata}")

    print("\nFirst 1000 characters:\n")
    print(document.content[:1000])

    print("\n" + "=" * 80)
    print(f"Total Characters : {len(document.content):,}")
    print("=" * 80)


if __name__ == "__main__":
    main()