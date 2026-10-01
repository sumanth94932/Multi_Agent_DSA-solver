import os
from dotenv import load_dotenv
load_dotenv()

import os
import glob
import re

base_path = r'c:\Users\cc221\Downloads\multi-agent-codegen-main\multi-agent-codegen-main\agents\*.py'

def replace_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace import
    content = re.sub(r'from langchain_anthropic import ChatAnthropic', r'from langchain_openai import ChatOpenAI', content)

    # Replace get_llm definition
    # We will match the entire def get_llm(...) -> ChatAnthropic: block
    
    # We need a robust regex or just manual replace.
    # Because tester has a different signature.
    
    if 'def get_llm() -> ChatAnthropic:' in content:
        new_def = '''def get_llm() -> ChatOpenAI:
    return ChatOpenAI(
        model="openrouter/free",
        base_url="https://openrouter.ai/api/v1",
        api_key=os.environ.get("OPENROUTER_API_KEY"),
        temperature=0.2,
        callbacks=[BudgetCallbackHandler()],
    )'''
        content = re.sub(r'def get_llm\(\) -> ChatAnthropic:[\s\S]*?\)\n', new_def + '\n', content)
        
    elif 'def get_llm(model: str | None = None) -> ChatAnthropic:' in content:
        new_def = '''def get_llm(model: str | None = None) -> ChatOpenAI:
    return ChatOpenAI(
        model="openrouter/free",
        base_url="https://openrouter.ai/api/v1",
        api_key=os.environ.get("OPENROUTER_API_KEY"),
        temperature=0.2,
        callbacks=[BudgetCallbackHandler()],
    )'''
        content = re.sub(r'def get_llm\(model: str \| None = None\) -> ChatAnthropic:[\s\S]*?\)\n', new_def + '\n', content)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for filepath in glob.glob(base_path):
    replace_in_file(filepath)

print('Done')
