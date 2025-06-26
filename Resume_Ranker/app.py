import streamlit as st
import pandas as pd
from ranker import extract_text_from_pdf, score_resumes
from utils import get_pdf_files, read_job_description, extract_jd_keywords

# Streamlit page settings
st.set_page_config(page_title="AI Resume Ranker", layout="centered")

st.title("📄 AI Resume Ranker - Enhanced Version")
st.markdown("""
Ranks resumes based on job relevance using **synonym-aware skill matching** 🧠  
Upload resume PDFs and a job description to get a smart ranking.
""")

# Input paths
resume_folder = st.text_input("📁 Resume Folder (PDFs only)", "sample_resumes")
jd_path = st.text_input("📄 Job Description File", "job_description.txt")

# Run ranking
if st.button("🚀 Rank Resumes"):
    try:
        # Load files
        resume_files = get_pdf_files(resume_folder)
        jd_text = read_job_description(jd_path)
        jd_keywords = extract_jd_keywords(jd_text)

        if not jd_keywords:
            st.warning("⚠️ No recognizable skills found in job description. Please check the file.")
        else:
            resume_texts = [extract_text_from_pdf(f) for f in resume_files]
            results = score_resumes(resume_texts, jd_keywords)

            # Format output
            df = pd.DataFrame({
                "Resume": [f.split("/")[-1] for f in resume_files],
                "Score (%)": [r[0] for r in results],
                "Skills Matched": [", ".join(r[1]) if r[1] else "None" for r in results]
            }).sort_values(by="Score (%)", ascending=False)

            st.success("✅ Ranking complete!")
            st.dataframe(df)

            # Download button
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button("⬇️ Download Results as CSV", csv, file_name="resume_ranking.csv", mime="text/csv")

            # Preview matched keywords per resume
            st.markdown("### ✅ Summary of Matches")
            for i, row in df.iterrows():
                st.markdown(f"- **{row['Resume']}** matched: `{row['Skills Matched']}`")

    except Exception as e:
        st.error(f"❌ Error: {e}")
