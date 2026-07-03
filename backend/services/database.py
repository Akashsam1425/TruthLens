"""SQLite persistence for TruthLens analysis history.

All database access is intentionally kept in this module so that Flask routes
do not depend on SQLite details.  The public functions accept an optional
database path, which also makes the service straightforward to test.
"""

from __future__ import annotations

import os
import sqlite3
from datetime import datetime, timezone
from typing import Any


DEFAULT_DATABASE_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "truthlens.db",
)


def _connect(database_path: str | None = None) -> sqlite3.Connection:
    connection = sqlite3.connect(database_path or DEFAULT_DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database(database_path: str | None = None) -> None:
    """Create the analysis history table and indexes when they do not exist."""
    resolved_path = database_path or DEFAULT_DATABASE_PATH
    database_directory = os.path.dirname(resolved_path)
    if database_directory:
        os.makedirs(database_directory, exist_ok=True)

    with _connect(resolved_path) as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS analyses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                filename TEXT NOT NULL,
                file_type TEXT NOT NULL,
                upload_datetime TEXT NOT NULL,
                ai_score REAL NOT NULL CHECK (ai_score >= 0 AND ai_score <= 100),
                risk_level TEXT NOT NULL CHECK (risk_level IN ('Low', 'Medium', 'High')),
                report_path TEXT NOT NULL,
                preview_text TEXT NOT NULL DEFAULT '',
                analysis_type TEXT NOT NULL CHECK (analysis_type IN ('Document', 'Image'))
            )
            """
        )
        connection.execute(
            "CREATE INDEX IF NOT EXISTS idx_analyses_uploaded ON analyses(upload_datetime DESC)"
        )
        connection.execute(
            "CREATE INDEX IF NOT EXISTS idx_analyses_filename ON analyses(filename)"
        )
        connection.execute(
            "CREATE INDEX IF NOT EXISTS idx_analyses_filters ON analyses(file_type, risk_level)"
        )


def save_analysis(
    filename: str,
    file_type: str,
    ai_score: float,
    risk_level: str,
    report_path: str,
    preview_text: str,
    analysis_type: str,
    upload_datetime: str | None = None,
    database_path: str | None = None,
) -> int:
    """Insert a completed analysis and return its generated identifier."""
    timestamp = upload_datetime or datetime.now(timezone.utc).isoformat(timespec="seconds")

    with _connect(database_path) as connection:
        cursor = connection.execute(
            """
            INSERT INTO analyses (
                filename,
                file_type,
                upload_datetime,
                ai_score,
                risk_level,
                report_path,
                preview_text,
                analysis_type
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                filename,
                file_type.upper(),
                timestamp,
                float(ai_score),
                risk_level,
                report_path,
                preview_text,
                analysis_type,
            ),
        )
        return int(cursor.lastrowid)


def get_all_analyses(
    page: int = 1,
    per_page: int = 20,
    database_path: str | None = None,
) -> tuple[list[dict[str, Any]], int]:
    """Return one page of analyses and the total record count."""
    return search_analyses(page=page, per_page=per_page, database_path=database_path)


def search_analyses(
    filename: str = "",
    file_type: str = "",
    risk_level: str = "",
    upload_date: str = "",
    page: int = 1,
    per_page: int = 20,
    database_path: str | None = None,
) -> tuple[list[dict[str, Any]], int]:
    """Search and filter analyses, returning results and the total match count."""
    page = max(1, int(page))
    per_page = max(1, min(int(per_page), 100))
    conditions: list[str] = []
    parameters: list[Any] = []

    if filename.strip():
        conditions.append("filename LIKE ? COLLATE NOCASE")
        parameters.append(f"%{filename.strip()}%")
    if file_type.strip():
        conditions.append("file_type = ? COLLATE NOCASE")
        parameters.append(file_type.strip())
    if risk_level.strip():
        conditions.append("risk_level = ? COLLATE NOCASE")
        parameters.append(risk_level.strip())
    if upload_date.strip():
        conditions.append("date(upload_datetime) = ?")
        parameters.append(upload_date.strip())

    where_clause = f" WHERE {' AND '.join(conditions)}" if conditions else ""
    offset = (page - 1) * per_page

    with _connect(database_path) as connection:
        total = connection.execute(
            f"SELECT COUNT(*) FROM analyses{where_clause}",
            parameters,
        ).fetchone()[0]
        rows = connection.execute(
            f"""
            SELECT id, filename, file_type, upload_datetime, ai_score,
                   risk_level, report_path, preview_text, analysis_type
            FROM analyses
            {where_clause}
            ORDER BY upload_datetime DESC, id DESC
            LIMIT ? OFFSET ?
            """,
            [*parameters, per_page, offset],
        ).fetchall()

    return [dict(row) for row in rows], int(total)


def delete_analysis(analysis_id: int, database_path: str | None = None) -> bool:
    """Delete one history record without deleting its generated report file."""
    with _connect(database_path) as connection:
        cursor = connection.execute(
            "DELETE FROM analyses WHERE id = ?",
            (analysis_id,),
        )
        return cursor.rowcount > 0
