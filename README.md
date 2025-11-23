# AI Chatbot with Semantic Search

A **Flask-based AI chatbot** leveraging **OpenAI GPT** and **FAISS vector database** for context-aware, intelligent responses. This project demonstrates an **end-to-end NLP pipeline** using embeddings for semantic search and retrieval-augmented generation (RAG).  

---

## Features

- **Context-aware responses** powered by OpenAI’s GPT models.  
- **Semantic search** using FAISS and Sentence Transformers embeddings.  
- **Modular architecture** with clear separation of controllers and services.  
- **Persistent vector storage** for retaining knowledge across sessions.  
- Easily extendable for **personal or portfolio projects**.  

---

## Tech Stack

- **Backend:** Flask  
- **AI/ML:** OpenAI GPT-3.5-turbo, Sentence Transformers  
- **Vector Database:** FAISS  
- **Data:** NumPy for embedding storage  
- **Environment Management:** python-dotenv  

---

## Installation

1. Clone the repository:

git clone https://github.com/your-username/chatbot.git
cd chatbot

2. Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

3. Install dependencies:

pip install -r requirements.txt

4. Create a `.env` file in the root directory and add your OpenAI API key:

OPENAI_API_KEY=your_openai_api_key

---

## Usage

1. Run the Flask app:

python app.py

2. Send a POST request to the chatbot API:

POST http://127.0.0.1:5000/api/chat
Content-Type: application/json

{
  "query": "Hello, how are you?"
}

3. Receive a response from the AI chatbot:

{
  "response": "Hello! I'm an AI chatbot. How can I assist you today?"
}

---

## How It Works

1. **User Query → Embedding**  
   - The input query is converted into a numeric embedding using a pre-trained **Sentence Transformer**.  

2. **Vector Search in FAISS**  
   - The embedding is used to retrieve the **most similar texts** from the FAISS index.  

3. **Context + Query → GPT**  
   - Retrieved texts are sent as context to **OpenAI GPT**, generating an intelligent response.  

4. **Return Response**  
   - The response is sent back to the user via the API.  

> Note: FAISS stores **embeddings**, not readable text. Data retrieval is based on similarity search.  

---

## Future Improvements

- Add **authentication** for API requests.  
- Dockerize the app for **easy deployment**.  
- Integrate with **web UI or messaging platforms**.  
- Automate **data indexing** for larger knowledge bases.  

---
