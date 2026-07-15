"""Standalone test for DocumentChunker."""

from utils.file_reader import FileReader
from rag.document_chunker import DocumentChunker


def main() -> None:

    reader = FileReader()

    text = reader.read(
        "sample_inputs/bank_transfer_requirement.docx"
    )

    chunker = DocumentChunker()
    

    chunks = chunker.split(text)

    print("=" * 60)
    print(f"Total Chunks : {len(chunks)}")
    print("=" * 60)

    for index, chunk in enumerate(chunks, start=1):

        print(f"\nChunk {index}")
        print("-" * 60)
        print(chunk)
        print("-" * 60)
        print(f"Length : {len(chunk)}")


if __name__ == "__main__":
    main()