filepath = r'c:\Users\cc221\Downloads\multi-agent-codegen-main\multi-agent-codegen-main\sandbox\runner.py'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

import re

# Remove the docker image ensure logic entirely
content = re.sub(r'def _ensure_image\(\) -> None:.*?(?=\ndef run_in_sandbox)', '', content, flags=re.DOTALL)
content = re.sub(r'_image_ready = False\n+', '', content)
content = re.sub(r'SANDBOX_IMAGE = "multi-agent-sandbox"\n', '', content)
content = re.sub(r'SANDBOX_DIR = Path\(__file__\)\.parent\n', '', content)

new_run = '''def run_in_sandbox(files: list[CodeFile]) -> SandboxResult:
    \"\"\"Write files to a temp dir and run pytest locally using the host Python interpreter.\"\"\"
    import sys
    
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp = Path(tmpdir)

        for f in files:
            dest = tmp / f.filename
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(f.content)

        try:
            # We run pytest locally in the tmpdir instead of using docker
            proc = subprocess.run(
                [sys.executable, "-m", "pytest", "."],
                cwd=tmpdir,
                capture_output=True,
                text=True,
                timeout=TIMEOUT_SECONDS,
            )
            return SandboxResult(
                success=proc.returncode == 0,
                stdout=proc.stdout,
                stderr=proc.stderr,
                exit_code=proc.returncode,
            )

        except subprocess.TimeoutExpired:
            return SandboxResult(
                success=False,
                stdout="",
                stderr=f"Sandbox timed out after {TIMEOUT_SECONDS} seconds.",
                exit_code=-1,
            )'''

content = re.sub(r'def run_in_sandbox\(files: list\[CodeFile\]\) -> SandboxResult:.*', new_run, content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
