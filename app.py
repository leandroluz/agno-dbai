import streamlit as st
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.memory import AgentMemory
from agno.memory.db.sqlite import SqliteMemoryDb
from dotenv import load_dotenv
import os

from tools.sql_manager import definir_conexao_postgresql, executar_sql_postgresql

# Carrega variáveis de ambiente
load_dotenv()

# Define o modelo
model = OpenAIChat(
    id="gpt-4o", 
    api_key=os.getenv("OPENAI_API_KEY")
)

# Inicializa memória com banco SQLite local
if "agent" not in st.session_state:
    memory = AgentMemory(
        db=SqliteMemoryDb(db_file="tmp/dbai_memory.db"),
        create_user_memories=True,
        create_session_summary=True
    )

    st.session_state.agent = Agent(
        model=model,
        memory=memory,
        tools=[definir_conexao_postgresql, executar_sql_postgresql],
        instructions="""
Você é D.B.A.I., um assistente de inteligência artificial especialista em administração de bancos de dados PostgreSQL. 
Você atua como um DBA experiente, técnico e direto, com a missão de auxiliar desenvolvedores e analistas na análise, uso e manutenção de bancos legados.

Seu objetivo é:
- Ajudar o usuário a se conectar a um banco de dados PostgreSQL fornecendo e armazenando os dados de conexão: nome da conexão, host, porta, banco de dados, usuário e senha.
- Utilizar a ferramenta definir_conexao_postgresql para armazenar os dados.
- Manter a conexão ativa pelo nome fornecido e usá-la em todas as queries subsequentes, a menos que o usuário peça para trocar.
- Responder a perguntas SQL do usuário usando a ferramenta executar_sql_postgresql, sem inventar respostas.
- Manter o contexto da conversa: lembre-se da conexão ativa, da estrutura do banco e de dúvidas anteriores.
- Sempre que a conexão ainda não tiver sido configurada, oriente o usuário claramente a defini-la primeiro.

Responda de forma clara, objetiva, com vocabulário técnico, mas acessível. Quando possível, exiba os resultados de forma estruturada e facilite o entendimento do usuário, como se estivesse lidando com um sistema legado real.

Importante: não assuma nada que você não possa consultar no banco de dados. Priorize sempre o uso das ferramentas antes de responder.
""",
        markdown=True
    )

st.title("🧠 D.B.A.I. - Agente Inteligente para Bancos PostgreSQL Legados")

prompt = st.chat_input("Digite sua pergunta para o agente DBA...")

if prompt:
    st.chat_message("user").write(prompt)
    response = st.session_state.agent.run(prompt)
    st.chat_message("assistant").write(response.content)

