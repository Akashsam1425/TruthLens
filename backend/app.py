from flask import Flask, render_template, request, send_from_directory
import os

import click
from werkzeug.utils import secure_filename

# ==========================
# Import Services
# ==========================

from text_extractor import extract_pdf_text, extract_docx_text
from ai_detector import analyze_text
from pattern_detector import detect_patterns

from services.image_detector import analyze_image
from history import history_blueprint
from services.database import initialize_database, save_analysis
from services.report_generator import generate_image_report, generate_report

# ==========================
# Flask App
# ==========================

app = Flask(__name__)

# ==========================
# Project Paths
# ==========================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

UPLOAD_FOLDER = os.path.join(
    BASE_DIR,
    "uploads"
)

REPORT_FOLDER = os.path.join(
    BASE_DIR,
    "backend",
    "reports"
)

DATABASE_PATH = os.path.join(
    BASE_DIR,
    "backend",
    "truthlens.db"
)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["DATABASE_PATH"] = DATABASE_PATH

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)

initialize_database(app.config["DATABASE_PATH"])
app.register_blueprint(history_blueprint)


@app.cli.command("init-db")
def init_db_command():
    """Initialize the TruthLens analysis history database."""
    initialize_database(app.config["DATABASE_PATH"])
    click.echo("TruthLens database initialized.")

os.makedirs(
    REPORT_FOLDER,
    exist_ok=True
)

# ==========================
# Home
# ==========================

@app.route("/")
def home():

    return render_template(
        "index.html"
    )


# ==========================
# Upload
# ==========================

@app.route(
    "/upload",
    methods=["POST"]
)
def upload():

    # ----------------------
    # File Exists?
    # ----------------------

    if "file" not in request.files:

        return "No file selected."

    file = request.files["file"]

    if file.filename == "":

        return "No file selected."

    filename = secure_filename(file.filename)

    if not filename:

        return render_template(

            "error.html",

            message="The selected file name is invalid."

        )

    filepath = os.path.join(

        app.config["UPLOAD_FOLDER"],

        filename

    )

    file.save(filepath)

    # ----------------------
    # Extension
    # ----------------------

    if "." in filename:

        extension = filename.rsplit(
            ".",
            1
        )[1].lower()

    else:

        extension = ""

    # ======================
    # IMAGE ANALYSIS
    # ======================

    if extension in [

        "jpg",
        "jpeg",
        "png"

    ]:

        image = analyze_image(
            filepath
        )

        risk_level = get_risk_level(image["ai_score"])

        report_path = generate_image_report(
            filename=filename,
            image=image,
            risk_level=risk_level,
            output_folder=REPORT_FOLDER
        )

        report_name = os.path.basename(report_path)

        preview_text = (
            f"Resolution: {image['resolution']}; "
            f"Format: {image['format']}; "
            f"Camera: {image['camera_make']} {image['camera_model']}"
        )

        save_analysis(
            filename=filename,
            file_type=extension,
            ai_score=image["ai_score"],
            risk_level=risk_level,
            report_path=report_name,
            preview_text=preview_text,
            analysis_type="Image",
            database_path=app.config["DATABASE_PATH"]
        )

        return render_template(

            "image_result.html",

            filename=filename,

            image=image,

            risk_level=risk_level,

            report_name=report_name

        )

    # ======================
    # PDF
    # ======================

    elif extension == "pdf":

        text = extract_pdf_text(
            filepath
        )

    # ======================
    # DOCX
    # ======================

    elif extension == "docx":

        text = extract_docx_text(
            filepath
        )

    # ======================
    # Unsupported
    # ======================

    else:

        return render_template(

            "error.html",

            message="Unsupported file type."

        )

    # ======================
    # TEXT ANALYSIS
    # ======================

    analysis = analyze_text(text)

    reasons = detect_patterns(text)

    final_ai_score = analysis["ai_score"]

    if "Frequent use of transition words" in reasons:

        final_ai_score += 20

    if "Very uniform sentence lengths" in reasons:

        final_ai_score += 20

    if "Repeated phrase patterns detected" in reasons:

        final_ai_score += 20

    final_ai_score = min(
        final_ai_score,
        100
    )

    # ======================
    # Risk Level
    # ======================

    risk_level = get_risk_level(final_ai_score)

    # ======================
    # Statistics
    # ======================

    paragraph_count = len(

        [

            p

            for p in text.split("\n")

            if p.strip()

        ]

    )

    preview_text = text[:800]    # ======================
    # Generate PDF Report
    # ======================

    report_path = generate_report(

        filename=filename,

        analysis=analysis,

        ai_score=final_ai_score,

        risk_level=risk_level,

        reasons=reasons,

        output_folder=REPORT_FOLDER

    )

    report_name = os.path.basename(report_path)

    save_analysis(
        filename=filename,
        file_type=extension,
        ai_score=final_ai_score,
        risk_level=risk_level,
        report_path=report_name,
        preview_text=preview_text,
        analysis_type="Document",
        database_path=app.config["DATABASE_PATH"]
    )

    # ======================
    # Render Result
    # ======================

    return render_template(

        "result.html",

        filename=filename,

        file_type="Document",

        analysis=analysis,

        paragraph_count=paragraph_count,

        final_ai_score=final_ai_score,

        risk_level=risk_level,

        reasons=reasons,

        preview_text=preview_text,

        report_name=report_name

    )


# ==========================
# Download Report
# ==========================

@app.route("/reports/<filename>")
def download_report(filename):

    return send_from_directory(

        REPORT_FOLDER,

        filename,

        as_attachment=request.args.get("view") != "1"

    )


def get_risk_level(ai_score):
    """Map an AI suspicion score to the shared TruthLens risk scale."""
    if ai_score < 30:
        return "Low"
    if ai_score < 60:
        return "Medium"
    return "High"


# ==========================
# Run Application
# ==========================

if __name__ == "__main__":

    app.run(
        debug=True
    )
