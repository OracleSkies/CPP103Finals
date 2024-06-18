import tkinter as tk
from PIL import ImageTk, Image

class WindowBackground(tk.Tk):
    def __init__(self, screenName=None, baseName=None, className="Tk", useTk=True, sync=False, use=None):
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.title("Window Background")
        self.geometry("1800x600")

        # Load and display background image
        self.background_image = ImageTk.PhotoImage(Image.open("dashboard.png"))
        self.bg_image_label = tk.Label(self, image=self.background_image)
        self.bg_image_label.pack()

class texts:
    def __init__(self, root):
        self.root = root

    def clear_screen(self):
        # Clear all widgets from the screen
        for widget in self.root.winfo_children():
            widget.destroy()

    def home(self):
        # Method to go back to home interface
        self.clear_screen()
        self.create_home_interface()

    def create_home_interface(self):
        # Create the home interface with a "Home" button
        self.home_button = tk.Button(self.root, text="Home", command=self.home)
        self.home_button.pack(pady=20)

    def Text(self):
        # Method to create text-related widgets
        self.text_button = tk.Button(self.root, text="waiting for result", fg="red")
        self.text_button.pack(pady=10)

        entry = tk.Entry(self.root, fg="black", font="Arial 20")
        entry.pack(pady=10)

        # Command to change text of text_button
        change_text_button = tk.Button(self.root, text="pindot", font="Arial 16", command=lambda: self.text_button.config(text="HOME"))
        change_text_button.pack(pady=10)

        # Add additional buttons
        button1 = tk.Button(self.root, text="Button 1", fg="blue", font="Arial 16")
        button1.pack(pady=10)

        button2 = tk.Button(self.root, text="Button 2", fg="green", font="Arial 16")
        button2.pack(pady=10)

        button3 = tk.Button(self.root, text="Button 3", fg="orange", font="Arial 16")
        button3.pack(pady=10)

if __name__ == "__main__":
    root = WindowBackground()
    my_texts = texts(root)
    my_texts.Text()
    root.mainloop()