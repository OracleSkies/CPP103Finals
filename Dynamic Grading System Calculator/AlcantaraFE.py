import tkinter as tk
from tkinter import PhotoImage

# Import statements for your custom modules
from DonascoBE import Registration_System, Login_System


class LoginAndRegisterWindow:
    def __init__(self, root):
        self.LoginWindow = root
        self.LoginWindow.title("Grocery Store Inventory System")
        self.LoginWindow.geometry("1000x800")
        self.LoginWindow.resizable(False, False)

        self.bg_image_path = "LOGIN GrADEBOOK.png"
        self.bg = PhotoImage(file=self.bg_image_path)

        self.bg_label = tk.Label(self.LoginWindow, image=self.bg)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.entry_username = tk.Entry(self.LoginWindow, font=('Times New Roman', 20))
        self.entry_username.place(relx=.20, rely=.53, relheight=.05, relwidth=.60)

        self.entry_password = tk.Entry(self.LoginWindow, font=('Times New Roman', 20), show="*")
        self.entry_password.place(relx=.20, rely=.67, relheight=.05, relwidth=.60)

        self.button_logIN = tk.Button(self.LoginWindow, text="Log IN", font=('Telegraf', 20, "bold"), bg="#042C40", fg="white", borderwidth=0, command=self.login)
        self.button_logIN.place(relx=.20, rely=.77, relheight=.07, relwidth=.19)

        self.button_SignUP = tk.Button(self.LoginWindow, text="Sign UP", font=('Telegraf', 20, "bold"), bg="#042C40", fg="white", command=self.signUP, borderwidth=0)
        self.button_SignUP.place(relx=.61, rely=.77, relheight=.07, relwidth=.19)

    def signUP(self):
        self.signUP_window = tk.Toplevel(self.LoginWindow)
        self.signUP_window.geometry('1560x1000')
        self.signUP_window.resizable(False, False)

        bg_image_path_signup = "signup window.png"
        self.signup_bg = PhotoImage(file=bg_image_path_signup)

        self.bg_label_signup = tk.Label(self.signUP_window, image=self.signup_bg)
        self.bg_label_signup.place(x=0, y=0, relwidth=1, relheight=1)

        self.username_entry = tk.Entry(self.signUP_window, font=('Times New Roman', 20))
        self.username_entry.place(relx=.47, rely=.27, relheight=.05, relwidth=.37)

        self.emailAcc_entry = tk.Entry(self.signUP_window, font=('Times New Roman', 20))
        self.emailAcc_entry.place(relx=.47, rely=.40, relheight=.05, relwidth=.37)

        self.password_entry = tk.Entry(self.signUP_window, font=('Times New Roman', 20), show="*")
        self.password_entry.place(relx=.47, rely=.53, relheight=.05, relwidth=.37)

        self.confirm_password_entry = tk.Entry(self.signUP_window, font=('Times New Roman', 20), show="*")
        self.confirm_password_entry.place(relx=.47, rely=.66, relheight=.05, relwidth=.37)

        self.submit_button = tk.Button(self.signUP_window, text="Submit", font=('Telegraf', 20, "bold"), bg="#042C40", fg="white", borderwidth=0, command=self.register)
        self.submit_button.place(relx=.56, rely=.78, relheight=.05, relwidth=.15)

    def register(self):
        # Add your registration logic here
        self.registerSystem = Registration_System(self.username_entry.get(),self.password_entry.get(), self.confirm_password_entry.get(),self.signUP_window)
        self.registerSystem.register_Account()

    def login(self):
        # Add your login logic here
        self.loginSystem = Login_System(self.entry_username.get(),self.entry_password.get(),self.LoginWindow)
        self.loginSystem.login_Account()
        self.homeDashboard()

    def homeDashboard(self):
        self.home_window = tk.Tk()
        self.home_window.title("Dashboard")
        self.home_window.geometry('1560x1000')
        self.home_window.resizable(False, False)

        bg_image_path_dashboard = "Dashboard1pls.png"
        self.dashboard_bg = PhotoImage(file=bg_image_path_dashboard)

        self.bg_label_dashboard = tk.Label(self.home_window, image=self.dashboard_bg)
        self.bg_label_dashboard.place(x=0, y=0, relwidth=1, relheight=1)

        home_dashboard_button = tk.Button(self.home_window, text="Home", font=("Telegraf", 20, "bold"), bg="#084766", fg="white")
        home_dashboard_button.place(relx=.07, rely=.24, relheight=.05, relwidth=.13)

        home_grade_button = tk.Button(self.home_window, text="Grade", font=("Telegraf", 20, "bold"), bg="#084766", fg="white", command=self.gradeDashboard)
        home_grade_button.place(relx=.07, rely=.34, relheight=.05, relwidth=.13)

        home_subject_button = tk.Button(self.home_window, text="Subject", font=("Telegraf", 20, "bold"), bg="#084766", fg="white")
        home_subject_button.place(relx=.07, rely=.42, relheight=.05, relwidth=.13)

        home_student_button = tk.Button(self.home_window, text="Student", font=("Telegraf", 20, "bold"), bg="#084766", fg="white")
        home_student_button.place(relx=.07, rely=.51, relheight=.05, relwidth=.13)

        home_logout_button = tk.Button(self.home_window, text="Log Out", font=("Telegraf", 20, "bold"), bg="#084766", fg="white")
        home_logout_button.place(relx=.07, rely=.61, relheight=.05, relwidth=.13)

        self.home_window.mainloop()

    def gradeDashboard(self):
        self.grade_window = root
        self.grade_window.title("Create Grading System")
        self.grade_window.geometry('1560x1000')
        self.grade_window.resizable(False, False)

        bg_image_path_grade = "grade1.png"
        self.grade_bg = PhotoImage(file=bg_image_path_grade)

        self.bg_label_grade = tk.Label(self.grade_window, image=self.grade_bg)
        self.bg_label_grade.place(x=0, y=0, relwidth=1, relheight=1)

        grade_dashboard_button = tk.Button(self.grade_window, text="Home", font=("Telegraf", 20, "bold"), bg="#084766", fg="white")
        grade_dashboard_button.place(relx=.07, rely=.24, relheight=.05, relwidth=.13)

        grade_grade_button = tk.Button(self.grade_window, text="Grade", font=("Telegraf", 20, "bold"), bg="#084766", fg="white", command=self.gradeDashboard)
        grade_grade_button.place(relx=.07, rely=.34, relheight=.05, relwidth=.13)

        grade_subject_button = tk.Button(self.grade_window, text="Subject", font=("Telegraf", 20, "bold"), bg="#084766", fg="white")
        grade_subject_button.place(relx=.07, rely=.42, relheight=.05, relwidth=.13)

        grade_student_button = tk.Button(self.grade_window, text="Student", font=("Telegraf", 20, "bold"), bg="#084766", fg="white")
        grade_student_button.place(relx=.07, rely=.51, relheight=.05, relwidth=.13)

        grade_logout_button = tk.Button(self.grade_window, text="Log Out", font=("Telegraf", 20, "bold"), bg="#084766", fg="white")
        grade_logout_button.place(relx=.07, rely=.61, relheight=.05, relwidth=.13)
        
        
        grade_entry_subject = tk.Entry(self.grade_window, font = ("Times New Roman", 30))
        grade_entry_subject.place(relx=.43, rely=.250, relheight=.05, relwidth=.31)
        
        grade_entry_criteria = tk.Entry(self.grade_window, font = ("Times New Roman", 30))
        grade_entry_criteria.place(relx=.43, rely=.320, relheight=.05, relwidth=.31)
        
        
        grade_entry_percentage = tk.Entry(self.grade_window, font = ("Times New Roman", 30))
        grade_entry_percentage.place(relx=.43, rely=.394, relheight=.05, relwidth=.31)
        
        
        self.grade_window.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = LoginAndRegisterWindow(root)
    root.mainloop()