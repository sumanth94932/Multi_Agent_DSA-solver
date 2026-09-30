filepath = r'c:\Users\cc221\Downloads\multi-agent-codegen-main\multi-agent-codegen-main\app.py'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('ANTHROPIC_API_KEY', 'OPENROUTER_API_KEY')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
