
import streamlit as st
import requests
import pandas as pd

BACKEND_URL = "http://127.0.0.1:8000"

# 🔥 Session State Initialization
DEFAULT_STATE = {
    "file_paths": [],
    "analysis": {},
    "plan": "",
    "questions": ""
}

for key, value in DEFAULT_STATE.items():
    if key not in st.session_state:
        st.session_state[key] = value

st.set_page_config(page_title="AI Exam Strategist", layout="centered")

st.title("🎯 AI Exam Strategist")
st.markdown("Analyze past papers, find important topics, and plan your study smartly.")

# ================== SYLLABUS UPLOAD ==================
st.header("📘 Upload Syllabus")

syllabus_file = st.file_uploader("Upload Syllabus PDF", type=["pdf"])

if st.button("Upload Syllabus") and syllabus_file:
    files = {"file": (syllabus_file.name, syllabus_file, "application/pdf")}
    response = requests.post(f"{BACKEND_URL}/upload-syllabus", files=files)

    if response.status_code == 200:
        st.success("Syllabus uploaded!")

# ================== FILE UPLOAD ==================
st.header("📂 Upload Question Papers")

uploaded_files = st.file_uploader(
    "Upload PDFs",
    accept_multiple_files=True,
    type=["pdf"]
)

if st.button("Upload Files") and uploaded_files:
    files = [("files", (f.name, f, "application/pdf")) for f in uploaded_files]
    response = requests.post(f"{BACKEND_URL}/upload", files=files)

    if response.status_code == 200:
        st.success("Files uploaded successfully!")
        st.session_state["file_paths"] = response.json()["file_paths"]

# ================== ANALYZE ==================
analysis = st.session_state.get("analysis", {})

if st.session_state["file_paths"]:
    st.header("📊 Analyze Papers")

    if st.button("Run Analysis"):
        response = requests.post(
            f"{BACKEND_URL}/analyze",
            json=st.session_state["file_paths"]
        )

        if response.status_code == 200:
            data = response.json()
            st.session_state["analysis"] = data
            analysis = data
            st.success("Analysis complete!")

# ================== SHOW ANALYSIS ==================
if analysis and analysis.get("topics"):

    # ----- Syllabus Coverage -----
    syllabus = analysis.get("syllabus")
    if syllabus:
        st.header("📚 Top Missing Topics To Study")

        missing_topics = syllabus.get("missing", [])
        top_missing_topics = missing_topics[:5]

        if top_missing_topics:
            for t in top_missing_topics:
                st.markdown(f"- {t}")
        else:
            st.success("Great job! No missing topics found.")

    # ----- Topic Insights -----
    st.header("📈 Topic Insights")

    topics = analysis["topics"]
    topic_names = [t["topic"] for t in topics]
    frequencies = [t["frequency"] for t in topics]

    st.bar_chart(dict(zip(topic_names, frequencies)))
    st.dataframe(topics)

    # ----- Difficulty Trends -----
    if analysis.get("classified"):
        st.header("📊 Difficulty Trends")

        df = pd.DataFrame(analysis["classified"])
        # 🔥 Normalize difficulty (equates "easy" and "Easy")
        df["difficulty"] = df["difficulty"].str.lower().str.strip()

        difficulty_counts = df["difficulty"].value_counts()
        st.bar_chart(df["difficulty"].value_counts())

        # Topic vs Difficulty
        st.header("📈 Topic Difficulty Distribution")
        pivot = pd.crosstab(df["topic"], df["difficulty"])
        st.bar_chart(pivot)

   

    # ----- Top Topics -----
    st.header("🏆 Top Important Topics")
    for t in topics[:3]:
        st.markdown(f"### 🔥 {t['topic']} (Importance: {t['importance']})")

    # ----- Year Distribution -----
    st.header("📅 Topic Trends Over Years")

if analysis.get("classified"):
    df = pd.DataFrame(analysis["classified"])
    def normalize_topic(topic):
        topic = topic.lower().replace("_", " ").replace("-", " ").strip()

        if "nlp" in topic:
            return "natural language processing"

        return topic

    df["topic"] = df["topic"].apply(normalize_topic)

    # Normalize
    df["topic"] = df["topic"].str.lower().str.strip()
    df["year"] = df["year"].astype(str)

    pivot = pd.crosstab(df["year"], df["topic"])

    st.bar_chart(pivot)
    top_topic = df["topic"].value_counts().idxmax()
    st.success(f"🔥 Most asked topic overall: {top_topic}")
# ================== STUDY PLANNER ==================
if analysis and analysis.get("topics"):
    st.header("🧠 Study Planner")

    days = st.slider("Days available", 1, 30, 5)

    if st.button("Generate Plan"):
        response = requests.post(
            f"{BACKEND_URL}/planner",
            json={
                "topics": analysis["topics"],
                "days": days
            }
        )

        if response.status_code == 200:
            st.session_state["plan"] = response.json()["study_plan"]

# Show plan
if st.session_state.get("plan"):
    st.markdown("## 📅 Study Plan")
    for line in st.session_state["plan"].split("\n"):
        if line.strip():
            st.markdown(f"- {line}")

# ================== PRACTICE QUESTIONS ==================
if analysis and analysis.get("topics"):
    st.header("📝 Practice Questions")

    topic = st.selectbox(
        "Select Topic",
        [t["topic"] for t in analysis["topics"]]
    )

    if st.button("Generate Questions"):
        response = requests.get(
            f"{BACKEND_URL}/practice",
            params={"topic": topic}
        )

        if response.status_code == 200:
            st.markdown("## 📝 Practice Questions")

            for q in response.json()["questions"].split("\n"):
                if q.strip():
                    st.markdown(f"- {q}")

# ================== CHAT ==================
st.header("💬 Ask AI")

query = st.text_input("Ask anything about your preparation or doubts.")

if st.button("Ask") and query:
    context = st.session_state.get("analysis", {})

    response = requests.post(
        f"{BACKEND_URL}/chat",
        json={
            "query": query,
            "context": context
        }
    )

    if response.status_code == 200:
        st.write(response.json()["response"])

st.header("📏 Model Evaluation")

if st.button("Run Evaluation"):
    response = requests.get(f"{BACKEND_URL}/evaluate")

    if response.status_code == 200:
        data = response.json()

        scores = data["scores"]

        st.subheader("Accuracy Metrics")
        st.write(f"Topic Accuracy: {scores['topic_accuracy']}")
        st.write(f"Difficulty Accuracy: {scores['difficulty_accuracy']}")
        st.write(f"Total Samples: {scores['total_samples']}")

        #st.subheader("Predictions")
        #st.json(data["predictions"])
    else:
        st.error(f"Evaluation request failed with status code {response.status_code}")
