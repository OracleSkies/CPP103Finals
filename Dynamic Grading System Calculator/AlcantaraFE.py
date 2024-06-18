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
        self.entry_username.place(relx = .20, rely = .53, relheight = .04, relwidth= .60)
        
        self.entry_password = tk.Entry(root, font = ('Times New Roman', 20))
        self.entry_password.place(relx = .20, rely = .67, relheight = .05, relwidth= .60)
        
        
        self.button_logIN = tk.Button(root,text = "Log IN",font = ('Telegraf', 20, "bold"), bg = "midnight blue", fg = "white")
        self.button_logIN.place(relx = .20, rely = .77, relheight = .07, relwidth= .19)
        
        
        self.button_SignUP = tk.Button(root,text = "Sign UP",font = ('Telegraf', 20, "bold"), bg = "midnight blue", fg = "white")
        self.button_SignUP.place(relx = .61, rely = .77, relheight = .07, relwidth= .19)
        
        
       
        
        
        
if __name__ == "__main__":
    root = tk.Tk()
    app = GroceryApp(root)
    root.mainloop()