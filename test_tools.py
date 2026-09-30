import os
import sys

os.environ['OPENROUTER_API_KEY'] = 'YOUR_API_KEY_HERE'

from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

class TestOutput(BaseModel):
    success: bool = Field(description="Always true")
    message: str = Field(description="A greeting message")

models_to_test = [
    'google/gemma-4-31b-it:free',
    'qwen/qwen3.8-27b:free',
    'nvidia/nemotron-3-super-120b-a12b:free',
]

for model in models_to_test:
    print(f"Testing {model}...")
    try:
        llm = ChatOpenAI(
            model=model,
            base_url="https://openrouter.ai/api/v1",
            api_key=os.environ['OPENROUTER_API_KEY'],
            max_retries=0
        )
        structured_llm = llm.with_structured_output(TestOutput)
        res = structured_llm.invoke("Hello!")
        print("Success:", res)
    except Exception as e:
        print("Failed:", str(e)[:200])
