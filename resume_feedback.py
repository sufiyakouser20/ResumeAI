
import re


def generate_resume_feedback(resume_text, skills, target_role):

    feedback = []

    text = resume_text.lower()

    # 1. Check professional summary

    summary_keywords = [
        "summary",
        "objective",
        "profile",
        "about me"
    ]

    if not any(word in text for word in summary_keywords):

        feedback.append({
            "category": "Professional Summary",
            "suggestion": "Add a professional summary or career objective at the beginning of your resume.",
            "importance": "High"
        })

    # 2. Check education section

    education_keywords = [
        "education",
        "academic",
        "qualification"
    ]

    if not any(word in text for word in education_keywords):

        feedback.append({
            "category": "Education",
            "suggestion": "Add an education section with your degree, college name and academic details.",
            "importance": "High"
        })

    # 3. Check project section

    project_keywords = [
        "project",
        "projects",
        "academic project"
    ]

    if not any(word in text for word in project_keywords):

        feedback.append({
            "category": "Projects",
            "suggestion": "Include practical or academic projects to demonstrate your technical knowledge.",
            "importance": "High"
        })

    # 4. Check certifications

    certification_keywords = [
        "certification",
        "certifications",
        "certificate",
        "certificates"
    ]

    if not any(word in text for word in certification_keywords):

        feedback.append({
            "category": "Certifications",
            "suggestion": "Add relevant certifications, workshops or technical training you have completed.",
            "importance": "Medium"
        })

    # 5. Check experience or internship

    experience_keywords = [
        "experience",
        "internship",
        "intern",
        "work history"
    ]

    if not any(word in text for word in experience_keywords):

        feedback.append({
            "category": "Experience",
            "suggestion": "If applicable, include internships, volunteering, training or practical experience.",
            "importance": "Medium"
        })

    # 6. Check resume length

    word_count = len(resume_text.split())

    if word_count < 150:

        feedback.append({
            "category": "Resume Content",
            "suggestion": "Your resume contains limited content. Add relevant academic details, skills and project descriptions.",
            "importance": "High"
        })

    elif word_count > 1000:

        feedback.append({
            "category": "Resume Content",
            "suggestion": "Your resume is quite lengthy. Consider removing repeated or less relevant information.",
            "importance": "Medium"
        })

    # 7. Check technical skills

    if not skills:

        feedback.append({
            "category": "Technical Skills",
            "suggestion": "Add a dedicated technical skills section containing relevant tools and technologies.",
            "importance": "High"
        })

    # 8. Target role suggestion

    if target_role:

        feedback.append({
            "category": "Career Targeting",
            "suggestion": f"Highlight projects, skills and achievements relevant to the {target_role} role.",
            "importance": "High"
        })

    # 9. Check measurable achievements

    numbers = re.findall(r"\b\d+%?\b", resume_text)

    if len(numbers) < 2:

        feedback.append({
            "category": "Achievements",
            "suggestion": "Where possible, include measurable results such as project accuracy, performance improvements or participation numbers.",
            "importance": "Medium"
        })

    return feedback
