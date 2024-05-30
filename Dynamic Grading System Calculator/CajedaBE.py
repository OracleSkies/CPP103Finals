import tkinter as tk
from tkinter import messagebox
import sqlite3

class GradingSystemApp:
    def __init__(self, root):
        self.root = root
        self.root.title("A Dynamic Grading System Application")
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.students = {}
        self.criterias = {}

        # Connect to the SQLite3 database
        self.conn = sqlite3.connect('grades.db')
        self.cursor = self.conn.cursor()

        # Create the users table if it doesn't exist
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)''')

        # Create the students table if it doesn't exist
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS students (student_number TEXT PRIMARY KEY, name TEXT, lastname TEXT, section TEXT, subject TEXT, homework REAL, seatwork REAL, quizzes REAL, exams REAL)''')

        # Create the criterias table if it doesn't exist
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS criterias (subject TEXT, criteria TEXT, percentage REAL, PRIMARY KEY (subject, criteria))''')

        self.create_login_frame()

    def create_login_frame(self):
        self.clear_frame()

        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack()

        tk.Label(self.login_frame, text="Username:").grid(row=0, column=0)
        tk.Entry(self.login_frame, textvariable=self.username).grid(row=0, column=1)
        tk.Label(self.login_frame, text="Password:").grid(row=1, column=0)
        tk.Entry(self.login_frame, textvariable=self.password, show='*').grid(row=1, column=1)
        tk.Button(self.login_frame, text="Login", command=self.login).grid(row=2, column=0, columnspan=2)
        tk.Button(self.login_frame, text="Register", command=self.create_register_frame).grid(row=3, column=0, columnspan=2)

    def create_register_frame(self):
        self.clear_frame()

        self.register_frame = tk.Frame(self.root)
        self.register_frame.pack()

        tk.Label(self.register_frame, text="Username:").grid(row=0, column=0)
        tk.Entry(self.register_frame, textvariable=self.username).grid(row=0, column=1)
        tk.Label(self.register_frame, text="Password:").grid(row=1, column=0)
        tk.Entry(self.register_frame, textvariable=self.password, show='*').grid(row=1, column=1)
        tk.Button(self.register_frame, text="Confirm", command=self.register).grid(row=2, column=0, columnspan=2)
        tk.Button(self.register_frame, text="Back", command=self.create_login_frame).grid(row=3, column=0, columnspan=2)

    def create_dashboard(self):
        self.clear_frame()

        self.dashboard_frame = tk.Frame(self.root)
        self.dashboard_frame.pack()

        tk.Button(self.dashboard_frame, text="Create Grading System", command=self.create_subject_frame).grid(row=0, column=0)
        tk.Button(self.dashboard_frame, text="Search Subject", command=self.create_search_subject_frame).grid(row=1, column=0)
        tk.Button(self.dashboard_frame, text="Logout", command=self.logout).grid(row=2, column=0)

    def create_subject_frame(self):
        self.clear_frame()

        self.subject_frame = tk.Frame(self.root)
        self.subject_frame.pack()

        self.subject_name = tk.StringVar()

        tk.Label(self.subject_frame, text="Subject:").grid(row=0, column=0)
        tk.Entry(self.subject_frame, textvariable=self.subject_name).grid(row=0, column=1)

        self.criteria_frame = tk.Frame(self.subject_frame)
        self.criteria_frame.grid(row=1, column=0, columnspan=2)

        self.criteria_entries = []

        self.add_criteria_button = tk.Button(self.subject_frame, text="Add Criteria", command=lambda: self.add_criteria_entry(self.criteria_frame))
        self.add_criteria_button.grid(row=2, column=0, columnspan=2)
        self.confirm_button = tk.Button(self.subject_frame, text="Confirm", command=self.save_subject)
        self.confirm_button.grid(row=3, column=0, columnspan=2)
        self.back_button = tk.Button(self.subject_frame, text="Back", command=self.create_dashboard)
        self.back_button.grid(row=4, column=0, columnspan=2)
        
        self.add_criteria_entry(self.criteria_frame)  # Add the first criteria entry

    def add_criteria_entry(self, frame):
        row = len(self.criteria_entries)
        criteria_name = tk.StringVar()
        percentage = tk.IntVar()
        self.criteria_entries.append((criteria_name, percentage))

        tk.Label(frame, text=f"Criteria {row + 1}:").grid(row=row, column=0)
        tk.Entry(frame, textvariable=criteria_name).grid(row=row, column=1)
        tk.Label(frame, text="Percentage:").grid(row=row, column=2)
        tk.Entry(frame, textvariable=percentage).grid(row=row, column=3)
        remove_button_state = "normal" if len(self.criteria_entries) > 1 else "disabled"
        tk.Button(frame, text="Remove", command=lambda idx=row: self.remove_criteria_entry(idx, frame), state=remove_button_state).grid(row=row, column=4)

    def remove_criteria_entry(self, index, frame):
        if len(self.criteria_entries) <= 1:
            messagebox.showwarning("Warning", "At least one criteria must be present.")
            return
        # Remove criteria entry from the list
        self.criteria_entries.pop(index)
        self.rebuild_criteria_entries(frame)

    def rebuild_criteria_entries(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()
        
        # Rebuild criteria entries
        for idx, (criteria_name, percentage) in enumerate(self.criteria_entries):
            tk.Label(frame, text=f"Criteria {idx + 1}:").grid(row=idx, column=0)
            tk.Entry(frame, textvariable=criteria_name).grid(row=idx, column=1)
            tk.Label(frame, text="Percentage:").grid(row=idx, column=2)
            tk.Entry(frame, textvariable=percentage).grid(row=idx, column=3)
            remove_button_state = "normal" if len(self.criteria_entries) > 1 else "disabled"
            tk.Button(frame, text="Remove", command=lambda idx=idx: self.remove_criteria_entry(idx, frame), state=remove_button_state).grid(row=idx, column=4)

    def create_search_subject_frame(self):
        self.clear_frame()

        self.search_frame = tk.Frame(self.root)
        self.search_frame.pack()

        tk.Label(self.search_frame, text="Subject:").grid(row=0, column=0)
        self.search_subject_name = tk.StringVar()
        tk.Entry(self.search_frame, textvariable=self.search_subject_name).grid(row=0, column=1)
        tk.Button(self.search_frame, text="Search", command=self.search_subject).grid(row=1, column=0, columnspan=2)
        tk.Button(self.search_frame, text="Back", command=self.create_dashboard).grid(row=2, column=0, columnspan=2)
        tk.Button(self.search_frame, text="Logout", command=self.logout).grid(row=3, column=0, columnspan=2)

    def create_subject_details_frame(self, subject_name):
        self.clear_frame()

        self.subject_details_frame = tk.Frame(self.root)
        self.subject_details_frame.pack()

        tk.Label(self.subject_details_frame, text=f"Subject: {subject_name}").grid(row=0, column=0)
        tk.Button(self.subject_details_frame, text="Show Criteria", command=lambda: self.show_criteria(subject_name)).grid(row=1, column=0)
        tk.Button(self.subject_details_frame, text="Student Records", command=lambda: self.show_student_records(subject_name)).grid(row=2, column=0)
        tk.Button(self.subject_details_frame, text="Add Students", command=lambda: self.add_student(subject_name)).grid(row=3, column=0)
        tk.Button(self.subject_details_frame, text="Edit Criteria", command=lambda: self.edit_criteria(subject_name)).grid(row=4, column=0)
        tk.Button(self.subject_details_frame, text="Back", command=self.create_search_subject_frame).grid(row=5, column=0)
        tk.Button(self.subject_details_frame, text="Logout", command=self.logout).grid(row=6, column=0)

    def show_criteria(self, subject_name):
        self.clear_frame()
        self.criteria_frame = tk.Frame(self.root)
        self.criteria_frame.pack()

        criteria = self.criterias.get(subject_name, {})
        criteria_text = "\n".join([f"{key}: {value}%" for key, value in criteria.items()])

        tk.Label(self.criteria_frame, text="Criteria:").grid(row=0, column=0)
        tk.Label(self.criteria_frame, text=criteria_text).grid(row=1, column=0)
        tk.Button(self.criteria_frame, text="Back", command=lambda: self.create_subject_details_frame(subject_name)).grid(row=2, column=0)
        tk.Button(self.criteria_frame, text="Logout", command=self.logout).grid(row=3, column=0)

    def show_student_records(self, subject_name):
        self.clear_frame()

        self.records_frame = tk.Frame(self.root)
        self.records_frame.pack()

        student_records = self.students.get(subject_name, [])
        headers = ["Name", "Student Number", "Homework", "Seatwork", "Quizzes", "Exams"]

        for idx, header in enumerate(headers):
            tk.Label(self.records_frame, text=header, anchor='w').grid(row=0, column=idx, padx=5, pady=5, sticky='w')

        for i, student_record in enumerate(student_records):
            student_name = student_record[3]
            student_lastname = student_record[4]
            student_number = student_record[0]
            homework = student_record[5]
            seatwork = student_record[6]
            quizzes = student_record[7]
            exams = student_record[8]

            student_data = [
                f"{student_name} {student_lastname}",
                student_number,
                homework,
                seatwork,
                quizzes,
                exams
            ]

            for idx, data in enumerate(student_data):
                tk.Label(self.records_frame, text=data, anchor='w').grid(row=i + 1, column=idx, padx=5, pady=5, sticky='w')

        tk.Button(self.records_frame, text="Back", command=lambda: self.create_subject_details_frame(subject_name)).grid(row=len(student_records) + 1, column=0, columnspan=len(headers), pady=10)
        tk.Button(self.records_frame, text="Logout", command=self.logout).grid(row=len(student_records) + 2, column=0, columnspan=len(headers), pady=10)

    def add_student(self, subject_name):
        self.clear_frame()
        self.add_student_frame = tk.Frame(self.root)
        self.add_student_frame.pack()

        self.student_number = tk.StringVar()
        self.name = tk.StringVar()
        self.lastname = tk.StringVar()
        self.section = tk.StringVar()

        tk.Label(self.add_student_frame, text="Student Number:").grid(row=0, column=0)
        tk.Entry(self.add_student_frame, textvariable=self.student_number).grid(row=0, column=1)
        tk.Label(self.add_student_frame, text="Name:").grid(row=1, column=0)
        tk.Entry(self.add_student_frame, textvariable=self.name).grid(row=1, column=1)
        tk.Label(self.add_student_frame, text="Lastname:").grid(row=2, column=0)
        tk.Entry(self.add_student_frame, textvariable=self.lastname).grid(row=2, column=1)
        tk.Label(self.add_student_frame, text="Section:").grid(row=3, column=0)
        tk.Entry(self.add_student_frame, textvariable=self.section).grid(row=3, column=1)
        tk.Button(self.add_student_frame, text="Add", command=lambda: self.save_student(subject_name)).grid(row=4, column=0, columnspan=2)
        tk.Button(self.add_student_frame, text="Back", command=lambda: self.create_subject_details_frame(subject_name)).grid(row=5, column=0, columnspan=2)
        tk.Button(self.add_student_frame, text="Logout", command=self.logout).grid(row=6, column=0, columnspan=2)

    def edit_criteria(self, subject_name):
        self.clear_frame()
        self.edit_criteria_frame = tk.Frame(self.root)
        self.edit_criteria_frame.pack()

        criteria = self.criterias.get(subject_name, {})
        self.criteria_entries = []

        criteria_frame = tk.Frame(self.edit_criteria_frame)
        criteria_frame.grid(row=0, column=0, columnspan=5)

        for idx, (criterion, percentage) in enumerate(criteria.items()):
            criteria_name = tk.StringVar(value=criterion)
            percentage_value = tk.IntVar(value=percentage)
            self.criteria_entries.append((criteria_name, percentage_value))

            tk.Label(criteria_frame, text=f"Criteria {idx + 1}:").grid(row=idx, column=0)
            tk.Entry(criteria_frame, textvariable=criteria_name).grid(row=idx, column=1)
            tk.Label(criteria_frame, text="Percentage:").grid(row=idx, column=2)
            tk.Entry(criteria_frame, textvariable=percentage_value).grid(row=idx, column=3)

            remove_button_state = "normal" if len(criteria) > 1 else "disabled"
            tk.Button(criteria_frame, text="Remove", command=lambda idx=idx: self.remove_criteria_entry(idx, criteria_frame), state=remove_button_state).grid(row=idx, column=4)

        self.add_criteria_button = tk.Button(self.edit_criteria_frame, text="Add Criteria", command=lambda: self.add_criteria_entry(criteria_frame))
        self.add_criteria_button.grid(row=len(criteria) + 1, column=0, columnspan=2)
        self.save_button = tk.Button(self.edit_criteria_frame, text="Save", command=lambda: self.save_criteria(subject_name))
        self.save_button.grid(row=len(criteria) + 2, column=0, columnspan=2)
        self.back_button = tk.Button(self.edit_criteria_frame, text="Back", command=lambda: self.create_subject_details_frame(subject_name))
        self.back_button.grid(row=len(criteria) + 3, column=0, columnspan=2)
        self.logout_button = tk.Button(self.edit_criteria_frame, text="Logout", command=self.logout)
        self.logout_button.grid(row=len(criteria) + 4, column=0, columnspan=2)

    def save_subject(self):
        subject_name = self.subject_name.get()
        self.criterias[subject_name] = {}

        for criteria_name, percentage in self.criteria_entries:
            self.criterias[subject_name][criteria_name.get()] = percentage.get()

        # Save the criteria to the database
        for criteria_name, percentage in self.criterias[subject_name].items():
            self.cursor.execute("INSERT OR REPLACE INTO criterias (subject, criteria, percentage) VALUES (?, ?, ?)",
                                (subject_name, criteria_name, percentage))
        self.conn.commit()

        messagebox.showinfo("Success", "Subject and criteria saved successfully!")
        self.create_dashboard()

    def save_student(self, subject_name):
        student_number = self.student_number.get()
        name = self.name.get()
        lastname = self.lastname.get()
        section = self.section.get()

        self.students.setdefault(subject_name, []).append((student_number, name, lastname, section, subject_name, 0, 0, 0, 0))

        # Save the student to the database
        self.cursor.execute("INSERT OR REPLACE INTO students (student_number, name, lastname, section, subject, homework, seatwork, quizzes, exams) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                            (student_number, name, lastname, section, subject_name, 0, 0, 0, 0))
        self.conn.commit()

        messagebox.showinfo("Success", "Student added successfully!")
        self.create_subject_details_frame(subject_name)

    def save_criteria(self, subject_name):
        self.criterias[subject_name] = {}
        for criteria_name, percentage in self.criteria_entries:
            self.criterias[subject_name][criteria_name.get()] = percentage.get()

        # Save the criteria to the database
        for criteria_name, percentage in self.criterias[subject_name].items():
            self.cursor.execute("INSERT OR REPLACE INTO criterias (subject, criteria, percentage) VALUES (?, ?, ?)",
                                (subject_name, criteria_name, percentage))
        self.conn.commit()

        messagebox.showinfo("Success", "Criteria updated successfully!")
        self.create_subject_details_frame(subject_name)

    def search_subject(self):
        subject_name = self.search_subject_name.get()
        if subject_name in self.criterias:
            self.create_subject_details_frame(subject_name)
        else:
            messagebox.showerror("Error", "Subject not found.")

    def login(self):
        username = self.username.get()
        password = self.password.get()

        self.cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        if self.cursor.fetchone():
            self.create_dashboard()
        else:
            messagebox.showerror("Error", "Invalid username or password.")

    def register(self):
        username = self.username.get()
        password = self.password.get()

        try:
            self.cursor.execute("INSERT INTO users (username, password) VALUES (?, ?, ?)", (username, password))
            self.conn.commit()
            messagebox.showinfo("Success", "User registered successfully!")
            self.create_login_frame()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Username already exists.")

    def logout(self):
        self.username.set("")
        self.password.set("")
        self.create_login_frame()

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = GradingSystemApp(root)
    root.mainloop()
