from typing import List, Dict, TypedDict

class GraphState(TypedDict):
    file_paths: List[str]
    questions: List[str]
    classified: List[Dict]
    topics: List[Dict]
    plan: str