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
        max_tokens=1500,
        callbacks=[BudgetCallbackHandler()]
    )


import json
import os
from pathlib import Path

from langchain_core.messages import HumanMessage
from pydantic import BaseModel, field_validator

from models.schemas import AgentState, CodeArtifact
from utils import BudgetCallbackHandler, cached_system, with_retries

_PROMPT = (Path(__file__).parent.parent / "prompts" / "coder.md").read_text()


class ArtifactList(BaseModel):
    artifacts: list[CodeArtifact]

    @field_validator("artifacts", mode="before")
    @classmethod
    def coerce_artifacts(cls, v: object) -> object:
        if isinstance(v, str):
            return json.loads(v)
        return v




def _build_prompt(state: AgentState) -> str:
    parts = [f"User request: {state.user_request}"]

    if state.plan:
        parts.append(f"\nImplementation plan:\n{json.dumps(state.plan.model_dump(), indent=2)}")

    if state.review and not state.review.approved:
        issues = "\n".join(f"- {i}" for i in state.review.issues)
        parts.append(f"\nReview issues to fix:\n{issues}")

    if state.test_result and not state.test_result.passed:
        parts.append("\nTest execution errors to fix (real sandbox output):")
        if state.test_result.errors:
            for err in state.test_result.errors:
                parts.append(err)
        if state.test_result.output:
            parts.append(f"\nFull pytest output:\n{state.test_result.output}")

    if state.artifacts:
        parts.append("\nExisting code to revise:")
        for artifact in state.artifacts:
            parts.append(
                f"\n### {artifact.filename}\n"
                f"```{artifact.language}\n{artifact.content}\n```"
            )

    return "\n".join(parts)


def coder_node(state: AgentState) -> dict:
    """Generates or revises code artifacts based on the plan and feedback."""
    llm = get_llm().with_structured_output(ArtifactList)

    messages = [
        cached_system(_PROMPT),
        HumanMessage(content=_build_prompt(state)),
    ]

    result: ArtifactList = with_retries(llm.invoke)(messages)  # type: ignore[assignment]

    filenames = [a.filename for a in result.artifacts]
    summary = HumanMessage(
        content=f"Code generated: {len(result.artifacts)} file(s) — {', '.join(filenames)}"
    )

    return {
        "artifacts": result.artifacts,
        "messages": [summary],
        "iteration": state.iteration + 1,
    }
