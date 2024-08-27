# ui/add_income.py
import tkinter as tk
from income import add_income


def add_income_ui(user_id):
    def submit_income():
        source = source_entry.get()
        amount = float(amount_entry.get())
        date = date_entry.get()
        description = description_entry.get()

        add_income(user_id, source, amount, date, description)
        tk.Label(root, text="Income Added!").grid(row=5, column=1)

    root = tk.Tk()
    root.title("Add Income")

    tk.Label(root, text="Source").grid(row=0)
    tk.Label(root, text="Amount").grid(row=1)
    tk.Label(root, text="Date").grid(row=2)
    tk.Label(root, text="Description").grid(row=3)

    source_entry = tk.Entry(root)
    amount_entry = tk.Entry(root)
    date_entry = tk.Entry(root)
    description_entry = tk.Entry(root)

    source_entry.grid(row=0, column=1)
    amount_entry.grid(row=1, column=1)
    date_entry.grid(row=2, column=1)
    description_entry.grid(row=3, column=1)

    tk.Button(root, text="Add Income", command=submit_income).grid(row=4, column=1)

    root.mainloop()
