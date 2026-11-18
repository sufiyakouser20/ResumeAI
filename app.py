
import streamlit as st
import pandas as pd
import html


from resume_feedback import generate_resume_feedback
from learning_roadmap import generate_learning_roadmap
from report_generator import generate_pdf_report
from resume_parser import extract_text
from skill_extractor import extract_skills
from job_matcher import recommend_jobs
from ats_analyzer import analyze_ats


# ==================================================
# 1. PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="ResumeAI | Career Intelligence",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==================================================
# 2. CUSTOM DARK THEME
# ==================================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #0B1220, #111D32);
    color: #E2EAF5;
}

[data-testid="stSidebar"] {
    background: #101B2D;
    border-right: 1px solid #293B55;
}

h1, h2, h3 {
    color: #EAF0FA !important;
}

p, label {
    color: #B9C8DC;
}

.hero {
    background: linear-gradient(110deg, #443B91, #145B75);
    padding: 30px;
    border-radius: 18px;
    border: 1px solid #6476C7;
    margin-bottom: 25px;
}

.hero h1 {
    color: #FFFFFF !important;
    font-size: 34px;
    margin: 0;
}

.hero p {
    color: #D8E8F5 !important;
    font-size: 15px;
}

[data-testid="stFileUploaderDropzone"] {
    background: #17243A !important;
    border: 2px dashed #8B7CFF !important;
    border-radius: 15px !important;
    padding: 25px !important;
}

[data-testid="stFileUploaderDropzone"] * {
    color: #EAF0FA !important;
}

[data-testid="stFileUploaderDropzone"] button {
    background: #34476A !important;
    color: #FFFFFF !important;
    border: 1px solid #8B7CFF !important;
    border-radius: 8px !important;
}

[data-testid="stFileUploaderFile"] {
    background: #243651 !important;
    border: 1px solid #6476C7 !important;
    border-radius: 10px !important;
}

[data-testid="stFileUploaderFile"] * {
    color: #EAF0FA !important;
}

.metric-card {
    background: #17243A;
    border: 1px solid #344A68;
    border-radius: 16px;
    padding: 20px;
    min-height: 115px;
    transition: 0.25s;
}

.metric-card:hover {
    border-color: #8B7CFF;
    transform: translateY(-4px);
}

.metric-label {
    color: #9DB0C9;
    font-size: 14px;
}

.metric-value {
    color: #EAF0FA;
    font-size: 29px;
    font-weight: bold;
    margin-top: 10px;
}

.skill-tag {
    display: inline-block;
    background: #293B68;
    color: #DDE6FF;
    border: 1px solid #536DA5;
    padding: 7px 12px;
    border-radius: 20px;
    margin: 4px;
    font-size: 13px;
}

.stButton > button {
    background: linear-gradient(90deg, #6955E8, #168EAA) !important;
    color: #FFFFFF !important;
    border: 1px solid #7185F5 !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
    min-height: 43px;
    transition: 0.25s;
}

.stButton > button:hover {
    border-color: #A99EFF !important;
    box-shadow: 0 4px 18px #6955E855;
    transform: translateY(-2px);
}

.stTextArea textarea {
    background: #17243A !important;
    color: #EAF0FA !important;
    border: 1px solid #425B7C !important;
    border-radius: 10px !important;
}

[data-baseweb="select"] > div {
    background: #17243A !important;
    border-color: #536DA5 !important;
    color: #EAF0FA !important;
}

[data-testid="stAlert"] {
    background: #17243A !important;
    border: 1px solid #425B7C !important;
    border-radius: 10px !important;
}

[data-testid="stAlert"] * {
    color: #EAF0FA !important;
}

.stProgress > div > div {
    background-color: #8B7CFF !important;
}

hr {
    border-color: #344A68 !important;
}

.footer {
    text-align: center;
    color: #8195B1;
    padding: 25px;
    font-size: 13px;
}

.roadmap-card {
    background: #17243A;
    border: 1px solid #425B7C;
    border-left: 5px solid #8B7CFF;
    border-radius: 14px;
    padding: 20px;
    margin-bottom: 18px;
}

.roadmap-card h3 {
    color: #C7C0FF !important;
}

.roadmap-duration {
    color: #52D6C5;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)


# ==================================================
# 3. SESSION STATE
# ==================================================

defaults = {
    "resume_text": "",
    "skills": [],
    "results": None,
    "uploaded_name": "",
    "learning_progress": {}
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# ==================================================
# 4. SIDEBAR NAVIGATION
# ==================================================

st.sidebar.markdown("## 📄 ResumeAI")
st.sidebar.caption("CAREER INTELLIGENCE PLATFORM")
st.sidebar.divider()

page = st.sidebar.radio(
    "EXPLORE",
    [
        "Dashboard",
        "Resume Analysis",
        "Job Recommendations",
        "Skill Gap Analysis",
        "Learning Roadmap",
        "Resume Improvement",
        "ATS Score & Keywords"
    ]
)

st.sidebar.divider()
st.sidebar.markdown("### ✨ Your Career Assistant")

st.sidebar.caption(
    "Analyze your resume, discover your skills "
    "and explore career opportunities."
)

st.sidebar.divider()
st.sidebar.caption("Built with Python • Streamlit • ML")


# ==================================================
# 5. HERO SECTION
# ==================================================

st.markdown("""
<div class="hero">
    <h1>Welcome to ResumeAI ✨</h1>
    <p>
        Your personal career intelligence platform.
        Discover your strengths, explore job opportunities
        and identify the skills you need to grow.
    </p>
</div>
""", unsafe_allow_html=True)


# ==================================================
# 6. RESUME UPLOAD
# ==================================================

st.subheader("📤 Upload Your Resume")

st.caption(
    "Upload a PDF or DOCX resume to begin your analysis."
)

uploaded_file = st.file_uploader(
    "Choose your resume",
    type=["pdf", "docx"],
    help="Supported formats: PDF and DOCX",
    key="resume_uploader"
)

if uploaded_file is not None:

    st.caption(f"Selected: {uploaded_file.name}")

    if st.button(
        "🚀 Analyze My Resume",
        use_container_width=True
    ):

        with st.spinner("Analyzing your resume..."):

            try:

                resume_text = extract_text(uploaded_file)

                if not resume_text.strip():

                    st.error(
                        "No readable text found. "
                        "Please upload a text-based resume."
                    )

                else:

                    skills = extract_skills(resume_text)

                    st.session_state.resume_text = resume_text
                    st.session_state.skills = skills
                    st.session_state.uploaded_name = uploaded_file.name

                    if skills:

                        results = recommend_jobs(skills)
                        st.session_state.results = results

                        st.success("Resume analysis completed!")

                    else:

                        st.session_state.results = None

                        st.warning(
                            "No matching skills were identified."
                        )

            except Exception as error:

                st.error(f"Analysis error: {error}")


# ==================================================
# 7. GET SESSION DATA
# ==================================================

skills = st.session_state.skills
results = st.session_state.results


# ==================================================
# 8. DASHBOARD
# ==================================================

if page == "Dashboard":

    st.divider()
    st.subheader("📊 Career Overview")

    best_match = (
        f"{results.iloc[0]['match_score']:.1f}%"
        if results is not None and not results.empty
        else "—"
    )

    total_jobs = len(results) if results is not None else 0

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">💡 Skills Identified</div>
            <div class="metric-value">{len(skills)}</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">💼 Job Roles Analyzed</div>
            <div class="metric-value">{total_jobs}</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">🏆 Best Job Match</div>
            <div class="metric-value">{best_match}</div>
        </div>
        """, unsafe_allow_html=True)

    st.divider()
    st.subheader("💡 Your Technical Skills")

    if skills:

        skill_html = "".join(
            f'<span class="skill-tag">{html.escape(str(skill))}</span>'
            for skill in skills
        )

        st.markdown(skill_html, unsafe_allow_html=True)

    else:
        st.info("Upload and analyze a resume to see your skills.")

    st.divider()
    st.subheader("🏆 Top Career Recommendations")

    if results is not None and not results.empty:

        for _, row in results.head(3).iterrows():

            role = html.escape(str(row["role"]))
            score = float(row["match_score"])

            with st.container(border=True):

                st.markdown(f"### 💼 {role}")

                col1, col2 = st.columns([3, 1])

                with col1:
                    st.progress(min(max(score / 100, 0), 1))

                with col2:
                    st.metric("Similarity", f"{score:.1f}%")

    else:
        st.info("Your recommended careers will appear here.")

    if results is not None and not results.empty:

        st.divider()
        st.subheader("📊 Interactive Career Analytics")

        st.caption(
            "Compare your resume similarity scores "
            "across different career roles."
        )

        chart_data = results[
            ["role", "match_score"]
        ].copy()

        chart_data["match_score"] = pd.to_numeric(
            chart_data["match_score"],
            errors="coerce"
        )

        chart_data = chart_data.dropna()

        chart_data = chart_data.sort_values(
            "match_score",
            ascending=False
        )

        if not chart_data.empty:

            selected_role = st.selectbox(
                "Explore a specific career role",
                chart_data["role"].tolist(),
                key="analytics_role"
            )

            selected_score = chart_data.loc[
                chart_data["role"] == selected_role,
                "match_score"
            ].iloc[0]

            col1, col2 = st.columns(2)

            with col1:
                st.metric("Selected Career", selected_role)

            with col2:
                st.metric(
                    "Resume Similarity",
                    f"{selected_score:.2f}%"
                )

            st.markdown("### 📈 Job Role Comparison")

            st.bar_chart(
                chart_data.set_index("role"),
                y="match_score",
                height=350
            )

            st.caption(
                "Higher scores indicate greater text similarity "
                "between your resume and sample job requirements. "
                "They are not hiring probabilities."
            )


# ==================================================
# 9. RESUME ANALYSIS PAGE
# ==================================================

elif page == "Resume Analysis":

    st.subheader("📑 Resume Analysis")

    if st.session_state.resume_text:

        st.success(
            f"Analyzed file: {st.session_state.uploaded_name}"
        )

        with st.expander("View extracted resume text", expanded=True):

            st.text_area(
                "Resume content",
                st.session_state.resume_text,
                height=300
            )

        st.divider()
        st.subheader("Identified Technical Skills")

        if skills:

            skill_html = "".join(
                f'<span class="skill-tag">{html.escape(str(skill))}</span>'
                for skill in skills
            )

            st.markdown(skill_html, unsafe_allow_html=True)

            st.metric("Total skills identified", len(skills))

        else:
            st.info("No matching skills found.")

    else:
        st.info("Upload and analyze your resume first.")


# ==================================================
# 10. JOB RECOMMENDATIONS PAGE
# ==================================================

elif page == "Job Recommendations":

    st.subheader("🎯 Career Recommendations")

    st.caption(
        "Explore job roles ranked by similarity "
        "to your resume skills."
    )

    if results is not None and not results.empty:

        sort_order = st.selectbox(
            "Sort recommendations",
            [
                "Highest match first",
                "Lowest match first"
            ]
        )

        display_results = results.sort_values(
            "match_score",
            ascending=(sort_order == "Lowest match first")
        )

        for _, row in display_results.iterrows():

            role = html.escape(str(row["role"]))
            score = float(row["match_score"])

            with st.container(border=True):

                st.markdown(f"### 💼 {role}")

                st.progress(min(max(score / 100, 0), 1))

                st.metric(
                    "Resume similarity score",
                    f"{score:.2f}%"
                )

        st.caption(
            "These are text-similarity scores, "
            "not probabilities of getting hired."
        )

    else:
        st.info("Analyze a resume to see job recommendations.")


# ==================================================
# 11. SKILL GAP ANALYSIS PAGE
# ==================================================

elif page == "Skill Gap Analysis":

    st.subheader("🔍 Skill Gap Analysis")

    st.caption(
        "Discover which required skills are present "
        "and which skills you can work on."
    )

    if results is not None and skills:

        selected_role = st.selectbox(
            "Choose your target career",
            results["role"].tolist(),
            key="gap_role"
        )

        selected_job = results[
            results["role"] == selected_role
        ].iloc[0]

        required_skills = [
            skill.strip()
            for skill in str(selected_job["skills"]).split(",")
            if skill.strip()
        ]

        user_skills = [
            str(skill).lower()
            for skill in skills
        ]

        matched = [
            skill for skill in required_skills
            if skill.lower() in user_skills
        ]

        missing = [
            skill for skill in required_skills
            if skill.lower() not in user_skills
        ]

        total = len(required_skills)

        percentage = (
            len(matched) / total * 100
            if total > 0
            else 0
        )

        st.divider()
        st.markdown("### 📈 Skill Readiness Overview")

        st.metric(
            "Required skills matched",
            f"{len(matched)} / {total}",
            f"{percentage:.1f}%"
        )

        st.progress(percentage / 100)

        col1, col2 = st.columns(2)

        with col1:

            st.markdown("### ✅ Skills You Have")

            if matched:

                for skill in matched:
                    st.success(skill)

            else:
                st.info("No matching skills.")

        with col2:

            st.markdown("### 📚 Skills to Learn")

            if missing:

                for skill in missing:
                    st.warning(skill)

            else:
                st.success("All listed skills are matched!")

        st.divider()
        st.markdown("### 🎯 Suggested Learning Focus")

        if missing:

            st.write(
                "Focus on learning the missing skills "
                "for your selected career role."
            )

            for skill in missing:
                st.markdown(f"- Learn **{skill}**")

        else:

            st.success(
                "Your resume includes all skills listed "
                "in this sample job dataset."
            )

        st.caption(
            "This comparison uses the requirements "
            "in your sample job dataset."
        )

        # PDF REPORT DOWNLOAD

        st.divider()
        st.markdown("### 📥 Download Your Career Report")

        st.caption(
            "Generate a PDF containing your resume skills, "
            "job recommendations and skill gap analysis."
        )

        if st.button(
            "📄 Generate PDF Report",
            use_container_width=True
        ):

            try:

                pdf_path = "ResumeAI_Career_Report.pdf"

                generate_pdf_report(
                    filename=pdf_path,
                    resume_name=st.session_state.uploaded_name,
                    skills=skills,
                    job_results=results,
                    selected_role=selected_role,
                    matched_skills=matched,
                    missing_skills=missing
                )

                with open(pdf_path, "rb") as pdf_file:
                    pdf_data = pdf_file.read()

                st.success("Your PDF report is ready!")

                st.download_button(
                    label="⬇️ Download Career Report",
                    data=pdf_data,
                    file_name="ResumeAI_Career_Report.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )

            except Exception as error:

                st.error(f"PDF generation failed: {error}")

    else:

        st.info("Analyze a resume first to view your skill gaps.")


# ==================================================
# 12. LEARNING ROADMAP PAGE
# ==================================================

elif page == "Learning Roadmap":

    st.subheader("🚀 Your Personal Learning Roadmap")

    st.caption(
        "Turn your missing skills into a structured learning plan "
        "and move closer to your target career."
    )

    if results is not None and skills:

        selected_role = st.selectbox(
            "Choose your target career",
            results["role"].tolist(),
            key="roadmap_role"
        )

        selected_job = results[
            results["role"] == selected_role
        ].iloc[0]

        required_skills = [
            skill.strip()
            for skill in str(selected_job["skills"]).split(",")
            if skill.strip()
        ]

        user_skills = [
            str(skill).lower()
            for skill in skills
        ]

        missing = [
            skill for skill in required_skills
            if skill.lower() not in user_skills
        ]

        st.divider()

        st.markdown("### 🎯 Your Learning Goal")

        st.info(
            f"Build the skills required for the "
            f"**{selected_role}** career path."
        )

        if missing:

            roadmap = generate_learning_roadmap(missing)

            st.markdown("### 📚 Skills to Develop")

            total_skills = len(roadmap)

            st.metric(
                "Skills to improve",
                total_skills
            )

            st.progress(0.0)

            st.caption(
                "Your roadmap is organized skill by skill. "
                "Complete the learning activities at your own pace."
            )

            for index, item in enumerate(roadmap, start=1):

                skill_name = html.escape(str(item["skill"]))
                duration = html.escape(str(item["duration"]))
                resource = html.escape(str(item["resource"]))
                link = html.escape(str(item["link"]), quote=True)

                with st.container(border=True):

                    st.markdown(
                        f"### {index}. {skill_name}"
                    )

                    st.markdown(
                        f'<p class="roadmap-duration">'
                        f'⏱ Estimated learning time: {duration}'
                        f'</p>',
                        unsafe_allow_html=True
                    )

                    st.markdown("#### Learning Steps")

                    for step_number, step in enumerate(
                        item["steps"],
                        start=1
                    ):

                        st.markdown(
                            f"{step_number}. {step}"
                        )

                    st.markdown("#### Recommended Resource")

                    st.markdown(
                        f"[{resource}]({link})"
                    )

            st.divider()

            st.success(
                "Your personalized learning roadmap is ready!"
            )

            st.caption(
                "Estimated durations are learning suggestions, "
                "not guaranteed completion times."
            )

        else:

            st.success(
                "Excellent! Your resume already contains "
                "all the skills listed for this career role."
            )

            st.balloons()

            st.markdown(
                "You can continue improving your knowledge "
                "through projects, certifications and practical experience."
            )

    else:

        st.info(
            "Please upload and analyze your resume first "
            "to generate your personalized learning roadmap."
        )


# ==================================================
# 13. LEARNING PROGRESS TRACKER
# ==================================================

if page == "Learning Roadmap" and results is not None and skills:

    st.divider()

    st.markdown("## 📊 Learning Progress Tracker")

    selected_role = st.session_state.get("roadmap_role")

    if selected_role:

        selected_job = results[
            results["role"] == selected_role
        ].iloc[0]

        required_skills = [
            skill.strip()
            for skill in str(selected_job["skills"]).split(",")
            if skill.strip()
        ]

        user_skills = [
            str(skill).lower()
            for skill in skills
        ]

        missing = [
            skill for skill in required_skills
            if skill.lower() not in user_skills
        ]

        roadmap = generate_learning_roadmap(missing)

        total_steps = 0
        completed_steps = 0

        for item in roadmap:

            skill = item["skill"]

            for index, step in enumerate(item["steps"]):

                progress_key = f"{selected_role}_{skill}_{index}"

                if progress_key not in st.session_state.learning_progress:
                    st.session_state.learning_progress[progress_key] = False

                total_steps += 1

                if st.session_state.learning_progress[progress_key]:
                    completed_steps += 1

        overall_progress = (
            completed_steps / total_steps * 100
            if total_steps > 0
            else 100
        )

        st.metric(
            "Overall Learning Progress",
            f"{overall_progress:.1f}%",
            f"{completed_steps} of {total_steps} activities completed"
        )

        st.progress(overall_progress / 100)

        for item in roadmap:

            st.markdown(f"### 📚 {item['skill']}")

            skill_completed = 0

            for index, step in enumerate(item["steps"]):

                progress_key = f"{selected_role}_{item['skill']}_{index}"

                st.checkbox(
                    step,
                    key=f"tracker_{progress_key}",
                    value=st.session_state.learning_progress[progress_key],
                    on_change=lambda key=progress_key: st.session_state.learning_progress.update({
                        key: not st.session_state.learning_progress[key]
                    })
                )

                if st.session_state.learning_progress[progress_key]:
                    skill_completed += 1

            skill_progress = (
                skill_completed / len(item["steps"])
                if item["steps"]
                else 0
            )

            st.progress(skill_progress)

            st.caption(
                f"{skill_completed}/{len(item['steps'])} learning activities completed"
            )

        if total_steps > 0 and completed_steps == total_steps:

            st.success("🎉 Congratulations! You completed your entire learning roadmap!")

        st.caption(
            "Progress is stored during the current Streamlit session. "
            "It resets when the session is restarted."
        )

# ==================================================
# 14. RESUME IMPROVEMENT PAGE
# ==================================================

elif page == "Resume Improvement":

    st.subheader("✨ Resume Improvement Suggestions")

    st.caption(
        "Get actionable suggestions to improve your resume "
        "and make it more relevant to your target career."
    )

    if st.session_state.resume_text and results is not None:

        st.divider()

        selected_role = st.selectbox(
            "Choose your target career",
            results["role"].tolist(),
            key="feedback_role"
        )

        if st.button(
            "🔍 Analyze Resume Quality",
            use_container_width=True
        ):

            feedback = generate_resume_feedback(
                st.session_state.resume_text,
                st.session_state.skills,
                selected_role
            )

            st.session_state["resume_feedback"] = feedback

        if "resume_feedback" in st.session_state:

            feedback = st.session_state.resume_feedback

            st.divider()

            st.markdown("### 📋 Your Improvement Report")

            if feedback:

                high_count = sum(
                    1 for item in feedback
                    if item["importance"] == "High"
                )

                medium_count = sum(
                    1 for item in feedback
                    if item["importance"] == "Medium"
                )

                col1, col2, col3 = st.columns(3)

                with col1:
                    st.metric("Total Suggestions", len(feedback))

                with col2:
                    st.metric("High Priority", high_count)

                with col3:
                    st.metric("Medium Priority", medium_count)

                st.divider()

                for index, item in enumerate(feedback, start=1):

                    with st.container(border=True):

                        st.markdown(
                            f"### {index}. {item['category']}"
                        )

                        if item["importance"] == "High":
                            st.error("🔴 High Priority")
                        else:
                            st.warning("🟡 Medium Priority")

                        st.write(item["suggestion"])

                st.divider()

                st.success(
                    "Your resume improvement analysis is complete!"
                )

            else:

                st.success(
                    "Excellent! No suggestions were identified "
                    "by the current resume checks."
                )

            st.caption(
                "These suggestions are based on basic resume-content "
                "checks and should be reviewed before making changes."
            )

    else:

        st.info(
            "Please upload and analyze your resume first "
            "to receive improvement suggestions."
        )


# ==================================================
# 15. ATS SCORE & KEYWORD ANALYSIS
# ==================================================

elif page == "ATS Score & Keywords":

    st.subheader("🎯 ATS Score & Keyword Optimization")

    st.caption(
        "Check how well your resume matches the skills "
        "required for your selected career."
    )

    if st.session_state.resume_text and results is not None:

        selected_role = st.selectbox(
            "Select your target job role",
            results["role"].tolist(),
            key="ats_role"
        )

        selected_job = results[
            results["role"] == selected_role
        ].iloc[0]

        required_skills = [
            skill.strip()
            for skill in str(selected_job["skills"]).split(",")
            if skill.strip()
        ]

        if st.button(
            "🚀 Calculate ATS Score",
            use_container_width=True
        ):

            ats_result = analyze_ats(
                st.session_state.resume_text,
                required_skills
            )

            st.session_state["ats_result"] = ats_result

        if "ats_result" in st.session_state:

            ats_result = st.session_state.ats_result

            st.divider()

            st.markdown("### 📊 ATS Compatibility Report")

            score = ats_result["ats_score"]

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("Estimated ATS Score", f"{score}%")

            with col2:
                st.metric(
                    "Matched Keywords",
                    len(ats_result["matched_keywords"])
                )

            with col3:
                st.metric(
                    "Missing Keywords",
                    len(ats_result["missing_keywords"])
                )

            st.progress(score / 100)

            if score >= 75:
                st.success("Strong keyword match!")
            elif score >= 45:
                st.warning("Moderate keyword match. Some improvements are needed.")
            else:
                st.error("Low keyword match. Consider improving your resume.")

            st.divider()

            col1, col2 = st.columns(2)

            with col1:

                st.markdown("### ✅ Matched Keywords")

                if ats_result["matched_keywords"]:

                    for skill in ats_result["matched_keywords"]:
                        st.success(skill)

                else:
                    st.info("No matching keywords found.")

            with col2:

                st.markdown("### 📚 Missing Keywords")

                if ats_result["missing_keywords"]:

                    for skill in ats_result["missing_keywords"]:
                        st.warning(skill)

                else:
                    st.success("All required keywords are present!")

            st.divider()

            st.markdown("### 💡 Optimization Suggestions")

            if ats_result["missing_keywords"]:

                st.write(
                    "Consider adding these skills to your resume "
                    "if you genuinely possess them:"
                )

                for skill in ats_result["missing_keywords"]:
                    st.markdown(f"- **{skill}**")

            else:

                st.success(
                    "Your resume contains all the required "
                    "keywords in this job dataset."
                )

            st.caption(
                "This is an estimated keyword-match score based on "
                "your selected role's sample skill requirements. "
                "It is not an official ATS score or a guarantee "
                "of passing an employer's screening system."
            )

    else:

        st.info(
            "Please upload and analyze your resume first "
            "to calculate your ATS score."
        )


# ==================================================
# 13. FOOTER
# ==================================================

st.divider()

st.markdown("""
<div class="footer">
    ResumeAI | Career Intelligence Platform
    <br>
    Developed using Python, Streamlit and Machine Learning
</div>
""", unsafe_allow_html=True)
