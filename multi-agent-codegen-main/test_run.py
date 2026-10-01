import os
from dotenv import load_dotenv
load_dotenv()

import os
import sys

# Setup environment for testing
os.environ['OPENROUTER_API_KEY'] = os.environ.get("OPENROUTER_API_KEY")

from graph.workflow import run

print("Starting run...")
try:
    final_state = run("Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with 6 places after the decimal. Input Format - First line: An integer, n, the size of the array.", max_iterations=1)
    print("Run completed successfully.")
    print("Test passed:", final_state.test_result.passed if final_state.test_result else "No test result")
except Exception as e:
    print(f"Exception: {e}")
