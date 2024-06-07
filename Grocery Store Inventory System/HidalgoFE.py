#File para sa front end person 2

from tkinter import *
import tkinter as tk

def open_new_window():
    username = User_Entry.get()
    password = Password_Entry.get()
    
    if not username or not password:
        error_label.config(text="Username and Password must be filled! ano ba!", fg="red")
    else:
        open_window = tk.Toplevel(root)
        open_window.title("IN, OUT, INVENTORY")
        open_window.geometry("1000x800")
        
        bg_image_path = "blue.png"
        open_window.bg = PhotoImage(file=bg_image_path)
        bg_label = tk.Label(open_window, image=open_window.bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        new_window_in = tk.Button(open_window, text="IN", font=("Roboto", 70, "bold"), fg="Silver", command=window_IN)
        new_window_in.pack()
        
        new_window_inventory = tk.Button(open_window, text="INVENTORY", font=("Roboto", 70, "bold"), fg="Silver", command=window_INVENTORY)
        new_window_inventory.pack(pady=30)
        
        new_window_out = tk.Button(open_window, text="OUT", font=("Roboto", 70, "bold"), fg="Silver", command=window_OUT)
        new_window_out.pack(pady=30)

def window_IN():
    open_window_IN = tk.Toplevel(root)
    open_window_IN.title("IN WINDOW")
    open_window_IN.geometry("1000x800")
    bg_image_path = "blue.png"
    open_window_IN.bg = PhotoImage(file=bg_image_path)
    bg_label = tk.Label(open_window_IN, image=open_window_IN.bg)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    new_window_IN_button = tk.Button(open_window_IN, text="kaya mo na to elisha")
    new_window_IN_button.pack()

def window_INVENTORY():
    open_window_INVENTORY = tk.Toplevel(root)
    open_window_INVENTORY.title("INVENTORY WINDOW")
    open_window_INVENTORY.geometry("1000x800")
    bg_image_path = "blue.png"
    open_window_INVENTORY.bg = PhotoImage(file=bg_image_path)
    bg_label = tk.Label(open_window_INVENTORY, image=open_window_INVENTORY.bg)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    new_window_INVENTORY_button = tk.Button(open_window_INVENTORY, text="kaya mo na to elisha")
    new_window_INVENTORY_button.pack()

def window_OUT():
    open_window_OUT = tk.Toplevel(root)
    open_window_OUT.title("OUT WINDOW")
    open_window_OUT.geometry("1000x800")
    bg_image_path = "C:\\Users\\aaron\\OneDrive\\Documents\\GitHub\\CPP103Finals\\blue.png"
    open_window_OUT.bg = PhotoImage(file=bg_image_path)
    bg_label = tk.Label(open_window_OUT, image=open_window_OUT.bg)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    new_window_OUT_button = tk.Button(open_window_OUT, text="kaya mo na to elisha")
    new_window_OUT_button.pack()


root = tk.Tk()
root.title("Grocery Store Inventory System")
root.geometry("1000x800")


bg_image_path = "1.png"
bg = PhotoImage(file=bg_image_path)

bg_label = tk.Label(root, image=bg)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


log_in_text = tk.Label(root, text="Log In", font=("Times", 70, "bold"), fg="white", bg="#000029")
log_in_text.pack(pady=80)

User_Entry = tk.StringVar()
Password_Entry = tk.StringVar()


username_label = tk.Label(root, text="Username", font=("Roboto", 20), fg="white", bg="#000150")
username_label.pack(pady=20)
username_entry = tk.Entry(root, textvariable=User_Entry, font=("Arial", 14), width=30, borderwidth=5)
username_entry.pack(pady=10)


password_label = tk.Label(root, text="Password", font=("Roboto", 20), fg="white", bg="#00006E")
password_label.pack(pady=20)
password_entry = tk.Entry(root, textvariable=Password_Entry, font=("Arial", 14), width=30, borderwidth=5, show="*")
password_entry.pack(pady=10)


error_label = tk.Label(root, text="", font=("Arial", 14), fg="red", bg="#000029")
error_label.pack()

login_button = tk.Button(root, text="Log In", font=("Roboto", 16), borderwidth=3, command=open_new_window)
login_button.pack(pady=40)

root.mainloop()
