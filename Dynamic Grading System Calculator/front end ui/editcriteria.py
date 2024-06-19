import tkinter as tk


def show_subject_details():
    print("Show Subject Details button clicked!")


def search():
    print("Search button clicked!")


def back():
    print("Back button clicked!")


def add_criteria():
    global criteria_frame, criteria_entry_list, percentage_entry_list

    row = len(criteria_entry_list) + 2

    criteria_label = tk.Label(
        criteria_frame, text=f"CRITERIA {len(criteria_entry_list) + 1}", bg="#ffffff")
    criteria_label.pack(side="top", padx=10, pady=5)

    frame = tk.Frame(criteria_frame, bg="#ffffff")
    frame.pack(side="top", padx=10, pady=5)

    criteria_entry = tk.Entry(frame, width=15)
    criteria_entry.pack(side="left", padx=5)

    percentage_label = tk.Label(frame, text="PERCENTAGE", bg="#ffffff")
    percentage_label.pack(side="left", padx=5)

    percentage_entry = tk.Entry(frame, width=15)
    percentage_entry.pack(side="left", padx=5)

    criteria_entry_list.append(
        (criteria_label, frame, criteria_entry, percentage_entry))


def delete_criteria():
    if criteria_entry_list:
        criteria_label, frame, criteria_entry, percentage_entry = criteria_entry_list.pop()
        criteria_label.pack_forget()
        frame.pack_forget()
        criteria_entry.pack_forget()
        percentage_entry.pack_forget()


def confirm():
    print("Confirm button clicked")
    # Add your confirmation logic here


root = tk.Tk()
root.title("Subject Details")
root.geometry("600x600")
root.resizable(False, False)

# Set background color
root.configure(bg="#f0f0f0")

# Create subject label
subject_label = tk.Label(root, text="SUBJECT:",
                         font=("Helvetica", 18), bg="#f0f0f0")
subject_label.pack(pady=20)

# Create input field for subject
subject_entry = tk.Entry(root, width=30)
subject_entry.insert(0, "PHYSICS")
subject_entry.pack()

# Create Search button
search_button = tk.Button(root, text="SEARCH", command=search,
                          bg="#90ee90", fg="#000000", font=("Helvetica", 12))
search_button.pack(pady=10)

# Create frame for subject details
subject_details_frame = tk.Frame(
    root, borderwidth=2, relief="solid", bg="#ffffff")
subject_details_frame.pack(pady=20)

# Create button to show subject details
show_details_button = tk.Button(root, text="SHOW SUBJECT DETAILS",
                                command=show_subject_details, bg="#90ee90", fg="#000000", font=("Helvetica", 12))
show_details_button.pack(pady=10)

# Create Add Criteria button
add_criteria_button = tk.Button(root, text="ADD CRITERIA", command=add_criteria,
                                bg="#90ee90", fg="#000000", font=("Helvetica", 12))
add_criteria_button.pack(pady=10)

# Create Delete Criteria button
delete_criteria_button = tk.Button(
    root, text="DELETE CRITERIA", command=delete_criteria, bg="red", fg="#ffffff", font=("Helvetica", 12))
delete_criteria_button.pack(pady=10)

# Create frame for criteria and percentage
criteria_frame = tk.Frame(root, bg="#f0f0f0")
criteria_frame.pack(pady=10)

criteria_entry_list = []

# Create Confirm button
confirm_button = tk.Button(root, text="CONFIRM", command=confirm,
                           bg="green", fg="white", font=("Helvetica", 12))
confirm_button.pack(side="bottom", fill="x", padx=10, pady=10)

# Create back button
back_button = tk.Button(root, text="BACK", command=back,
                        bg="green", fg="white", font=("Helvetica", 12))
back_button.pack(side="bottom", fill="x", padx=10, pady=10)

# Run the application
root.mainloop()
