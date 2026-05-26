from src.vector_store import load_vector_store

vector_store = load_vector_store()

docs = vector_store.similarity_search(
    "What is the CGPA requirement for TCS?",
    k=4,
    filter={"section": "company_eligibility"}
)

for i, doc in enumerate(docs, start=1):
    print(f"\n--- Document {i} ---")
    print(doc.page_content)
    print(doc.metadata)