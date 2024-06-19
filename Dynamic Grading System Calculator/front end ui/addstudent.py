import tkinter as tk
from tkinter import ttk


def confirm():
    print("Confirm button clicked")


def back():
    print("Back button clicked")


root = tk.Tk()
root.title("Add Student")

# Title Label
title_label = tk.Label(root, text="ADD STUDENT", font=("Arial", 16))
title_label.pack(pady=20)

# Input fields
name_label = tk.Label(root, text="NAME:", font=("Arial", 12))
name_label.pack()
name_entry = tk.Entry(root, width=40)
name_entry.pack(pady=5)

student_number_label = tk.Label(
    root, text="STUDENT NUMBER:", font=("Arial", 12))
student_number_label.pack()
student_number_entry = tk.Entry(root, width=40)
student_number_entry.pack(pady=5)

section_label = tk.Label(root, text="SECTION:", font=("Arial", 12))
section_label.pack()
section_entry = tk.Entry(root, width=40)
section_entry.pack(pady=5)

# Buttons
confirm_button = ttk.Button(root, text="CONFIRM", command=confirm)
confirm_button.pack(pady=10, side="left")
back_button = ttk.Button(root, text="BACK", command=back)
back_button.pack(pady=10, side="right")

root.mainloop()
