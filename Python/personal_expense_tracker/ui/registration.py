# ui/registration.py
import tkinter as tk
from tkinter import messagebox
from src.auth import register_user
from ui.login import login_ui


def registration_ui():
    def register():
        username = username_entry.get()
        password = password_entry.get()

        if register_user(username, password):
            # Successfully registered
            messagebox.showinfo("Registration Successful", "You can now log in.")
            root.destroy()
            login_ui()
        else:
            # Registration failed (username might be taken)
            messagebox.showerror("Registration Failed", "Username already exists or registration failed.")

    root = tk.Tk()
    root.title("Register")

    tk.Label(root, text="Username").grid(row=0)
    tk.Label(root, text="Password").grid(row=1)

    username_entry = tk.Entry(root)
    password_entry = tk.Entry(root, show="*")

    username_entry.grid(row=0, column=1)
    password_entry.grid(row=1, column=1)

    tk.Button(root, text="Register", command=register).grid(row=2, column=1)

    root.mainloop()
