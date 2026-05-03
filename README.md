# 🎯 AI Exam Strategist

An AI-powered application that analyzes past exam papers and helps students **identify important topics, understand exam patterns, and generate smart study plans**.

---

## 🚀 Problem

Students often go through multiple past question papers but struggle to:

* Identify **high-weightage topics**
* Understand **exam difficulty trends**
* Track **syllabus coverage gaps**
* Plan their preparation effectively

---

## 💡 Solution

**AI Exam Strategist** automates this entire workflow:

1. Upload past question papers (PDFs)
2. Extract and analyze questions using AI
3. Identify **frequent topics and patterns**
4. Map topics against the **official syllabus**
5. Generate a **personalized study plan**
6. Provide **practice questions and AI assistance**

---

## ✨ Features

### 📂 Multi-PDF Upload

* Upload multiple past question papers
* Supports analysis across **multiple years and subjects**

---

### 🧠 AI Pattern Analysis

* Topic extraction and classification
* Frequency-based **topic importance scoring**
* Difficulty classification (easy / medium / hard)
* Year-wise trend analysis

---

### 📚 Syllabus Cross-Referencing

* Upload official syllabus
* Automatically identifies:

  * ✅ Covered topics
  * ❌ Missing topics (focus areas)

---

### 📊 Visual Analytics Dashboard

* Topic frequency charts
* Difficulty distribution
* Topic vs difficulty analysis
* Year-wise topic trends
* Syllabus coverage heatmap

---

### 🧠 Smart Study Planner

* Generates a **day-wise study plan**
* Prioritizes high-importance topics
* Adjustable based on available days

---

### 📝 Practice Question Generator

* Generate practice questions for selected topics

---

### 💬 AI Assistant

* Ask questions related to preparation
* Context-aware responses based on analyzed data

---

### 📏 Evaluation Module

* Uses a small ground-truth dataset
* Measures:

  * Topic classification accuracy
  * Difficulty classification accuracy

---

## 🏗️ Tech Stack

* **Backend:** FastAPI
* **Frontend:** Streamlit
* **LLM:** Groq API
* **Pipeline:** LangGraph (for workflow orchestration)
* **Data Processing:** Pandas

---

## ⚙️ How It Works

```text
Upload PDFs → Extract Questions → Classify Topics & Difficulty
→ Score Importance → Map with Syllabus → Generate Insights
→ Create Study Plan → Enable Practice & Chat
```

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <your-repo-link>
cd <repo-name>
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run backend

```bash
uvicorn app.main:app --reload
```

### 4. Run frontend

```bash
streamlit run app/frontend/streamlit_app.py
```

---

## 📸 Demo Flow

1. Upload past question papers
2. Run analysis
3. View:

   * Topic insights
   * Difficulty trends
   * Syllabus coverage
4. Generate study plan
5. Practice questions
6. Ask AI assistant
7. View evaluation metrics

---

## ⚠️ Limitations

* OCR for scanned PDFs not implemented (text-based PDFs supported)
* Evaluation is based on a small manually created dataset
* LLM outputs may vary slightly across runs

---

## 🌟 Future Improvements

* OCR support for scanned documents
* Persistent memory across sessions
* More robust evaluation framework
* Enhanced UI/UX and filtering

---

## 👨‍💻 Author

Built as a hackathon project exploring **GenAI + education use cases**

---

## 🏁 Conclusion

**AI Exam Strategist** helps students:

> Study smarter, not harder — by focusing on what actually matters.

---
