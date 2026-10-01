import os
from dotenv import load_dotenv
load_dotenv()

import os
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="openai/gpt-oss-120b",
    base_url="https://api.groq.com/openai/v1",
    api_key=os.environ.get("GROQ_API_KEY")
)

try:
    res = llm.invoke("Hi")
    print("? openai/gpt-oss-120b works!")
except Exception as e:
    print(f"? Failed: {e}")
