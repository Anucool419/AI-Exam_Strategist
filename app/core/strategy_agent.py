from app.core.llm import get_llm

llm = get_llm()

def generate_study_plan(topics, days):
    prompt = f"""
    You are a smart exam strategist.

    Given:
    - Topics with importance scores: {topics}
    - Total study days: {days}

    Create a day-wise study plan.
    STRICT INSTRUCTIONS:
    - DO NOT explain your reasoning
    - DO NOT write code
    - DO NOT include steps
    - ONLY output the final study plan
    Rules:
    - Focus more on high importance topics
    - Include revision
    - Distribute workload realistically
    - Mention what to skip if low importance
    - Suggest which topics can be skipped
    - Add "last-day crash plan"

    
   
    Output format:
    Day 1: ...
    Day 2: ...
    """

    response = llm.invoke(prompt)
    return response.content