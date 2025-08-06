import os
import docx2txt
from pdfminer.high_level import extract_text

def extract_resume_text(file_path: str) -> str:
    if file_path.endswith('.pdf'):
        return extract_text(file_path)
    elif file_path.endswith('.docx'):
        return docx2txt.process(file_path)
    else:
        raise ValueError("Unsupported file format: only PDF and DOCX are allowed.")
