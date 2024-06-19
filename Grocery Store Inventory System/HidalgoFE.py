import tkinter as tk
from tkinter import PhotoImage, ttk, messagebox
import sqlite3
from TuasonBE import DatabaseManagement,InventoryManagement


class GroceryApp(DatabaseManagement):

    def __init__(self, root):
        super().__init__()
        self.root = root
        self.root.title("Grocery Store Inventory System")
        self.root.geometry("1000x800")

        self.bg_image_path = "main.png"
        self.bg = PhotoImage(file=self.bg_image_path)

        self.bg_label = tk.Label(root, image=self.bg)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.log_in_text = tk.Label(root, text="Log In", font=("Times", 70, "bold"), fg="white", bg="#000029")
        self.log_in_text.pack(pady=80)

        self.user_entry_var = tk.StringVar()
        self.password_entry_var = tk.StringVar()

        self.username_label = tk.Label(root, text="Username", font=("Roboto", 20), fg="white", bg="#000150")
        self.username_label.pack(pady=20)
        self.username_entry = tk.Entry(root, textvariable=self.user_entry_var, font=("Arial", 14), width=30, borderwidth=5)
        self.username_entry.pack(pady=10)

        self.password_label = tk.Label(root, text="Password", font=("Roboto", 20), fg="white", bg="#000150")
        self.password_label.pack(pady=20)
        self.password_entry = tk.Entry(root, textvariable=self.password_entry_var, font=("Arial", 14), width=30, borderwidth=5, show="*")
        self.password_entry.pack(pady=10)

        self.error_label = tk.Label(root, text="", font=("Arial", 14), fg="red", bg="#000029")
        self.error_label.pack()

        self.sign_in_button = tk.Button(root, text="Sign In", font=("Roboto", 16), borderwidth=3, command=self.open_new_window)
        self.sign_in_button.pack(pady=40)

        self.sign_up_button = tk.Button(root, text="Sign Up", font=("Roboto", 16), borderwidth=3, command=self.sign_up)
        self.sign_up_button.pack(pady=20)


    def sign_up(self):
        sign_up_window = tk.Toplevel(self.root)
        sign_up_window.title('SIGN UP')
        sign_up_window.geometry('1000x800')
        sign_up_window.resizable(True, True)

        bg_image_path = "main.png"
        sign_up_window.bg = PhotoImage(file=bg_image_path)
        bg_label = tk.Label(sign_up_window, image=sign_up_window.bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        
        
    def open_new_window(self):
        username = self.user_entry_var.get()
        password = self.password_entry_var.get()

        if not username or not password:
            self.error_label.config(text="Username and Password must be filled!", fg="red")
        else:
            open_window = tk.Toplevel(self.root)
            open_window.title("IN, OUT, INVENTORY")
            open_window.geometry("1000x800")
            open_window.resizable(True, True)

            bg_image_path = "main.png"
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
        self.open_window_in = tk.Toplevel(self.root)
        self.open_window_in.title("IN WINDOW")
        self.open_window_in.geometry("1000x800")
        self.bg_image_path = "main.png"
        self.open_window_in.bg = PhotoImage(file=self.bg_image_path)
        self.bg_label = tk.Label(self.open_window_in, image=self.open_window_in.bg)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.open_window_in.resizable(True, True)

        self.new_window_in_label = tk.Label(self.open_window_in, text="IN", font=("Times New Roman", 40), width=10)
        self.new_window_in_label.pack()

        self.new_window_in_type = tk.Label(self.open_window_in, text="TYPE", font=("Times New Roman", 35))
        self.new_window_in_type.pack(pady=20)

        self.new_window_in_type_entry = tk.Entry(self.open_window_in, fg="Black", font=("Times New Roman", 30), width=15)
        self.new_window_in_type_entry.pack()

        self.new_window_in_quantity = tk.Label(self.open_window_in, text="QUANTITY", font=("Times New Roman", 35))
        self.new_window_in_quantity.pack(pady=20)

        self.new_window_in_quantity_entry = tk.Entry(self.open_window_in, fg="Black", font=("Times New Roman", 30), width=15)
        self.new_window_in_quantity_entry.pack()

        self.new_window_in_price = tk.Label(self.open_window_in, text="PRICE", font=("Times New Roman", 35))
        self.new_window_in_price.pack(pady=20)

        self.new_window_in_price_entry = tk.Entry(self.open_window_in, fg="Black", font=("Times New Roman", 30), width=15)
        self.new_window_in_price_entry.pack()

        self.new_window_in_name = tk.Label(self.open_window_in, text="NAME", font=("Times New Roman", 35))
        self.new_window_in_name.pack(pady=20)

        self.new_window_in_name_entry = tk.Entry(self.open_window_in, fg="Black", font=("Times New Roman", 30), width=15)
        self.new_window_in_name_entry.pack()

        self.new_window_in_barcode = tk.Label(self.open_window_in, text="BARCODE", font=("Times New Roman", 35))
        self.new_window_in_barcode.pack(pady=20)

        self.new_window_in_barcode_entry = tk.Entry(self.open_window_in, fg="Black", font=("Times New Roman", 30), width=15)
        self.new_window_in_barcode_entry.pack()

        self.confirm_button = tk.Button(self.open_window_in, text="Confirm", font=("Times New Roman", 30), command = self.confirm_inventory_in,width=15)
        self.confirm_button.pack(pady=20)

    def window_inventory(self):
        self.open_window_invetory = tk.Toplevel(self.root)
        self.open_window_invetory.title("OUT WINDOW")
        self.open_window_invetory.geometry("1000x800")
        bg_image_path = "main.png"
        self.open_window_invetory.bg = PhotoImage(file=bg_image_path)
        bg_label = tk.Label(self.open_window_invetory, image=self.open_window_invetory.bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.open_window_invetory.resizable(True, True)

        
        main_frame = tk.Frame(self.open_window_invetory)
        main_frame.pack(fill=tk.BOTH, expand=True)

        
        title_label = tk.Label(main_frame, text="INVENTORY", bg='#add8e6', font=("Helvetica", 16, "bold"))
        title_label.pack(pady=10)

        
        search_frame = tk.Frame(main_frame, bg='#add8e6')
        search_frame.pack(fill=tk.X, padx=20, pady=5)

        search_label = tk.Label(search_frame, text="Search", bg='#add8e6')
        search_label.pack(side=tk.LEFT)

        search_entry = tk.Entry(search_frame)
        search_entry.pack(side=tk.LEFT, padx=10)

        search_button = tk.Button(search_frame, text="🔍")
        search_button.pack(side=tk.LEFT)

        
        table_frame = tk.Frame(main_frame)
        table_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        columns = ("Name", "Barcode", "Price", "Type", "Quantity")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings")

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        self.tree.pack(fill=tk.BOTH, expand=True)
        self.sync_database()

    def sync_database(self):
        self.tree.delete(*self.tree.get_children())
        self.cursor.execute("SELECT * FROM ITEMS")
        rows = self.cursor.fetchall()
        for row in rows:
            self.tree.insert("", tk.END, values=row)

    def window_out(self):
        open_window_out = tk.Toplevel(self.root)
        open_window_out.title("OUT WINDOW")
        open_window_out.geometry("1000x800")
        bg_image_path = "main.png"
        open_window_out.bg = PhotoImage(file=bg_image_path)
        bg_label = tk.Label(open_window_out, image=open_window_out.bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        open_window_out.resizable(True, True)

        
        search_label = tk.Label(open_window_out, text="SEARCH", font=("Arial", 14), fg="white", bg="light blue")
        search_label.pack(pady=20)

        search_entry = tk.Entry(open_window_out, font=("Arial", 14), width=30, borderwidth=5)
        search_entry.pack(pady=10)

        table_frame = tk.Frame(open_window_out, bg="#000029")
        table_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        
        headers = ["NAME", "BARCODE", "TYPE", "PRICE", "QUANTITY"]
        for i, header in enumerate(headers):
            label = tk.Label(table_frame, text=header, font=("Arial", 12), fg="white", bg="#000029", width=15, anchor="center")
            label.grid(row=0, column=i, padx=10, pady=10)

       
       

        
        back_button = tk.Button(open_window_out, text="BACK", font=("Roboto", 16), borderwidth=3, bg="#00CED1", fg="White", width=10 )
        back_button.pack(side=tk.LEFT, padx=20, pady=20)

        confirm_button = tk.Button(open_window_out, text="CONFIRM", font=("Roboto", 16), borderwidth=3, bg="#00CED1", fg="White", width=10)
        confirm_button.pack(side=tk.RIGHT, padx=20, pady=20)
    
    def insert_inventory(self):
        sql_command = "INSERT INTO ITEMS (barcode, brand_name, item_type, item_quantity, item_price) VALUES (?, ?, ?, ?, ?)"
        values = (self.barcode, self.brand_name, self.item_type, self.item_quantity, self.item_price)
        self.cursor.execute(sql_command, values)
        self.connection.commit()

    def confirm_inventory_in(self):
        dataManagement = InventoryManagement(self.new_window_in_barcode_entry.get(), self.new_window_in_name_entry.get(), self.new_window_in_type_entry.get(),self.new_window_in_quantity_entry.get(), self.new_window_in_price_entry.get())
        dataManagement.insert_inventory()
        messagebox.showinfo("Inventory In", "Item added to invetory")
        self.open_window_in.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = GroceryApp(root)
    root.mainloop()