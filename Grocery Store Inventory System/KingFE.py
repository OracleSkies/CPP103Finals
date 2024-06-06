#File para sa front end person 1

from tkinter import *
import tkinter as tk

# Create the main window
root= tk.Tk()
root.title("Grocery Store Inventory System")
root.geometry("1000x800")

# backgorund image
bg_image = ("blue.png")
bg = PhotoImage(file=bg_image)
# display backgroung image
bg_label = tk.Label(root, image=bg)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# log in text
log_in_text = tk.Label(root, text="Log In", font=("Times",70,"bold"), fg="white", bg="#000029").pack(pady=80)

###################################################

User_Entry = tk.StringVar()
Password_Entry = tk.StringVar()

# username
username_label = tk.Label(root, text="Username", font=("Roboto", 20), fg="white", bg="#000150").pack(pady=20)
username_entry = tk.Entry(root, text= User_Entry, font=("Arial", 14), width=30, borderwidth=5).pack(pady=10)

# passsword
password_label = tk.Label(root, text="Password", font=("Roboto", 20), fg="white", bg="#00006E").pack(pady=20)
password_entry = tk.Entry(root, text= Password_Entry, font=("Arial", 14), width=30, borderwidth=5).pack(pady=10)

# login button
login_button = tk.Button(root, text="Log In", font=("Roboto", 16), borderwidth=3)
login_button.pack()

# login button
sign_in_button = tk.Button(root, text="Sign In", font=("Roboto", 16), borderwidth=3)
sign_in_button.place()


root.mainloop()
