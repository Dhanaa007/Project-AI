import streamlit as st
import os

API_KEY = st.secrets["GROQ_API_KEY"]

from groq import Groq
client = Groq(api_key=API_KEY)

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="Problem2Project AI",
    page_icon="🚀",
    layout="wide"
)

# -------------------------------
# Custom CSS
# -------------------------------
st.markdown("""
<style>
.main {
    background-color: #F8FAFC;
}
h1 {
    color: #1E3A8A;
    text-align: center;
}
.stButton > button {
    background: #2563EB;
    color: white;
    border-radius: 10px;
    padding: 12px;
    width: 100%;
    font-size: 18px;
}
.stButton > button:hover {
    background: #1D4ED8;
}
.box {
    background: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 0px 12px rgba(0, 0, 0, 0.1);
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# Header
# -------------------------------
st.title("🚀 Problem2Project AI")
st.markdown("""
### Transform Real-World Problems into Software Projects
Enter a problem, choose your domain and skill level,
and let AI generate a complete project idea.
""")

# -------------------------------
# Sidebar
# -------------------------------
st.sidebar.title("Project Settings")

domain = st.sidebar.selectbox(
    "Select Domain",
    [
        "Artificial Intelligence",
        "Web Development",
        "Machine Learning",
        "Cyber Security",
        "Data Science",
        "IoT",
        "Cloud Computing",
        "Blockchain"
    ]
)

level = st.sidebar.selectbox(
    "Skill Level",
    [
        "Beginner",
        "Intermediate",
        "Advanced"
    ]
)

project_type = st.sidebar.selectbox(
    "Project Type",
    [
        "Mini Project",
        "Portfolio Project",
        "Hackathon",
        "Major Project"
    ]
)

# -------------------------------
# Main Input
# -------------------------------
problem = st.text_area(
    "Describe a Real-World Problem",
    height=180,
    placeholder="Example: Students struggle to manage assignments and deadlines..."
)

generate = st.button("🚀 Generate Project")

# -------------------------------
# AI Prompt
# -------------------------------
prompt = f"""
You are an expert Software Architect.
Generate ONE innovative software project idea.

User Problem: {problem}
Domain: {domain}
Skill Level: {level}
Project Type: {project_type}

Generate the response in the following format:

# Project Title

## Problem Statement
(3-4 lines)

## Key Features
- Feature 1
- Feature 2
- Feature 3
- Feature 4
- Feature 5

## Recommended Tech Stack
List the technologies

## Development Steps
- Step 1
- Step 2
- Step 3
- Step 4

## Future Scope
- Point 1
- Point 2
- Point 3

## Difficulty
Easy / Intermediate / Advanced

## Innovation Score
X/10 — (one line reason)
"""

# -------------------------------
# Generate & Display
# -------------------------------
if generate:
    if problem.strip() == "":
        st.warning("⚠️ Please describe a real-world problem before generating.")
    else:
        with st.spinner("✨ Generating your project idea..."):
            try:
                completion = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    temperature=0.7,
                    max_tokens=1500
                )
                result = completion.choices[0].message.content

                st.success(" Project idea generated!")
                st.divider()
                st.markdown(result)

            except Exception as e:
                st.error(f" Something went wrong: {e}")
