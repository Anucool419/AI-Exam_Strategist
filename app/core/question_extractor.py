import re
import re

def extract_questions(text):
    # Normalize spacing
    text = text.replace("\n", " ")

    # Split on question numbers
    parts = re.split(r"\s\d+\.\s", text)

    # Remove garbage first element
    questions = parts[1:]

    # Clean
    questions = [q.strip() for q in questions if len(q.strip()) > 20]

    return questions
# def extract_questions(text):
#     # Simple heuristic: split by question numbers
#     #pattern = r"\d+\.\s"
#     # Match question number + content
#     pattern = r"\d+\.\s+(.*?)(?=\n\d+\.|\Z)"
#     questions = re.split(pattern, text)

#     # Clean empty
#     questions = [q.strip() for q in questions if len(q.strip()) > 20]

#     return questions