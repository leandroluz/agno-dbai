import psycopg2
from agno.tools import tool
from typing import Dict

# Conexões nomeadas
CONEXOES_POSTGRESQL: Dict[str, Dict[str, str]] = {}

@tool(name="definir_conexao_postgresql", description="Armazena os parâmetros de conexão com o banco PostgreSQL.")
def definir_conexao_postgresql(nome_conexao: str, host: str, port: str, database: str, user: str, password: str) -> str:
    CONEXOES_POSTGRESQL[nome_conexao] = {
        "host": host,
        "port": port,
        "database": database,
        "user": user,
        "password": password
    }
    return f"✅ Conexão '{nome_conexao}' salva com sucesso."

@tool(name="executar_sql_postgresql", description="Executa uma query SQL em uma conexão PostgreSQL previamente definida.")
def executar_sql_postgresql(nome_conexao: str, query: str) -> str:
    if nome_conexao not in CONEXOES_POSTGRESQL:
        return f"❌ Conexão '{nome_conexao}' não encontrada. Use 'definir_conexao_postgresql' primeiro."

    conn_info = CONEXOES_POSTGRESQL[nome_conexao]

    try:
        conn = psycopg2.connect(**conn_info)
        cur = conn.cursor()
        cur.execute(query)
        if cur.description:
            colnames = [desc[0] for desc in cur.description]
            rows = cur.fetchall()
            cur.close()
            conn.close()
            resultado = [dict(zip(colnames, row)) for row in rows]
            return str(resultado)
        else:
            conn.commit()
            cur.close()
            conn.close()
            return "✅ Comando executado com sucesso (sem retorno)."
    except Exception as e:
        return f"⚠️ Erro ao executar comando: {str(e)}"
