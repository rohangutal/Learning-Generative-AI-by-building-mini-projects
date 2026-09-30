from dotenv import load_dotenv      
load_dotenv()

from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver 

llm = ChatGroq(model="openai/gpt-oss-120b")
search = GoogleSerperAPIWrapper()

agent = create_agent(
    model = llm,
    tools=[search.run],
    checkpointer = MemorySaver(),
    system_prompt="You are a agent and can search any question on google"
)

while True:
    query = input("User: ")
    if query.lower() == "exit":
        print("Agent: Goodbye!")
        break
    response = agent.invoke(
        {"messages":[{"role":"user","content":query}]},
        {"configurable": {"thread_id": "asd1234"}}
        )
    print("Agent:", response["messages"][-1].content)









