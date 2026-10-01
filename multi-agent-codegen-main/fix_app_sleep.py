import re

file_path = "app.py"
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

if "import time" not in content:
    content = "import time\n" + content

# Add time.sleep(2) inside the loop
content = content.replace("final_state.update(state_update)", "final_state.update(state_update)\n\n                    import time\n                    time.sleep(2)")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated app.py")
