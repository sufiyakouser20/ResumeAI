
import re

# List of skills our system can recognize
SKILLS = [
    "Python",
    "Java",
    "C++",
    "C",
    "Machine Learning",
    "Deep Learning",
    "Artificial Intelligence",
    "Data Science",
    "Data Analysis",
    "SQL",
    "MySQL",
    "HTML",
    "CSS",
    "JavaScript",
    "React",
    "Flask",
    "Django",
    "Streamlit",
    "TensorFlow",
    "PyTorch",
    "Pandas",
    "NumPy",
    "Scikit-learn",
    "NLP",
    "Computer Vision",
    "Git",
    "GitHub",
    "Power BI",
    "Excel",
    "Tableau"
]


def extract_skills(resume_text):

    found_skills = []

    text = resume_text.lower()

    for skill in SKILLS:

        pattern = r"(?<!\w)" + re.escape(skill.lower()) + r"(?!\w)"

        if re.search(pattern, text):
            found_skills.append(skill)

    return found_skills
