"""Tests for InMemoryKnowledgeRepository."""

from pathlib import Path

from knowledge.ingestion.pdf_ingestor import PDFIngestor
from knowledge.repository.in_memory_repository import (
    InMemoryKnowledgeRepository,
)


def main():
    project_root = Path(__file__).resolve().parent.parent

    pdf = (
        project_root
        / "knowledge"
        / "ISTQB_CTFL_Syllabus_v4.0.1.pdf"
    )

    ingestor = PDFIngestor()

    document = ingestor.ingest(pdf)[0]

    repository = InMemoryKnowledgeRepository()

    print(f"Initial Count : {repository.count()}")

    repository.add(document)

    print(f"After Add     : {repository.count()}")

    print(f"Exists        : {repository.exists(document.id)}")

    retrieved = repository.get(document.id)

    print(f"Retrieved     : {retrieved.title}")

    print(f"Total Docs    : {len(repository.list())}")

    repository.remove(document.id)

    print(f"After Remove  : {repository.count()}")


if __name__ == "__main__":
    main()