import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Show Criteria")
root.geometry("600x400")
root.configure(bg="#f0f0f0")

# Create the labels
physics_label = tk.Label(root, text="SUBJECT NAME",
                         font=("Arial", 16), bg="#f0f0f0")
physics_label.pack(pady=20)

criteria_label = tk.Label(root, text="CRITERIA",
                          font=("Arial", 16), bg="#f0f0f0")
criteria_label.pack()

homeworks_label = tk.Label(root, text="HOMEWORKS",
                           font=("Arial", 14), bg="#f0f0f0")
homeworks_label.pack(pady=5)

seatworks_label = tk.Label(root, text="SEATWORKS",
                           font=("Arial", 14), bg="#f0f0f0")
seatworks_label.pack(pady=5)

quizzes_label = tk.Label(root, text="QUIZZES",
                         font=("Arial", 14), bg="#f0f0f0")
quizzes_label.pack(pady=5)

examinations_label = tk.Label(
    root, text="EXAMINATIONS", font=("Arial", 14), bg="#f0f0f0")
examinations_label.pack(pady=5)

# Create the percentage labels
percentage_label1 = tk.Label(
    root, text="10%", font=("Arial", 14), bg="#f0f0f0")
percentage_label1.place(x=450, y=100)

percentage_label2 = tk.Label(
    root, text="20%", font=("Arial", 14), bg="#f0f0f0")
percentage_label2.place(x=450, y=140)

percentage_label3 = tk.Label(
    root, text="20%", font=("Arial", 14), bg="#f0f0f0")
percentage_label3.place(x=450, y=180)

percentage_label4 = tk.Label(
    root, text="50%", font=("Arial", 14), bg="#f0f0f0")
percentage_label4.place(x=450, y=220)

# Create the back button
back_button = ttk.Button(root, text="BACK", command=root.destroy, width=10)
back_button.place(x=450, y=300)

# Create the green background
green_canvas = tk.Canvas(root, width=200, height=400, bg="#90ee90")
green_canvas.place(x=400, y=0)

# Add some overlaying shapes
green_canvas.create_polygon(400, 0, 500, 100, 600,
                            0, fill="#69f069", outline="#69f069")
green_canvas.create_polygon(500, 100, 600, 200, 500,
                            300, fill="#3cb371", outline="#3cb371")

back_button = tk.Button(root, text="BACK",
                        width=10, bg="green", fg="white")
back_button.pack(side="bottom", padx=10, pady=10)

# Run the main loop
root.mainloop()
