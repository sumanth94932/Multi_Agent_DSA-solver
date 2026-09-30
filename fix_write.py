filepath = r'c:\Users\cc221\Downloads\multi-agent-codegen-main\multi-agent-codegen-main\app.py'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()
content = content.replace('dest.write_text(artifact.content)', 'dest.write_text(artifact.content, encoding="utf-8")')
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

filepath = r'c:\Users\cc221\Downloads\multi-agent-codegen-main\multi-agent-codegen-main\scripts\run_evals.py'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()
content = content.replace('Path(args.out).write_text(', 'Path(args.out).write_text(encoding="utf-8", ')
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
