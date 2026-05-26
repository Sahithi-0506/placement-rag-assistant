from src.vector_store import load_vector_store

def test_retrieval(query):
    vector_store = load_vector_store()
    retriever = vector_store.as_retriever(search_kwargs={"k": 3})

    results = retriever.invoke(query)

    print("\nQuery:", query)
    print("\nRetrieved Chunks:\n")

    for i, doc in enumerate(results, start=1):
        print(f"--- Chunk {i} ---")
        print(doc.page_content[:700])
        print()

if __name__ == "__main__":
    test_retrieval("What is the CGPA requirement for TCS?")