import json

def normalize_topic(topic):
    return (
        str(topic)
        .lower()
        .replace("_", " ")
        .replace("-", " ")
        .strip()
    )

def normalize(text):
    return str(text).lower().strip()
def normalize_topic_eval(topic):
    topic = topic.lower().replace("_", " ").strip()

    if "nlp" in topic:
        return "natural language processing"
    if "machine learning" in topic:
        return "machine learning"

    return topic
def evaluate(predictions, ground_truth):
    correct_topic = 0
    correct_difficulty = 0
    total = len(ground_truth)

    for gt, pred in zip(ground_truth, predictions):
        if normalize_topic_eval(gt["topic"]) == normalize_topic_eval(pred["topic"]):
            correct_topic += 1

        if normalize(gt["difficulty"]) == normalize(pred["difficulty"]):
            correct_difficulty += 1

    return {
        "topic_accuracy": round(correct_topic / total, 2),
        "difficulty_accuracy": round(correct_difficulty / total, 2),
        "total_samples": total
    }