from tkinter import *
import tkinter as tk

def close_other_windows(exclude_window=None):
    """Close all Toplevel windows except the one specified."""
    for window in root.winfo_children():
        if isinstance(window, tk.Toplevel) and window is not exclude_window:
            window.destroy()

def open_new_window():
    username = User_Entry.get()
    password = Password_Entry.get()
    
    if not username or not password:
        error_label.config(text="Username and Password must be filled! ano ba!", fg="red")
    else:
        close_other_windows()  # Close other windows before opening a new one

        open_window = tk.Toplevel(root)
        open_window.title("IN, OUT, INVENTORY")
        open_window.geometry("1000x800")
        open_window.resizable(True, True)

        # Create a frame that will expand and fill the window
        frame = tk.Frame(open_window)
        frame.pack(fill=BOTH, expand=True)

        new_window_in = tk.Button(frame, text="IN", font=("Times New Roman", 60, "bold"), bg="#00CED1", fg="White", command=lambda: window_IN(open_window), borderwidth=0)
        new_window_in.pack(fill=BOTH, expand=True, padx=10, pady=10)
        
        new_window_inventory = tk.Button(frame, text="INVENTORY", font=("Times New Roman", 60, "bold"), bg="#00CED1", fg="White", command=lambda: window_INVENTORY(open_window), borderwidth=0)
        new_window_inventory.pack(fill=BOTH, expand=True, padx=10, pady=10)
        
        new_window_out = tk.Button(frame, text="OUT", font=("Times New Roman", 60, "bold"), bg="#00CED1", fg="White", command=lambda: window_OUT(open_window), borderwidth=0)
        new_window_out.pack(fill=BOTH, expand=True, padx=10, pady=10)

def window_IN(parent_window):
    close_other_windows(exclude_window=parent_window)  # Close other windows except the parent

    open_window_IN = tk.Toplevel(root)
    open_window_IN.title("IN WINDOW")
    open_window_IN.geometry("1000x800")
    open_window_IN.resizable(True, True)

    # Create a frame that will expand and fill the window
    frame = tk.Frame(open_window_IN)
    frame.pack(fill=BOTH, expand=True)

    new_window_IN_button = tk.Button(frame, text="kaya mo na to A-ARON", bg="#00CED1", font=("Arial", 20), borderwidth=0)
    new_window_IN_button.pack(fill=BOTH, expand=True, padx=10, pady=10)

def window_INVENTORY(parent_window):
    close_other_windows(exclude_window=parent_window)  # Close other windows except the parent

    open_window_INVENTORY = tk.Toplevel(root)
    open_window_INVENTORY.title("INVENTORY WINDOW")
    open_window_INVENTORY.geometry("1000x800")
    open_window_INVENTORY.resizable(True, True)

    # Create a frame that will expand and fill the window
    frame = tk.Frame(open_window_INVENTORY)
    frame.pack(fill=BOTH, expand=True)

    new_window_INVENTORY_button = tk.Button(frame, text="kaya mo na to A=ARON", bg="#00CED1", font=("Arial", 20), borderwidth=0)
    new_window_INVENTORY_button.pack(fill=BOTH, expand=True, padx=10, pady=10)

def window_OUT(parent_window):
    close_other_windows(exclude_window=parent_window)  # Close other windows except the parent

    open_window_OUT = tk.Toplevel(root)
    open_window_OUT.title("OUT WINDOW")
    open_window_OUT.geometry("1000x800")
    open_window_OUT.resizable(True, True)

    # Create a frame that will expand and fill the window
    frame = tk.Frame(open_window_OUT)
    frame.pack(fill=BOTH, expand=True)

    new_window_OUT_button = tk.Button(frame, text="kaya mo na to A-ARON", bg="#00CED1", font=("Arial", 20), borderwidth=0)
    new_window_OUT_button.pack(fill=BOTH, expand=True, padx=10, pady=10)

def register_window():
    close_other_windows()  # Close other windows before opening a new one

    open_register = tk.Toplevel(root)
    open_register.title("Register")
    open_register.geometry("600x400")
    open_register.resizable(True, True)

    # Create a frame that will expand and fill the window
    frame = tk.Frame(open_register)
    frame.pack(fill=BOTH, expand=True)

    register_label = tk.Label(frame, text="Register New User", font=("Times", 40, "bold"), fg="black")
    register_label.pack(pady=20)

    reg_username_label = tk.Label(frame, text="Username", font=("Roboto", 20))
    reg_username_label.pack(pady=10)
    reg_username_entry = tk.Entry(frame, font=("Arial", 14), width=30, borderwidth=5)
    reg_username_entry.pack(pady=5)

    reg_password_label = tk.Label(frame, text="Password", font=("Roboto", 20))
    reg_password_label.pack(pady=10)
    reg_password_entry = tk.Entry(frame, font=("Arial", 14), width=30, borderwidth=5, show="*")
    reg_password_entry.pack(pady=5)

    reg_button = tk.Button(frame, text="Register", font=("Roboto", 16), borderwidth=3, bg="#00CED1")
    reg_button.pack(pady=20)

root = tk.Tk()
root.title("Grocery Store Inventory System")
root.geometry("1000x800")
root.resizable(True, True)

# Create a frame that will expand and fill the root window
frame = tk.Frame(root)
frame.pack(fill=BOTH, expand=True)

log_in_text = tk.Label(frame, text="Log In", font=("Times", 70, "bold"), fg="white", bg="#000029")
log_in_text.pack(pady=40)

User_Entry = tk.StringVar()
Password_Entry = tk.StringVar()

username_label = tk.Label(frame, text="Username", font=("Roboto", 20), fg="white", bg="#000150")
username_label.pack(pady=20)
username_entry = tk.Entry(frame, textvariable=User_Entry, font=("Arial", 14), width=30, borderwidth=5)
username_entry.pack(pady=10)

password_label = tk.Label(frame, text="Password", font=("Roboto", 20), fg="white", bg="#00006E")
password_label.pack(pady=20)
password_entry = tk.Entry(frame, textvariable=Password_Entry, font=("Arial", 14), width=30, borderwidth=5, show="*")
password_entry.pack(pady=10)

error_label = tk.Label(frame, text="", font=("Arial", 14), fg="red", bg="#000029")
error_label.pack()

login_button = tk.Button(frame, text="Log In", font=("Roboto", 16), borderwidth=3, command=open_new_window)
login_button.pack(pady=20)

register_button = tk.Button(frame, text="Register", font=("Roboto", 16), borderwidth=3, command=register_window)
register_button.pack(pady=20)

root.mainloop()