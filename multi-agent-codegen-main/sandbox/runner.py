from __future__ import annotations

import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path

TIMEOUT_SECONDS = 30

@dataclass
class CodeFile:
    filename: str
    content: str


@dataclass
class SandboxResult:
    success: bool
    stdout: str
    stderr: str
    exit_code: int



def run_in_sandbox(files: list[CodeFile]) -> SandboxResult:
    """Write files to a temp dir and run pytest locally using the host Python interpreter."""
    import sys
    
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp = Path(tmpdir)

        for f in files:
            dest = tmp / f.filename
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(f.content, encoding="utf-8")

        try:
            # We run pytest locally in the tmpdir instead of using docker
            proc = subprocess.run(
                [sys.executable, "-m", "pytest", "."],
                cwd=tmpdir,
                capture_output=True,
                text=True, encoding="utf-8",
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
            )