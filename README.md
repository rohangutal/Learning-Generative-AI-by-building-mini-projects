# 🚀 Learning Generative AI by Building Mini Projects

Welcome to **Learning Generative AI by Building Mini Projects**! This repository is a curated collection of practical hands-on mini-projects, interactive Streamlit applications, and Jupyter Notebooks designed to master modern Generative AI techniques, Large Language Models (LLMs), AI Agents, and RAG/SQL Toolkits.

---

## 📌 Repository Overview

This project explores building real-world AI applications using:
- **LangChain** & **LangGraph** (Agent workflows, memory checkpointers, tool integration)
- **Groq** & **OpenRouter** & **Ollama** (High-speed inference, open-source & local LLMs)
- **Streamlit** (Interactive web applications)
- **Google Serper API** (Real-time web search integration)
- **SQLDatabaseToolkit** (Natural language database querying with SQLite)

---

## 📂 Project Structure

```
├── apps/
│   ├── 1_QNA_Chatbot.py           # Streamlit Q&A Chatbot with OpenRouter & session memory
│   ├── 2_google_search_agent.py   # CLI search agent using ChatGroq & Google Serper
│   ├── 3_chatbot_using_groq.py    # Streamlit search assistant with streaming responses
│   └── 4_sql_task_manager.py      # Natural language SQL Task Manager (SQLite + Groq toolkit)
├── notebooks/
│   ├── 1_basic_langchain_chatbot.ipynb  # Getting started with LangChain LLMs
│   ├── 2_ollama_app.ipynb               # Integrating local models via Ollama
│   ├── 3_Groq_langchain.ipynb            # Fast inference with Groq and LangChain
│   ├── 4_streaming_response.ipynb       # Real-time token streaming techniques
│   ├── 5_basic_agent.ipynb              # Tool calling and agent creation
│   └── 6_google_search_agent.ipynb      # Building search agents with LangGraph
├── requirements.txt
└── README.md
```

---

## 🛠️ App Descriptions

### 1. 🤖 AskBuddy - AI Q&A Bot (`apps/1_QNA_Chatbot.py`)
- **Framework:** Streamlit + LangChain + OpenRouter
- **Features:** Conversational chatbot with session state memory that interfaces with open models hosted on OpenRouter.

### 2. 🔍 Google Search Agent CLI (`apps/2_google_search_agent.py`)
- **Framework:** LangGraph + ChatGroq + Google Serper API
- **Features:** A CLI agent equipped with web search capabilities and LangGraph checkpointer memory.

### 3. ⚡ QuickAnswer Streamlit Assistant (`apps/3_chatbot_using_groq.py`)
- **Framework:** Streamlit + LangGraph + ChatGroq
- **Features:** Web search assistant streaming real-time responses to user queries in a Streamlit chat interface.

### 4. 📜 TaskBot - SQL Task Manager (`apps/4_sql_task_manager.py`)
- **Framework:** Streamlit + LangChain SQLDatabaseToolkit + SQLite + Groq
- **Features:** Manage tasks using natural language! Insert, view, update, and delete tasks in an SQLite database using an AI SQL agent.

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/rohangutal/Learning-Generative-AI-by-building-mini-projects.git
cd Learning-Generative-AI-by-building-mini-projects
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure `.env`
Create a `.env` file in the root directory and add your API keys:
```env
OPENROUTER_API_KEY=your_openrouter_key
GROQ_API_KEY=your_groq_key
SERPER_API_KEY=your_serper_key
```

### 4. Run a Streamlit App
```bash
streamlit run apps/4_sql_task_manager.py
```

---

## 📄 License
Distributed under the MIT License. See `LICENSE` for more information.
