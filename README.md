# 🏢 Enterprise RAG Assistant

An AI-powered Enterprise Knowledge Assistant that enables users to upload enterprise documents and ask natural language questions. The system uses **Retrieval-Augmented Generation (RAG)** to retrieve relevant information from uploaded documents and generates accurate, context-aware responses using **Google Gemini**.

---

## 🚀 Features

* 📄 Upload one or multiple PDF documents
* 🔍 Intelligent document chunking
* 🧠 Semantic search using FAISS Vector Database
* 🤖 AI-generated answers powered by Google Gemini
* 💬 Conversation memory for follow-up questions
* 📚 Displays source document names and page numbers
* 🌐 FastAPI backend with interactive Swagger API
* 🎨 Streamlit-based user interface

---

## 🛠️ Tech Stack

### Backend

* FastAPI
* Python
* FAISS
* LangChain
* Google Gemini API
* Hugging Face Embeddings
* PyPDF

### Frontend

* Streamlit

### Database

* FAISS Vector Store

---

## 📂 Project Structure

```text
Enterprise-RAG-Assistant/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── models/
│   │   ├── services/
│   │   ├── utils/
│   │   ├── vector_db/
│   │   ├── config.py
│   │   └── main.py
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   └── app.py
│
└── README.md
```

---

## ⚙️ How It Works

1. Upload enterprise PDF documents.
2. Extract text from each document.
3. Split the text into semantic chunks.
4. Generate embeddings for each chunk.
5. Store embeddings in the FAISS vector database.
6. User asks a question.
7. The system retrieves the most relevant chunks.
8. Gemini generates an answer using the retrieved context.
9. The response includes the document name and page number used as evidence.

---

## ▶️ Running the Project

### 1. Clone the Repository

```bash
git clone https://github.com/Abhay-kumar-jangid/Enterprise-RAG-Assistant.git
```

### 2. Install Dependencies

```bash
pip install -r backend/requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file inside the `backend` folder and add:

```text
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

### 4. Start the Backend

```bash
cd backend
python -m uvicorn app.main:app --reload
```

### 5. Start the Frontend

```bash
cd frontend
streamlit run app.py
```

---

## 📷 Application Workflow

```text
Enterprise PDFs
        │
        ▼
PDF Loader
        │
        ▼
Text Chunking
        │
        ▼
Embeddings
        │
        ▼
FAISS Vector Store
        │
        ▼
Retriever
        │
        ▼
Google Gemini
        │
        ▼
Generated Answer + Source Citations
```

---

## 🎯 Use Cases

* Enterprise Knowledge Management
* HR Policy Assistant
* Employee Handbook Search
* IT & Security Documentation
* Standard Operating Procedures (SOPs)
* Internal Documentation Search
* Corporate Knowledge Base

---

## 📈 Future Enhancements

* User authentication and role-based access
* Multi-user chat sessions
* Document categorization
* OCR support for scanned PDFs
* Database integration (PostgreSQL/MongoDB)
* Cloud deployment (AWS/Azure/GCP)
* Advanced analytics dashboard

---

## 👨‍💻 Author

**Abhay Kumar**

B.Tech – Computer Science & Engineering (AI & ML)

KIET Group of Institutions

---

## 📄 License

This project is developed for academic and educational purposes.
