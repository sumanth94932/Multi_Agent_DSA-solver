import glob

for filepath in glob.glob("agents/*.py"):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "gemini-2.5-flash" in content:
        content = content.replace("gemini-2.5-flash", "gemini-3.8-flash")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")
