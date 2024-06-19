import tkinter as tk
from tkinter import ttk


def confirm():
    print("Confirm button clicked!")


def create_grading_system():
    print("Create Grading System button clicked!")


def search_subject():
    print("Search Subject button clicked!")


def back():
    print("Back button clicked!")


root = tk.Tk()
root.title("Dashboard")

root.configure(bg="#f0f0f0")

main_frame = tk.Frame(root, borderwidth=2, relief="solid", bg="#ffffff")
main_frame.pack(pady=20, padx=20)

confirm_button = tk.Button(main_frame, text="CONFIRM", command=confirm,
                           bg="#90ee90", fg="#000000", font=("Helvetica", 12))
confirm_button.pack(pady=10)

dashboard_button = tk.Button(main_frame, text="DASHBOARD", command=lambda: print(
    "Dashboard button clicked!"), bg="#90ee90", fg="#000000", font=("Helvetica", 12))
dashboard_button.pack(pady=10)

create_grading_system_button = tk.Button(main_frame, text="CREATE GRADING SYSTEM",
                                         command=create_grading_system, bg="#90ee90", fg="#000000", font=("Helvetica", 12))
create_grading_system_button.pack(pady=10)

search_subject_button = tk.Button(main_frame, text="SEARCH SUBJECT",
                                  command=search_subject, bg="#90ee90", fg="#000000", font=("Helvetica", 12))
search_subject_button.pack(pady=10)

back_button = tk.Button(main_frame, text="BACK", command=back,
                        bg="#90ee90", fg="#000000", font=("Helvetica", 12))
back_button.pack(pady=10)

root.mainloop()
