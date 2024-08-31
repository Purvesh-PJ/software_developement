import tkinter as tk
from tkinter import font as tkfont, PhotoImage
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
    frame.pack(pady=20)

    # Helper function to create a card
    def create_card(parent_frame, text, icon_path, command):
        card = tk.Frame(parent_frame, bg="white", width=200, height=150, relief="flat", bd=2)
        card.grid_propagate(False)  # Prevents the frame from shrinking to fit the widgets inside
        card.grid_columnconfigure(0, weight=1)  # Center-align the contents
        card.grid(row=0, column=parent_frame.grid_size()[0], padx=20, pady=20)

        # Load and display the icon
        icon = PhotoImage(file=icon_path)  # Provide the path to your icon image
        icon_label = tk.Label(card, image=icon, bg="white")
        icon_label.image = icon  # Keep a reference to avoid garbage collection
        icon_label.grid(row=0, column=0, pady=10)

        # Card text
        tk.Label(card, text=text, font=card_font, bg="white", fg="#333").grid(row=1, column=0, pady=5)

        # Button
        tk.Button(card, text="Open", command=command, bg="#007BFF", fg="white", bd=0, relief="raised").grid(row=2, column=0, pady=10)

    # Create the cards
    create_card(frame, "Add Expense", "../assets/icons/wallet.png", lambda: add_expense_ui(user_id))
    create_card(frame, "Add Income", "../assets/icons/coins_hand.png", lambda: add_income_ui(user_id))
    create_card(frame, "Manage Budget", "../assets/icons/calculator.png", lambda: budget_ui(user_id))
    create_card(frame, "View Reports", "../assets/icons/reports.png", lambda: report_ui(user_id))

    root.mainloop()
