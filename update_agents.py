import glob
import re

base_path = r'c:\Users\cc221\Downloads\multi-agent-codegen-main\multi-agent-codegen-main\agents\*.py'
old_key = 'YOUR_API_KEY_HERE'
new_key = 'YOUR_API_KEY_HERE'

def replace_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    content = content.replace(old_key, new_key)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for filepath in glob.glob(base_path):
    replace_in_file(filepath)

print('Done')
