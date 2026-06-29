import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Enterprise Knowledge Assistant",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown("""
<style>

            
/* Fix chat input at bottom */

.stChatInput{
    position:fixed;
    bottom:20px;
    left:24%;
    right:2%;
    background:white;
    padding:12px;
    z-index:999;
    border-top:1px solid #E5E7EB;
}

/* Leave space so messages don't hide behind input */

.main .block-container{
    padding-bottom:120px;
}
            
.block-container{
    padding-top:2rem;
    padding-bottom:1rem;
}

.metric-card{
    background:#F7F9FC;
    border-radius:12px;
    padding:18px;
    border:1px solid #E6EAF0;
    text-align:center;
}

.metric-title{
    font-size:14px;
    color:#666;
}

.metric-value{
    font-size:30px;
    font-weight:bold;
    color:#1565C0;
}

.status-card{
    background:#F8F9FA;
    padding:15px;
    border-radius:12px;
    border-left:5px solid #2E7D32;
    margin-bottom:12px;
}

.doc-card{
    background:#F9FAFB;
    padding:12px;
    border-radius:10px;
    border:1px solid #DDDDDD;
    margin-bottom:10px;
}

.footer{
    text-align:center;
    color:gray;
    margin-top:40px;
}

            section[data-testid="stSidebar"]{
    display:none;
}

header{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

#MainMenu{
    visibility:hidden;
}
            
</style>
""", unsafe_allow_html=True)

# =====================================================
# HEADER
# =====================================================

st.markdown("""
<div style="
background: linear-gradient(135deg,#2563EB,#3B82F6);
padding:28px;
border-radius:18px;
color:white;
margin-bottom:20px;
box-shadow:0 8px 25px rgba(37,99,235,.25);
">

<h1 style="
margin:0;
font-size:40px;
color:white;
">
🏢 Enterprise Knowledge Assistant
</h1>

<p style="
margin-top:10px;
font-size:18px;
color:#E5F0FF;
">

AI-powered document intelligence platform for enterprise knowledge retrieval.

</p>

</div>
""", unsafe_allow_html=True)

# =====================================================
# LAYOUT
# =====================================================

left,right = st.columns([0.8,4.2],gap="medium")

# =====================================================
# LEFT PANEL
# =====================================================

with left:

    st.markdown("""
    <div style="
    background:white;
    padding:20px;
    border-radius:18px;
    box-shadow:0 8px 24px rgba(15,23,42,.08);
    ">
    """, unsafe_allow_html=True)

    st.subheader("📂 Document Management")

    uploaded_files = st.file_uploader(
        "Upload Enterprise PDFs",
        type=["pdf"],
        accept_multiple_files=True
    )

    if uploaded_files:

        st.markdown("### 📄 Selected Documents")

        for pdf in uploaded_files:

            st.markdown(f"""
<div style="
background:#FFFFFF;
padding:14px;
border-radius:12px;
border-left:4px solid #2563EB;
margin-bottom:10px;
box-shadow:0 3px 12px rgba(0,0,0,.05);
">

📄 <b>{pdf.name}</b>

<br>

<span style="
font-size:12px;
color:#64748B;
">
Ready for upload
</span>

</div>
""",unsafe_allow_html=True)

    if st.button(
        "📤 Upload Documents",
        use_container_width=True
    ):

        if uploaded_files:

            with st.spinner(
                "Building Enterprise Knowledge Base..."
            ):

                files=[]

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

                response=requests.post(
                    f"{BACKEND_URL}/upload/",
                    files=files
                )

            if response.status_code==200:

                st.success(
                    "Knowledge Base Updated Successfully!"
                )

            else:

                st.error(response.text)

    st.write("")

    if st.button(
        "🗑 Clear Knowledge Base",
        use_container_width=True
    ):

        response=requests.post(
            f"{BACKEND_URL}/clear/"
        )

        if response.status_code==200:

            st.session_state.messages=[]

            st.success(
                "Knowledge Base Cleared!"
            )

            st.rerun()

        else:

            st.error(response.text)

    st.divider()

    st.subheader("🟢 System Status")

    st.markdown("""
    <div style="
    background:#F8FAFC;
    border:1px solid #E2E8F0;
    border-radius:12px;
    padding:12px;
    font-size:14px;
    line-height:2;
    ">

    🟢 <b>Backend</b> &nbsp;&nbsp; Online

    <br>

    🟢 <b>Gemini</b> &nbsp;&nbsp; Connected

    <br>

    🟢 <b>FAISS</b> &nbsp;&nbsp; Ready

    </div>
    """, unsafe_allow_html=True)
   

# =====================================================
# RIGHT PANEL
# =====================================================

st.markdown("</div>", unsafe_allow_html=True)
with right:

    st.write("")

    st.subheader("💬 Enterprise AI Assistant")

    st.caption(
        "Ask questions about your uploaded enterprise documents."
    )

    # =====================================================
    # CHAT
    # =====================================================

    if "messages" not in st.session_state:
        st.session_state.messages = []

    question = st.chat_input(
        "💬 Ask anything about your enterprise documents..."
    )

    if question:

        with st.spinner("🤖 Enterprise AI is analyzing your documents..."):

            response = requests.post(
                f"{BACKEND_URL}/chat/",
                json={
                    "question": question
                }
            )

            if response.status_code != 200:

                st.error(response.text)

            else:

                data = response.json()

                st.session_state.messages.append(
                    {
                        "question": question,
                        "answer": data["answer"],
                        "sources": data["sources"]
                    }
                )

                st.rerun()

    st.write("")

    # =====================================================
    # CHAT HISTORY
    # =====================================================

    for chat in st.session_state.messages:

        with st.container(border=True):

            col1, col2 = st.columns([1, 20])

            with col1:
                st.markdown("👤")

            with col2:

                st.markdown("#### You")

                st.write(chat["question"])

            st.divider()

            col1, col2 = st.columns([1, 20])

            with col1:
                st.markdown("🤖")

            with col2:

                st.markdown("#### Enterprise AI")

                st.write(chat["answer"])

            if chat["sources"]:

                st.write("")

                st.markdown("### 📚 Sources Used")

                cols = st.columns(
                    min(3, len(chat["sources"]))
                )

                for i, source in enumerate(chat["sources"]):

                    with cols[i % len(cols)]:

                        st.markdown(f"""
<div style="
background:#F8FAFC;
padding:15px;
border-radius:12px;
border:1px solid #E5E7EB;
height:120px;
">

<h5 style="margin-bottom:10px;">
📄 Document
</h5>

<b>{source['filename']}</b>

<br><br>

📑 Page <b>{source['page']}</b>

</div>
""", unsafe_allow_html=True)

        st.write("")

    # =====================================================
    # FOOTER
    # =====================================================

    st.markdown("---")

    st.caption(
        "Enterprise Knowledge Assistant • Powered by FastAPI • Gemini • FAISS"
    )