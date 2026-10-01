import os
import sys

from langgraph.graph import START, END, StateGraph
from models.schemas import AgentState, CodeArtifact

def mock_coder(state: AgentState):
    artifacts = [CodeArtifact(filename="test.py", language="python", content="print('hello')", description="")]
    return {"artifacts": artifacts}

def mock_reviewer(state: AgentState):
    return {"review": None}

graph = StateGraph(AgentState)
graph.add_node("coder", mock_coder)
graph.add_node("reviewer", mock_reviewer)
graph.add_edge(START, "coder")
graph.add_edge("coder", "reviewer")
graph.add_edge("reviewer", END)

app = graph.compile()
initial_state = AgentState(user_request="test")

final_state = {}
for chunk in app.stream(initial_state):
    for node_name, state_update in chunk.items():
        print(f"Node: {node_name}")
        print("Keys in state_update:", list(state_update.keys()))
        final_state.update(state_update)

print("Keys in final_state:", list(final_state.keys()))
