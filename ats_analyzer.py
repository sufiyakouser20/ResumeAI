
import re


def analyze_ats(resume_text, required_skills):

    resume_text = resume_text.lower()

    matched_skills = []
    missing_skills = []

    for skill in required_skills:

        skill = skill.strip()

        if not skill:
            continue

        pattern = r"(?<!\w)" + re.escape(skill.lower()) + r"(?!\w)"

        if re.search(pattern, resume_text):
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    total_skills = len(matched_skills) + len(missing_skills)

    if total_skills > 0:
        ats_score = (len(matched_skills) / total_skills) * 100
    else:
        ats_score = 0

    return {
        "ats_score": round(ats_score, 2),
        "matched_keywords": matched_skills,
        "missing_keywords": missing_skills,
        "total_keywords": total_skills
    }
