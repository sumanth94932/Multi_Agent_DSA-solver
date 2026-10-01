import glob

for filepath in ["agents/orchestrator.py", "agents/planner.py"]:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace('model="llama-3.3-70b-versatile"', 'model="openai/gpt-oss-120b"')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")
