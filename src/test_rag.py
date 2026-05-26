from src.vector_store import load_vector_store
from src.rag_chain import get_rag_response

query = "What is the package offered by Google?"

vector_store = load_vector_store()

retriever = vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 1}
)

docs = retriever.invoke(query)

print("\n========== RETRIEVED CONTEXT ==========\n")

for doc in docs:
    print(doc.page_content)

print("\n========== FINAL RESPONSE ==========\n")

response = get_rag_response(query)

print(response)