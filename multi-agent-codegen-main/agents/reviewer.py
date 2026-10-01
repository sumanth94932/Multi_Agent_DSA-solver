from __future__ import annotations
import os
from dotenv import load_dotenv
load_dotenv()


import os
from pathlib import Path

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

from models.schemas import AgentState, ReviewFeedback, TaskStatus
from utils import BudgetCallbackHandler, cached_system, with_retries

_PROMPT = (Path(__file__).parent.parent / "prompts" / "reviewer.md").read_text()


def get_llm():
    return ChatGoogleGenerativeAI(
        model="gemini-3.5-flash-lite",
        max_tokens=1500,
        max_retries=6,
        google_api_key=os.environ.get("GOOGLE_API_KEY", os.environ.get("GOOGLE_API_KEY")),
        callbacks=[BudgetCallbackHandler()]
    )


def _format_artifacts(state: AgentState) -> str:
    parts = [f"Original request: {state.user_request}\n"]
    for artifact in state.artifacts:
        parts.append(f"### {artifact.filename}\n```{artifact.language}\n{artifact.content}\n```\n")
    return "\n".join(parts)


def reviewer_node(state: AgentState) -> dict:
    """Reviews generated code and returns structured feedback."""
    llm = get_llm().with_structured_output(ReviewFeedback)

    messages = [
        cached_system(_PROMPT),
        HumanMessage(content=_format_artifacts(state)),
    ]

    review: ReviewFeedback = with_retries(llm.invoke)(messages)  # type: ignore[assignment]

    status = TaskStatus.COMPLETED if review.approved else TaskStatus.NEEDS_REVISION
    summary = HumanMessage(
        content=(
            f"Review complete — score: {review.score}/10, "
            f"approved: {review.approved}. {review.summary}"
        )
    )

    return {
        "review": review,
        "status": status,
        "messages": [summary],
    }
