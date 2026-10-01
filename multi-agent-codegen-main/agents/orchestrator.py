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


import os
from pathlib import Path

from langchain_core.messages import HumanMessage

from models.schemas import AgentState, TaskStatus
from utils import BudgetCallbackHandler, cached_system, with_retries

_PROMPT = (Path(__file__).parent.parent / "prompts" / "orchestrator.md").read_text()




def orchestrator_node(state: AgentState) -> dict:
    """Entry point: interprets the user request and sets the initial status."""
    llm = get_llm()

    messages = [
        cached_system(_PROMPT),
        HumanMessage(
            content=(
                f"User request: {state.user_request}\n\n"
                f"Current iteration: {state.iteration}/{state.max_iterations}\n"
                f"Status: {state.status}"
            )
        ),
    ]

    response = with_retries(llm.invoke)(messages)

    return {
        "messages": [response],
        "status": TaskStatus.IN_PROGRESS,
    }


def should_continue(state: AgentState) -> str:
    """Route after review + test: continue, revise, or finish."""
    if state.status == TaskStatus.COMPLETED:
        return "end"

    if state.status == TaskStatus.FAILED:
        return "end"

    if state.iteration >= state.max_iterations:
        return "end"

    review = state.review
    test = state.test_result

    score_ok = review is not None and review.score >= state.min_review_score
    if review and review.approved and score_ok and test and test.passed:
        return "end"

    if state.iteration < state.max_iterations:
        return "revise"

    return "end"
