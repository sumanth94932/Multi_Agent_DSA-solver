filepath = r'c:\Users\cc221\Downloads\multi-agent-codegen-main\multi-agent-codegen-main\scripts\run_evals.py'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()
content = content.replace('with path.open() as f:', 'with path.open(encoding="utf-8") as f:')
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
