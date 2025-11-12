# chat_agent.py
import os
import sys

# Use absolute import for the utils module
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.google_llm import create_google_llm


class ChatAgent:
    def __init__(self, faiss_index_path=None, llm=None, embeddings=None):
        # Delay creation of embeddings/LLM objects until actually needed.
        self.embeddings = embeddings  # may be None; initialize later if needed
        self.llm = llm
        self.faiss_index_path = faiss_index_path

    def _ensure_llm_and_embeddings(self):
        # Initialize llm and embeddings if they weren't provided.
        try:
            from langchain_openai import OpenAIEmbeddings
            from langchain_openai import ChatOpenAI
        except Exception:
            OpenAIEmbeddings = None
            ChatOpenAI = None

        if self.embeddings is None:
            if OpenAIEmbeddings is not None:
                self.embeddings = OpenAIEmbeddings()
            else:
                self.embeddings = None

        if self.llm is None:
            if os.environ.get("GOOGLE_API_KEY"):
                self.llm = create_google_llm()
            elif ChatOpenAI is not None:
                self.llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.1)
            else:
                self.llm = None

    def build_chain(self, retriever):
        # Import conversational chain lazily
        try:
            from langchain.chains import ConversationalRetrievalChain
        except Exception:
            raise RuntimeError("langchain is required for conversational retrieval chain")

        # Ensure llm is available
        self._ensure_llm_and_embeddings()
        if self.llm is None:
            raise RuntimeError("No LLM is configured for ChatAgent")

        return ConversationalRetrievalChain.from_llm(
            self.llm,
            retriever=retriever,
            return_source_documents=True,
        )
