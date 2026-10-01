import re

file_path = "app.py"
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Powered by
content = content.replace("Powered by LangGraph + Claude", "Powered by LangGraph + Gemini")

# Remove TESTER_MODELS definition
content = re.sub(r'TESTER_MODELS = \{[\s\S]*?\}\n\n', '', content)

# Remove the radio button widget and replace with tester_model assignment
radio_pattern = r'\s*st\.markdown\("\*\*Tester agent model\*\*"\)\s*tester_choice = st\.radio\([\s\S]*?tester_model = TESTER_MODELS\[tester_choice\]'
replacement = '\n        tester_model = "gemini-3.6-flash"'
content = re.sub(radio_pattern, replacement, content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated app.py")
