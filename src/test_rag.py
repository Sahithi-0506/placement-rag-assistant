from src.rag_chain import get_rag_response

query = "What is the CGPA requirement for TCS?"

response = get_rag_response(query)

print(response)