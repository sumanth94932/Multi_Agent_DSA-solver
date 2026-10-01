import os
from dotenv import load_dotenv
load_dotenv()

import os
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="qwen/qwen3.8-27b",
    base_url="https://api.groq.com/openai/v1",
    api_key=os.environ.get("GROQ_API_KEY")
)

try:
    res = llm.invoke("Hi")
    print("? qwen/qwen3.8-27b works on Groq!")
except Exception as e:
    print(f"? Failed: {e}")
