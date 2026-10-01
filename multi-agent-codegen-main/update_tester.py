import os
from dotenv import load_dotenv
load_dotenv()

import os
import re

file_path = "agents/tester.py"
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'from langchain_openai import ChatOpenAI', 'from langchain_google_genai import ChatGoogleGenerativeAI', content)

def repl(m):
    return '''def get_llm(model: str | None = None):
    return ChatGoogleGenerativeAI(
        model="gemini-3.7-flash",
        temperature=0.2,
        max_tokens=1500,
        google_api_key=os.environ.get("GOOGLE_API_KEY", os.environ.get("GOOGLE_API_KEY")),
        callbacks=[BudgetCallbackHandler()]
    )
'''

new_content = re.sub(r'def get_llm\(model: str \| None = None\).*?:\s+return ChatOpenAI\([\s\S]*?\n\s*\)\n', repl, content)

if new_content != content:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Updated tester.py")
else:
    print("Failed to update tester.py")
