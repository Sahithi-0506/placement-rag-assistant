def classify_query(query):
    query_lower = query.lower()

    out_of_context_keywords = [
        "ceo", "stock price", "current", "today", "campus visit date",
        "visit our college", "work from home", "world", "salary in world"
    ]

    multi_company_keywords = [
        "which companies", "list all", "compare", "highest", "lowest",
        "above", "more than", "at least", "bond-free", "python-focused",
        "zero-bond", "rank"
    ]

    structured_keywords = [
        "cgpa", "package", "backlog", "bond", "technology",
        "tech focus", "technical focus"
    ]

    if any(word in query_lower for word in out_of_context_keywords):
        return "out_of_context"

    if any(word in query_lower for word in multi_company_keywords):
        return "multi_company"

    if any(word in query_lower for word in structured_keywords):
        return "structured"

    return "general"