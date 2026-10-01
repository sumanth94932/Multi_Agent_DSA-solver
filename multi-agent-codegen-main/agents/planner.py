from __future__ import annotations
import os
from dotenv import load_dotenv
load_dotenv()

import os
from langchain_openai import ChatOpenAI
from utils import BudgetCallbackHandler

def get_llm():
    return ChatOpenAI(
        model="openai/gpt-oss-120b",
        base_url="https://api.groq.com/openai/v1",
        api_key=os.environ.get("GROQ_API_KEY", os.environ.get("GROQ_API_KEY")),
        max_tokens=500,
        callbacks=[BudgetCallbackHandler()]
    )


import json
import os
from pathlib import Path

from langchain_core.messages import HumanMessage

from models.schemas import AgentState, Plan
from utils import BudgetCallbackHandler, cached_system, with_retries

_PROMPT = (Path(__file__).parent.parent / "prompts" / "planner.md").read_text()




def planner_node(state: AgentState) -> dict:
    """Produces a structured implementation plan for the user's request."""
    llm = get_llm().with_structured_output(Plan)

    messages = [
        cached_system(_PROMPT),
        HumanMessage(content=f"Create an implementation plan for: {state.user_request}"),
    ]

    plan: Plan = with_retries(llm.invoke)(messages)  # type: ignore[assignment]

    return {
        "plan": plan,
        "messages": [
            HumanMessage(
                content=f"Plan created:\n{json.dumps(plan.model_dump(), indent=2)}"
            )
        ],
    }
