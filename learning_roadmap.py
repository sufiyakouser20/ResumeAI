
# Learning Roadmap Generator

def generate_learning_roadmap(missing_skills):

    learning_resources = {
        "python": {
            "steps": [
                "Learn Python variables, data types and operators.",
                "Practice conditions, loops and functions.",
                "Learn lists, dictionaries and file handling."
            ],
            "resource": "Python Official Tutorial",
            "link": "https://docs.python.org/3/tutorial/",
            "duration": "2 weeks"
        },

        "sql": {
            "steps": [
                "Understand databases and tables.",
                "Practice SELECT, WHERE and ORDER BY.",
                "Learn JOIN, GROUP BY and subqueries."
            ],
            "resource": "W3Schools SQL Tutorial",
            "link": "https://www.w3schools.com/sql/",
            "duration": "2 weeks"
        },

        "power bi": {
            "steps": [
                "Understand Power BI interface and data import.",
                "Learn data cleaning using Power Query.",
                "Create charts, dashboards and reports."
            ],
            "resource": "Microsoft Power BI Learning",
            "link": "https://learn.microsoft.com/en-us/training/powerplatform/power-bi/",
            "duration": "2 weeks"
        },

        "pandas": {
            "steps": [
                "Understand Series and DataFrames.",
                "Practice filtering and cleaning datasets.",
                "Learn grouping, merging and data analysis."
            ],
            "resource": "Pandas Documentation",
            "link": "https://pandas.pydata.org/docs/",
            "duration": "1 week"
        },

        "numpy": {
            "steps": [
                "Learn NumPy arrays and array creation.",
                "Practice indexing and mathematical operations.",
                "Understand array reshaping and broadcasting."
            ],
            "resource": "NumPy Learn",
            "link": "https://numpy.org/learn/",
            "duration": "1 week"
        },

        "excel": {
            "steps": [
                "Learn formulas and basic functions.",
                "Practice sorting, filtering and pivot tables.",
                "Create charts and interactive reports."
            ],
            "resource": "Microsoft Excel Training",
            "link": "https://support.microsoft.com/excel",
            "duration": "1 week"
        },

        "machine learning": {
            "steps": [
                "Understand supervised and unsupervised learning.",
                "Learn regression and classification algorithms.",
                "Practice building models using Scikit-learn."
            ],
            "resource": "Scikit-learn Tutorials",
            "link": "https://scikit-learn.org/stable/tutorial/",
            "duration": "3 weeks"
        },

        "java": {
            "steps": [
                "Learn Java syntax, variables and data types.",
                "Practice loops, arrays and methods.",
                "Understand object-oriented programming."
            ],
            "resource": "Oracle Java Tutorials",
            "link": "https://docs.oracle.com/javase/tutorial/",
            "duration": "3 weeks"
        },

        "html": {
            "steps": [
                "Learn HTML structure and elements.",
                "Practice forms, tables and links.",
                "Build a simple webpage."
            ],
            "resource": "MDN HTML Guide",
            "link": "https://developer.mozilla.org/en-US/docs/Web/HTML",
            "duration": "1 week"
        },

        "css": {
            "steps": [
                "Learn selectors, colors and typography.",
                "Practice layouts using Flexbox and Grid.",
                "Build a responsive webpage."
            ],
            "resource": "MDN CSS Guide",
            "link": "https://developer.mozilla.org/en-US/docs/Web/CSS",
            "duration": "1 week"
        },

        "javascript": {
            "steps": [
                "Learn variables, functions and conditions.",
                "Practice arrays and objects.",
                "Understand DOM manipulation."
            ],
            "resource": "JavaScript Guide",
            "link": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide",
            "duration": "3 weeks"
        },

        "git": {
            "steps": [
                "Understand version control.",
                "Practice add, commit and push commands.",
                "Learn branches and merging."
            ],
            "resource": "Git Documentation",
            "link": "https://git-scm.com/doc",
            "duration": "1 week"
        },

        "communication": {
            "steps": [
                "Practice speaking clearly and confidently.",
                "Improve professional writing and email skills.",
                "Practice group discussions and presentations."
            ],
            "resource": "Toastmasters Resources",
            "link": "https://www.toastmasters.org/",
            "duration": "Ongoing"
        }
    }

    roadmap = []

    for skill in missing_skills:

        skill_key = skill.strip().lower()

        if skill_key in learning_resources:
            details = learning_resources[skill_key]

            roadmap.append({
                "skill": skill,
                "steps": details["steps"],
                "resource": details["resource"],
                "link": details["link"],
                "duration": details["duration"]
            })

        else:
            roadmap.append({
                "skill": skill,
                "steps": [
                    f"Understand the basic concepts of {skill}.",
                    f"Practice {skill} through beginner exercises.",
                    f"Build a small practical project using {skill}."
                ],
                "resource": "Search for beginner tutorials",
                "link": "https://www.google.com/search?q="
                        + skill.replace(" ", "+")
                        + "+beginner+tutorial",
                "duration": "1–2 weeks"
            })

    return roadmap
