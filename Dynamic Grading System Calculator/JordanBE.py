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

        # Create the login frame with a background color and padding
        self.login_frame = tk.Frame(self.root, bg="blue4", bd=5, relief=tk.RIDGE)
        self.login_frame.pack(pady=150, padx=150)

        # Title label
        tk.Label(self.login_frame, text="GRADEBOOK", font=("Helvetica", 24, "bold"), bg="#f0f0f0", fg="navy").grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # Username label and entry
        tk.Label(self.login_frame, text="Username:", font=("Helvetica", 12), bg="#f0f0f0").grid(row=1, column=0, padx=20, pady=10, sticky="w")
        tk.Entry(self.login_frame, textvariable=self.username, font=("Helvetica", 12), bd=2, relief=tk.SOLID).grid(row=1, column=1, padx=20, pady=10)

        # Password label and entry
        tk.Label(self.login_frame, text="Password:", font=("Helvetica", 12), bg="#f0f0f0").grid(row=2, column=0, padx=20, pady=10, sticky="w")
        tk.Entry(self.login_frame, textvariable=self.password, show='*', font=("Helvetica", 12), bd=2, relief=tk.SOLID).grid(row=2, column=1, padx=20, pady=10)

        # Login and Register buttons
        tk.Button(self.login_frame, text="Login", command=self.login, font=("Helvetica", 12), bg="navy", fg="white", bd=2, relief=tk.RAISED).grid(row=3, column=0, columnspan=2, pady=20)
        tk.Button(self.login_frame, text="Register", command=self.create_register_frame, font=("Helvetica", 12), bg="navy", fg="white", bd=2, relief=tk.RAISED).grid(row=4, column=0, columnspan=2, pady=10)

    def create_register_frame(self):
        self.clear_frame()

        # Create the registration frame
        self.register_frame = tk.Frame(self.root, bg="blue2", bd=5, relief=tk.RIDGE)
        self.register_frame.pack(pady=150, padx=150)

        
        # Username label and entry
        tk.Label(self.register_frame, text="Username:", font=("Helvetica", 12), bg="#f0f0f0").grid(row=1, column=0, padx=20, pady=10, sticky="w")
        tk.Entry(self.register_frame, textvariable=self.username, font=("Helvetica", 12), bd=2, relief=tk.SOLID).grid(row=1, column=1, padx=20, pady=10)

        # Password label and entry
        tk.Label(self.register_frame, text="Password:", font=("Helvetica", 12), bg="#f0f0f0").grid(row=2, column=0, padx=20, pady=10, sticky="w")
        tk.Entry(self.register_frame, textvariable=self.password, show='*', font=("Helvetica", 12), bd=2, relief=tk.SOLID).grid(row=2, column=1, padx=20, pady=10)

        # Register and Back buttons
        tk.Button(self.register_frame, text="Register", command=self.register, font=("Helvetica", 12), bg="green", fg="white", bd=2, relief=tk.RAISED).grid(row=3, column=0, columnspan=2, pady=20)
        tk.Button(self.register_frame, text="Back", command=self.go_back, font=("Helvetica", 12), bg="navy", fg="white", bd=2, relief=tk.RAISED).grid(row=4, column=0, columnspan=2, pady=10)

    def create_dashboard(self):
        self.clear_frame()

        # Create the dashboard frame
        self.dashboard_frame = tk.Frame(self.root, bg="blue3", bd=5, relief=tk.RIDGE)
        self.dashboard_frame.pack(padx=200, pady=200)

        # Welcome label
        tk.Label(self.dashboard_frame, text="Welcome to GRADEBOOK PROMAX", font=("Helvetica", 15, "bold"), bg="#f0f0f0").grid(row=0, column=0, columnspan=2, pady=20)

        # Add Subject button
        tk.Button(self.dashboard_frame, text="Add Subject", command=self.add_subject, font=("Helvetica", 12), bg="green", fg="white", bd=2, relief=tk.RAISED, width=15).grid(row=1, column=0, padx=20, pady=10)

        # Search Subject button
        tk.Button(self.dashboard_frame, text="Search Subject", command=self.create_search_subject_frame, font=("Helvetica", 12), bg="blue", fg="white", bd=2, relief=tk.RAISED, width=15).grid(row=1, column=1, padx=20, pady=10)

        # Logout button
        tk.Button(self.dashboard_frame, text="Logout", command=self.logout, font=("Helvetica", 12), bg="red", fg="white", bd=2, relief=tk.RAISED, width=15).grid(row=2, column=0, columnspan=2, pady=20)


    def add_subject(self):
        self.clear_frame()

        # Create the add subject frame
        self.add_subject_frame = tk.Frame(self.root, bg="green", bd=5, relief=tk.RIDGE)
        self.add_subject_frame.pack(padx=200, pady=200)

        # Subject Name label and entry
        tk.Label(self.add_subject_frame, text="Subject Name:", font=("Helvetica", 20), bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=10)
        tk.Entry(self.add_subject_frame, textvariable=self.subject_name, font=("Helvetica", 20)).grid(row=0, column=1, padx=10, pady=10)

        # Add Subject button
        tk.Button(self.add_subject_frame, text="Add Subject", command=self.save_subject_name, font=("Helvetica", 12), bg="green", fg="white", bd=2, relief=tk.RAISED, width=15).grid(row=1, column=0, columnspan=2, padx=10, pady=20)

        # Back button
        tk.Button(self.add_subject_frame, text="Back", command=self.go_back, font=("Helvetica", 12), bg="blue", fg="white", bd=2, relief=tk.RAISED, width=15).grid(row=2, column=0, columnspan=2, padx=10, pady=10)

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

        # Create the search subject frame
        self.search_subject_frame = tk.Frame(self.root, bg="green", bd=5, relief=tk.RIDGE)
        self.search_subject_frame.pack(padx=200, pady=200)

        # Search Subject label and entry
        tk.Label(self.search_subject_frame, text="Search Subject:", font=("Helvetica", 15), bg="gray").grid(row=0, column=0, padx=10, pady=10)
        tk.Entry(self.search_subject_frame, textvariable=self.search_subject_name, font=("Helvetica", 15)).grid(row=0, column=1, padx=10, pady=10)

        # Search and Back buttons
        tk.Button(self.search_subject_frame, text="Search", command=self.search_subject, font=("Helvetica", 12), bg="green", fg="white", bd=2, relief=tk.RAISED, width=15).grid(row=1, column=0, columnspan=2, padx=10, pady=20)
        tk.Button(self.search_subject_frame, text="Back", command=self.go_back, font=("Helvetica", 12), bg="blue", fg="white", bd=2, relief=tk.RAISED, width=15).grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def create_subject_details_frame(self, subject_name):
        self.clear_frame()

        # Create the subject details frame
        self.subject_details_frame = tk.Frame(self.root, bg="#f0f0f0", bd=5, relief=tk.RIDGE)
        self.subject_details_frame.pack(padx=200, pady=200)

        # Subject label
        tk.Label(self.subject_details_frame, text=f"Subject: {subject_name}", font=("Helvetica", 16, "bold"), bg="#f0f0f0").grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Buttons for different actions
        manage_criteria_btn = tk.Button(self.subject_details_frame, text="Manage Criteria", command=lambda: self.manage_criteria(subject_name), font=("Helvetica", 12), bg="#4CAF50", fg="white", bd=2, relief=tk.RAISED, width=15)
        manage_criteria_btn.grid(row=1, column=0, padx=10, pady=20)

        show_criteria_btn = tk.Button(self.subject_details_frame, text="Show Criteria", command=lambda: self.show_criteria(subject_name), font=("Helvetica", 12), bg="#2196F3", fg="white", bd=2, relief=tk.RAISED, width=15)
        show_criteria_btn.grid(row=1, column=1, padx=10, pady=20)

        student_records_btn = tk.Button(self.subject_details_frame, text="Student Records", command=lambda: self.show_student_records(subject_name), font=("Helvetica", 12), bg="#FF9800", fg="white", bd=2, relief=tk.RAISED, width=15)
        student_records_btn.grid(row=2, column=0, padx=10, pady=20)

        add_student_btn = tk.Button(self.subject_details_frame, text="Add Student", command=lambda: self.add_student(subject_name), font=("Helvetica", 12), bg="#9C27B0", fg="white", bd=2, relief=tk.RAISED, width=15)
        add_student_btn.grid(row=2, column=1, padx=10, pady=20)

        # Back button
        back_btn = tk.Button(self.subject_details_frame, text="Back", command=self.go_back, font=("Helvetica", 12), bg="#607D8B", fg="white", bd=2, relief=tk.RAISED, width=30)
        back_btn.grid(row=3, column=0, columnspan=2, padx=10, pady=20)

    def manage_criteria(self, subject_name):
        self.clear_frame()

        self.criteria_frame = tk.Frame(self.root)
        self.criteria_frame.pack(padx=100, pady=100)

        self.subject_name = tk.StringVar(value=subject_name)

        tk.Label(self.criteria_frame, text=f"Manage Criteria for: {subject_name}", font=("Helvetica", 18, "bold")).grid(row=0, column=0, columnspan=3, pady=20)

        # Load existing criteria from database
        rows = self.db.fetch_all("SELECT criteria, percentage FROM criterias WHERE subject=?", (subject_name,))
        self.criteria_entries = [(tk.StringVar(value=row[0]), tk.IntVar(value=row[1])) for row in rows]
        self.criteria_entries.append((tk.StringVar(), tk.IntVar()))  # Add an empty entry for new criteria

        self.update_criteria_display(self.criteria_frame)

        # Back button
        tk.Button(self.criteria_frame, text="Back", command=lambda: self.previous_frame_function(), font=("Helvetica", 12), bg="gray", fg="white", bd=2, relief=tk.RAISED, width=20).grid(row=len(self.criteria_entries) + 1, column=0, columnspan=3, pady=20)

    def update_criteria_display(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

        tk.Label(frame, text=f"Subject: {self.subject_name.get()}", font=("Helvetica", 16, "bold")).grid(row=0, column=0, columnspan=3, pady=10)

        for i, (criteria_var, percentage_var) in enumerate(self.criteria_entries):
            tk.Entry(frame, textvariable=criteria_var, width=30).grid(row=i + 1, column=0, padx=10, pady=5)
            tk.Entry(frame, textvariable=percentage_var, width=10).grid(row=i + 1, column=1, padx=10, pady=5)
            tk.Button(frame, text="Delete", command=lambda i=i: self.delete_criteria(i), width=10).grid(row=i + 1, column=2, padx=10, pady=5)

        if len(self.criteria_entries) < 6:  # Allow up to 6 criteria entries
            tk.Button(frame, text="Add Criteria", command=self.add_criteria, width=30).grid(row=len(self.criteria_entries) + 1, column=0, columnspan=3, pady=10)

        tk.Button(frame, text="Save", command=self.save_criteria, width=30).grid(row=len(self.criteria_entries) + 2, column=0, columnspan=3, pady=10)
        tk.Button(frame, text="Back", command=lambda: self.previous_frame_function(), width=30).grid(row=len(self.criteria_entries) + 3, column=0, columnspan=3, pady=10)

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
        self.show_criteria_frame.pack(padx=100, pady=50)

        self.previous_frame_function = lambda: self.create_subject_details_frame(subject_name)

        tk.Label(self.show_criteria_frame, text=f"Criteria for {subject_name}", font=("Helvetica", 20, "bold"), bg="green").grid(row=0, column=0, columnspan=2, pady=20)

        rows = self.db.fetch_all("SELECT criteria, percentage FROM criterias WHERE subject=?", (subject_name,))
        for i, (criteria, percentage) in enumerate(rows):
            tk.Label(self.show_criteria_frame, text=criteria, font=("Helvetica", 12)).grid(row=i + 1, column=0, padx=10, pady=5)
            tk.Label(self.show_criteria_frame, text=f"{percentage}%", font=("Helvetica", 12)).grid(row=i + 1, column=1, padx=10, pady=5)

        tk.Button(self.show_criteria_frame, text="Back", command=self.go_back, font=("Helvetica", 12), bg="gray", fg="white", bd=2, relief=tk.RAISED, width=30).grid(row=len(rows) + 1, column=0, columnspan=2, pady=20)

    def show_student_records(self, subject_name):
        self.clear_frame()

        self.student_records_frame = tk.Frame(self.root)
        self.student_records_frame.pack(padx=50, pady=30)

        self.previous_frame_function = lambda: self.create_subject_details_frame(subject_name)

        tk.Label(self.student_records_frame, text=f"Student Records for {subject_name}", font=("Helvetica", 18, "bold")).grid(row=0, column=0, columnspan=8, pady=20)

        headers = ["Student Number", "Name", "Last Name", "Section", "Homework", "Seatwork", "Quizzes", "Exams"]
        for col, header in enumerate(headers):
            tk.Label(self.student_records_frame, text=header, font=("Helvetica", 12, "bold")).grid(row=1, column=col, padx=10, pady=5)

        rows = self.db.fetch_all("SELECT student_number, name, lastname, section, subject, homework, seatwork, quizzes, exams FROM students WHERE subject=?", (subject_name,))
        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                tk.Label(self.student_records_frame, text=value).grid(row=i + 2, column=j, padx=10, pady=5)

        tk.Button(self.student_records_frame, text="Back", command=self.go_back, font=("Helvetica", 12), bg="gray", fg="white", bd=2, relief=tk.RAISED, width=30).grid(row=len(rows) + 2, column=0, columnspan=8, pady=20)

    def add_student(self, subject_name):
        self.clear_frame()

        self.add_student_frame = tk.Frame(self.root)
        self.add_student_frame.pack(padx=50, pady=30)

        self.previous_frame_function = lambda: self.create_subject_details_frame(subject_name)

        self.student_number = tk.StringVar()
        self.student_name = tk.StringVar()
        self.student_lastname = tk.StringVar()
        self.student_section = tk.StringVar()
        self.homework = tk.DoubleVar()
        self.seatwork = tk.DoubleVar()
        self.quizzes = tk.DoubleVar()
        self.exams = tk.DoubleVar()

        tk.Label(self.add_student_frame, text="Student Number:", font=("Helvetica", 12)).grid(row=0, column=0, padx=10, pady=10)
        tk.Entry(self.add_student_frame, textvariable=self.student_number).grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.add_student_frame, text="Name:", font=("Helvetica", 12)).grid(row=1, column=0, padx=10, pady=10)
        tk.Entry(self.add_student_frame, textvariable=self.student_name).grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.add_student_frame, text="Last Name:", font=("Helvetica", 12)).grid(row=2, column=0, padx=10, pady=10)
        tk.Entry(self.add_student_frame, textvariable=self.student_lastname).grid(row=2, column=1, padx=10, pady=10)

        tk.Label(self.add_student_frame, text="Section:", font=("Helvetica", 12)).grid(row=3, column=0, padx=10, pady=10)
        tk.Entry(self.add_student_frame, textvariable=self.student_section).grid(row=3, column=1, padx=10, pady=10)

        tk.Label(self.add_student_frame, text="Homework:", font=("Helvetica", 12)).grid(row=4, column=0, padx=10, pady=10)
        tk.Entry(self.add_student_frame, textvariable=self.homework).grid(row=4, column=1, padx=10, pady=10)

        tk.Label(self.add_student_frame, text="Seatwork:", font=("Helvetica", 12)).grid(row=5, column=0, padx=10, pady=10)
        tk.Entry(self.add_student_frame, textvariable=self.seatwork).grid(row=5, column=1, padx=10, pady=10)

        tk.Label(self.add_student_frame, text="Quizzes:", font=("Helvetica", 12)).grid(row=6, column=0, padx=10, pady=10)
        tk.Entry(self.add_student_frame, textvariable=self.quizzes).grid(row=6, column=1, padx=10, pady=10)

        tk.Label(self.add_student_frame, text="Exams:", font=("Helvetica", 12)).grid(row=7, column=0, padx=10, pady=10)
        tk.Entry(self.add_student_frame, textvariable=self.exams).grid(row=7, column=1, padx=10, pady=10)

        tk.Button(self.add_student_frame, text="Add Student", command=lambda: self.save_student(subject_name), font=("Helvetica", 12), bg="green", fg="white", bd=2, relief=tk.RAISED, width=30).grid(row=8, column=0, columnspan=2, padx=10, pady=20)
        tk.Button(self.add_student_frame, text="Back", command=self.go_back, font=("Helvetica", 12), bg="gray", fg="white", bd=2, relief=tk.RAISED, width=30).grid(row=9, column=0, columnspan=2, padx=10, pady=20)

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