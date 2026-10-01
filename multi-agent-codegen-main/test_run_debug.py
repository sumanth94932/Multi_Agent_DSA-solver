import os
from dotenv import load_dotenv
load_dotenv()

import os
import sys
import logging

logging.basicConfig(level=logging.DEBUG)

os.environ['OPENROUTER_API_KEY'] = os.environ.get("OPENROUTER_API_KEY")

from graph.workflow import run

print("Starting run...")
try:
    final_state = run("Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.", max_iterations=1)
    print("Run completed successfully.")
except Exception as e:
    print(f"Exception: {e}")
