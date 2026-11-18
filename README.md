# ResumeAI – AI Resume Analyzer and Job Recommendation System

## Project Overview
ResumeAI is an AI-based resume analysis and job recommendation system developed using Python and Streamlit.

It analyzes uploaded resumes, extracts skills, identifies suitable job roles, calculates job-match scores, and provides personalized recommendations to improve career readiness.

## Objectives
- Extract text from PDF and DOCX resumes.
- Identify technical and professional skills.
- Compare resume skills with job requirements.
- Recommend suitable job roles.
- Identify missing skills and suggest learning resources.
- Generate a downloadable PDF career report.

## Technologies Used
- Python
- Streamlit
- Pandas and NumPy
- Scikit-learn
- TF-IDF and Cosine Similarity
- PyPDF
- Python-docx
- ReportLab

## Main Features
1. PDF and DOCX resume upload.
2. Resume text extraction.
3. Automatic skill identification.
4. Job matching and recommendations.
5. Skill gap analysis.
6. Personalized learning roadmap.
7. Resume improvement suggestions.
8. ATS keyword analysis.
9. Downloadable PDF career report.

## Project Workflow
1. Upload a resume.
2. Extract resume text.
3. Identify skills.
4. Load job role requirements.
5. Calculate job-match scores.
6. Display suitable job recommendations.
7. Analyze missing skills.
8. Generate improvement suggestions and a learning roadmap.
9. Download the career report.

## Project Structure
```text
major project1/
├── app.py
├── resume_parser.py
├── skill_extractor.py
├── job_matcher.py
├── ats_analyzer.py
├── resume_feedback.py
├── learning_roadmap.py
├── report_generator.py
├── test_matcher.py
├── requirements.txt
├── README.md
├── data/
│   └── jobs.csv
└── .streamlit/
    └── config.toml
