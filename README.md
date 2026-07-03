# 🔍 TruthLens

**AI-Powered Content Authenticity Verification System**

TruthLens is a production-oriented Flask application that helps determine the authenticity of documents and images using AI-assisted detection, statistical analysis, and forensic techniques. It generates detailed analysis reports, maintains analysis history, and provides a simple, professional web interface.

---

## 🚀 Features

### 📄 Document Analysis
- PDF and DOCX support
- Text extraction
- AI suspicion score
- Writing pattern analysis
- Readability statistics
- Risk level classification
- Preview extracted text
- PDF report generation

### 🖼 Image Analysis
- JPG, JPEG and PNG support
- Image metadata inspection
- EXIF analysis
- Image forensic heuristics
- AI suspicion score
- Risk classification
- PDF report generation

### 📊 Analysis History
- Stores previous analyses
- Search and filter history
- Download previous reports
- Delete history records

---

## 🛠 Tech Stack

**Backend**
- Python
- Flask

**Libraries**
- PyMuPDF
- python-docx
- Pillow
- ReportLab
- SQLite

**Frontend**
- HTML5
- CSS3
- JavaScript
- Jinja2

---

## 📂 Project Structure

```
TruthLens/
│
├── backend/
│   ├── app.py
│   ├── ai_detector.py
│   ├── history.py
│   ├── pattern_detector.py
│   ├── text_extractor.py
│   ├── services/
│   ├── templates/
│   └── static/
│
├── dataset/
├── models/
├── uploads/
├── reports/
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙ Installation

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

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python backend/app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

## 📈 Current Capabilities

- Document authenticity analysis
- Image authenticity analysis
- Statistical text analysis
- Pattern detection
- AI suspicion scoring
- Report generation
- Analysis history
- Responsive interface

---

## 🔮 Roadmap

- User Authentication
- Dashboard Analytics
- Machine Learning Text Detection
- Advanced Image Forensics
- Explainable AI
- REST API
- Security Hardening
- Cloud Deployment

---

## 👨‍💻 Author

**Akash Sam**

GitHub:
https://github.com/Akashsam1425

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
