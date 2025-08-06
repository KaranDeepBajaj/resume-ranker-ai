import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_gpt_explanation(jd_text, resume_text, score):
    try:
        api_key = os.getenv("OPENROUTER_API_KEY")
        if not api_key:
            raise ValueError("Missing OpenRouter API key")

        headers = {
            "Authorization": f"Bearer {api_key}",
            "HTTP-Referer": "https://resume-ranker.ai",  # Can be anything
            "X-Title": "Resume Ranker AI"
        }

        payload = {
            "model": "mistralai/mistral-7b-instruct",
            "messages": [
                {"role": "system", "content": "You are an expert AI recruiter."},
                {"role": "user", "content": f"""
Job Description: {jd_text.strip()[:400]}

Resume: {resume_text.strip()[:400]}

This resume scored {score:.2f}. Why is it a good or bad match?
"""}
            ]
        }

        res = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)
        res.raise_for_status()
        return res.json()["choices"][0]["message"]["content"]

    except Exception as e:
        return f"⚠️ Could not generate explanation: {str(e)}"
