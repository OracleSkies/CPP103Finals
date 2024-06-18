#File para sa front end person 1
import tkinter as tk
from tkinter import PhotoImage, ttk

class GroceryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Grocery Store Inventory System")
        self.root.geometry("1000x800")

        self.bg_image_path = "LOGIN GrADEBOOK.png"
        self.bg = PhotoImage(file=self.bg_image_path)
       
        
        self.bg_label = tk.Label(root, image=self.bg)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        
        
        self.button = tk.Entry(root)
        self.button.grid(column= 3, row = 4, pady= 90, padx= 70)
        
        
        
       
        
        
        
if __name__ == "__main__":
    root = tk.Tk()
    app = GroceryApp(root)
    root.mainloop()