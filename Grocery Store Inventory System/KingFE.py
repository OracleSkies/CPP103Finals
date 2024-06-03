#File para sa front end person 1

from tkinter import *
import tkinter as tk

# Create the main window
root= tk.Tk()
root.title("Grocery Store Inventory System")
root.geometry("1000x800")

# backgorund image
bg_image = ("C:\\Users\\Memayk21\\Downloads\\CPP103-OOP-LAB3\\CPP103_FINALS_exam\\blue.png")
bg = PhotoImage(file=bg_image)
# display backgroung image
bg_label = tk.Label(root, image=bg)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# log in text
log_in_text = tk.Label(root, text="Log In", font=("Times",70,"bold"), fg="white", bg="#000029").grid(row=0, column=5)


user_label = tk.Label(root, text="Username", font=("Helvetica", 20), fg="white", bg="#000150").grid(row=1, column=0)
user_entry = tk.Entry(root, text="Entry", width=30).grid(row=2, column=0)


'''
class GradingSystemApp:
    def __init__(self, root):
        self.root = root
        self.root.title("A Dynamic Grading System Application")
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.students = {}
        self.criterias = {}


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
'''
 

root.mainloop()
