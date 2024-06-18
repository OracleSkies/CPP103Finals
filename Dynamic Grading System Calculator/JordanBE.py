import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from PIL import ImageTk, Image

class WindowBackground(tk.Tk):
    def __init__(self, screenName: str | None = None, baseName: str | None = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.title("Window Background")
        self.geometry("1980x1080")

        self.background_Image = ImageTk.PhotoImage(Image.open("window background.png"))
        self.bg_Image_Label = tk.Label(self, image=self.background_Image)
        self.bg_Image_Label.pack()


"""class texts:
    def __init__(self,root):
        self.root = root
    
    def Text(self):
       
        home = ttk.Button.pack_forget()
                
      
        entry = tk.Label(root, text = home,font = ("Signataria,20,Italic"),command = home )"""

if __name__ == "__main__":
    window = WindowBackground()
    window.mainloop()
