import os
from dotenv import load_dotenv
load_dotenv()

import os

filepath = "agents/coder.py"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace OpenRouter URL, key, and model
import re
content = re.sub(r'model="qwen/qwen3\.8-27b:free"', 'model="qwen/qwen3.8-27b"', content)
content = re.sub(r'base_url="https://openrouter\.ai/api/v1"', 'base_url="https://api.groq.com/openai/v1"', content)
content = re.sub(r'api_key=os\.environ\.get\("OPENROUTER_API_KEY",[^)]+\)', 'api_key=os.environ.get("GROQ_API_KEY", os.environ.get("GROQ_API_KEY"))', content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Updated {filepath}")
