import fitz  # PyMuPDF
from utils import SYNONYMS

# 📄 Extract raw text from PDF
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text.lower()

# 🧠 Match resume text to JD skills using synonyms
def match_resume_to_keywords(resume_text, jd_keywords):
    matched = []
    for skill in jd_keywords:
        for synonym in SYNONYMS[skill]:
            if synonym in resume_text:
                matched.append(skill)
                break
    return matched

# 🧮 Compute score & matched skills for each resume
def score_resumes(resume_texts, jd_keywords):
    all_results = []
    for text in resume_texts:
        matched = match_resume_to_keywords(text, jd_keywords)
        score = round((len(matched) / len(jd_keywords)) * 100, 2) if jd_keywords else 0
        all_results.append((score, matched))
    return all_results
