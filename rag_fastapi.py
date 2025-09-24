import os
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from langchain_ollama import OllamaLLM
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import Chroma
from langchain.embeddings import SentenceTransformerEmbeddings

app = FastAPI()

# --- Configuración RAG ---
pdf_store = os.path.join(os.path.dirname(__file__), "chroma_store")
llm = OllamaLLM(model="gemma3:1b", base_url="http://localhost:11434")
embedder = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
vectordb = Chroma(persist_directory=pdf_store, embedding_function=embedder)
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=vectordb.as_retriever(), chain_type="stuff")


class Query(BaseModel):
    question: str

@app.get("/")
async def root():
    return {"message": "Go to /docs for the API documentation."}

@app.post("/ask")
async def ask(query: Query):
    def generate():
        result = qa_chain.run(query.question)
        for token in result.split():
            yield token + " "
    return StreamingResponse(generate(), media_type="text/plain")