import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage, ttk
from PIL import Image, ImageTk

class MarketMate():
    def __init__(self, root):
        self.root = root
        self.root.title("Grocery Store Inventory System")
        self.root.wm_attributes("-fullscreen", True)

        self.bg_image_path = "2.png"
        self.bg = PhotoImage(file=self.bg_image_path)

        self.bg_label = tk.Label(root, image=self.bg)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.log_in_text = tk.Label(root, text="  MARKETMATE  ", font=("Times", 80, "bold"), fg="white", bg="#000029")
        self.log_in_text.pack(pady=60)
        
        self.logo = Image.open("logo1.png")
        self.new_logo = ImageTk.PhotoImage(self.logo)
        
        self.image_label = tk.Label(root, image=self.new_logo, bg="blue3", width=160, height=160)
        self.image_label.pack(side="left", fill="none", expand=True)
        
        self.image_label = tk.Label(root, image=self.new_logo, bg="blue3", width=160, height=160)
        self.image_label.pack(side="right", fill="none", expand=True)
        
        self.login_text = tk.Label(root, text="   LOG IN   ", font=("Times", 50, "bold"), fg="white", bg="#000029")
        self.login_text.pack(pady=30)

        self.user_entry_var = tk.StringVar()
        self.password_entry_var = tk.StringVar()

        self.username_label = tk.Label(root, text=" Username ", font=("Roboto", 30), fg="white", bg="#000150")
        self.username_label.pack(pady=5)
        self.username_entry = tk.Entry(root, textvariable=self.user_entry_var, font=("Arial", 14), width=30, borderwidth=5)
        self.username_entry.pack(pady=5)

        self.password_label = tk.Label(root, text=" Password ", font=("Roboto", 30), fg="white", bg="#000150")
        self.password_label.pack(pady=5)
        self.password_entry = tk.Entry(root, textvariable=self.password_entry_var, font=("Arial", 14), width=30, borderwidth=5, show="*")
        self.password_entry.pack(pady=5)

        self.error_label = tk.Label(root, text="", font=("Arial", 14), fg="red", bg="blue3")
        self.error_label.pack(pady=10)

        self.sign_in_button = tk.Button(root, text="Sign In", font=("Roboto", 20), width=10, borderwidth=3, command=self.open_new_window)
        self.sign_in_button.pack(pady=5)

        self.sign_up_button = tk.Button(root, text="Sign Up", font=("Roboto", 20), width=10, borderwidth=3, command=self.sign_up)
        self.sign_up_button.pack(pady=5)
        
        self.back_image = PhotoImage(file="back_login.png")
        self.back_label = tk.Label(image=self.back_image)
        self.back_button = tk.Button(root, image=self.back_image, command=root.destroy)
        self.back_button.pack(pady=10)
    
    def sign_up(self):
        sign_up_window = tk.Toplevel(self.root)
        sign_up_window.title('SIGN UP')
        sign_up_window.wm_attributes("-fullscreen", True)

        bg_image_path = "1.png"
        sign_up_window.bg = PhotoImage(file=bg_image_path)
        bg_label = tk.Label(sign_up_window, image=sign_up_window.bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    def open_new_window(self):
        username = self.user_entry_var.get()
        password = self.password_entry_var.get()

        if not username or not password:
            self.error_label.config(text="Username and Password must be filled!", fg="red2")
        else:
            open_window = tk.Toplevel(self.root)
            open_window.title("IN, OUT, INVENTORY")
            open_window.wm_attributes("-fullscreen", True)

            bg_image_path = "1.png"
            open_window.bg = PhotoImage(file=bg_image_path)
            bg_label = tk.Label(open_window, image=open_window.bg)
            bg_label.place(x=0, y=0, relwidth=1, relheight=1)

            new_window_in = tk.Button(open_window, text="IN", font=("Times New Roman", 60, "bold"), bg="#00CED1", fg="White", command=self.window_in, width=15)
            new_window_in.pack(pady=70)

            new_window_inventory = tk.Button(open_window, text="INVENTORY", font=("Times New Roman", 60, "bold"), bg="#00CED1", fg="White", width=15, command=self.window_inventory)
            new_window_inventory.pack(pady=70)

            new_window_out = tk.Button(open_window, text="OUT", font=("Times New Roman", 60, "bold"), bg="#00CED1", fg="White", width=15, command=self.window_out)
            new_window_out.pack(pady=70)
            
    def window_in(self):
        open_window_in = tk.Toplevel(self.root)
        open_window_in.title("IN WINDOW")
        open_window_in.wm_attributes("-fullscreen", True)
        bg_image_path = "1.png"
        open_window_in.bg = PhotoImage(file=bg_image_path)
        bg_label = tk.Label(open_window_in, image=open_window_in.bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        open_window_in.resizable(True, True)

        new_window_in_label = tk.Label(open_window_in, text="IN", font=("Times New Roman", 40), width=10)
        new_window_in_label.pack()

        new_window_in_type = tk.Label(open_window_in, text="TYPE", font=("Times New Roman", 35))
        new_window_in_type.pack(pady=20)

        new_window_in_type_entry = tk.Entry(open_window_in, fg="Black", font=("Times New Roman", 30), width=15)
        new_window_in_type_entry.pack()

        new_window_in_quantity = tk.Label(open_window_in, text="QUANTITY", font=("Times New Roman", 35))
        new_window_in_quantity.pack(pady=20)

        new_window_in_quantity_entry = tk.Entry(open_window_in, fg="Black", font=("Times New Roman", 30), width=15)
        new_window_in_quantity_entry.pack()

        new_window_in_price = tk.Label(open_window_in, text="PRICE", font=("Times New Roman", 35))
        new_window_in_price.pack(pady=20)

        new_window_in_price_entry = tk.Entry(open_window_in, fg="Black", font=("Times New Roman", 30), width=15)
        new_window_in_price_entry.pack()

        new_window_in_name = tk.Label(open_window_in, text="NAME", font=("Times New Roman", 35))
        new_window_in_name.pack(pady=20)

        new_window_in_name_entry = tk.Entry(open_window_in, fg="Black", font=("Times New Roman", 30), width=15)
        new_window_in_name_entry.pack()

        new_window_in_barcode = tk.Label(open_window_in, text="BARCODE", font=("Times New Roman", 35))
        new_window_in_barcode.pack(pady=20)

        new_window_in_barcode_entry = tk.Entry(open_window_in, fg="Black", font=("Times New Roman", 30), width=15)
        new_window_in_barcode_entry.pack()

    def window_inventory(self):
        open_window_inventory = tk.Toplevel(self.root)
        open_window_inventory.title("INVENTORY WINDOW")
        open_window_inventory.wm_attributes("-fullscreen", True)
        bg = PhotoImage(file="2.png")  
        open_window_inventory.bg = PhotoImage(file=self.bg_image_path)
        bg_label = tk.Label(open_window_inventory, image=open_window_inventory.bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        open_window_inventory.resizable(True, True)

        # Inventory UI
        main_frame = tk.Frame(open_window_inventory)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Title
        title_label = tk.Label(main_frame, text="INVENTORY", bg='#add8e6', font=("Helvetica", 16, "bold"))
        title_label.pack(pady=10)

        # Search Bar Frame
        search_frame = tk.Frame(main_frame, bg='#add8e6')
        search_frame.pack(fill=tk.X, padx=20, pady=5)

        search_label = tk.Label(search_frame, text="Search", bg='#add8e6')
        search_label.pack(side=tk.LEFT)

        search_entry = tk.Entry(search_frame)
        search_entry.pack(side=tk.LEFT, padx=10)

        search_button = tk.Button(search_frame, text="🔍")
        search_button.pack(side=tk.LEFT)

        # Table Frame
        table_frame = tk.Frame(main_frame)
        table_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        columns = ("Name", "Barcode", "Price", "Type", "Quantity")
        tree = ttk.Treeview(table_frame, columns=columns, show="headings")

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=100)

        tree.pack(fill=tk.BOTH, expand=True)

    def window_out(self):
        open_window_out = tk.Toplevel(self.root)
        open_window_out.title("OUT WINDOW")
        open_window_out.wm_attributes("-fullscreen", True)
        bg_image_path = "1.png"
        open_window_out.bg = PhotoImage(file=bg_image_path)
        bg_label = tk.Label(open_window_out, image=open_window_out.bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        new_window_out_button = tk.Button(open_window_out, text="kaya mo na to A-ARON", bg="#00CED1", width=15)
        new_window_out_button.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = MarketMate(root)
    root.mainloop()