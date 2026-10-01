import subprocess
import sys
proc = subprocess.run([sys.executable, "-m", "pytest", "--version"], capture_output=True, text=True)
print("Return code:", proc.returncode)
print("Stdout:", proc.stdout)
print("Stderr:", proc.stderr)
