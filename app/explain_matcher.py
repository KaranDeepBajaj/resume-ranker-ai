import os
import requests
from dotenv import load_dotenv

load_dotenv()
COHERE_API_KEY = os.getenv("COHERE_API_KEY")

API_URL = "https://api.cohere.ai/v1/generate"
headers = {
    "Authorization": f"Bearer {COHERE_API_KEY}",
    "Content-Type": "application/json"
}

def get_gpt_explanation(jd_text, resume_text, score):
    prompt = f"""You are an AI HR Assistant.

Job Description:
{jd_text.strip()[:600]}

Candidate Resume:
{resume_text.strip()[:600]}

This resume scored {score:.2f}.
Explain briefly why this resume is a good or bad fit.
"""

    try:
        payload = {
            "model": "command",   # You can also try "command-light"
            "prompt": prompt,
            "max_tokens": 150,
            "temperature": 0.6
        }

        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()

        return result.get("generations", [{}])[0].get("text", "⚠️ No response generated").strip()

    except Exception as e:
        return f"⚠️ Could not generate explanation: {str(e)}"
