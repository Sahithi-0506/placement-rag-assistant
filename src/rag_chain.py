from langchain_ollama import OllamaLLM
from src.vector_store import load_vector_store
from src.query_router import classify_query

llm = OllamaLLM(model="phi3:mini")


def get_all_company_eligibility_docs(vector_store):
    results = vector_store.get(
        where={"section": "company_eligibility"},
        include=["documents", "metadatas"]
    )

    context = ""

    for i, doc in enumerate(results["documents"], start=1):
        context += f"\nCompany Record {i}:\n{doc}\n"

    return context


def get_rag_response(query):
    vector_store = load_vector_store()
    query_type = classify_query(query)

    if query_type == "out_of_context":
        return "I don't have enough information in the provided document."

    if query_type == "multi_company":
        context = get_all_company_eligibility_docs(vector_store)

    elif query_type == "structured":
        docs = vector_store.similarity_search(
            query,
            k=4,
            filter={"section": "company_eligibility"}
        )

        context = ""
        for i, doc in enumerate(docs, start=1):
            context += f"\nDocument {i}:\n{doc.page_content}\n"

    else:
        docs = vector_store.similarity_search(query, k=5)

        context = ""
        for i, doc in enumerate(docs, start=1):
            context += f"\nDocument {i}:\n{doc.page_content}\n"

    prompt = f"""
You are a strict Placement Intelligence RAG Assistant.

Use ONLY the provided context.

Rules:
- Never use outside knowledge.
- Do not guess.
- For list questions, check every company record in the context.
- If the question asks for "technical focus" or "tech focus", use ONLY the line "Tech Focus".
- Do NOT use "Key Topics" as technical focus.
- If exact answer is not present, say:
"I don't have enough information in the provided document."
- Give only the final answer, no extra explanation.

Context:
{context}

Question:
{query}

Answer:
"""

    response = llm.invoke(prompt)
    return response.strip()