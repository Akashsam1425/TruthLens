import fitz
from docx import Document


def extract_pdf_text(filepath):

    text = ""

    pdf = fitz.open(filepath)

    for page in pdf:
        text += page.get_text()

    return text


def extract_docx_text(filepath):

    doc = Document(filepath)

    text = ""

    for para in doc.paragraphs:
        text += para.text + "\n"

    return text