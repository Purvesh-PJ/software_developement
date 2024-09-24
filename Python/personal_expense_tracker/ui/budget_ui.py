# ui/budget_ui.py
import tkinter as tk
from src.budget import set_budget, view_budget


def budget_ui(user_id):
    def submit_budget():
        category = category_entry.get()
        amount = float(amount_entry.get())

        set_budget(user_id, category, amount)
        tk.Label(root, text="Budget Set!").grid(row=3, column=1)

    def show_budget():
        budget_data = view_budget(user_id)
        budget_text = "\n".join([f"{cat}: {amt}" for cat, amt in budget_data.items()])
        tk.Label(root, text=budget_text).grid(row=4, column=1)

    root = tk.Tk()
    root.title("Manage Budget")

    tk.Label(root, text="Category").grid(row=0)
    tk.Label(root, text="Budget Amount").grid(row=1)

    category_entry = tk.Entry(root)
    amount_entry = tk.Entry(root)

    category_entry.grid(row=0, column=1)
    amount_entry.grid(row=1, column=1)

    tk.Button(root, text="Set Budget", command=submit_budget).grid(row=2, column=1)
    tk.Button(root, text="View Budget", command=show_budget).grid(row=2, column=2)

    root.mainloop()
