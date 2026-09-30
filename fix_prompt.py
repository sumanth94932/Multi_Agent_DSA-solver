filepath = r'c:\Users\cc221\Downloads\multi-agent-codegen-main\multi-agent-codegen-main\prompts\coder.md'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

content += "\n\nCRITICAL: You MUST return a JSON object with a single top-level key called rtifacts. The value must be a list of code files."
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
