# ui/categories_ui.py
import tkinter as tk
from src.categories import add_category, edit_category, delete_category


def categories_ui(user_id):
    def submit_category():
        category_name = category_entry.get()
        category_type = type_entry.get()

        add_category(user_id, category_name, category_type)
        tk.Label(root, text="Category Added!").grid(row=5, column=1)

    root = tk.Tk()
    root.title("Manage Categories")

    tk.Label(root, text="Category Name").grid(row=0)
    tk.Label(root, text="Type (income/expense)").grid(row=1)

    category_entry = tk.Entry(root)
    type_entry = tk.Entry(root)

    category_entry.grid(row=0, column=1)
    type_entry.grid(row=1, column=1)

    tk.Button(root, text="Add Category", command=submit_category).grid(row=2, column=1)

    # Additional buttons for editing and deleting categories can be added similarly

    root.mainloop()
