# 🧠 Resume Matcher + JD Scorer + Smart Search

This is an AI-powered HR tool that allows users to upload multiple resumes and job descriptions (JDs), automatically score them based on relevance using sentence embeddings, and intelligently search for the most suitable resumes using natural language queries.

> Built with: **Flask**, **Sentence Transformers**, **Next.js**, and **Tailwind CSS**

---

## 🚀 Features

- 📂 Upload **multiple resumes** (PDF/DOCX or `.zip` of resumes)
- 📄 Upload **one or more JDs**
- 🤖 Get a **Match % score** between each resume and JD
- 🔍 Use **Smart Search** — type queries like  
  `"Looking for a Python developer with React in Pune"`  
  to instantly find the top relevant candidates
- 📥 Download matched resumes directly from the result table
- 🔐 Basic login system with hardcoded credentials

---

## 🛠️ Tech Stack

| Frontend           | Backend           | AI/ML Engine         |
|--------------------|-------------------|-----------------------|
| Next.js + Tailwind | Flask (Python)    | Sentence-Transformers |

---

## 📦 Setup Instructions

### 1. Clone the repo


git clone this repo
cd resume-matcher

### 2. 🔙 Backend (Python)
Install dependencies
bash
cd backend
python -m venv env
source env/bin/activate  # or `env\Scripts\activate` on Windows
pip install -r requirements.txt
python app.py
Backend runs at: http://localhost:5000

### 3. 🔜 Frontend (Next.js)
Install dependencies
bash
cd ../frontend/ui
npm install
Run frontend
bash

npm run dev 

# 🧠 How It Works
Text Extraction
Extracts text from PDFs/DOCX using pdfplumber and python-docx.

AI Matching
Uses sentence-transformers (default: all-MiniLM-L6-v2 or better) to compute embeddings and cosine similarity between resumes and job descriptions.

Smart Search
Transforms user queries into embeddings and retrieves top matching resumes using cosine similarity.

Download Feature
Each resume match includes a download button served from Flask static routes.

# 🔐 Credentials (Login)
This project includes a simple login page with hardcoded credentials.

Username: admin
Password: admin123

#💡 Future Ideas
Use MongoDB to store resume text and metadata

Add OCR support for scanned/image-based resumes

Implement JWT auth + user registration

Export results as downloadable CSV
