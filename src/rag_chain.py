from langchain_ollama import OllamaLLM

from src.vector_store import load_vector_store
from src.query_router import classify_query

from src.reasoning_engine import (
    companies_above_cgpa,
    companies_allowing_backlogs,
    bond_free_companies,
    python_focused_companies,
    highest_package_python_focused,
    zero_bond_above_package,
    highest_paying_for_student,
    company_with_most_interns,
    compare_sde_amazon_google,
    role_hiring_count,
    largest_package_growth,
    amazon_cgpa_conflict,
    companies_with_conflicting_cgpa,
    best_package_to_cgpa_ratio,
    rank_eligible_zero_backlog_8_plus,
    compare_google_amazon,
)

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


def get_context_from_docs(docs):
    context = ""

    for i, doc in enumerate(docs, start=1):
        context += f"\nDocument {i}:\n{doc.page_content}\n"

    return context


def handle_reasoning_query(query):
    q = query.lower()

    if "cgpa above 8.0" in q or "cgpa above 8" in q:
        return companies_above_cgpa(8.0)

    if "at least 2 backlogs" in q or "allow at least 2 backlogs" in q:
        return companies_allowing_backlogs(2)

    if "bond-free" in q or "bond free" in q:
        if "40" in q or "more than 40" in q:
            return zero_bond_above_package(40)
        return bond_free_companies()

    if "zero-bond" in q and "40" in q:
        return zero_bond_above_package(40)

    if "companies use python" in q or "python as technical focus" in q:
        return python_focused_companies()

    if "python-focused company offers highest package" in q or "python-focused companies" in q:
        return highest_package_python_focused()

    if "7.6" in q and "1 backlog" in q:
        return highest_paying_for_student(7.6, 1)

    if "most interns" in q:
        return company_with_most_interns()

    if "amazon" in q and "google" in q and "sde" in q:
        return compare_sde_amazon_google()

    if "how many" in q and "sde" in q and "amazon" in q:
        return role_hiring_count("Amazon", "sde")

    if "how many" in q and "sde" in q and "google" in q:
        return role_hiring_count("Google", "sde")

    if "how many" in q and "intern" in q and "oracle" in q:
        return role_hiring_count("Oracle", "intern")

    if "package grew the most" in q or "largest package growth" in q:
        return largest_package_growth()

    if "amazon" in q and "cgpa" in q and (
        "conflict" in q or "cutoff" in q or "6.4" in q or "7.0" in q
    ):
        return amazon_cgpa_conflict()

    if "conflicting cgpa" in q or "conflicting data" in q:
        return companies_with_conflicting_cgpa()

    if "package-to-cgpa" in q or "package to cgpa" in q:
        return best_package_to_cgpa_ratio()

    if "rank companies by package" in q or "8.0+" in q:
        return rank_eligible_zero_backlog_8_plus()

    if "compare google and amazon" in q:
        return compare_google_amazon()

    return None


def get_rag_response(query):
    reasoning_answer = handle_reasoning_query(query)

    if reasoning_answer:
        return reasoning_answer

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
        context = get_context_from_docs(docs)

    else:
        docs = vector_store.similarity_search(query, k=5)
        context = get_context_from_docs(docs)

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