🩺 MediBridge

MediBridge is an AI-powered medical report assistant that leverages Retrieval-Augmented Generation (RAG) to help users better understand their medical reports. Instead of manually searching through lengthy reports, users can upload a PDF and ask questions in natural language. The application retrieves the most relevant information from the report using semantic search and generates accurate, context-aware responses with a Large Language Model (LLM).

The project combines FastAPI, Streamlit, LangChain, FAISS, and Groq LLM to provide an interactive and intelligent medical document question-answering experience.

✨ Features
📄 Upload medical reports in PDF format
💬 Ask questions about the uploaded report in natural language
🧠 Retrieval-Augmented Generation (RAG) for accurate, context-aware responses
🔍 Semantic document retrieval using FAISS vector database
🤖 AI-powered responses using Groq LLM
📝 Automatic PDF parsing and intelligent document chunking
💭 Session-based conversational chat with memory
⚡ FastAPI backend with RESTful APIs
🎨 Interactive and user-friendly Streamlit interface
🛠️ Tech Stack
Backend
Python
FastAPI
LangChain
Pydantic
Frontend
Streamlit
AI & Machine Learning
Groq LLM (Llama 3)
Hugging Face Sentence Transformers
Retrieval-Augmented Generation (RAG)
Vector Database
FAISS
Document Processing
PyPDF
Recursive Character Text Splitter
🚀 How It Works
Upload a medical report in PDF format.
The PDF is parsed and converted into text.
The document is split into smaller chunks for efficient retrieval.
Each chunk is converted into vector embeddings using a Hugging Face embedding model.
The embeddings are stored in a FAISS vector database.
When a user asks a question, the system retrieves the most relevant chunks from the document.
The retrieved context is combined with the user's query and sent to the Groq LLM.
The AI generates a context-aware response based on the uploaded medical report.
📂 Key Features of the Architecture
Clean separation of backend and frontend
Modular service-based architecture
Session-based vector store management
Retrieval-Augmented Generation pipeline
RESTful APIs built with FastAPI
Interactive chat interface using Streamlit
Easily extensible for additional document types and AI models
⚙️ Run Locally
Clone the Repository
git clone https://github.com/<your-username>/MediBridge.git
cd MediBridge
Install Dependencies
pip install -r requirements.txt
Configure Environment Variables

Create a .env file in the project root and add your Groq API key:

GROQ_API_KEY=your_api_key
MODEL_NAME=llama-3.3-70b-versatile
Start the Backend
uvicorn backend.main:app --reload
Start the Frontend
streamlit run frontend/streamlit_app.py
