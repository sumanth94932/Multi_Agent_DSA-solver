import re

file_path = "app.py"
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Change Powered by
content = content.replace("Powered by LangGraph + Claude", "Powered by LangGraph + Google Gemini")

# 2. Remove TESTER_MODELS dictionary
content = re.sub(r'TESTER_MODELS = \{\n[^}]+\n\}\n+', '', content)

# 3. Remove tester agent radio button
# It looks like:
#         st.write("**Tester agent model**")
#         tester_choice = st.radio(
#             ...
#         )
#         tester_model = TESTER_MODELS[tester_choice]

content = re.sub(
    r'\s*st\.write\("\*\*Tester agent model\*\*"\)\s*tester_choice = st\.radio\(\s*label="tester_model",\s*options=list\(TESTER_MODELS\.keys\(\)\),\s*index=1,\s*label_visibility="collapsed",\s*help=\([\s\S]*?\),\s*\)\s*tester_model = TESTER_MODELS\[tester_choice\]\s*',
    '\n        tester_model = "gemini-3.6-flash"\n',
    content
)

# wait, I should just modify render_sidebar manually because regex can be brittle here.
