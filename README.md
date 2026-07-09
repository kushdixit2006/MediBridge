# 🩺 MediBridge

Production-oriented Retrieval-Augmented Generation (RAG) application for understanding medical reports through natural language conversations. Users can upload a PDF medical report, ask context-aware questions, and receive AI-generated responses using semantic retrieval and a Large Language Model.

## Architecture

```
Presentation Layer
        │
        ▼
FastAPI API Layer
        │
        ▼
RAG Service Layer
        │
        ▼
Session Management Layer
        │
        ▼
FAISS Vector Store
        │
        ▼
Groq LLM
```

The Streamlit frontend handles PDF uploads, sends chat requests, and displays responses. FastAPI exposes REST APIs for document upload and chat. The RAG service manages document retrieval, prompt construction, and LLM interaction. Session management maintains per-user vector stores and chat history, while FAISS performs semantic retrieval over the uploaded medical report.

## Run

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

export GROQ_API_KEY="your-key"

uvicorn backend.main:app --reload
streamlit run frontend/streamlit_app.py
```

## Current Workflow

```
START
   │
   ▼
Upload PDF
   │
   ▼
Load Document
   │
   ▼
Chunk Document
   │
   ▼
Generate Embeddings
   │
   ▼
Create FAISS Vector Store
   │
   ▼
Store Session
   │
   ▼
User Question
   │
   ▼
Retrieve Relevant Chunks
   │
   ▼
Groq LLM
   │
   ▼
Response
   │
   ▼
END
```

## Future Enhancements

* Multiple PDF support
* Persistent vector database (Chroma/Qdrant)
* User authentication
* Medical report summarization
* Report comparison
* Docker support
* Cloud deployment
* Multi-user session management
* Conversation export

## Tech Stack

* Python
* FastAPI
* Streamlit
* LangChain
* Groq LLM
* FAISS
* Hugging Face Embeddings
* PyPDF
* Pydantic
