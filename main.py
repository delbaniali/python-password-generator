import tkinter as tk
from tkinter import messagebox
from tkinter import ttk   # ✅ add this
import random
import string

def generate_password():
    length = length_entry.get()
    
    try:
        length = int(length)
        if length <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Enter a valid positive number")
        return

    characters = string.ascii_letters

    if numbers_var.get():
        characters += string.digits
    if symbols_var.get():
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

    check_strength(password)

def check_strength(password):
    strength_points = 0

    # Simple rules
    if len(password) >= 8:
        strength_points += 1
    if any(c.isdigit() for c in password):
        strength_points += 1
    if any(c.isupper() for c in password):
        strength_points += 1
    if any(c in string.punctuation for c in password):
        strength_points += 1

    # Map points -> label + color + progress %
    if strength_points <= 1:
        result = "Weak"
        color = "red"
        percent = 25
    elif strength_points == 2:
        result = "Moderate"
        color = "orange"
        percent = 50
    elif strength_points == 3:
        result = "Strong"
        color = "green"
        percent = 75
    else:
        result = "Very Strong"
        color = "green"
        percent = 100

    strength_label.config(text=f"Strength: {result}", fg=color)
    strength_bar["value"] = percent
# GUI Setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")

tk.Label(root, text="Password Length:").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack()

numbers_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).pack()
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).pack()

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

password_entry = tk.Entry(root, width=30)
password_entry.pack(pady=5)

strength_label = tk.Label(root, text="Strength: ")
strength_label.pack(pady=5)
# ✅ Strength Progress Bar
strength_bar = ttk.Progressbar(root, length=250, mode="determinate", maximum=100)
strength_bar.pack(pady=8)

root.mainloop()