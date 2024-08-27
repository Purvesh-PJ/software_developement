# income.py
import sqlite3
from src.database import create_connection


def add_income(user_id, source, amount, date, description):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO income (user_id, source, amount, date, description) VALUES (?, ?, ?, ?, ?)",
                   (user_id, source, amount, date, description))
    conn.commit()
    conn.close()


def edit_income(income_id, source, amount, date, description):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("UPDATE income SET source = ?, amount = ?, date = ?, description = ? WHERE id = ?",
                   (source, amount, date, description, income_id))
    conn.commit()
    conn.close()


def delete_income(income_id):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM income WHERE id = ?", (income_id,))
    conn.commit()
    conn.close()