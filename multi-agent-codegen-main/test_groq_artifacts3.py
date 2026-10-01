import os
from dotenv import load_dotenv
load_dotenv()

import os
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from langchain_core.messages import HumanMessage
from models.schemas import CodeArtifact

class ArtifactList(BaseModel):
    artifacts: list[CodeArtifact] = Field(
        description="A list of generated source code files.",
        default_factory=list,
    )

llm = ChatOpenAI(
    model="openai/gpt-oss-120b",
    base_url="https://api.groq.com/openai/v1",
    api_key=os.environ.get("GROQ_API_KEY")
).with_structured_output(ArtifactList)

try:
    res = llm.invoke([HumanMessage(content="Write a hello world python script.")])
    print(res)
except Exception as e:
    print(f"Failed: {e}")
