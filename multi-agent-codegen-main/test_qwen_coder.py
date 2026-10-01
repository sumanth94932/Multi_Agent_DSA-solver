import os
from dotenv import load_dotenv
load_dotenv()

import os
import sys
import json

os.environ['OPENROUTER_API_KEY'] = os.environ.get("OPENROUTER_API_KEY")

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from pydantic import BaseModel
from models.schemas import CodeArtifact

class ArtifactList(BaseModel):
    artifacts: list[CodeArtifact]

llm = ChatOpenAI(
    model="qwen/qwen3.8-27b:free",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ['OPENROUTER_API_KEY'],
    max_retries=1
)
structured_llm = llm.with_structured_output(ArtifactList)

messages = [
    HumanMessage(content="Write a Python script that prints 'hello world'. Ensure it is in a file called main.py.")
]

try:
    res = structured_llm.invoke(messages)
    print("Success. Artifacts:")
    for a in res.artifacts:
        print(f"- {a.filename}")
except Exception as e:
    print(f"Error: {e}")
