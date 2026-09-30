import re

filepath = r'c:\Users\cc221\Downloads\multi-agent-codegen-main\multi-agent-codegen-main\utils\budget.py'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('ChatAnthropic', 'ChatOpenAI')

# we need to fix the token extraction
'''
                meta = getattr(msg, "response_metadata", {}) or {}
                usage = meta.get("usage") or {}
                model = (
                    meta.get("model_name")
                    or meta.get("model")
                    or "claude-sonnet-4-6"
                )
                input_tokens = int(usage.get("input_tokens", 0) or 0)
                output_tokens = int(usage.get("output_tokens", 0) or 0)
'''

new_extraction = '''
                meta = getattr(msg, "response_metadata", {}) or {}
                usage = meta.get("usage") or meta.get("token_usage") or {}
                model = (
                    meta.get("model_name")
                    or meta.get("model")
                    or "openrouter/free"
                )
                input_tokens = int(usage.get("input_tokens") or usage.get("prompt_tokens") or 0)
                output_tokens = int(usage.get("output_tokens") or usage.get("completion_tokens") or 0)
'''

content = re.sub(
    r'                meta = getattr\(msg, "response_metadata", \{\}\) or \{\}\n                usage = meta\.get\("usage"\) or \{\}\n                model = \(\n                    meta\.get\("model_name"\)\n                    or meta\.get\("model"\)\n                    or "claude-sonnet-4-6"\n                \)\n                input_tokens = int\(usage\.get\("input_tokens", 0\) or 0\)\n                output_tokens = int\(usage\.get\("output_tokens", 0\) or 0\)',
    new_extraction.strip('\n'),
    content
)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

