import os
from langchain_ollama import OllamaLLM
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain.embeddings import SentenceTransformerEmbeddings

# 1. Cargar PDF (ruta relativa)
loader = PyPDFLoader(os.path.join(os.path.dirname(__file__), "sample.pdf"))
docs = loader.load()
texts = [d.page_content for d in docs]

# 2. Crear embeddings con un modelo compatible
embedder = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

# 3. Guardar en Chroma (Chroma generará los embeddings internamente)
vectordb = Chroma.from_texts(
    texts=texts,
    embedding=embedder,
    persist_directory=os.path.join(os.path.dirname(__file__), "chroma_store")
)

# 4. LLM: Gemma3 para generar respuestas
llm = OllamaLLM(model="gemma3:1b", base_url="http://localhost:11434")

# 5. Pipeline RAG
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectordb.as_retriever(),
    chain_type="stuff"
)

# 6. Interacción: hacer preguntas al PDF
while True:
    query = input("\nPregunta: ")
    if query.lower() in ["salir", "exit", "quit"]:
        break
    result = qa_chain.run(query)
    print("Respuesta:", result)
