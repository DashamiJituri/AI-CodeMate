import os

# ✅ Synonym dictionary to expand JD intelligently
SYNONYMS = {
    "machine learning": ["ml", "machine learning", "deep learning"],
    "python": ["python"],
    "sql": ["sql", "structured query language"],
    "data analysis": ["data analysis", "analytics", "insights"],
    "data visualization": ["power bi", "tableau", "data viz", "visualization"],
    "communication": ["communication", "presenting", "public speaking"]
}

# 📂 Get all PDF files in folder
def get_pdf_files(folder_path):
    return [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith(".pdf")]

# 📄 Read job description
def read_job_description(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.read().lower()

# 🧠 Expand JD into a list of all skills/synonyms
def extract_jd_keywords(jd_text):
    keywords = []
    for key, synonyms in SYNONYMS.items():
        for word in synonyms:
            if word in jd_text:
                keywords.append(key)
                break
    return list(set(keywords))  # Remove duplicates
