import glob
import re

base_path = r'c:\Users\cc221\Downloads\multi-agent-codegen-main\multi-agent-codegen-main\agents\*.py'

def replace_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    content = content.replace('model="meta-llama/llama-3.3-70b-instruct:free"', 'model="meta-llama/llama-3.3-70b-instruct"')
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for filepath in glob.glob(base_path):
    replace_in_file(filepath)

print('Done')
