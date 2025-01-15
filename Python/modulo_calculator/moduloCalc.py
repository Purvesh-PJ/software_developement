import sys
import tkinter as tk
from tkinter import ttk


def calculate_modulo_gui():
    try:
        dividend = int(entry_dividend.get())
        divisor = int(entry_divisor.get())
        if divisor == 0:
            label_error.config(text="Divisor cannot be zero.", foreground="red", background="#ffdcd9")
        else:
            result = dividend - divisor * (dividend // divisor)
            label_result.config(text=f"{dividend} mod {divisor} = {result}")
            label_error.config(text="", background="")  # Clear any previous errors
    except ValueError:
        label_error.config(text="Please enter valid integers.", foreground="red", background="#ffdcd9")


def calculate_modulo(dividend, divisor):
    try:
        dividend = int(dividend)
        divisor = int(divisor)
        if divisor == 0:
            return "Error: Divisor cannot be zero."
        else:
            result = dividend - divisor * (dividend // divisor)
            return f"Result: {result}"
    except ValueError:
        return "Error: Please enter valid integers."


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if len(sys.argv) != 3:
            print("Usage: python modulo_calculator.py <dividend> <divisor>")
        else:
            dividend, divisor = sys.argv[1], sys.argv[2]
            print(calculate_modulo(dividend, divisor))
    else:
        # Create the main window
        root = tk.Tk()
        root.title("Modulo Calculator")
        root.geometry("320x400")  # Set fixed window size
        root.config(bg="#ffffff")  # Background color
        root.resizable(False, False)  # Disable resizing the window

        # Create a style object
        style = ttk.Style()

        # Custom style for label
        style.configure("CustomLabel.TLabel", font=("Helvetica", 14))

        # Custom style for entry field
        style.configure("CustomEntry.TEntry", font=("Helvetica", 16), padding=10, relief="solid", borderwidth=3)

        # Custom style for button
        style.configure("CustomButton.TButton", font=("Helvetica", 12), padding=8)
        style.map("CustomButton.TButton", background=[("active", "#45a049")])

        # Center the content using grid layout
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)

        # Create a frame for the content with padding
        frame = ttk.Frame(root, padding="20")
        frame.grid(row=0, column=0, sticky="nsew")

        # Labels and entry fields with modern design using custom styles
        label_dividend = ttk.Label(frame, text="Dividend", style="CustomLabel.TLabel")
        label_dividend.grid(row=0, column=0, padx=10, pady=8, sticky="ew")

        entry_dividend = ttk.Entry(frame, style="CustomEntry.TEntry", width=40)
        entry_dividend.grid(row=1, column=0, padx=10, pady=8, sticky="ew")

        label_divisor = ttk.Label(frame, text="Divisor", style="CustomLabel.TLabel")
        label_divisor.grid(row=2, column=0, padx=10, pady=8, sticky="w")

        entry_divisor = ttk.Entry(frame, style="CustomEntry.TEntry", width=40)
        entry_divisor.grid(row=3, column=0, padx=10, pady=8, sticky="ew")

        # Custom styled button
        button_calculate = ttk.Button(frame, text="Calculate", command=calculate_modulo_gui, style="CustomButton.TButton")
        button_calculate.grid(row=4, column=0, columnspan=2, pady=20, sticky="ew")

        # Result label with improved font
        label_result = ttk.Label(frame, font=("Helvetica", 12))
        label_result.grid(row=5, column=0, columnspan=2, pady=10)

        # Error label with proper placement below the button
        label_error = ttk.Label(frame, font=("Helvetica", 12), padding=8)
        label_error.grid(row=6, column=0, columnspan=2)

        # Run the application
        root.mainloop()
