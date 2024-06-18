import tkinter as tk
from tkinter import messagebox
import sqlite3

class DatabaseManager:
    def __init__(self):
        self.conn = sqlite3.connect("grading_system.db")
        self.cursor = self.conn.cursor()
        self.create_tables()
        self.update_schema_if_needed()

    def create_tables(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                password TEXT NOT NULL
            )
            """
        )
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS subjects (
                subject TEXT PRIMARY KEY
            )
            """
        )
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS criterias (
                subject TEXT,
                criteria TEXT,
                percentage INTEGER,
                PRIMARY KEY (subject, criteria),
                FOREIGN KEY (subject) REFERENCES subjects(subject)
            )
            """
        )
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS students (
                student_number TEXT PRIMARY KEY,
                name TEXT,
                lastname TEXT,
                section TEXT,
                subject TEXT,
                homework REAL,
                seatwork REAL,
                quizzes REAL,
                exams REAL,
                FOREIGN KEY (subject) REFERENCES subjects(subject)
            )
            """
        )
        self.conn.commit()

    def update_schema_if_needed(self):
        # Check if the 'students' table has the correct structure
        self.cursor.execute("PRAGMA table_info(students)")
        columns = [info[1] for info in self.cursor.fetchall()]

        required_columns = ["subject", "lastname"]
        for col in required_columns:
            if col not in columns:
                self.cursor.execute(f"ALTER TABLE students ADD COLUMN {col} TEXT")
                self.conn.commit()

    def execute_query(self, query, params=()):
        self.cursor.execute(query, params)
        self.conn.commit()

    def fetch_one(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchone()

    def fetch_all(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

class StudentGradingSystem:
    def __init__(self):
        self.db = DatabaseManager()
        self.root = tk.Tk()
        self.root.title("Student Grading System")

        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.subject_name = tk.StringVar()
        self.search_subject_name = tk.StringVar()

        self.criteria_entries = []
        self.previous_frame = None
        self.previous_frame_function = None

        self.create_login_frame()

    def create_login_frame(self):
        self.clear_frame()

        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack()
        self.previous_frame_function = None  # No previous frame before login

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
        self.previous_frame_function = self.create_login_frame

        tk.Label(self.register_frame, text="Username:").grid(row=0, column=0)
        tk.Entry(self.register_frame, textvariable=self.username).grid(row=0, column=1)
        tk.Label(self.register_frame, text="Password:").grid(row=1, column=0)
        tk.Entry(self.register_frame, textvariable=self.password, show='*').grid(row=1, column=1)

        tk.Button(self.register_frame, text="Register", command=self.register).grid(row=2, column=0, columnspan=2)
        tk.Button(self.register_frame, text="Back", command=self.go_back).grid(row=3, column=0, columnspan=2)

    def create_dashboard(self):
        self.clear_frame()

        self.dashboard_frame = tk.Frame(self.root)
        self.dashboard_frame.pack()
        self.previous_frame_function = None  # Dashboard is the main frame

        tk.Label(self.dashboard_frame, text="Welcome to the Student Grading System").grid(row=0, column=0, columnspan=2)
        tk.Button(self.dashboard_frame, text="Add Subject", command=self.add_subject).grid(row=1, column=0)
        tk.Button(self.dashboard_frame, text="Search Subject", command=self.create_search_subject_frame).grid(row=1, column=1)
        tk.Button(self.dashboard_frame, text="Logout", command=self.logout).grid(row=2, column=0, columnspan=2)

    def add_subject(self):
        self.clear_frame()

        self.add_subject_frame = tk.Frame(self.root)
        self.add_subject_frame.pack()
        self.previous_frame_function = self.create_dashboard

        tk.Label(self.add_subject_frame, text="Subject Name:").grid(row=0, column=0)
        tk.Entry(self.add_subject_frame, textvariable=self.subject_name).grid(row=0, column=1)

        tk.Button(self.add_subject_frame, text="Add Subject", command=self.save_subject_name).grid(row=1, column=0, columnspan=2)
        tk.Button(self.add_subject_frame, text="Back", command=self.go_back).grid(row=2, column=0, columnspan=2)

    def save_subject_name(self):
        subject_name = self.subject_name.get()
        if subject_name:
            self.db.execute_query("INSERT OR REPLACE INTO subjects (subject) VALUES (?)", (subject_name,))
            messagebox.showinfo("Success", "Subject added successfully")
            self.create_subject_details_frame(subject_name)
        else:
            messagebox.showerror("Error", "Subject name cannot be empty")

    def create_search_subject_frame(self):
        self.clear_frame()

        self.search_subject_frame = tk.Frame(self.root)
        self.search_subject_frame.pack()
        self.previous_frame_function = self.create_dashboard

        tk.Label(self.search_subject_frame, text="Search Subject:").grid(row=0, column=0)
        tk.Entry(self.search_subject_frame, textvariable=self.search_subject_name).grid(row=0, column=1)

        tk.Button(self.search_subject_frame, text="Search", command=self.search_subject).grid(row=1, column=0, columnspan=2)
        tk.Button(self.search_subject_frame, text="Back", command=self.go_back).grid(row=2, column=0, columnspan=2)

    def create_subject_details_frame(self, subject_name):
        self.clear_frame()

        self.subject_details_frame = tk.Frame(self.root)
        self.subject_details_frame.pack()
        self.previous_frame_function = self.create_dashboard

        tk.Label(self.subject_details_frame, text=f"Subject: {subject_name}").grid(row=0, column=0, columnspan=2)
        tk.Button(self.subject_details_frame, text="Manage Criteria", command=lambda: self.manage_criteria(subject_name)).grid(row=1, column=0)
        tk.Button(self.subject_details_frame, text="Show Criteria", command=lambda: self.show_criteria(subject_name)).grid(row=1, column=1)
        tk.Button(self.subject_details_frame, text="Show Student Records", command=lambda: self.show_student_records(subject_name)).grid(row=2, column=0)
        tk.Button(self.subject_details_frame, text="Add Student", command=lambda: self.add_student(subject_name)).grid(row=2, column=1)
        tk.Button(self.subject_details_frame, text="Back", command=self.go_back).grid(row=3, column=0, columnspan=2)

    def manage_criteria(self, subject_name):
        self.clear_frame()

        self.criteria_frame = tk.Frame(self.root)
        self.criteria_frame.pack()
        self.previous_frame_function = lambda: self.create_subject_details_frame(subject_name)

        self.subject_name = tk.StringVar(value=subject_name)

        tk.Label(self.criteria_frame, text=f"Subject: {subject_name}").grid(row=0, column=0, columnspan=3)

        # Load existing criteria from database
        rows = self.db.fetch_all("SELECT criteria, percentage FROM criterias WHERE subject=?", (subject_name,))

        self.criteria_entries = [(tk.StringVar(value=row[0]), tk.IntVar(value=row[1])) for row in rows]
        self.criteria_entries.append((tk.StringVar(), tk.IntVar()))  # Add an empty entry for new criteria

        self.update_criteria_display(self.criteria_frame)

    def update_criteria_display(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

        tk.Label(frame, text=f"Subject: {self.subject_name.get()}").grid(row=0, column=0, columnspan=3)

        for i, (criteria_var, percentage_var) in enumerate(self.criteria_entries):
            tk.Entry(frame, textvariable=criteria_var).grid(row=i + 1, column=0)
            tk.Entry(frame, textvariable=percentage_var).grid(row=i + 1, column=1)
            tk.Button(frame, text="Delete", command=lambda i=i: self.delete_criteria(i)).grid(row=i + 1, column=2)

        if len(self.criteria_entries) < 7:  # Allow up to 6 criteria entries
            tk.Button(frame, text="Add Criteria", command=self.add_criteria).grid(row=len(self.criteria_entries) + 1, column=0, columnspan=3)
        tk.Button(frame, text="Save", command=self.save_criteria).grid(row=len(self.criteria_entries) + 2, column=0, columnspan=3)
        tk.Button(frame, text="Back", command=self.go_back).grid(row=len(self.criteria_entries) + 3, column=0, columnspan=3)

    def add_criteria(self):
        if len(self.criteria_entries) < 7:
            self.criteria_entries.append((tk.StringVar(), tk.IntVar()))
            self.update_criteria_display(self.criteria_frame)

    def delete_criteria(self, index):
        del self.criteria_entries[index]
        self.update_criteria_display(self.criteria_frame)

    def save_criteria(self):
        subject_name = self.subject_name.get()
        total_percentage = sum(var.get() for _, var in self.criteria_entries)

        if total_percentage != 100:
            messagebox.showerror("Error", "The total percentage of all criteria must equal 100")
            return

        self.db.execute_query("DELETE FROM criterias WHERE subject=?", (subject_name,))
        for criteria_var, percentage_var in self.criteria_entries:
            criteria = criteria_var.get()
            percentage = percentage_var.get()
            if criteria and percentage:
                self.db.execute_query(
                    "INSERT INTO criterias (subject, criteria, percentage) VALUES (?, ?, ?)",
                    (subject_name, criteria, percentage),
                )

        messagebox.showinfo("Success", "Criteria saved successfully")
        self.create_subject_details_frame(subject_name)

    def show_criteria(self, subject_name):
        self.clear_frame()

        self.show_criteria_frame = tk.Frame(self.root)
        self.show_criteria_frame.pack()
        self.previous_frame_function = lambda: self.create_subject_details_frame(subject_name)

        tk.Label(self.show_criteria_frame, text=f"Criteria for {subject_name}").grid(row=0, column=0, columnspan=2)

        rows = self.db.fetch_all("SELECT criteria, percentage FROM criterias WHERE subject=?", (subject_name,))
        for i, (criteria, percentage) in enumerate(rows):
            tk.Label(self.show_criteria_frame, text=criteria).grid(row=i + 1, column=0)
            tk.Label(self.show_criteria_frame, text=f"{percentage}%").grid(row=i + 1, column=1)

        tk.Button(self.show_criteria_frame, text="Back", command=self.go_back).grid(row=len(rows) + 1, column=0, columnspan=2)

    def show_student_records(self, subject_name):
        self.clear_frame()

        self.student_records_frame = tk.Frame(self.root)
        self.student_records_frame.pack()
        self.previous_frame_function = lambda: self.create_subject_details_frame(subject_name)

        tk.Label(self.student_records_frame, text=f"Student Records for {subject_name}").grid(row=0, column=0, columnspan=5)

        rows = self.db.fetch_all("SELECT student_number, name, lastname, section, subject, homework, seatwork, quizzes, exams FROM students WHERE subject=?", (subject_name,))
        headers = ["Student Number", "Name", "Last Name", "Section", "Homework", "Seatwork", "Quizzes", "Exams"]

        for col, header in enumerate(headers):
            tk.Label(self.student_records_frame, text=header).grid(row=1, column=col)

        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                tk.Label(self.student_records_frame, text=value).grid(row=i + 2, column=j)

        tk.Button(self.student_records_frame, text="Back", command=self.go_back).grid(row=len(rows) + 2, column=0, columnspan=5)

    def add_student(self, subject_name):
        self.clear_frame()

        self.add_student_frame = tk.Frame(self.root)
        self.add_student_frame.pack()
        self.previous_frame_function = lambda: self.create_subject_details_frame(subject_name)

        self.student_number = tk.StringVar()
        self.student_name = tk.StringVar()
        self.student_lastname = tk.StringVar()
        self.student_section = tk.StringVar()
        self.homework = tk.DoubleVar()
        self.seatwork = tk.DoubleVar()
        self.quizzes = tk.DoubleVar()
        self.exams = tk.DoubleVar()

        tk.Label(self.add_student_frame, text="Student Number:").grid(row=0, column=0)
        tk.Entry(self.add_student_frame, textvariable=self.student_number).grid(row=0, column=1)
        tk.Label(self.add_student_frame, text="Name:").grid(row=1, column=0)
        tk.Entry(self.add_student_frame, textvariable=self.student_name).grid(row=1, column=1)
        tk.Label(self.add_student_frame, text="Last Name:").grid(row=2, column=0)
        tk.Entry(self.add_student_frame, textvariable=self.student_lastname).grid(row=2, column=1)
        tk.Label(self.add_student_frame, text="Section:").grid(row=3, column=0)
        tk.Entry(self.add_student_frame, textvariable=self.student_section).grid(row=3, column=1)
        tk.Label(self.add_student_frame, text="Homework:").grid(row=4, column=0)
        tk.Entry(self.add_student_frame, textvariable=self.homework).grid(row=4, column=1)
        tk.Label(self.add_student_frame, text="Seatwork:").grid(row=5, column=0)
        tk.Entry(self.add_student_frame, textvariable=self.seatwork).grid(row=5, column=1)
        tk.Label(self.add_student_frame, text="Quizzes:").grid(row=6, column=0)
        tk.Entry(self.add_student_frame, textvariable=self.quizzes).grid(row=6, column=1)
        tk.Label(self.add_student_frame, text="Exams:").grid(row=7, column=0)
        tk.Entry(self.add_student_frame, textvariable=self.exams).grid(row=7, column=1)

        tk.Button(self.add_student_frame, text="Add Student", command=lambda: self.save_student(subject_name)).grid(row=8, column=0, columnspan=2)
        tk.Button(self.add_student_frame, text="Back", command=self.go_back).grid(row=9, column=0, columnspan=2)

    def save_student(self, subject_name):
        student_number = self.student_number.get()
        name = self.student_name.get()
        lastname = self.student_lastname.get()
        section = self.student_section.get()
        homework = self.homework.get()
        seatwork = self.seatwork.get()
        quizzes = self.quizzes.get()
        exams = self.exams.get()

        self.db.execute_query(
            "INSERT OR REPLACE INTO students (student_number, name, lastname, section, subject, homework, seatwork, quizzes, exams) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (student_number, name, lastname, section, subject_name, homework, seatwork, quizzes, exams),
        )
        messagebox.showinfo("Success", "Student added successfully")
        self.create_subject_details_frame(subject_name)

    def search_subject(self):
        subject_name = self.search_subject_name.get()
        if subject_name:
            self.create_subject_details_frame(subject_name)
        else:
            messagebox.showerror("Error", "Subject name cannot be empty")

    def login(self):
        username = self.username.get()
        password = self.password.get()
        user = self.db.fetch_one("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        if user:
            self.create_dashboard()
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def register(self):
        username = self.username.get()
        password = self.password.get()
        if username and password:
            self.db.execute_query("INSERT OR REPLACE INTO users (username, password) VALUES (?, ?)", (username, password))
            messagebox.showinfo("Success", "User registered successfully")
            self.create_login_frame()
        else:
            messagebox.showerror("Error", "Username and password cannot be empty")

    def logout(self):
        self.username.set("")
        self.password.set("")
        self.create_login_frame()

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def go_back(self):
        if self.previous_frame_function:
            self.previous_frame_function()

if __name__ == "__main__":
    app = StudentGradingSystem()
    app.root.mainloop()
