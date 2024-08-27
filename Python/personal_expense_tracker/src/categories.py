# categories.py
from src.database import create_connection


def add_category(user_id, category_name, category_type):
    """Add a new category for the user."""
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO categories (user_id, name, type) VALUES (?, ?, ?)",
                   (user_id, category_name, category_type))
    conn.commit()
    conn.close()


def get_categories(user_id, category_type):
    """Retrieve all categories of a specific type (income/expense) for the user."""
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, name FROM categories WHERE user_id = ? AND type = ?",
                   (user_id, category_type))
    categories = cursor.fetchall()
    conn.close()

    return categories


def edit_category(category_id, new_name):
    """Edit the name of an existing category."""
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("UPDATE categories SET name = ? WHERE id = ?",
                   (new_name, category_id))
    conn.commit()
    conn.close()


def delete_category(category_id):
    """Delete an existing category."""
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM categories WHERE id = ?", (category_id,))
    conn.commit()
    conn.close()
