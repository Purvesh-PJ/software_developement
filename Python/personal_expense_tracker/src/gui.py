import tkinter as tk
from tkinter import ttk
from src.database import create_table

def setup_gui():
    root = tk.Tk()
    root.title("Personal Expense Tracker")

    # Set up frames, labels, buttons, etc.
    # Example: Add Expense Button
    add_button = ttk.Button(root, text="Add Expense", command=add_expense)
    add_button.pack()

    root.mainloop()

def add_expense():
    # Logic for adding an expense
    pass
