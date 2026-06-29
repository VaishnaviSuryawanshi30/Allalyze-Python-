import sqlite3
from datetime import datetime

DB_NAME = "data.db"


# ---------------- CREATE TABLE ----------------
def create_table():
    """
    Creates a single table to store analysis results
    for ALL file types (pdf, image, video, audio, csv).
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS analysis_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            file_name TEXT,
            file_type TEXT,
            analysis_result TEXT,
            created_at TEXT
        )
    """)

    conn.commit()
    conn.close()


# ---------------- SAVE RESULT ----------------
def save_result(file_name, file_type, result):
    """
    Saves analysis output into SQLite database.
    `result` is stored as TEXT (JSON / string).
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO analysis_results (file_name, file_type, analysis_result, created_at)
        VALUES (?, ?, ?, ?)
    """, (
        file_name,
        file_type,
        str(result),
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()
    conn.close()


# ---------------- FETCH ALL RESULTS ----------------
def fetch_all_results():
    """
    Fetches all stored analysis history.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT file_name, file_type, analysis_result, created_at
        FROM analysis_results
        ORDER BY created_at DESC
    """)

    rows = cursor.fetchall()
    conn.close()
    return rows