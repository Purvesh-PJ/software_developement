# ui/report_ui.py
import tkinter as tk
from src.report import generate_report


def report_ui(user_id):
    def show_report():
        report_type = report_type_entry.get()
        report_data = generate_report(user_id, report_type)

        report_text = "\n".join([f"{date}: {cat} - {amt}" for date, cat, amt in report_data])
        report_label.config(text=report_text)

    root = tk.Tk()
    root.title("View Reports")

    tk.Label(root, text="Report Type (income/expense)").grid(row=0)

    report_type_entry = tk.Entry(root)
    report_type_entry.grid(row=0, column=1)

    tk.Button(root, text="Generate Report", command=show_report).grid(row=1, column=1)

    report_label = tk.Label(root, text="")
    report_label.grid(row=2, column=1)

    root.mainloop()
