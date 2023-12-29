from typing import Iterable
from dotenv import load_dotenv

load_dotenv()
from llama_index.agent import OpenAIAgent
from llama_index.llms import OpenAI, ChatMessage
from tools import obj_index
import os

llm = OpenAI(model="gpt-3.5-turbo", api_key=os.getenv("OPENAI_API_KEY"))
tool_retriever = obj_index.as_retriever()
agent = OpenAIAgent.from_tools(
    tool_retriever=tool_retriever,
    chat_history=[],
    llm=llm,
    verbose=True,
)
async def chat_agent_generate(chat_messages: list[ChatMessage] = []) -> Iterable[str]:
    # split chat messages history from user response
    if len(chat_messages) == 0:
        raise ValueError("chat_messages cannot be empty")
    last_message = chat_messages.pop(-1)
    agent = OpenAIAgent.from_tools(
        tool_retriever=tool_retriever,
        chat_history=chat_messages,
        llm=llm,
        verbose=True,
    )
    response = await agent.astream_chat("test")

    async for token in response.async_response_gen():
        yield token