"""Analysis history routes for TruthLens."""

from __future__ import annotations

import math

from flask import Blueprint, current_app, redirect, render_template, request, url_for

from services.database import delete_analysis, search_analyses


history_blueprint = Blueprint("history", __name__)
RECORDS_PER_PAGE = 20


def _positive_page(value: str | None) -> int:
    try:
        return max(1, int(value or 1))
    except (TypeError, ValueError):
        return 1


@history_blueprint.get("/history")
def history():
    filters = {
        "filename": request.args.get("search", "").strip(),
        "file_type": request.args.get("file_type", "").strip(),
        "risk_level": request.args.get("risk_level", "").strip(),
        "upload_date": request.args.get("date", "").strip(),
    }
    page = _positive_page(request.args.get("page"))
    analyses, total_records = search_analyses(
        **filters,
        page=page,
        per_page=RECORDS_PER_PAGE,
        database_path=current_app.config["DATABASE_PATH"],
    )
    total_pages = max(1, math.ceil(total_records / RECORDS_PER_PAGE))

    if page > total_pages:
        page = total_pages
        analyses, total_records = search_analyses(
            **filters,
            page=page,
            per_page=RECORDS_PER_PAGE,
            database_path=current_app.config["DATABASE_PATH"],
        )

    return render_template(
        "history.html",
        analyses=analyses,
        filters=filters,
        page=page,
        total_pages=total_pages,
        total_records=total_records,
    )


@history_blueprint.post("/history/<int:analysis_id>/delete")
def delete_history_record(analysis_id: int):
    delete_analysis(analysis_id, current_app.config["DATABASE_PATH"])
    return redirect(
        url_for(
            "history.history",
            search=request.form.get("search", ""),
            file_type=request.form.get("file_type", ""),
            risk_level=request.form.get("risk_level", ""),
            date=request.form.get("date", ""),
            page=_positive_page(request.form.get("page")),
        )
    )
