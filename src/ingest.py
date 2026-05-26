from src.load_pdf import load_pdf
from src.chunking import split_documents
from src.vector_store import create_vector_store

PDF_PATH = "data/Placement_RAG_Dataset_Enhanced.pdf"

def main():
    print("Loading PDF...")
    documents = load_pdf(PDF_PATH)

    print(f"Loaded {len(documents)} pages")

    print("Splitting documents into chunks...")
    chunks = split_documents(documents)

    print(f"Created {len(chunks)} chunks")

    print("Creating ChromaDB vector store...")
    create_vector_store(chunks)

    print("Vector store created successfully!")

if __name__ == "__main__":
    main()