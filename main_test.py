from app.resume_parser import extract_resume_text
from app.jd_parser import parse_job_description
from app.ranker import rank_resumes

# Load JD
with open("jds/sample_jd.txt", "r") as f:
    jd_text = parse_job_description(f.read())

# Load resumes
resumes = [
    extract_resume_text("resumes/sample_resume_1.pdf"),
    extract_resume_text("resumes/sample_resume_2.pdf")
]

# Rank them
results = rank_resumes(jd_text, resumes)

# Show results
for idx, score in results:
    print(f"Resume #{idx + 1}: Match Score = {score:.4f}")

# Show best match
best = max(results, key=lambda x: x[1])
print(f"\n✅ Best Match: Resume #{best[0]+1} with score {best[1]:.4f}")
