from PIL import Image
from PIL.ExifTags import TAGS
import os


def analyze_image(filepath):
    """
    Analyze an uploaded image and return useful information.
    """

    image = Image.open(filepath)

    width, height = image.size

    image_format = image.format

    color_mode = image.mode

    file_size = round(
        os.path.getsize(filepath) / 1024,
        2
    )

    resolution = f"{width} x {height}"

    # -----------------------------
    # EXIF Metadata
    # -----------------------------

    exif_data = {}

    try:

        raw_exif = image.getexif()

        if raw_exif:

            for tag_id, value in raw_exif.items():

                tag = TAGS.get(tag_id, tag_id)

                exif_data[tag] = value

    except Exception:

        exif_data = {}

    # -----------------------------
    # Camera Information
    # -----------------------------

    camera_make = exif_data.get("Make", "Unknown")

    camera_model = exif_data.get("Model", "Unknown")

    capture_date = exif_data.get("DateTime", "Unknown")

    # -----------------------------
    # AI Suspicion Score
    # -----------------------------

    ai_score = 0

    reasons = []

    if camera_make == "Unknown":

        ai_score += 20

        reasons.append(
            "No camera manufacturer found."
        )

    if camera_model == "Unknown":

        ai_score += 20

        reasons.append(
            "No camera model found."
        )

    if width < 512 or height < 512:

        ai_score += 10

        reasons.append(
            "Low image resolution."
        )

    if image_format not in ["JPEG", "PNG"]:

        ai_score += 10

        reasons.append(
            "Uncommon image format."
        )

    ai_score = min(ai_score, 100)

    # -----------------------------
    # Return Result
    # -----------------------------

    return {

        "width": width,

        "height": height,

        "resolution": resolution,

        "format": image_format,

        "color_mode": color_mode,

        "file_size": file_size,

        "camera_make": camera_make,

        "camera_model": camera_model,

        "capture_date": capture_date,

        "ai_score": ai_score,

        "reasons": reasons

    }