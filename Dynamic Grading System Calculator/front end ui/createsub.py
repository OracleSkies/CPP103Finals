import tkinter as tk
from tkinter import ttk


def add_criteria():
    global criteria_frame, criteria_entry_list, percentage_entry_list

    row = len(criteria_entry_list) + 2

    criteria_label = tk.Label(
        criteria_frame, text=f"CRITERIA {len(criteria_entry_list) + 1}")
    criteria_label.pack(side="top", padx=10, pady=10)

    frame = tk.Frame(criteria_frame)
    frame.pack(side="top", padx=10, pady=10)

    criteria_entry = tk.Entry(frame, width=15)
    criteria_entry.pack(side="left", padx=10)

    percentage_label = tk.Label(frame, text=f"PERCENTAGE")
    percentage_label.pack(side="left", padx=10)

    percentage_entry = tk.Entry(frame, width=15)
    percentage_entry.pack(side="left", padx=10)

    criteria_entry_list.append(criteria_entry)
    percentage_entry_list.append(percentage_entry)


def confirm():
    print("Confirm button clicked")
    # Add your confirmation logic here


def back():
    print("Back button clicked")
    # Add your back logic here


root = tk.Tk()
root.title("Subject Evaluation")

# Subject Entry
subject_label = tk.Label(root, text="SUBJECT:")
subject_label.pack(side="top", fill="x", padx=10, pady=10)

subject_entry = tk.Entry(root, width=30)
subject_entry.pack(side="top", fill="x", padx=10, pady=10)

# Criteria and Percentage Frame
criteria_frame = tk.Frame(root)
criteria_frame.pack(side="top", fill="x", padx=10, pady=10)

add_criteria_button = tk.Button(
    criteria_frame, text="ADD CRITERIA", command=add_criteria, width=15)
add_criteria_button.pack(side="top", fill="x", padx=10, pady=10)

criteria_entry_list = []
percentage_entry_list = []

# Buttons
confirm_button = tk.Button(
    root, text="CONFIRM", command=confirm, width=10, bg="green", fg="white")
confirm_button.pack(side="bottom", fill="x", padx=10, pady=10)

back_button = tk.Button(root, text="BACK", command=back,
                        width=10, bg="green", fg="white")
back_button.pack(side="bottom", fill="x", padx=10, pady=10)

root.mainloop()
