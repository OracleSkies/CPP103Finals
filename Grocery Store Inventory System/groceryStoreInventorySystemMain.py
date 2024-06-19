import tkinter as tk
from tkinter import ttk
from FrontEnd import MarketMate


if __name__ == "__main__":
    root = tk.Tk()
    app = MarketMate(root)
    root.mainloop()