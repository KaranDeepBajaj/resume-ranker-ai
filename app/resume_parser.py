from pdfminer.high_level import extract_text
import docx2txt

def extract_resume_text(file_obj):
    if hasattr(file_obj, 'name'):
        filename = file_obj.name
    elif isinstance(file_obj, str):
        filename = file_obj
    else:
        raise ValueError("Invalid file input")

    if filename.endswith('.pdf'):
        return extract_text(file_obj)
    elif filename.endswith('.docx'):
        return docx2txt.process(file_obj)
    elif filename.endswith('.txt'):
        return file_obj.read().decode('utf-8') if not isinstance(file_obj, str) else open(file_obj).read()
    else:
        raise ValueError("Unsupported file format")
