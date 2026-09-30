filepath = r'c:\Users\cc221\Downloads\multi-agent-codegen-main\multi-agent-codegen-main\sandbox\runner.py'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

import re

# Add try-except around subprocess.run for docker
new_ensure_image = '''def _ensure_image() -> None:
    \"\"\"Build the sandbox Docker image on first use if it isn't already present.\"\"\"
    global _image_ready
    if _image_ready:
        return

    try:
        inspect = subprocess.run(
            ["docker", "image", "inspect", SANDBOX_IMAGE],
            capture_output=True,
            text=True,
        )
    except FileNotFoundError:
        raise RuntimeError("Docker is not installed or not found in PATH. Please install Docker Desktop to use the Tester sandbox.")

    if inspect.returncode == 0:
        _image_ready = True
        return

    build = subprocess.run(
        ["docker", "build", "-t", SANDBOX_IMAGE, str(SANDBOX_DIR)],
        capture_output=True,
        text=True,
    )
    if build.returncode != 0:
        raise RuntimeError(
            f"Failed to build sandbox image '{SANDBOX_IMAGE}':\\n{build.stderr}"
        )
    _image_ready = True
'''

content = re.sub(r'def _ensure_image\(\) -> None:.*?(?=\ndef run_in_sandbox)', new_ensure_image, content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
