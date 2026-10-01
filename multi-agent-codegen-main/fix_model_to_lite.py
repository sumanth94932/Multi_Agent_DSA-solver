import glob

for filepath in glob.glob("agents/*.py"):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We might have gemini-3.5-flash or gemini-3.6-flash or gemini-2.5-flash right now.
    import re
    content = re.sub(r'model="gemini-[\d\.]+-flash"', 'model="gemini-2.5-flash-lite"', content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")
