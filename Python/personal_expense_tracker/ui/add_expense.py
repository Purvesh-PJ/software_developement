# ui/add_expense.py
import tkinter as tk
from expenses import add_expense


def add_expense_ui(user_id):
    def submit_expense():
        category = category_entry.get()
        amount = float(amount_entry.get())
        date = date_entry.get()
        description = description_entry.get()

        add_expense(user_id, category, amount, date, description)
        tk.Label(root, text="Expense Added!").grid(row=5, column=1)

    root = tk.Tk()
    root.title("Add Expense")

    tk.Label(root, text="Category").grid(row=0)
    tk.Label(root, text="Amount").grid(row=1)
    tk.Label(root, text="Date").grid(row=2)
    tk.Label(root, text="Description").grid(row=3)

    category_entry = tk.Entry(root)
    amount_entry = tk.Entry(root)
    date_entry = tk.Entry(root)
    description_entry = tk.Entry(root)

    category_entry.grid(row=0, column=1)
    amount_entry.grid(row=1, column=1)
    date_entry.grid(row=2, column=1)
    description_entry.grid(row=3, column=1)

    tk.Button(root, text="Add Expense", command=submit_expense).grid(row=4, column=1)

    root.mainloop()
