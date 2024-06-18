import tkinter as tk
from tkinter import ttk

# Create main window
root = tk.Tk()
root.title("PHYSICS")

# Create table
table = ttk.Treeview(root, columns=("NAME", "STUDENT NUMBER",
                     "HOMEWORK", "SEATWORK", "QUIZZES", "EXAMS"), show="headings")

# Define column headings
table.heading("NAME", text="NAME")
table.heading("STUDENT NUMBER", text="STUDENT NUMBER")
table.heading("HOMEWORK", text="HOMEWORK")
table.heading("SEATWORK", text="SEATWORK")
table.heading("QUIZZES", text="QUIZZES")
table.heading("EXAMS", text="EXAMS")

# Insert data into table
table.insert("", tk.END, values=("BEN", "2103456",
             "20/20", "20/35", "32/40", "80/100"))
table.insert("", tk.END, values=("MEDEA", "2103214",
             "14/20", "35/35", "32/40", "90/100"))
table.insert("", tk.END, values=("CALLIOPE", "2103220",
             "19/20", "32/35", "40/40", "85/100"))

# Pack table into window
table.pack()

# Create "Back" button
back_button = tk.Button(root, text="BACK", bg="green", fg="white")
back_button.pack(pady=10)

# Start main loop
root.mainloop()
