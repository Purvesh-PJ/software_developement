import tkinter as tk
from tkinter import font as tkfont
from tkinter import PhotoImage  # For using icons or images
from ui.add_expense import add_expense_ui
from ui.add_income import add_income_ui
from ui.budget_ui import budget_ui
from ui.report_ui import report_ui


def create_modern_button(parent, text, command, icon=None):
    """Create a modern styled button with optional icon."""
    button_font = tkfont.Font(family="Helvetica", size=12, weight="bold")

    button = tk.Button(parent, text=text, font=button_font, command=command, relief="flat",
                       bg="#007BFF", fg="white", padx=10, pady=10, bd=0, height=2, width=20)
    if icon:
        icon_image = PhotoImage(file=icon)  # Load icon image
        button.config(image=icon_image, compound="left")  # Set icon with text
        button.image = icon_image  # Keep a reference to avoid garbage collection

    # Modern button styling
    button.configure(bg="#007BFF", fg="white", borderwidth=0, relief="flat")
    button.bind("<Enter>", lambda e: button.config(bg="#0056b3"))
    button.bind("<Leave>", lambda e: button.config(bg="#007BFF"))

    # Apply shadow effect
    shadow = tk.Label(parent, bg="#0056b3", width=22, height=2)
    shadow.grid(row=0, column=0, padx=10, pady=10)
    shadow.place(x=button.winfo_x() + 2, y=button.winfo_y() + 2)

    return button


def dashboard_ui(user_id):
    root = tk.Tk()
    root.title("Dashboard")
    root.geometry("800x600")
    root.configure(bg="#f7f9fc")

    # Set a consistent font
    title_font = tkfont.Font(family="Helvetica", size=24, weight="bold")

    # Create a frame to hold the content
    main_frame = tk.Frame(root, bg="#f7f9fc")
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Welcome message
    welcome_label = tk.Label(main_frame, text=f"Welcome, User {user_id}!", font=title_font, bg="#f7f9fc", fg="#333")
    welcome_label.pack(pady=(0, 30))

    # Button frame
    button_frame = tk.Frame(main_frame, bg="#f7f9fc")
    button_frame.pack(fill="both", expand=True)

    # Create buttons
    add_expense_button = create_modern_button(button_frame, "Add Expense", lambda: add_expense_ui(user_id))
    add_income_button = create_modern_button(button_frame, "Add Income", lambda: add_income_ui(user_id))
    manage_budget_button = create_modern_button(button_frame, "Manage Budget", lambda: budget_ui(user_id))
    view_reports_button = create_modern_button(button_frame, "View Reports", lambda: report_ui(user_id))

    # Arrange buttons in a grid with spacing
    add_expense_button.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
    add_income_button.grid(row=0, column=1, padx=20, pady=20, sticky="ew")
    manage_budget_button.grid(row=1, column=0, padx=20, pady=20, sticky="ew")
    view_reports_button.grid(row=1, column=1, padx=20, pady=20, sticky="ew")

    # Adjust column and row weights for responsive design
    button_frame.columnconfigure(0, weight=1)
    button_frame.columnconfigure(1, weight=1)
    button_frame.rowconfigure(0, weight=1)
    button_frame.rowconfigure(1, weight=1)

    root.mainloop()
