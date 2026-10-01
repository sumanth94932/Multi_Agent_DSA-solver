import os
from dotenv import load_dotenv
load_dotenv()

import os
import sys

os.environ['OPENROUTER_API_KEY'] = os.environ.get("OPENROUTER_API_KEY")

from graph.workflow import build_graph
from models.schemas import AgentState

app = build_graph()
initial_state = AgentState(
    user_request="Write a python function to add two numbers.",
    max_iterations=1,
)

for chunk in app.stream(initial_state):
    for node, state in chunk.items():
        print(f"Node: {node}")
        if 'artifacts' in state:
            print("Artifacts returned:", len(state['artifacts']))
        else:
            print("NO ARTIFACTS RETURNED IN THIS CHUNK")
