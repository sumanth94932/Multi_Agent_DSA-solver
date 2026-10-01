import glob

for filepath in glob.glob("agents/*.py"):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "temperature=0.2," in content:
        content = content.replace("        temperature=0.2,\n", "")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")
