from fastapi import APIRouter
import json
from pathlib import Path
from app.core.evaluation import evaluate
from app.core.topic_classifier import classify_question

router = APIRouter()

@router.get("/evaluate")
async def evaluate_model():
    ground_truth_path = Path(__file__).resolve().parents[1] / "data" / "ground_truth.json"

    with open(ground_truth_path, "r") as f:
        ground_truth = json.load(f)

    predictions = []

    for item in ground_truth:
        result = classify_question(item["question"])
        predictions.append({
            "topic": result.get("topic", ""),
            "difficulty": result.get("difficulty", "")
        })

    scores = evaluate(predictions, ground_truth)

    return {
        "scores": scores,
        "predictions": predictions
    }