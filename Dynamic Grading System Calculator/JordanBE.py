import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage

class WindowBackground:
    def __init__(self, root):
        self.root = root
        self.root.title("Window Background")
        self.root.geometry("1000x800")

        bg_image_path = "window_background.png"
        self.open_window = PhotoImage(file="window background.png")
        
        self.bg_label = ttk.Label(self.root, image=self.open_window)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

class texts:
    def __init__(self,root):
        self.root = root
    
    def Text(self):
       
        home = ttk.Button.pack_forget()
                
      
        entry = tk.Label(root, text = home,font = ("Signataria,20,Italic"),command = home )





























if __name__ == "__main__":
    root = tk.Tk()
    app = WindowBackground(root)
    root.mainloop()
