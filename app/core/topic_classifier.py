from app.core.llm import get_llm
import json
llm = get_llm()

def classify_question(question):
    prompt = f"""
    You are an academic expert.

    Given the question below, classify it into:
    1. Topic
    2. Subtopic
    3. Difficulty (easy/medium/hard)

    Return ONLY JSON like:
    {{
        "topic": "...",
        "subtopic": "...",
        "difficulty": "..."
    }}

    Use standard academic topic names.
    Avoid synonyms.
    Be consistent across responses.
    Question:
    {question}
    """
    response = llm.invoke(prompt)

    try:
        return json.loads(response.content)
    except:
        return {"error": response.content}
    