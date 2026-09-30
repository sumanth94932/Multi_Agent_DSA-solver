filepath = r'c:\Users\cc221\Downloads\multi-agent-codegen-main\multi-agent-codegen-main\pyproject.toml'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('"langchain-anthropic>=0.3.0",', '"langchain-openai>=0.3.0",')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
