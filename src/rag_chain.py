from langchain_ollama import OllamaLLM
from src.vector_store import load_vector_store

llm = OllamaLLM(model="llama3.2:1b")

def get_rag_response(query):
    vector_store = load_vector_store()

    retriever = vector_store.as_retriever(search_kwargs={"k": 2})

    docs = retriever.invoke(query)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are a strict RAG assistant.

Use ONLY the context below.
Extract the exact value asked in the question.
Do not say section name unless needed.
Do not explain extra.

Context:
{context}

Question:
{query}

Answer in one sentence:
"""

    response = llm.invoke(prompt)

    return response