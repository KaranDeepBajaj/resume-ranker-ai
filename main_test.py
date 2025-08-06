from app.resume_parser import extract_resume_text
from app.jd_parser import parse_job_description
from app.ranker import rank_resumes

# Load sample resume
resume_text = extract_resume_text("resumes/sample_resume.pdf")

# Load job description
with open("jds/sample_jd.txt", "r") as f:
    jd_text = parse_job_description(f.read())

# Test ranking (with 1 resume for now)
results = rank_resumes(jd_text, [resume_text])

# Print match score
for idx, score in results:
    print(f"Resume #{idx + 1}: Match Score = {score:.4f}")