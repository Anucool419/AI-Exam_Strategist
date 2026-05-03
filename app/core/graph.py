from langgraph.graph import StateGraph
from app.core.state import GraphState
from app.core.graph_nodes import (
    extract_node,
    classify_node,
    analyze_node,
    plan_node
)

def build_graph():
    builder = StateGraph(GraphState)

    builder.add_node("extract", extract_node)
    builder.add_node("classify", classify_node)
    builder.add_node("analyze", analyze_node)
    builder.add_node("plan", plan_node)

    builder.set_entry_point("extract")

    builder.add_edge("extract", "classify")
    builder.add_edge("classify", "analyze")
    builder.add_edge("analyze", "plan")

    return builder.compile()