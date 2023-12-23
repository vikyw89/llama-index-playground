from dotenv import load_dotenv
load_dotenv()
from llama_index.agent import OpenAIAgent
from llama_index.llms import OpenAI
from tools import obj_index
import os

llm = OpenAI(model="gpt-3.5-turbo", api_key=os.getenv("OPENAI_API_KEY"))
tool_retriever = obj_index.as_retriever()
from tools import all_tools
agent = OpenAIAgent.from_tools(
    tool_retriever=tool_retriever,
    chat_history=[],
    llm=llm,
    verbose=True,
)
