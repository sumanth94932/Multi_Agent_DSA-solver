import glob

def fix_future_import(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # If the file has from __future__ import annotations but not at the top
    if 'from __future__ import annotations' in content and not content.startswith('from __future__ import annotations'):
        # Remove all instances of it
        content = content.replace('from __future__ import annotations\n', '')
        # Add it to the top
        content = 'from __future__ import annotations\n' + content
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {filepath}")

for filepath in glob.glob("agents/*.py"):
    fix_future_import(filepath)

