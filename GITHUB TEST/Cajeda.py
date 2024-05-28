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

    def create_subject_frame(self):
        self.clear_frame()

        self.subject_frame = tk.Frame(self.root)
        self.subject_frame.pack()

        self.subject_name = tk.StringVar()

        tk.Label(self.subject_frame, text="Subject:").grid(row=0, column=0)
        tk.Entry(self.subject_frame, textvariable=self.subject_name).grid(row=0, column=1)

        self.criteria_entries = []

        # Initialize buttons here
        self.add_criteria_button = tk.Button(self.subject_frame, text="Add Criteria", command=self.add_criteria_entry)
        self.add_criteria_button.grid(row=1, column=0, columnspan=2)
        self.confirm_button = tk.Button(self.subject_frame, text="Confirm", command=self.save_subject)
        self.confirm_button.grid(row=2, column=0, columnspan=2)
        self.back_button = tk.Button(self.subject_frame, text="Back", command=self.create_dashboard)
        self.back_button.grid(row=3, column=0, columnspan=2)
        
        self.add_criteria_entry()  # Add the first criteria entry

    def add_criteria_entry(self):
        row = len(self.criteria_entries) + 1
        criteria_name = tk.StringVar()
        percentage = tk.IntVar()
        self.criteria_entries.append((criteria_name, percentage))
        
        tk.Label(self.subject_frame, text=f"Criteria {row}:").grid(row=row, column=0)
        tk.Entry(self.subject_frame, textvariable=criteria_name).grid(row=row, column=1)
        tk.Label(self.subject_frame, text="Percentage:").grid(row=row, column=2)
        tk.Entry(self.subject_frame, textvariable=percentage).grid(row=row, column=3)

        # Move the buttons down
        self.add_criteria_button.grid(row=row + 1, column=0, columnspan=2)
        self.confirm_button.grid(row=row + 2, column=0, columnspan=2)
        self.back_button.grid(row=row + 3, column=0, columnspan=2)

    def create_search_subject_frame(self):
        self.clear_frame()

        self.search_frame = tk.Frame(self.root)
        self.search_frame.pack()

        tk.Label(self.search_frame, text="Subject:").grid(row=0, column=0)
        self.search_subject_name = tk.StringVar()
        tk.Entry(self.search_frame, textvariable=self.search_subject_name).grid(row=0, column=1)
        tk.Button(self.search_frame, text="Search", command=self.search_subject).grid(row=1, column=0, columnspan=2)
        tk.Button(self.search_frame, text="Back", command=self.create_dashboard).grid(row=2, column=0, columnspan=2)

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

    def show_criteria(self, subject_name):
        self.clear_frame()
        self.criteria_frame = tk.Frame(self.root)
        self.criteria_frame.pack()

        criteria = self.criterias.get(subject_name, {})
        criteria_text = "\n".join([f"{key}: {value}%" for key, value in criteria.items()])

        tk.Label(self.criteria_frame, text="Criteria:").grid(row=0, column=0)
        tk.Label(self.criteria_frame, text=criteria_text).grid(row=1, column=0)
        tk.Button(self.criteria_frame, text="Back", command=lambda: self.create_subject_details_frame(subject_name)).grid(row=2, column=0)

    def show_student_records(self, subject_name):
        self.clear_frame()
        self.records_frame = tk.Frame(self.root)
        self.records_frame.pack()

        records = self.students.get(subject_name, [])

        # Retrieve student records from the students table
        student_numbers = [record[2] for record in records]
        self.cursor.execute("SELECT * FROM students WHERE student_number IN ({seq})".format(
            seq=','.join(['?']*len(student_numbers))), tuple(student_numbers))
        student_records = self.cursor.fetchall()

        tk.Label(self.records_frame, text="Name\tStudent Number\tHomework\tSeatwork\tQuizzes\tExams").grid(row=0, column=0)

        for i, student_record in enumerate(student_records):
            student_name = student_record[1]
            student_lastname = student_record[2]
            student_number = student_record[0]
            homework = student_record[5]
            seatwork = student_record[6]
            quizzes = student_record[7]
            exams = student_record[8]

            student_record_text = f"{student_name} {student_lastname}\t{student_number}\t{homework}\t{seatwork}\t{quizzes}\t{exams}"
            tk.Label(self.records_frame, text=student_record_text).grid(row=i+1, column=0)

        tk.Button(self.records_frame, text="Back", command=lambda: self.create_subject_details_frame(subject_name)).grid(row=len(student_records) + 1, column=0)

    def add_student(self, subject_name):
        self.clear_frame()
        self.add_student_frame = tk.Frame(self.root)
        self.add_student_frame.pack()

        self.student_name = tk.StringVar()
        self.student_lastname = tk.StringVar()
        self.student_number = tk.StringVar()
        self.student_section = tk.StringVar()

        tk.Label(self.add_student_frame, text="First Name:").grid(row=0, column=0)
        tk.Entry(self.add_student_frame, textvariable=self.student_name).grid(row=0, column=1)
        tk.Label(self.add_student_frame, text="Last Name:").grid(row=1, column=0)
        tk.Entry(self.add_student_frame, textvariable=self.student_lastname).grid(row=1, column=1)
        tk.Label(self.add_student_frame, text="Student Number:").grid(row=2, column=0)
        tk.Entry(self.add_student_frame, textvariable=self.student_number).grid(row=2, column=1)
        tk.Label(self.add_student_frame, text="Section:").grid(row=3, column=0)
        tk.Entry(self.add_student_frame, textvariable=self.student_section).grid(row=3, column=1)

        tk.Button(self.add_student_frame, text="Confirm", command=lambda: self.save_student(subject_name)).grid(row=4, column=0, columnspan=2)
        tk.Button(self.add_student_frame, text="Back", command=lambda: self.create_subject_details_frame(subject_name)).grid(row=5, column=0, columnspan=2)

    def save_student(self, subject_name):
        student_name = self.student_name.get()
        student_lastname = self.student_lastname.get()
        student_number = self.student_number.get()
        student_section = self.student_section.get()

        if not (student_name and student_lastname and student_number and student_section):
            messagebox.showerror("Error", "All fields are required")
            return

        student_record = (student_name, student_lastname, student_number, student_section, 0, 0, 0, 0)

        try:
            # Insert the new student into the students table
            self.cursor.execute("INSERT INTO students (student_number, name, lastname, section, subject, homework, seatwork, quizzes, exams) VALUES (?, ?, ?, ?, ?, 0, 0, 0, 0)",
                                (student_number, student_name, student_lastname, student_section, subject_name))
            self.conn.commit()

            if subject_name in self.students:
                self.students[subject_name].append(student_record)
            else:
                self.students[subject_name] = [student_record]

            messagebox.showinfo("Success", "Student added successfully")
            self.create_subject_details_frame(subject_name)
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Student number already exists")

    def edit_criteria(self, subject_name):
        self.clear_frame()
        self.edit_criteria_frame = tk.Frame(self.root)
        self.edit_criteria_frame.pack()

        criteria = self.criterias.get(subject_name, {})
        self.criteria_entries = []

        for i, (criteria_name, percentage) in enumerate(criteria.items()):
            criteria_var = tk.StringVar(value=criteria_name)
            percentage_var = tk.IntVar(value=percentage)
            self.criteria_entries.append((criteria_var, percentage_var))
            tk.Label(self.edit_criteria_frame, text=f"Criteria {i+1}:").grid(row=i, column=0)
            tk.Entry(self.edit_criteria_frame, textvariable=criteria_var).grid(row=i, column=1)
            tk.Label(self.edit_criteria_frame, text="Percentage:").grid(row=i, column=2)
            tk.Entry(self.edit_criteria_frame, textvariable=percentage_var).grid(row=i, column=3)

        self.add_criteria_button = tk.Button(self.edit_criteria_frame, text="Add Criteria", command=self.add_criteria_entry)
        self.add_criteria_button.grid(row=len(criteria) + 1, column=0, columnspan=2)
        self.confirm_button = tk.Button(self.edit_criteria_frame, text="Confirm", command=lambda: self.save_subject(subject_name))
        self.confirm_button.grid(row=len(criteria) + 2, column=0, columnspan=2)
        self.back_button = tk.Button(self.edit_criteria_frame, text="Back", command=lambda: self.create_subject_details_frame(subject_name))
        self.back_button.grid(row=len(criteria) + 3, column=0, columnspan=2)

    def save_subject(self, subject_name=None):
        if subject_name is None:
            subject_name = self.subject_name.get()
            if not subject_name:
                messagebox.showerror("Error", "Subject name is required")
                return

        criteria = {}
        for criteria_name, percentage in self.criteria_entries:
            name = criteria_name.get()
            perc = percentage.get()
            if name and perc:
                criteria[name] = perc

        if not criteria:
            messagebox.showerror("Error", "At least one criteria is required")
            return

        # Check if the subject already exists
        self.cursor.execute("SELECT subject FROM criterias WHERE subject=?", (subject_name,))
        existing_subject = self.cursor.fetchone()

        if existing_subject:
            # Update existing criteria
            for name, perc in criteria.items():
                self.cursor.execute("""
                    UPDATE criterias
                    SET percentage = ?
                    WHERE subject = ? AND criteria = ?
                """, (perc, subject_name, name))
        else:
            # Insert new criteria
            for name, perc in criteria.items():
                self.cursor.execute("INSERT INTO criterias (subject, criteria, percentage) VALUES (?, ?, ?)", (subject_name, name, perc))

        self.conn.commit()
        self.criterias[subject_name] = criteria

        messagebox.showinfo("Success", "Subject and criteria saved successfully")
        self.create_dashboard()

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def login(self):
        username = self.username.get()
        password = self.password.get()

        self.cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = self.cursor.fetchone()

        if user:
            self.create_dashboard()
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def register(self):
        username = self.username.get()
        password = self.password.get()

        if not (username and password):
            messagebox.showerror("Error", "All fields are required")
            return

        try:
            self.cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            self.conn.commit()
            messagebox.showinfo("Success", "User registered successfully")
            self.create_login_frame()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Username already exists")

    def search_subject(self):
        subject_name = self.search_subject_name.get()

        if subject_name in self.criterias:
            self.create_subject_details_frame(subject_name)
        else:
            messagebox.showerror("Error", "Subject not found")

    def close_database(self):
        self.conn.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = GradingSystemApp(root)
    root.mainloop()
    app.close_database()
