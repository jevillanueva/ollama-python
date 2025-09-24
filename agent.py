from langchain_ollama import OllamaLLM
from langchain.agents import initialize_agent, Tool
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_experimental.utilities.python import PythonREPL

# 1. LLM (Gemma en Ollama)
llm = OllamaLLM(model="gemma3:1b", base_url="http://localhost:11434")

# 2. Definir herramientas
wiki = WikipediaAPIWrapper()
python_repl = PythonREPL()

tools = [
    Tool(
        name="Wikipedia",
        func=wiki.run,
        description="Usa esto para buscar información en Wikipedia"
    ),
    Tool(
        name="PythonREPL",
        func=python_repl.run,
        description="Usa esto para hacer cálculos o ejecutar código Python"
    )
]

# 3. Crear agente
agent = initialize_agent(
    tools, llm,
    agent="zero-shot-react-description",
    verbose=True
)

# 4. Probar agente
print(agent.run("¿Cuál es la raíz cuadrada de la población de Francia según Wikipedia?"))
