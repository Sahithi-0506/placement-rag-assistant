from langchain_ollama import OllamaLLM
from src.vector_store import load_vector_store

# Initialize local Ollama model
llm = OllamaLLM(model="llama3.2:1b")


def get_rag_response(query):

    # Load ChromaDB vector store
    vector_store = load_vector_store()

    # Create retriever
    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 2}
    )

    # Retrieve relevant documents
    docs = retriever.invoke(query)

    # Combine retrieved chunks into context
    context = ""

    for i, doc in enumerate(docs, start=1):
        context += f"\nDocument {i}:\n{doc.page_content}\n"

    # Prompt
    prompt = f"""
You are a Placement Intelligence Assistant.

Answer ONLY from the provided context.

Rules:
- Give short exact answers.
- Do not guess.
- Do not use outside knowledge.
- If exact answer is unavailable, say:
"I don't have enough information in the provided document."

Context:
{context}

Question:
{query}

Exact Answer:
"""

    # Generate response from local LLM
    response = llm.invoke(prompt)

    return response