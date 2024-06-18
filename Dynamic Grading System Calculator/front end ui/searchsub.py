import tkinter as tk
from tkinter import ttk


def show_subject_details():
    # Implement logic to show subject details
    print("Show Subject Details button clicked!")


def search():
    # Implement logic to search for subjects
    print("Search button clicked!")


def back():
    # Implement logic to go back
    print("Back button clicked!")


root = tk.Tk()
root.title("Subject Details")
root.geometry("600x440")
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

# Create back button
back_button = tk.Button(root, text="BACK", command=back,
                        bg="#90ee90", fg="#000000", font=("Helvetica", 12))
back_button.pack(pady=10)

# Run the application
root.mainloop()
