# report.py
import sqlite3
from src.database import create_connection


def generate_report(user_id, report_type):
    conn = create_connection()
    cursor = conn.cursor()

    if report_type == "income":
        cursor.execute("SELECT date, source, amount FROM income WHERE user_id = ?", (user_id,))
    elif report_type == "expense":
        cursor.execute("SELECT date, category, amount FROM expenses WHERE user_id = ?", (user_id,))

    report_data = cursor.fetchall()
    conn.close()

    return report_data
