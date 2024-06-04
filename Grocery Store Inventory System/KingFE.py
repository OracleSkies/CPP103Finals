#File para sa front end person 1

from tkinter import *
import tkinter as tk

# Create the main window
root= tk.Tk()
root.title("Grocery Store Inventory System")
root.geometry("1000x800")

# backgorund image
bg_image = ("C:\\Users\\User\\Documents\\GitHub\\CPP103Finals\\blue.png")
bg = PhotoImage(file=bg_image)
# display backgroung image
bg_label = tk.Label(root, image=bg)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# log in text
log_in_text = tk.Label(root, text="Log In", font=("Times",70,"bold"), fg="white", bg="#000029").pack(pady=50)

username_label = tk.Label(root, text="Username", font=("Times", 20), fg="white", bg="#000150").pack(pady=20)
username_entry = tk.Entry(root, text="Entry", font=("Arial", 14), width=50, borderwidth=5).pack()


password_label = tk.Label(root, text="Password", font=("Times", 20), fg="white", bg="#01005E").pack(pady=20)
password_entry = tk.Entry(root, text="Entry", font=("Arial", 14), width=50, borderwidth=5).pack()






class Inventory:
    def __init__(self, root):
        self.root = root
        self.root.title("A Dynamic Grading System Application")
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.create_login_frame()

    def create_login_frame(self):
        self.clear_frame()

        """
        ===================================================
        SA FRONT END CLASS DAPAT MAKIKITA ANG METHOD NA ITO
        ===================================================
        """
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
        """
        ===================================================
        SA FRONT END CLASS DAPAT MAKIKITA ANG METHOD NA ITO
        ===================================================
        """
        
        self.register_frame = tk.Frame(self.root)
        self.register_frame.pack()

        tk.Label(self.register_frame, text="Username:").grid(row=0, column=0)
        tk.Entry(self.register_frame, textvariable=self.username).grid(row=0, column=1)
        tk.Label(self.register_frame, text="Password:").grid(row=1, column=0)
        tk.Entry(self.register_frame, textvariable=self.password, show='*').grid(row=1, column=1)
        tk.Button(self.register_frame, text="Confirm", command=self.register).grid(row=2, column=0, columnspan=2)
        tk.Button(self.register_frame, text="Back", command=self.create_login_frame).grid(row=3, column=0, columnspan=2)


 

root.mainloop()
