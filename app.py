import streamlit as st
from src.rag_chain import get_rag_response

st.set_page_config(
    page_title="Placement RAG Assistant",
    page_icon="🤖",
    layout="centered"
)

st.title("📘 Placement Intelligence RAG Assistant")

st.write("Ask questions from the placement dataset.")

query = st.text_input("Enter your question:")

if st.button("Get Answer"):
    if query.strip():

        with st.spinner("Generating response..."):
            response = get_rag_response(query)

        st.subheader("Answer")
        st.write(response)

    else:
        st.warning("Please enter a question.")