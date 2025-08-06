import streamlit as st
import pandas as pd
import tempfile

from app.resume_parser import extract_resume_text
from app.jd_parser import parse_job_description
from app.ranker import rank_resumes
from app.explain_matcher import get_gpt_explanation

# Page setup
st.set_page_config(page_title="AI Resume Ranker", layout="centered")
st.title("🧠 AI Resume Ranker")
st.markdown("Upload a job description and multiple resumes to see which candidate matches best using AI.")

# Upload section
jd_file = st.file_uploader("📄 Upload Job Description (.txt)", type="txt")
resume_files = st.file_uploader("📁 Upload Resumes (.pdf)", type="pdf", accept_multiple_files=True)

if jd_file and resume_files:
    with st.spinner("🔍 Analyzing resumes... please wait"):

        # ✅ Step 1: Parse JD
        jd_text = parse_job_description(jd_file.read().decode("utf-8"))

        # ✅ Step 2: Extract resume texts
        resume_texts = []
        for r in resume_files:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                tmp.write(r.read())
                tmp.seek(0)
                resume_texts.append(extract_resume_text(tmp.name))

        # ✅ Step 3: Rank resumes
        results = rank_resumes(jd_text, resume_texts)

        # ✅ Step 4: Show top match
        best_match_idx, best_score = results[0]
        st.success(f"🏅 Best Match: Resume #{best_match_idx + 1} (Score: {best_score:.4f})")

        # ✅ Step 5: Explanation from Cohere
        st.subheader("🧠 Why This Resume?")
        explanation = get_gpt_explanation(jd_text, resume_texts[best_match_idx], best_score)
        st.info(explanation)

        # ✅ Step 6: Show ranking table
        st.subheader("📊 Ranking Table")
        table_data = []
        for idx, score in results:
            table_data.append({
                "Resume #": idx + 1,
                "Score": f"{score:.4f}",
                "Preview": resume_texts[idx][:200].replace("\n", " ") + "..."
            })

        st.dataframe(pd.DataFrame(table_data), use_container_width=True)
