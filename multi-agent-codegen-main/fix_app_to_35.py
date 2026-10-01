file_path = "app.py"
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("gemini-3.6-flash", "gemini-3.5-flash")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated app.py")
