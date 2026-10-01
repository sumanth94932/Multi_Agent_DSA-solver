import glob

for filepath in glob.glob("agents/*.py"):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    import re
    content = re.sub(r'model="gemini-2.5-flash-lite"', 'model="gemini-3.5-flash-lite"', content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")
