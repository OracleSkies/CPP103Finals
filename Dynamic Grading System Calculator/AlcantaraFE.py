import tkinter as tk
from tkinter import PhotoImage, ttk
from DonascoBE import Registration_System,Login_System

class Login_and_Register_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Grocery Store Inventory System")
        self.root.geometry("1000x800")
        self.root.resizable(False, False)
        self.bg_image_path = "LOGIN GrADEBOOK.png"
        self.bg = PhotoImage(file=self.bg_image_path)
       
        
        self.bg_label = tk.Label(root, image=self.bg)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        
        
        self.entry_username = tk.Entry(root, font = ('Times New Roman', 20))
        self.entry_username.place(relx = .20, rely = .53, relheight = .05, relwidth= .60)
        
        self.entry_password = tk.Entry(root, font = ('Times New Roman', 20), show= "*")
        self.entry_password.place(relx = .20, rely = .67, relheight = .05, relwidth= .60)
        
        
        self.button_logIN = tk.Button(root,text = "Log IN",font = ('Telegraf', 20, "bold"), bg = "#042C40", fg = "white", borderwidth= 0, command=self.login)
        self.button_logIN.place(relx = .20, rely = .77, relheight = .07, relwidth= .19)
        
        
        self.button_SignUP = tk.Button(root,text = "Sign UP",font = ('Telegraf', 20, "bold"), bg = "#042C40", fg = "white", command = self.signUP, borderwidth= 0)
        self.button_SignUP.place(relx = .61, rely = .77, relheight = .07, relwidth= .19)
        
        
    def signUP(self):
        self.signUP_window = tk.Toplevel(self.root)
        self.signUP_window.geometry('1560x1000')
        self.signUP_window.resizable(False, False)
        
        self.bg_image_path = "signup window.png"
        self.signUP_window.bg = PhotoImage(file=self.bg_image_path)
        self.bg_label = tk.Label(self.signUP_window, image=self.signUP_window.bg)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        
        self.username_entry = tk.Entry(self.signUP_window, font = ('Times New Roman', 20))
        self.username_entry.place(relx = .47, rely = .27, relheight = .05, relwidth= .37)
        
        self.emailAcc_entry = tk.Entry(self.signUP_window, font = ('Times New Roman', 20))
        self.emailAcc_entry.place(relx = .47, rely = .40, relheight = .05, relwidth= .37)
        
        self.password_entry = tk.Entry(self.signUP_window, font = ('Times New Roman', 20), show="*")
        self.password_entry.place(relx = .47, rely = .53, relheight = .05, relwidth= .37)
        
        self.confirm_password_entry = tk.Entry(self.signUP_window, font = ('Times New Roman', 20), show = "*")
        self.confirm_password_entry.place(relx = .47, rely = .66, relheight = .05, relwidth= .37)
        
        self.sumbit_button = tk.Button(self.signUP_window,text = "Submit" ,font = ('Telegraf', 20, "bold"), bg = "#042C40", fg = "white", borderwidth= 0, command=self.register)
        self.sumbit_button.place(relx = .56, rely = .78, relheight = .05, relwidth= .15)
    
    def register(self):
        register = Registration_System(self.username_entry.get(),self.password_entry.get(),self.confirm_password_entry.get(),self.signUP_window)
        register.register_Account()
    
    def login(self):
        login = Login_System(self.entry_username.get(), self.entry_password.get(), self.root)
        login.login_Account()
        self.HomeDashBoard()

        
    def HomeDashBoard(self):
       
        self.Home_window = tk.Tk()
        self.Home_window.title("DashBoard")
        self.Home_window.geometry('1560x1000')
        self.Home_window.resizable(False, False)
        
        self.bg_image_path = "Dashboard1pls.png"
        self.Home_window.bg = PhotoImage(file=self.bg_image_path)
        self.bg_label = tk.Label(self.Home_window, image=self.Home_window.bg)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        
        
        HomeDasboard_button = tk.Button(self.Home_window, text = "Home", font= ("Telegraf", 20, "bold"), bg ="#084766", fg = "white" )
        HomeDasboard_button.place(relx = .07, rely = .24, relheight = .05, relwidth= .13)
        
        HomeDasboard_grade = tk.Button(self.Home_window, text = "Grade", font= ("Telegraf", 20, "bold"), bg ="#084766", fg = "white" )
        HomeDasboard_grade.place(relx = .07, rely = .34, relheight = .05, relwidth= .13)
        
        HomeDasboard_subject = tk.Button(self.Home_window, text = "Subject", font= ("Telegraf", 20, "bold"), bg ="#084766", fg = "white" )
        HomeDasboard_subject.place(relx = .07, rely = .42, relheight = .05, relwidth= .13)
        
        HomeDasboard_student = tk.Button(self.Home_window, text = "Student", font= ("Telegraf", 20, "bold"), bg ="#084766", fg = "white" )
        HomeDasboard_student.place(relx = .07, rely = .51, relheight = .05, relwidth= .13)
        
        HomeDasboard_logout = tk.Button(self.Home_window, text = "Log Out", font= ("Telegraf", 20, "bold"), bg ="#084766", fg = "white" )
        HomeDasboard_logout.place(relx = .07, rely = .61, relheight = .05, relwidth= .13)
  
        
        

        
        self.Home_window.mainloop() 
    
    
    
    
    
if __name__ == "__main__":
    root = tk.Tk()
    app = Login_and_Register_Window(root)
    root.mainloop()