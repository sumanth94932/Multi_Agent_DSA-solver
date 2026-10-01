import os
from dotenv import load_dotenv
load_dotenv()

import os
import sys

os.environ['OPENROUTER_API_KEY'] = os.environ.get("OPENROUTER_API_KEY")

from graph.workflow import run

final_state = run("Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.", max_iterations=1)
print(final_state.artifacts)
