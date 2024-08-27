import tkinter as tk
from tkinter import messagebox, font as tkfont
from src.auth import authenticate_user
from ui.dashboard import dashboard_ui
from src.database import get_user_id_by_username

def on_enter(e):
    e.widget['background'] = '#e8f0fe'

def on_leave(e):
    e.widget['background'] = 'white'

def on_button_enter(e):
    e.widget['background'] = '#0056b3'

def on_button_leave(e):
    e.widget['background'] = '#007BFF'

def login_ui():
    def login():
        username = username_entry.get()
        password = password_entry.get()

        if authenticate_user(username, password):
            user_id = get_user_id_by_username(username)
            if user_id:
                root.destroy()  # Close the login window
                dashboard_ui(user_id)  # Open the dashboard with user_id
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    root = tk.Tk()
    root.title("Login")
    root.geometry("400x500")
    root.configure(bg="#f7f9fc")

    root.geometry("800x500")  # Fixed size for the window

    # Disable resizing of the window
    root.resizable(False, False)

    # Create a frame to hold the login form
    frame = tk.Frame(root, bg="#f7f9fc")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # Custom fonts
    title_font = tkfont.Font(family="Helvetica", size=20, weight="bold")
    label_font = tkfont.Font(family="Helvetica", size=12)
    entry_font = tkfont.Font(family="Helvetica", size=14)
    button_font = tkfont.Font(family="Helvetica", size=12, weight="bold")

    # Title
    title_label = tk.Label(frame, text="Login to your account", font=title_font, bg="#f7f9fc", fg="#333")
    title_label.grid(row=0, column=0, columnspan=2, pady=30)

    # Email Label and Entry
    email_label = tk.Label(frame, text="Email", font=label_font, bg="#f7f9fc", fg="#555")
    email_label.grid(row=1, column=0, sticky="w", pady=10)

    username_entry = tk.Entry(frame, font=entry_font, width=30, bd=2, relief="flat", bg="white")
    username_entry.grid(row=2, column=0, pady=10, padx=10, ipadx=5, ipady=5)
    username_entry.bind("<Enter>", on_enter)
    username_entry.bind("<Leave>", on_leave)

    # Password Label and Entry
    password_label = tk.Label(frame, text="Password", font=label_font, bg="#f7f9fc", fg="#555")
    password_label.grid(row=3, column=0, sticky="w", pady=10)

    password_entry = tk.Entry(frame, font=entry_font, width=30, bd=2, relief="flat", show="*", bg="white")
    password_entry.grid(row=4, column=0, pady=10, padx=10, ipadx=5, ipady=5)
    password_entry.bind("<Enter>", on_enter)
    password_entry.bind("<Leave>", on_leave)

    # Login button with background shadow
    login_button = tk.Button(frame, text="Login", font=button_font, bg="#007BFF", fg="white", bd=0, padx=10, pady=10,
                             width=20, command=login)
    login_button.grid(row=5, column=0, columnspan=2, pady=30)
    login_button.bind("<Enter>", on_button_enter)
    login_button.bind("<Leave>", on_button_leave)

    # Apply a shadow to the button
    login_button.configure(relief="raised", bd=2)

    root.mainloop()
