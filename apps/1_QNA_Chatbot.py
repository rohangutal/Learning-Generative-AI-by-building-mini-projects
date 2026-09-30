import os
from dotenv import load_dotenv
import streamlit as st
from langchain_openai import ChatOpenAI

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

llm = ChatOpenAI(
    model="liquid/lfm-2.5-2.6b:free",
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1",
    temperature=0.7,
)

st.title("🤖 AskBuddy 🤖 AI QnA Bot")
st.markdown("My QnA Bot with LangChain and OpenRouter !")

# Initialize conversation memory in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display message history
for message in st.session_state.messages:
    role = message["role"]
    content = message["content"]
    st.chat_message(role).markdown(content)

# Chat input block with memory implementation
query = st.chat_input("Ask anything ?")
if query:
    st.session_state.messages.append({"role": "user", "content": query})
    st.chat_message("user").markdown(query)

    res = llm.invoke(st.session_state.messages)

    st.chat_message("ai").markdown(res.content)
    st.session_state.messages.append({"role": "ai", "content": res.content})
