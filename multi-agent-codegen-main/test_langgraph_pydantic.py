from langgraph.graph import START, END, StateGraph
from pydantic import BaseModel, Field

class MyState(BaseModel):
    items: list[str] = Field(default_factory=list)

def my_node(state: MyState):
    return {"items": ["hello"]}

graph = StateGraph(MyState)
graph.add_node("node", my_node)
graph.add_edge(START, "node")
graph.add_edge("node", END)
app = graph.compile()

res = app.invoke(MyState())
print(res)
