import streamlit as st
from app.resume_parser import extract_resume_text
from app.jd_parser import parse_job_description
from app.ranker import rank_resumes
import pandas as pd
import tempfile

st.set_page_config(page_title="AI Resume Ranker", layout="centered")
st.title("🧠 AI Resume Ranker")
st.markdown("Upload a job description and multiple resumes to see which candidate matches best.")

# Upload Job Description
jd_file = st.file_uploader("📄 Upload Job Description (.txt)", type="txt")

# Upload Resumes
resume_files = st.file_uploader("📁 Upload Resumes (PDF)", type="pdf", accept_multiple_files=True)

if jd_file and resume_files:
    with st.spinner("🔍 Analyzing resumes... please wait"):
        # Read job description
        jd_text = parse_job_description(jd_file.read().decode("utf-8"))

        # Extract text from all uploaded resumes
        resume_texts = []
        for r in resume_files:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                tmp.write(r.read())
                tmp.seek(0)
                resume_text = extract_resume_text(tmp.name)
                resume_texts.append(resume_text)

        # Rank resumes using your NLP model
        results = rank_resumes(jd_text, resume_texts)

        # 🏅 Display Top Match
        best_match_idx, best_score = results[0]
        st.success(f"🏅 Best Match: Resume #{best_match_idx + 1} (Score: {best_score:.4f})")

        # 📊 Show Ranking Table
        st.subheader("📊 Ranking Table")
        table_data = []
        for idx, score in results:
            table_data.append({
                "Resume #": idx + 1,
                "Score": f"{score:.4f}",
                "Preview": resume_texts[idx][:200].replace("\n", " ") + "..."
            })

        df = pd.DataFrame(table_data)
        st.dataframe(df, use_container_width=True)
