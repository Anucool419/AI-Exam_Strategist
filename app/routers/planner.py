
from fastapi import APIRouter
from app.core.strategy_agent import generate_study_plan
from app.schemas.planner_schema import PlannerRequest

router = APIRouter()

@router.post("/planner")
async def planner(request: PlannerRequest):
    plan = generate_study_plan(request.topics, request.days)

    return {
        "study_plan": plan
    }