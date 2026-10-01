import os
from dotenv import load_dotenv
load_dotenv()

import os

new_code = '''import os
from langchain_openai import ChatOpenAI
from utils import BudgetCallbackHandler

def get_llm():
    return ChatOpenAI(
        model="qwen/qwen3.8-27b:free",
        base_url="https://openrouter.ai/api/v1",
        api_key=os.environ.get("OPENROUTER_API_KEY", os.environ.get("OPENROUTER_API_KEY")),
        max_tokens=1500,
        callbacks=[BudgetCallbackHandler()]
    )
'''

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    import re
    content = re.sub(r'from langchain_google_genai import ChatGoogleGenerativeAI\n', '', content)
    content = re.sub(r'def get_llm\(\).*?:\n\s+return ChatGoogleGenerativeAI\([\s\S]*?\n\s*\)\n', '', content)
    
    content = new_code + "\n" + content
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")

update_file("agents/coder.py")
