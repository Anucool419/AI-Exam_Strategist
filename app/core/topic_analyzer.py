from collections import defaultdict

def normalize_topic(topic):
    return (
        str(topic)
        .lower()
        .replace("_", " ")
        .replace("-", " ")
        .strip()
    )

def analyze_topics(classified_questions):
    topic_counts = defaultdict(int)
    difficulty_weights = {
        "easy": 1,
        "medium": 2,
        "hard": 3
    }

    topic_scores = defaultdict(int)

    for item in classified_questions:
        topic = normalize_topic(item.get("topic", "Unknown"))
        difficulty = item.get("difficulty", "medium")

        topic_counts[topic] += 1
        topic_scores[topic] += difficulty_weights.get(difficulty, 2)

    results = []

    total = sum(topic_counts.values())

    for topic in topic_counts:
        frequency = topic_counts[topic]
        score = topic_scores[topic]

        importance = round(score / (total * 3), 2)  # normalized

        results.append({
            "topic": topic,
            "frequency": frequency,
            "score": score,
            "importance": importance
        })

    # Sort by importance
    results.sort(key=lambda x: x["importance"], reverse=True)

    return results