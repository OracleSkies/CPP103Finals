import tkinter as tk
from tkinter import ttk


class DashboardApp:
    def __init__(self, master):
        self.master = master
        master.title("DASHBOARD")
        master.geometry("700x500")  # Set the window size to 700x700
        master.resizable(False, False)  # Make the window unresizable

        # Create the buttons
        self.create_grading_button = ttk.Button(
            master, text="CREATE GRADING SYSTEM", width=25)
        self.create_grading_button.pack(pady=20)

        self.search_subject_button = ttk.Button(
            master, text="SEARCH SUBJECT", width=25)
        self.search_subject_button.pack(pady=10)

        self.confirm_button = ttk.Button(master, text="CONFIRM", width=10)
        self.confirm_button.pack(side="left", padx=20, pady=20)

        self.back_button = ttk.Button(master, text="BACK", width=10)
        self.back_button.pack(side="right", padx=20, pady=20)

        # Set background color
        master.configure(bg="#FFFFFF")


# Create the main window
root = tk.Tk()
app = DashboardApp(root)
root.mainloop()
