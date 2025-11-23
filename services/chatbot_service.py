import os
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import openai

# Load environment variables for OpenAI key
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

class ChatbotService:
    """
    Service to handle chatbot logic:
    - Embedding generation
    - Vector DB storage and retrieval (FAISS)
    - LLM completion via OpenAI
    """

    def __init__(self):
        # Load a sentence-transformer model for embeddings
        self.embed_model = SentenceTransformer('all-MiniLM-L6-v2')

        # FAISS index initialization (dim = embedding size)
        self.dim = 384  # all-MiniLM-L6-v2 embedding size
        self.index = faiss.IndexFlatL2(self.dim)

        # Placeholder for text data corresponding to embeddings
        self.texts = []

        # Optional: Load saved FAISS index if exists
        if os.path.exists("data/faiss_index.bin"):
            self.load_index()

    def add_texts(self, new_texts):
        """
        Add new texts to the FAISS vector store.
        """
        embeddings = self.embed_model.encode(new_texts)
        self.index.add(np.array(embeddings, dtype='float32'))
        self.texts.extend(new_texts)
        self.save_index()

    def save_index(self):
        """
        Persist FAISS index and texts to disk.
        """
        faiss.write_index(self.index, "data/faiss_index.bin")
        np.save("data/texts.npy", np.array(self.texts))

    def load_index(self):
        """
        Load FAISS index and texts from disk.
        """
        self.index = faiss.read_index("data/faiss_index.bin")
        self.texts = np.load("data/texts.npy", allow_pickle=True).tolist()

    def retrieve_relevant_texts(self, query, top_k=3):
        """
        Retrieve top_k relevant texts from FAISS based on query embedding.
        """
        query_embedding = self.embed_model.encode([query])
        D, I = self.index.search(np.array(query_embedding, dtype='float32'), top_k)
        return [self.texts[i] for i in I[0] if i < len(self.texts)]

    def get_response(self, query):
        """
        Main function to handle a user query:
        1. Retrieve relevant texts from FAISS
        2. Call OpenAI ChatCompletion API with context
        """
        # Retrieve context
        relevant_texts = self.retrieve_relevant_texts(query)
        context = "\n".join(relevant_texts) if relevant_texts else "No relevant context found."

        # Construct prompt for OpenAI
        prompt = f"Context:\n{context}\n\nUser: {query}\nAI:"

        # Call OpenAI ChatCompletion API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an intelligent assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.7
        )

        return response['choices'][0]['message']['content'].strip()
