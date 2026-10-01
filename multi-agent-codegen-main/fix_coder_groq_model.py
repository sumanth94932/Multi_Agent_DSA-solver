import os

filepath = "agents/coder.py"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

import re
content = re.sub(r'model="qwen/qwen3\.8-27b"', 'model="openai/gpt-oss-120b"', content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Updated {filepath}")
