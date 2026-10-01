import subprocess
import sys
import time

try:
    print("starting")
    proc = subprocess.run([sys.executable, "-c", "while True: pass"], timeout=3)
    print("done")
except subprocess.TimeoutExpired:
    print("timed out")
