import os
from dotenv import load_dotenv
load_dotenv()

import os
import glob

# Python code to replace
new_llm_code = '''import os
from langchain_google_genai import ChatGoogleGenerativeAI
from utils import BudgetCallbackHandler

def get_llm():
    return ChatGoogleGenerativeAI(
        model="gemini-3.7-flash",
        temperature=0.2,
        max_tokens=1500,
        google_api_key=os.environ.get("GOOGLE_API_KEY", "PASTE_YOUR_GEMINI_API_KEY_HERE"),
        callbacks=[BudgetCallbackHandler()]
    )
'''

for file_path in glob.glob("agents/*.py"):
    if file_path.endswith("__init__.py"): continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We need to replace the get_llm function and imports.
    import re
    
    # Replace from langchain_openai import ChatOpenAI with the new imports
    content = re.sub(r'from langchain_openai import ChatOpenAI', 'from langchain_google_genai import ChatGoogleGenerativeAI', content)
    
    # Replace the get_llm function
    pattern = r'def get_llm\(\).*?:\n(?:\s+return ChatOpenAI\([\s\S]*?\)\n)'
    # Since they might have a type hint: def get_llm() -> ChatOpenAI:
    pattern2 = r'def get_llm\(\).*?:\n(?:\s+return ChatOpenAI\([^)]*\)\n)'
    
    # Let's just do a simpler replacement
    # find def get_llm() -> ...:
    # return ChatOpenAI( ... )
    
    # We will use regex to find def get_llm and replace the whole block
    def repl(m):
        return '''def get_llm():
    return ChatGoogleGenerativeAI(
        model="gemini-3.7-flash",
        temperature=0.2,
        max_tokens=1500,
        google_api_key=os.environ.get("GOOGLE_API_KEY", os.environ.get("GOOGLE_API_KEY")),
        callbacks=[BudgetCallbackHandler()]
    )
'''
    
    new_content = re.sub(r'def get_llm\(\).*?:\s+return ChatOpenAI\([\s\S]*?\n\s*\)\n', repl, content)
    
    if new_content == content:
        print(f"Failed to match in {file_path}")
    else:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file_path}")

