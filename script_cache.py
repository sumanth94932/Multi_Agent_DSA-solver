filepath = r'c:\Users\cc221\Downloads\multi-agent-codegen-main\multi-agent-codegen-main\utils\cache.py'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    'return os.getenv("ENABLE_PROMPT_CACHE", "true").lower() not in {"0", "false", "no"}',
    'return False  # Disabled for OpenAI/OpenRouter compatibility'
)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
