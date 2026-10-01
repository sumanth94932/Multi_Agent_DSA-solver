import os

def append_to_file(filepath, text):
    with open(filepath, 'a', encoding='utf-8') as f:
        f.write("\n\n" + text + "\n")
    print(f"Updated {filepath}")

instruction = "CRITICAL: DO NOT plan or generate README.md files, test files, or any other documentation files. ONLY generate the core implementation code."

append_to_file("prompts/planner.md", instruction)
append_to_file("prompts/coder.md", instruction)

