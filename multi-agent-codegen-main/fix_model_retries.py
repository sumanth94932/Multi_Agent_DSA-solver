import glob
import re

for filepath in glob.glob("agents/*.py"):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the model name
    content = content.replace('model="gemini-3.6-flash",', 'model="gemini-2.5-flash",')
    
    # Add max_retries if not present
    if "max_retries" not in content:
        content = content.replace('max_tokens=1500,', 'max_tokens=1500,\n        max_retries=6,')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")
