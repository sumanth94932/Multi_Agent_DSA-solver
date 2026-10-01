import os
from dotenv import load_dotenv
load_dotenv()

import os
from langchain_google_genai import ChatGoogleGenerativeAI

api_key = os.environ.get("GOOGLE_API_KEY")

models_to_test = [
    "gemini-3.7-flash",
    "gemini-3.8-flash",
    "gemini-3.8-pro",
    "gemini-4.0-flash",
]

for model_name in models_to_test:
    try:
        llm = ChatGoogleGenerativeAI(model=model_name, google_api_key=api_key)
        res = llm.invoke("Hi")
        print(f"? {model_name} works!")
    except Exception as e:
        print(f"? {model_name} failed: {type(e).__name__} - {str(e)[:100]}")
