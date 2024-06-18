#File para sa front end person 1
import tkinter as tk
from tkinter import PhotoImage, ttk

class GroceryApp:
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
        
        self.entry_password = tk.Entry(root, font = ('Times New Roman', 20))
        self.entry_password.place(relx = .20, rely = .67, relheight = .05, relwidth= .60)
        
        
        self.button_logIN = tk.Button(root,text = "Log IN",font = ('Telegraf', 20, "bold"), bg = "#042C40", fg = "white", borderwidth= 0)
        self.button_logIN.place(relx = .20, rely = .77, relheight = .07, relwidth= .19)
        
        
        self.button_SignUP = tk.Button(root,text = "Sign UP",font = ('Telegraf', 20, "bold"), bg = "#042C40", fg = "white", command = self.signUP, borderwidth= 0)
        self.button_SignUP.place(relx = .61, rely = .77, relheight = .07, relwidth= .19)
        
        
    def signUP(self):
        signUP_window = tk.Toplevel(self.root)
        signUP_window.geometry('1560x1000')
        signUP_window.resizable(False, False)
        
        bg_image_path = "signup window.png"
        signUP_window.bg = PhotoImage(file=bg_image_path)
        bg_label = tk.Label(signUP_window, image=signUP_window.bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        
        username_entry = tk.Entry(signUP_window, font = ('Times New Roman', 20))
        username_entry.place(relx = .47, rely = .27, relheight = .05, relwidth= .37)
        
        emailAcc_entry = tk.Entry(signUP_window, font = ('Times New Roman', 20))
        emailAcc_entry.place(relx = .47, rely = .40, relheight = .05, relwidth= .37)
        
        password_entry = tk.Entry(signUP_window, font = ('Times New Roman', 20))
        password_entry.place(relx = .47, rely = .53, relheight = .05, relwidth= .37)
        
        confirm_password_entry = tk.Entry(signUP_window, font = ('Times New Roman', 20))
        confirm_password_entry.place(relx = .47, rely = .66, relheight = .05, relwidth= .37)
        
        sumbit_button = tk.Button(signUP_window,text = "Submit" ,font = ('Telegraf', 20, "bold"), bg = "#042C40", fg = "white", borderwidth= 0)
        sumbit_button.place(relx = .56, rely = .78, relheight = .05, relwidth= .15)
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    root = tk.Tk()
    app = GroceryApp(root)
    root.mainloop()