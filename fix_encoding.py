filepath = r'c:\Users\cc221\Downloads\multi-agent-codegen-main\multi-agent-codegen-main\sandbox\runner.py'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('dest.write_text(f.content)', 'dest.write_text(f.content, encoding="utf-8")')
content = content.replace('text=True,', 'text=True, encoding="utf-8",')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
