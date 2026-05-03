from app.core.llm import get_llm

llm = get_llm()

def generate_questions(topic):
    prompt = f"""
    Generate 10 exam-style questions for the topic: {topic}

    Include:
    - easy
    - medium
    - hard
    levels of difficulty of questions.
    """

    response = llm.invoke(prompt)
    return response.content