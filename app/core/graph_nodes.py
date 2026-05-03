from app.core.pdf_processor import extract_text_from_pdf
from app.core.question_extractor import extract_questions
from app.core.topic_classifier import classify_question
from app.core.topic_analyzer import analyze_topics
from app.core.strategy_agent import generate_study_plan
from app.core.year_extractor import extract_year


def extract_node(state):
    all_questions = []

    for path in state["file_paths"]:
        text = extract_text_from_pdf(path)
        questions = extract_questions(text)
        year = extract_year(path, text)
        #all_questions.extend(questions)
        for q in questions:
            all_questions.append({
                "question": q,
                "year": year
            })

    state["questions"] = all_questions
    return state


def classify_node(state):
    classified = []

    # for q in state["questions"]:
    #     result = classify_question(q)
    #     if "error" not in result:
    #         classified.append(result)
    for item in state["questions"]:
        result = classify_question(item["question"])

        if "error" not in result:
            result["year"] = item["year"]
            classified.append(result)

   

    state["classified"] = classified
    return state


def analyze_node(state):
    topics = analyze_topics(state["classified"])
    state["topics"] = topics
    return state


def plan_node(state):
    topics = state["topics"][:5]
    plan = generate_study_plan(topics, days=5)  # can be dynamic later
    state["plan"] = plan
    return state