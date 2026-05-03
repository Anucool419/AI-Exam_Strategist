from app.core.llm import get_llm

llm = get_llm()

def chat_with_system(query, context):
    prompt = f"""
    You are an AI exam assistant.

    Context:
    {context}

    Answer the user's question:
    {query}

    Be helpful, concise, and practical.
    """

    response = llm.invoke(prompt)
    return response.content