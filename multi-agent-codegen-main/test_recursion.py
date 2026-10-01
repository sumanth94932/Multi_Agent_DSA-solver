import os
from dotenv import load_dotenv
load_dotenv()

import os
import sys

from graph.workflow import build_graph
from models.schemas import AgentState

os.environ['GOOGLE_API_KEY'] = os.environ.get("GOOGLE_API_KEY")

graph = build_graph()
initial_state = AgentState(
    user_request="Build a completely impossible P=NP algorithm in Python that sorts an infinite array in O(1) time.",
    max_iterations=15, # Tell agents they can retry 15 times
    tester_model="gemini-2.5-flash-lite"
)

print("Starting graph run...")
try:
    for chunk in graph.stream(initial_state, config={"recursion_limit": 10}):
        print("Completed a node:", list(chunk.keys()))
except Exception as e:
    print(f"Graph execution stopped: {type(e).__name__} - {e}")
