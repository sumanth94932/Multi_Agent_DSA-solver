import os
import sys

from langchain_core.messages import AIMessage
from langchain_core.language_models import FakeListChatModel
from graph.workflow import build_graph
from models.schemas import AgentState

def test_pipeline():
    # Mock LLMs
    # We will patch get_llm in all agents to return a FakeListChatModel
    import agents.coder
    import agents.planner
    import agents.reviewer
    import agents.tester
    import agents.orchestrator

    dummy_coder_llm = FakeListChatModel(responses=[
        '{"artifacts": [{"filename": "main.py", "language": "python", "content": "print(1)", "description": "test"}]}'
    ])
    
    # Actually with_structured_output expects the LLM to support it. FakeListChatModel might not.
    pass

