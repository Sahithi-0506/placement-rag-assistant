import streamlit as st
from src.rag_chain import get_rag_response

st.set_page_config(
    page_title="Placement RAG Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Placement Intelligence RAG Assistant")
st.write("Ask questions from the placement dataset.")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

query = st.text_input("Enter your question:")

if st.button("Get Answer"):
    if query.strip():
        with st.spinner("Generating response..."):
            response = get_rag_response(query)

        st.session_state.chat_history.append({
            "question": query,
            "answer": response
        })
    else:
        st.warning("Please enter a question.")

if st.session_state.chat_history:
    st.subheader("Chat History")

    for chat in reversed(st.session_state.chat_history):
        st.markdown(f"**You:** {chat['question']}")
        st.markdown(f"**Assistant:** {chat['answer']}")
        st.divider()