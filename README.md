# 🧠 AI Resume Ranker

Upload a job description and multiple resumes to see which candidate matches best — using AI.

---

### 💡 Features:
- 📄 PDF Resume Parsing
- 📌 JD Matching using TF-IDF + Cosine Similarity
- 🧠 AI-Powered Explanations using **OpenRouter (Mistral 7B)**
- 📊 Ranked table with preview and match score

---

### 🛠️ Tech Stack:
- **Python**, **Streamlit**, **PDFMiner**
- **OpenRouter API** (LLM: `mistralai/mistral-7b-instruct`)
- **Scikit-learn** for similarity ranking
- **.env** for API key management

---

### 🚀 Try the live app:
👉 [https://resume-ranker-ai-1.streamlit.app/)

---

### 🔧 Local Setup (Optional)

1. **Clone the repo**
   ```bash
   git clone https://github.com/KaranDeepBajaj/resume-ranker-ai.git
   cd resume-ranker-ai
