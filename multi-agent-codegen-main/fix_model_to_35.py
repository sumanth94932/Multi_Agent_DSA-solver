import glob

for filepath in glob.glob("agents/*.py"):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "gemini-3.6-flash" in content:
        content = content.replace("gemini-3.6-flash", "gemini-3.5-flash")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")
