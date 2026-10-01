file_path = "app.py"
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

import re
# The current recursion_limit is 10. We want to change it to max_iterations * 5 + 5
content = re.sub(r'recursion_limit = 10', 'recursion_limit = max_iterations * 5 + 5', content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated app.py")
