# expenses.py
import sqlite3
from src.database import create_connection


def add_expense(user_id, category, amount, date, description):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO expenses (user_id, category, amount, date, description) VALUES (?, ?, ?, ?, ?)",
                   (user_id, category, amount, date, description))
    conn.commit()
    conn.close()


def edit_expense(expense_id, category, amount, date, description):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("UPDATE expenses SET category = ?, amount = ?, date = ?, description = ? WHERE id = ?",
                   (category, amount, date, description, expense_id))
    conn.commit()
    conn.close()


def delete_expense(expense_id):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    conn.commit()
    conn.close()



