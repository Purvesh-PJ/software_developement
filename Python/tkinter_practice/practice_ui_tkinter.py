import tkinter as tk

def goto_home():
    label.config(text="Home", font=("Arial", 16))

def goto_about():
    label.config(text="About", font=("Arial", 16))

root = tk.Tk()
root.title("Hello")
root.geometry("850x600")
# root.config(bg='black')

# Created label
label = tk.Label(root, text="Home", font=("Arial", 16))

# creating frame's
top_frame = tk.Frame(root, bg="#fafafa", height=50)
top_frame.pack(side="top", fill='x')
left_frame = tk.Frame(root, bg="#fafafa", width=100)
left_frame.pack(side="left", fill='y')
main_frame = tk.Frame(root, bg='white')
main_frame.pack(side='right', expand=True, fill='both')

tk.Label(main_frame, text="main frame", bg='lightblue').pack(pady=20)



root.mainloop()