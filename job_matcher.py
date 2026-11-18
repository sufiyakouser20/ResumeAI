
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def recommend_jobs(resume_skills):

    # Load job dataset
    jobs = pd.read_csv("data/jobs.csv")

    # Convert resume skills into text
    resume_text = " ".join(resume_skills)

    # Get required skills for each job
    job_skills = jobs["skills"].tolist()

    # Combine resume and job skills
    all_text = [resume_text] + job_skills

    # Convert text into numerical vectors
    vectorizer = TfidfVectorizer()

    tfidf_matrix = vectorizer.fit_transform(all_text)

    # Calculate similarity
    similarity_scores = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:]
    )

    # Store matching scores
    jobs["match_score"] = similarity_scores[0] * 100

    # Sort jobs by matching score
    jobs = jobs.sort_values(
        by="match_score",
        ascending=False
    )

    return jobs
