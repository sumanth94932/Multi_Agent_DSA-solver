file_path = 'app.py'
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 1. Change Powered by
lines[19] = lines[19].replace("Powered by LangGraph + Claude", "Powered by LangGraph + Gemini")

# 2. Remove TESTER_MODELS dict (lines 39-44 since 0-indexed)
# 40-44 is lines[39:44]
for i in range(39, 44):
    lines[i] = ""

# 3. Replace tester_model selection (lines 55-67 in 1-indexed)
# 55-67 is lines[54:67]
for i in range(55, 66):
    lines[i] = ""
lines[66] = "        tester_model = 'gemini-3.6-flash'\n"

# Remove the line 56 st.markdown("**Tester agent model**")
# Oh wait, lines[54] was max_iterations = st.slider(...). Let's be careful.
