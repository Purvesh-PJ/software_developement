# auth.py
import hashlib
import os
import sqlite3
from src.database import create_connection


def signup(username, password):
    conn = create_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        print("Signup successful!")
    except sqlite3.IntegrityError:
        print("Username already exists.")
    finally:
        conn.close()


def login(username, password):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    conn.close()

    if user:
        print("Login successful!")
        return user[0]  # return user_id
    else:
        print("Invalid credentials.")
        return None


def hash_password(password):
    """Hash a password for storing."""
    salt = os.urandom(16)
    pwdhash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return salt + pwdhash


def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user."""
    salt = stored_password[:16]
    stored_pwdhash = stored_password[16:]
    pwdhash = hashlib.pbkdf2_hmac('sha256', provided_password.encode('utf-8'), salt, 100000)
    return pwdhash == stored_pwdhash


def register_user(username, password):
    """Register a new user."""
    conn = create_connection()
    cursor = conn.cursor()

    hashed_password = hash_password(password)

    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                       (username, hashed_password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()


def authenticate_user(username, password):
    """Authenticate a user."""
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()

    conn.close()

    if result:
        stored_password = result[0]
        if verify_password(stored_password, password):
            return True  # Authentication successful
    return False  # Authentication failed

