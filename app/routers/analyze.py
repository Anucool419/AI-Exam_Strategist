# from fastapi import APIRouter
# from app.core.pdf_processor import extract_text_from_pdf
# from app.core.question_extractor import extract_questions
# from app.core.topic_classifier import classify_question
# from app.core.topic_analyzer import analyze_topics
# router = APIRouter()

# @router.post("/analyze")

# ##SINGLE FILE PATH
# # async def analyze(file_path: str):
# #     text = extract_text_from_pdf(file_path)
# #     questions = extract_questions(text)
# #     #Without classificaition based on difficulty/frequency/importance
# #     # results = []

# #     # for q in questions[:5]:  # limit for speed
# #     #     classification = classify_question(q)
# #     #     results.append({
# #     #         "question": q,
# #     #         "analysis": classification
# #     #     })

# #     # return {
# #     #     "num_questions": len(questions),
# #     #     "analysis_sample": results
# #     # }
    
    
# #     #With classification
# #     classified = []

# #     for q in questions:
# #         result = classify_question(q)
# #         if "error" not in result:
# #             classified.append(result)

# #     topic_analysis = analyze_topics(classified)

# #     return {
# #         "num_questions": len(questions),
# #         "topics": topic_analysis[:5]  # top 5
# #     }



# ## FOR MULTIPLE FILE PATHS
# @router.post("/analyze")
# async def analyze(file_paths: list[str]):
#     all_questions = []

#     # 🔥 Combine all PDFs
#     for path in file_paths:
#         text = extract_text_from_pdf(path)
#         questions = extract_questions(text)
#         all_questions.extend(questions)

#     classified = []

#     for q in all_questions:
#         result = classify_question(q)
#         if "error" not in result:
#             classified.append(result)

#     topic_analysis = analyze_topics(classified)

#     return {
#         "total_questions": len(all_questions),
#         "topics": topic_analysis[:5]
#     }
    
    
# from app.core.syllabus_parser import parse_syllabus
# from app.core.syllabus_mapper import map_syllabus

# import os

# SYLLABUS_TEXT = "data/syllabus.txt"

# @router.post("/analyze")
# async def analyze(file_paths: list[str]):
#     all_questions = []

#     for path in file_paths:
#         text = extract_text_from_pdf(path)
#         questions = extract_questions(text)
#         all_questions.extend(questions)

#     classified = []

#     for q in all_questions:
#         result = classify_question(q)
#         if "error" not in result:
#             classified.append(result)

#     topic_analysis = analyze_topics(classified)

#     # 🔥 NEW: syllabus comparison
#     syllabus_result = None

#     if os.path.exists(SYLLABUS_TEXT):
#         with open(SYLLABUS_TEXT, "r", encoding="utf-8") as f:
#             syllabus_text = f.read()

#         syllabus_topics = parse_syllabus(syllabus_text)

#         syllabus_result = map_syllabus(topic_analysis, syllabus_topics)

#     return {
#         "total_questions": len(all_questions),
#         "topics": topic_analysis[:5],
#         "syllabus": syllabus_result
#     }
    
## 
## Using LangGraph
from app.core.graph import build_graph
from fastapi import APIRouter
router = APIRouter()
graph = build_graph()

@router.post("/analyze")
async def analyze(file_paths: list[str]):
    result = graph.invoke({
        "file_paths": file_paths
    })

    return {
        "topics": result["topics"],
        "plan": result["plan"],
        "classified": result["classified"],  # 🔥 ADD THIS
        #"syllabus": result["syllabus_result"]
         "years": [c["year"] for c in result["classified"]]
        
    }