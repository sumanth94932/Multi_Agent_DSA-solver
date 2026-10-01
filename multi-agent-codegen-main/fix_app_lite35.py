file_path = "app.py"
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

import re
content = re.sub(r'tester_model = "gemini-2.5-flash-lite"', 'tester_model = "gemini-3.5-flash-lite"', content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated app.py")
