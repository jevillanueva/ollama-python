# Ollama con Python

Primero se tiene que instalar [Ollama](https://ollama.com/download).

Puede ser la version de Windows o Linux.

Para instalar la biblioteca de Ollama para Python, usa el siguiente comando:

```bash
pip install -r requirements.txt
```

El endpoint por defecto es `http://localhost:11434`, pero puedes cambiarlo creando una instancia de `Client`:

Ejemplo:

```bash
python hello.py
```

Para una llamada de chat con streaming:

```bash
python streaming.py
```


---

Para uso de RAG (Recuperación Augmentada por Generación), se instala

los paquetes adicionales listados en `requirements.rag.txt`.

```bash
pip install -r requirements.rag.txt
```

Donde: 
- `langchain` es para la gestión de cadenas de lenguaje.
- `chromadb` es para la base de datos de vectores.  
- `pypdf` es para manejar archivos PDF.

Donde la idea del RAG es usar un modelo de Ollama para responder preguntas basadas en documentos que se cargan en una base de datos de vectores.

Ejemplo:

```bash
python rag.py
```