# 🧠 D.B.A.I. – Assistente Inteligente para Sistemas Legados

D.B.A.I. (Database Artificial Intelligence) é um assistente interativo que atua como um DBA e desenvolvedor PHP experiente, com suporte a vários bancos de dados PostgreSQL (inclusive versões legadas como 8.2). Ele se conecta a diferentes bancos via chat e ajuda você a:

* Executar queries SQL
* Gerar e entender relatórios
* Criar, revisar e explicar código PHP
* Manter e evoluir sistemas legados com inteligência artificial

## 🚀 Funcionalidades

* 🔄 Conecta-se a diversos bancos PostgreSQL via conversa
* 🧠 Memória persistente das conversas e perguntas
* 💬 Interface de chat via Streamlit
* 🧾 Suporte a queries SQL e código PHP
* 🛠 Ferramentas personalizadas baseadas no framework Agno

## 🧰 Requisitos

* Python 3.10+
* pip
* OpenAI API Key

## 📦 Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/dbai.git
cd dbai
```

Crie o ambiente virtual e instale as dependências:

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Crie um arquivo `.env` com sua chave da OpenAI:

```
OPENAI_API_KEY=sk-sua-chave-aqui
```

## ▶️ Executando

```bash
streamlit run app.py
```

Abra o navegador em `http://localhost:8501`

## 💬 Comandos que você pode usar no chat

```txt
conectar
usar conexão sap_guarei
SELECT * FROM usuarios;
Corrija esse PHP: $user = $_POST['nome];
Explique o que essa função faz: function loadData() {...}
```

## 📁 Estrutura do projeto

```
/
├── app.py                         # Interface de chat com Streamlit
├── tools/
│   ├── sql_manager.py            # Ferramenta de conexão e execução SQL
│   └── php_assistant.py          # Ferramenta para código PHP
├── tmp/                          # Banco de memória local
│   └── agent_memory.db
├── .env                          # Chave da OpenAI (não versionar!)
├── requirements.txt              # Dependências do projeto
└── README.md
```

## 📜 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais informações.

---

Feito com ❤️ usando [Agno](https://www.agno.com) por [Leandro Luz](https://github.com/seu-usuario)
