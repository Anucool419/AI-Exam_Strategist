from pydantic import BaseModel
from typing import List, Dict

class PlannerRequest(BaseModel):
    topics: List[Dict]
    days: int