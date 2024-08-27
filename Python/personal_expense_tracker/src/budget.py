# budget.py
import sqlite3
from src.database import create_connection


def set_budget(user_id, category, amount):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO budgets (user_id, category, amount) VALUES (?, ?, ?)",
                   (user_id, category, amount))
    conn.commit()
    conn.close()


def view_budget(user_id):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT category, amount FROM budgets WHERE user_id = ?", (user_id,))
    budget_data = cursor.fetchall()
    conn.close()

    return {category: amount for category, amount in budget_data}
