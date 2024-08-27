import sqlite3
import os


def create_connection():
    connection = sqlite3.connect("expenses.db")
    return connection

    # """Create a database connection to the SQLite database."""
    # if not os.path.exists('expenses.db'):
    #     # If the file does not exist, create it and initialize it
    #     setup_database()
    # conn = sqlite3.connect('expenses.db')
    # return conn


def get_user_id_by_username(username):
    """Retrieve the user ID by username."""
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()

    conn.close()

    if result:
        return result[0]
    return None


def setup_database():
    conn = create_connection()
    cursor = conn.cursor()

    # Create users table
    cursor.execute('''
          CREATE TABLE IF NOT EXISTS users (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              username TEXT NOT NULL UNIQUE,
              password TEXT NOT NULL
          )
    ''')

    # Create tables
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL
                      )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS expenses (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER,
                        category TEXT,
                        amount REAL,
                        date TEXT,
                        description TEXT,
                        FOREIGN KEY(user_id) REFERENCES users(id)
                      )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS income (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER,
                        source TEXT,
                        amount REAL,
                        date TEXT,
                        description TEXT,
                        FOREIGN KEY(user_id) REFERENCES users(id)
                      )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS categories (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER,
                        name TEXT,
                        type TEXT, -- "income" or "expense"
                        FOREIGN KEY(user_id) REFERENCES users(id)
                      )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS budgets (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER,
                        category TEXT,
                        amount REAL,
                        FOREIGN KEY(user_id) REFERENCES users(id)
                      )''')

    conn.commit()
    conn.close()


if __name__ == "__main__":
    setup_database()
