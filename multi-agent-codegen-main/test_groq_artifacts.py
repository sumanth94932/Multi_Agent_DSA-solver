import os
from dotenv import load_dotenv
load_dotenv()

import os
from langchain_openai import ChatOpenAI
from models.schemas import ArtifactList
from langchain_core.messages import HumanMessage

llm = ChatOpenAI(
    model="qwen/qwen3.8-27b",
    base_url="https://api.groq.com/openai/v1",
    api_key=os.environ.get("GROQ_API_KEY")
).with_structured_output(ArtifactList)

try:
    res = llm.invoke([HumanMessage(content="Write a hello world python script.")])
    print(res)
except Exception as e:
    print(f"Failed: {e}")
