# 🧠 AI-Powered Resume Ranker

Ranks resumes against a job description using synonym-aware skill matching and smart keyword extraction.

## 🔧 Built With
- Python
- Streamlit
- PyMuPDF (PDF parser)
- Pandas

## 💡 Features
- PDF Resume matching
- JD keyword matching
- Synonym logic
- Result table + CSV export

## 📂 How to Run
ResumeRankerAI/
├── app.py
├── ranker.py
├── utils.py
├── job_description.txt
├── sample_resumes/
│ ├── sample_resume1.pdf
│ └── sample_resume2.pdf
├── README.md
└── Resume_Ranker_Report.pdf


---

## 💡 How It Works

1. User uploads resume PDFs + job description
2. JD is processed for known skills using a custom synonym dictionary
3. Each resume is scanned, text is extracted, and matched against JD skills
4. A match score is calculated (as percentage)
5. Output includes score + which skills matched, downloadable as CSV

---

## 📥 How to Run (Locally)

Make sure you have Python installed.

1. Open terminal or command prompt
2. Navigate to the folder:

cd path/to/ResumeRankerAI

3. Install dependencies:

pip install streamlit pymupdf pandas

4. Run the app:
streamlit run app.py


---

## 📘 Sample Use Case

> **Scenario**: An HR uploads 50 resumes for a Data Analyst job.  
> The app instantly shows which resumes match key skills like Python, SQL, and Data Visualization — saving hours of manual screening.

---

## 📄 Project Report

You can find the detailed project report here:  
[`Resume_Ranker_Report.pdf`](./Resume_Ranker_Report.pdf)

---

## 🏁 Status

✅ Complete and submission-ready  
🧠 Lightweight, explainable, and practical  
🎯 Built to stand out as a top performer

---

## ✨ Credits

Built with 💻 by DashamiJituri  
Mentored by ChatGPT
