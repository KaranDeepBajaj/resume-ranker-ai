import genai as genai

from app.resume_parser import extract_resume_text
from app.jd_parser import parse_job_description
from app.explain_matcher import get_gpt_explanation

print(get_gpt_explanation(
    "Looking for Python developer with cloud experience",
    "Worked with Python, deployed to AWS and GCP with Docker and CI/CD pipelines",
    0.87
))

