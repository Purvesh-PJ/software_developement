from ui.login import login_ui
from src.database import create_connection
from ui.registration import registration_ui
from src.database import setup_database


def check_users_exist():
    """Check if any users exist in the database."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users")
    user_count = cursor.fetchone()[0]
    conn.close()
    return user_count > 0


def main():
    setup_database()

    # Check if any users exist
    if check_users_exist():
        # Launch the login UI
        login_ui()
    else:
        # Launch the registration UI
        registration_ui()


if __name__ == "__main__":
    main()

