# 🚀 Problem2Project AI

> Transform real-world problems into complete software project ideas using AI.

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit)](https://project-ai-zjvz6jsvzx8f9hpd2xavbu.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)](https://python.org)
[![Groq](https://img.shields.io/badge/Powered%20by-Groq-orange?style=for-the-badge)](https://groq.com)

---

## Live Demo

🔗 [https://project-ai-zjvz6jsvzx8f9hpd2xavbu.streamlit.app/](https://project-ai-zjvz6jsvzx8f9hpd2xavbu.streamlit.app/)

---

## About

**Problem2Project AI** is an AI-powered web application that helps engineering students and developers instantly generate complete software project ideas from real-world problems.

Just enter a problem, choose your domain and skill level — and the AI generates a full project blueprint in seconds!

---

## Features

- AI-Powered Generation — Uses LLaMA 3.3 70B via Groq API for fast, intelligent responses
- Complete Project Blueprint — Title, Problem Statement, Key Features, Tech Stack, Development Steps, Future Scope
- Difficulty Rating — Know how hard your project is before starting
- Innovation Score — Get an innovation score out of 10
- Multiple Domains — AI, Web Dev, ML, Cyber Security, Data Science, IoT, Cloud, Blockchain
- Super Fast — Groq's LPU inference gives near-instant results
- Clean UI — Simple and intuitive interface built with Streamlit

---

## Screenshots

> Enter your problem → Choose domain & skill level → Click Generate → Get your project idea!

---

## Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.11 | Backend language |
| Streamlit | Web UI framework |
| Groq API | AI inference engine |
| LLaMA 3.3 70B | Language model |
| Streamlit Cloud | Deployment platform |

---

## How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/Dhanaa007/Project-AI.git
cd Project-AI
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Create a `.env` file
```
GROQ_API_KEY=your_groq_api_key_here
```

> Get your free API key at [console.groq.com](https://console.groq.com)

### 4. Run the app
```bash
streamlit run app.py
```

### 5. Open in browser
```
http://localhost:8501
```

---

## Requirements

```
groq==0.11.0
python-dotenv
httpx==0.27.0
```

---

## How to Use

1. Open the app
2. Select your **Domain** from the sidebar (AI, Web Dev, ML, etc.)
3. Select your **Skill Level** (Beginner, Intermediate, Advanced)
4. Select your **Project Type** (Mini, Portfolio, Hackathon, Major)
5. Describe your **real-world problem** in the text box
6. Click **Generate Project**
7. Get your complete project idea instantly!

---

## Project Structure

```
Project-AI/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .python-version     # Python version file
└── README.md           # Project documentation
```

---

## Example Output

**Input:** Students struggle to manage assignments and deadlines

**Output:**
- Project Title: Smart Student Planner
-  Problem Statement
-  5 Key Features
- Recommended Tech Stack
- Development Steps
-  Future Scope
-  Difficulty: Intermediate
-  Innovation Score: 8/10

---

## Future Scope

- [ ] Add GitHub repository auto-generator
- [ ] Export project idea as PDF
- [ ] Add team collaboration features
- [ ] Support more AI models
- [ ] Add project roadmap timeline

---

## Author

**Dhanaa**
- GitHub:https://github.com/Dhanaa007/Project-AI

