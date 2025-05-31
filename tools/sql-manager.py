from agno.tools.base import Tool
import psycopg2

class PostgreSQLMultiConnectionTool(Tool):
    def __init__(self):
        self.connections = {}  # nome -> dict de params
        self.active_connection = None
        self.step_state = {}

    def run(self, input_text: str) -> str:
        user_id = "default"  # Pode ser estendido para múltiplos usuários
        if user_id not in self.step_state:
            self.step_state[user_id] = {"step": None, "data": {}}

        state = self.step_state[user_id]

        if input_text.lower().startswith("usar conexão"):
            nome = input_text.split("usar conexão", 1)[-1].strip()
            if nome in self.connections:
                self.active_connection = nome
                return f"🔄 Conexão ativa agora é '{nome}'."
            return "⚠️ Conexão não encontrada."

        if input_text.lower().strip() == "conectar":
            state["step"] = "nome"
            return "📌 Qual nome deseja dar a essa conexão?"

        if state["step"] == "nome":
            state["data"]["nome"] = input_text.strip()
            state["step"] = "host"
            return "🔌 Digite o host (ex: 127.0.0.1):"

        elif state["step"] == "host":
            state["data"]["host"] = input_text.strip()
            state["step"] = "porta"
            return "🔢 Digite a porta (ex: 5432):"

        elif state["step"] == "porta":
            state["data"]["port"] = int(input_text.strip())
            state["step"] = "db"
            return "🗂️ Nome do banco de dados:"

        elif state["step"] == "db":
            state["data"]["dbname"] = input_text.strip()
            state["step"] = "user"
            return "👤 Nome do usuário:"

        elif state["step"] == "user":
            state["data"]["user"] = input_text.strip()
            state["step"] = "senha"
            return "🔐 Senha do banco de dados:"

        elif state["step"] == "senha":
            state["data"]["password"] = input_text.strip()
            nome = state["data"]["nome"]
            self.connections[nome] = state["data"].copy()
            self.active_connection = nome
            self.step_state[user_id] = {"step": None, "data": {}}
            return f"✅ Conexão '{nome}' salva e ativa com sucesso."

        if not self.active_connection:
            return "⚠️ Nenhuma conexão ativa. Use o comando 'conectar' ou 'usar conexão <nome>'."

        try:
            conn = psycopg2.connect(**self.connections[self.active_connection])
            cur = conn.cursor()
            cur.execute(input_text)
            if cur.description:
                cols = [desc[0] for desc in cur.description]
                rows = cur.fetchall()
                return str([dict(zip(cols, row)) for row in rows])
            return "✅ Comando executado com sucesso."
        except Exception as e:
            return f"❌ Erro ao executar SQL: {e}"
