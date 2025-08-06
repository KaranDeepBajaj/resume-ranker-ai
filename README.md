# 🤖 AI-Powered Resume Ranker

A smart, AI-driven system that ranks resumes based on a given job description using NLP and machine learning.

---

## 🚀 Demo
📹 [Insert demo video or link to live app--->> Coming Soon]

---

## 💡 Features

- Upload multiple resumes (PDF/DOCX)
- Upload a job description (JD)
- Rank resumes based on relevance to JD
- Show match score + missing keywords
- Optional: Explainable feedback using GPT

---

## 🛠️ Tech Stack

| Area | Tech |
|------|------|
| Backend | Python, FastAPI/Flask |
| NLP | spaCy, HuggingFace Transformers, OpenAI API |
| ML | TF-IDF, Cosine Similarity |
| Frontend | Streamlit / React (Optional) |
| Parsing | `pdfminer.six`, `python-docx`, `PyMuPDF` |
| Hosting | Hugging Face Spaces, Render, or AWS |
| Bonus | LangChain, FAISS (semantic search) |

---

## 📁 Folder Structure

resume-ranker-ai/
│
├── app/
│   ├── main.py                # FastAPI or Flask backend
│   ├── resume_parser.py       # Resume PDF/DOC parser
│   ├── jd_parser.py           # Job Description text processor
│   ├── ranker.py              # ML/NLP logic for ranking
│   ├── utils.py               # Helper functions
│   └── templates/             # (Flask) HTML templates if needed
│       └── index.html
│
├── frontend/                  # Optional if building frontend separately
│   ├── public/
│   └── src/
│       └── App.js
│
├── models/                    # Pretrained or saved models
│   └── tfidf_vectorizer.pkl
│
├── resumes/                   # Sample resumes for testing
│   └── sample_resume_1.pdf
│
├── jds/                       # Sample job descriptions
│   └── jd_software_engineer.txt
│
├── data/                      # Any CSVs or extracted metadata
│
├── notebooks/                 # Jupyter notebooks for experiments
│   └── similarity_experiments.ipynb
│
├── requirements.txt           # Python dependencies
├── .gitignore
├── README.md
└── LICENSE
