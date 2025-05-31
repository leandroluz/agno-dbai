# 🧠 D.B.A.I. – Agente Inteligente para Bancos PostgreSQL Legados

D.B.A.I. (Database Artificial Intelligence) é um assistente conversacional construído com [Agno](https://github.com/arthurdejong/agno) e [Streamlit](https://streamlit.io/) para ajudar desenvolvedores e analistas a interagir com bancos de dados PostgreSQL legados.

Este agente é capaz de:

- Solicitar dados de conexão via chat (host, porta, banco, usuário, senha).
- Armazenar várias conexões nomeadas durante a sessão.
- Executar comandos SQL diretamente no banco ativo.
- Lembrar o contexto da conversa e responder com precisão.

---

## 🚀 Como usar

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/agno-dbai.git
cd agno-dbai
```

### 2. Crie e ative um ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # ou .\venv\Scripts\activate no Windows
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Configure seu arquivo `.env`
Crie um arquivo `.env` com o seguinte conteúdo:

```env
OPENAI_API_KEY=sk-sua-chave-aqui
OPENAI_MODEL=gpt-4o
```

> Use `gpt-4o` ou `gpt-3.5-turbo` conforme sua assinatura da OpenAI.

### 5. Rode a aplicação
```bash
streamlit run app.py
```

Acesse no navegador em `http://localhost:8501`

---

## 🧠 Funcionamento do Agente

- Ao iniciar, o agente perguntará se você deseja configurar uma conexão.
- Os dados são armazenados internamente por nome da conexão.
- Quando você enviar perguntas como:

```
Liste todas as tabelas.
Quantos registros tem na tabela usuarios?
Me retorne os 10 primeiros registros da tabela clientes.
```

O D.B.A.I. irá usar a conexão ativa e executar o comando real no banco.

---

## 📁 Estrutura do Projeto

```
.
├── app.py
├── .env.example
├── requirements.txt
├── tools
│   └── sql_manager.py
└── tmp
    └── dbai_memory.db  # gerado em tempo de execução
```

---

## 🛠 Ferramentas utilizadas
- [Agno](https://github.com/arthurdejong/agno)
- [Streamlit](https://streamlit.io/)
- [psycopg2](https://pypi.org/project/psycopg2/)
- [OpenAI Python SDK](https://pypi.org/project/openai/)

---

## 📝 Licença
Este projeto é livre para uso e adaptação. Credite D.B.A.I. ao reutilizar o conceito. ✌️
