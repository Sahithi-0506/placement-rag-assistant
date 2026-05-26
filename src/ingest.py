from src.load_pdf import load_pdf
from src.chunking import split_documents
from src.vector_store import create_vector_store
from src.table_loader import load_company_table

PDF_PATH = "data/Placement_RAG_Dataset_Enhanced.pdf"


def main():
    print("Loading PDF...")
    documents = load_pdf(PDF_PATH)

    print(f"Loaded {len(documents)} pages")

    print("Loading structured company eligibility table...")
    table_documents = load_company_table()

    print(f"Loaded {len(table_documents)} structured table rows")

    # Exclude raw page 2 because it contains the company table
    # We already extracted that table cleanly using pdfplumber
    normal_documents = [
        doc for doc in documents
        if doc.metadata.get("page") != 1
    ]

    print("Splitting normal PDF text...")
    text_chunks = split_documents(normal_documents)

    all_chunks = text_chunks + table_documents

    print(f"Text chunks created: {len(text_chunks)}")
    print(f"Structured table chunks created: {len(table_documents)}")
    print(f"Total chunks created: {len(all_chunks)}")

    print("Creating ChromaDB vector store...")
    create_vector_store(all_chunks)

    print("Vector store created successfully!")


if __name__ == "__main__":
    main()