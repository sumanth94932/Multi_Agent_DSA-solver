import glob

instruction = "\n\nBe extremely concise. Output only the requested plan or code. Do not include markdown essays, chit-chat, or verbose commentary."

for filepath in glob.glob("prompts/*.md"):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "Be extremely concise" not in content:
        content += instruction
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")
