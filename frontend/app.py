import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Enterprise Knowledge Assistant",
    page_icon="🏢",
    layout="wide"
)

st.title("🏢 Enterprise Knowledge Assistant")

st.caption(
    "Ask questions enterprise documents using AI-powered Retrieval-Augmented Generation(RAG)."
)
# -------------------------------
# Upload PDF
# -------------------------------

with st.sidebar:

    st.title("📂 Enterprise Documents")

    uploaded_files = st.file_uploader(
        "Upload PDF Documents",
        type=["pdf"],
        accept_multiple_files=True
    )

    if st.button("📤 Upload Documents"):

        if uploaded_files:

            with st.spinner("Processing documents..."):

                files = []

                for uploaded_file in uploaded_files:

                    files.append(
                        (
                            "files",
                           (
                                uploaded_file.name,
                                uploaded_file.getvalue(),
                                "application/pdf"
                            )
                        )
                    )

                requests.post(
                    f"{BACKEND_URL}/upload/",
                    files=files
                )

            st.success("Documents uploaded successfully!")

    st.divider()

    if st.button("🗑 Clear Knowledge Base"):

        requests.post(
        f"{BACKEND_URL}/clear/"
    )

        st.session_state.messages = []

        st.success("Knowledge Base Cleared!")

        st.rerun()
# -------------------------------
# Chat
# -------------------------------

st.header("💬 Ask Enterprise AI")

if "messages" not in st.session_state:
    st.session_state.messages = []

question = st.chat_input(
    "Ask anything about your enterprise documents..."
)

if question:

    with st.spinner("Thinking..."):

        response = requests.post(
            f"{BACKEND_URL}/chat/",
            json={
                "question": question
            }
        )

        data = response.json()

        st.session_state.messages.append(
            {
                "question": question,
                "answer": data["answer"],
                "sources": data["sources"]
            }
        )

    st.rerun()

# -------------------------------
# Conversation
# -------------------------------

for chat in st.session_state.messages:

    with st.chat_message("user"):
        st.write(chat["question"])

    with st.chat_message("assistant"):

        st.write(chat["answer"])

        st.markdown("**📚 Sources**")

        for source in chat["sources"]:

            st.caption(
                f"📄 {source['filename']}  |  Page {source['page']}"
            )