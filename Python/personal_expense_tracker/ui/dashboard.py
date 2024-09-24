import tkinter as tk
from tkinter import font as tkfont
from PIL import Image, ImageTk  # Import from Pillow
from ui.add_expense import add_expense_ui
from ui.add_income import add_income_ui
from ui.budget_ui import budget_ui
from ui.report_ui import report_ui

def dashboard_ui(user_id):
    root = tk.Tk()
    root.title("Dashboard")
    root.configure(bg="#f0f4f8")

    # Set minimum window size
    root.minsize(800, 600)

    # Custom fonts
    title_font = tkfont.Font(family="Helvetica", size=18, weight="bold")
    card_font = tkfont.Font(family="Helvetica", size=12, weight="bold")

    # Title
    tk.Label(root, text=f"Welcome, User {user_id}!", font=title_font, bg="#f0f4f8", fg="#333").pack(pady=20)

    # Create a frame to hold the cards
    frame = tk.Frame(root, bg="#f0f4f8")
    frame.pack(pady=20, expand=True)

    # Helper function to create a card with proper icon resizing and click action
    def create_card(parent_frame, text, icon_path, command):
        card = tk.Frame(parent_frame, bg="white", width=200, height=150, relief="flat", bd=2)
        card.pack_propagate(False)  # Prevent frame from resizing
        card.pack(side=tk.LEFT, padx=20, pady=20)

        # Load and resize the icon using PIL
        icon = Image.open(icon_path)
        icon = icon.resize((50, 50), Image.Resampling.LANCZOS)  # Resize to 50x50 pixels with LANCZOS resampling
        icon_tk = ImageTk.PhotoImage(icon)
        icon_label = tk.Label(card, image=icon_tk, bg="white")
        icon_label.image = icon_tk  # Keep a reference to avoid garbage collection
        icon_label.pack(pady=10)

        # Card text
        text_label = tk.Label(card, text=text, font=card_font, bg="white", fg="#333")
        text_label.pack(pady=5)

        # Bind click event to the entire card, icon, and label
        def on_click(event):
            command()

        card.bind("<Button-1>", on_click)
        icon_label.bind("<Button-1>", on_click)
        text_label.bind("<Button-1>", on_click)

        # Add hover effect
        def on_enter(event):
            card.config(bg="#e0e0e0")

        def on_leave(event):
            card.config(bg="white")

        card.bind("<Enter>", on_enter)
        card.bind("<Leave>", on_leave)

    # Create the cards
    create_card(frame, "Add Expense", "../assets/icons/wallet.png", lambda: add_expense_ui(user_id))
    create_card(frame, "Add Income", "../assets/icons/coins_hand.png", lambda: add_income_ui(user_id))
    create_card(frame, "Manage Budget", "../assets/icons/calculator.png", lambda: budget_ui(user_id))
    create_card(frame, "View Reports", "../assets/icons/reports.png", lambda: report_ui(user_id))

    root.mainloop()
