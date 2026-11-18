
from job_matcher import recommend_jobs

# Sample resume skills
resume_skills = [
    "Python",
    "SQL",
    "Excel",
    "Power BI",
    "Pandas",
    "NumPy"
]

# Get job recommendations
results = recommend_jobs(resume_skills)

# Display results
print("\nJOB RECOMMENDATIONS")
print("---------------------------")

for index, row in results.iterrows():

    print("Job Role:", row["role"])
    print("Match Score:", round(row["match_score"], 2), "%")
    print("---------------------------")
