# 🔍 TruthLens

<p align="center">

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.1-black?logo=flask)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue?logo=sqlite)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-green)

</p>

<h3 align="center">
AI-Powered Content Authenticity Verification System
</h3>

<p align="center">
Analyze documents and images using AI-assisted detection, statistical analysis, and forensic techniques.
Generate detailed reports and maintain a searchable analysis history through a clean, modern web interface.
</p>

---

# 📖 Overview

TruthLens is a production-oriented Flask application designed to assist users in evaluating the authenticity of digital content.

The system analyzes uploaded **documents** and **images**, extracts meaningful metadata and statistical information, applies heuristic AI detection techniques, classifies risk levels, and generates downloadable PDF reports.

The project follows a modular architecture to ensure maintainability, scalability, and future integration of Machine Learning models.

---

# ✨ Features

## 📄 Document Analysis

- PDF Support
- DOCX Support
- Text Extraction
- Statistical Analysis
- Pattern Detection
- AI Suspicion Score
- Risk Classification
- Downloadable PDF Report

---

## 🖼 Image Analysis

- JPG Support
- JPEG Support
- PNG Support
- Image Metadata Analysis
- EXIF Inspection
- Camera Information Detection
- Image Forensics
- AI Suspicion Score
- Risk Classification
- PDF Report Generation

---

## 📊 Analysis History

- Stores Previous Analyses
- Search by Filename
- Filter by Risk Level
- Filter by File Type
- Filter by Upload Date
- Download Previous Reports
- Delete Analysis Records

---

## 📑 Report Generation

TruthLens automatically generates professional PDF reports including:

- File Information
- Analysis Results
- Suspicion Indicators
- AI Score
- Risk Classification
- Metadata Summary
- Statistical Insights

---

# 📸 Screenshots

## 🏠 Home Page

![Home](docs/screenshots/home.png)

---

## 📄 Document Analysis

![Document](docs/screenshots/document-report.png)

---

## 🖼 Image Analysis

![Image](docs/screenshots/image-report.png)

---

## 📜 Analysis History

![History](docs/screenshots/history.png)

---

## 📑 Generated Report

![PDF](docs/screenshots/report.png)

---

# 🏗 System Architecture

```
                Browser
                    │
                    ▼
             Flask Application
                    │
     ┌──────────────┼──────────────┐
     ▼              ▼              ▼
Document       Image Detector     History
 Analyzer                         Manager
     ▼              ▼
 AI Detector    Statistics Engine
     ▼              ▼
       Report Generator
              │
              ▼
            SQLite
```

---

# 🔄 Application Workflow

```
Upload File
     │
     ▼
Detect File Type
     │
     ▼
Extract Text / Metadata
     │
     ▼
Run AI Detection
     │
     ▼
Calculate Statistics
     │
     ▼
Generate PDF Report
     │
     ▼
Save Analysis History
     │
     ▼
Display Results
```

---

# 🛠 Technology Stack

## Backend

- Python
- Flask

## Frontend

- HTML5
- CSS3
- JavaScript
- Jinja2

## Database

- SQLite

## Libraries

- PyMuPDF
- python-docx
- Pillow
- ReportLab

---

# 📂 Project Structure

```
TruthLens/
│
├── backend/
│   ├── app.py
│   ├── ai_detector.py
│   ├── history.py
│   ├── pattern_detector.py
│   ├── text_extractor.py
│   │
│   ├── services/
│   │      ├── database.py
│   │      ├── image_detector.py
│   │      ├── report_generator.py
│   │      └── statistics.py
│   │
│   ├── templates/
│   ├── static/
│   ├── reports/
│   └── truthlens.db
│
├── docs/
│   └── screenshots/
│
├── dataset/
├── models/
├── uploads/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/Akashsam1425/TruthLens.git
```

Move into the project

```bash
cd TruthLens
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python backend/app.py
```

Open

```
http://127.0.0.1:5000
```

---

# 📊 Current Capabilities

- Document Authenticity Analysis
- Image Authenticity Analysis
- Metadata Inspection
- Statistical Text Analysis
- Pattern Detection
- AI Suspicion Scoring
- PDF Report Generation
- Analysis History
- Responsive User Interface

---

# 🚀 Future Roadmap

## Phase 1

- ✅ Document Analysis
- ✅ Image Analysis
- ✅ PDF Reports
- ✅ Analysis History

---

## Phase 2

- 🔐 User Authentication
- 📈 Dashboard Analytics
- 🤖 Machine Learning Text Detection
- 🖼 Advanced Image Forensics

---

## Phase 3

- 🧠 Explainable AI
- 🌐 REST API
- 🔒 Security Hardening
- ☁ Cloud Deployment

---

# 💡 Future Enhancements

- Deep Learning Models
- OCR Support
- Batch File Analysis
- Drag-and-Drop Improvements
- API Authentication
- Multi-user Support
- Docker Deployment
- CI/CD Pipeline
- Cloud Storage Integration

---

# 👨‍💻 Author

**Akash Sam**

Computer Science Engineering Student

SRM Institute of Science and Technology

GitHub

https://github.com/Akashsam1425

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

It helps others discover the project and motivates future improvements.

---

# 📜 License

This project is licensed under the MIT License.

---

<p align="center">

Made with ❤️ using Flask and Python

</p>