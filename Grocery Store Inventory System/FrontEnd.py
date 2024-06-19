import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class MarketMate:
    def __init__(self, root):
        self.root = root
        self.root.title("Grocery Store Inventory System")
        self.root.attributes('-fullscreen', True)
        self.root.resizable(True, True)

        # Background color instead of image
        self.root.configure(bg="#000029")

        # Exit Button on the top left
        self.exit_button = tk.Button(root, text="Exit", font=("Roboto", 20), command=root.destroy, bg="red", fg="white")
        self.exit_button.pack(anchor="nw", side="top", pady=10, padx=10)

        # Title Label
        self.log_in_text = tk.Label(root, text="  MARKETMATE  ", font=("Times", 80, "bold"), fg="white", bg="#000029")
        self.log_in_text.pack(pady=60)

        # Placeholder for logo (just a label with text)
        self.image_label_left = tk.Label(root, text="LOGO", bg="blue3", width=20, height=10, font=("Arial", 20, "bold"), fg="white")
        self.image_label_left.pack(side="left", fill="none", expand=True)
        
        self.image_label_right = tk.Label(root, text="LOGO", bg="blue3", width=20, height=10, font=("Arial", 20, "bold"), fg="white")
        self.image_label_right.pack(side="right", fill="none", expand=True)

        # Login Text
        self.login_text = tk.Label(root, text="   LOG IN   ", font=("Times", 50, "bold"), fg="white", bg="#000029")
        self.login_text.pack(pady=30)

        # Username Entry
        self.user_entry_var = tk.StringVar()
        self.username_label = tk.Label(root, text=" Username ", font=("Roboto", 30), fg="white", bg="#000150")
        self.username_label.pack(pady=5)
        self.username_entry = tk.Entry(root, textvariable=self.user_entry_var, font=("Arial", 14), width=30, borderwidth=5)
        self.username_entry.pack(pady=5)

        # Password Entry
        self.password_entry_var = tk.StringVar()
        self.password_label = tk.Label(root, text=" Password ", font=("Roboto", 30), fg="white", bg="#000150")
        self.password_label.pack(pady=5)
        self.password_entry = tk.Entry(root, textvariable=self.password_entry_var, font=("Arial", 14), width=30, borderwidth=5, show="*")
        self.password_entry.pack(pady=5)

        # Error Label
        self.error_label = tk.Label(root, text="", font=("Arial", 14), fg="red", bg="#000029")
        self.error_label.pack(pady=10)

        # Button Frame to hold Sign In and Sign Up buttons
        button_frame = tk.Frame(root, bg="#000029")
        button_frame.pack(pady=10)

        # Sign In Button
        self.sign_in_button = tk.Button(button_frame, text="Sign In", font=("Roboto", 20), width=10, borderwidth=3, command=self.sign_in)
        self.sign_in_button.pack(side="left", padx=10)

        # Sign Up Button
        self.sign_up_button = tk.Button(button_frame, text="Sign Up", font=("Roboto", 20), width=10, borderwidth=3, command=self.sign_up)
        self.sign_up_button.pack(side="left", padx=10)
        
        # Back Button (simple text button)
        self.back_button = tk.Button(root, text="Back", font=("Roboto", 20), command=root.destroy)
        self.back_button.pack(pady=10)

        # Inventory list to hold items
        self.inventory_items = []
        
        # Dictionary to hold users
        self.users = {}

    def sign_up(self):
        sign_up_window = tk.Toplevel(self.root)
        sign_up_window.title('SIGN UP')
        sign_up_window.attributes('-fullscreen', True)
        sign_up_window.resizable(True, True)

        # Background color instead of image
        sign_up_window.configure(bg="#ffffff")

        # Sign Up Form
        sign_up_label = tk.Label(sign_up_window, text="Sign Up", font=("Arial", 30), bg="#ffffff")
        sign_up_label.pack(pady=20)

        sign_up_username_label = tk.Label(sign_up_window, text="Username", font=("Arial", 20), bg="#ffffff")
        sign_up_username_label.pack(pady=5)
        self.sign_up_username_entry = tk.Entry(sign_up_window, font=("Arial", 14), width=30, borderwidth=5)
        self.sign_up_username_entry.pack(pady=5)

        sign_up_password_label = tk.Label(sign_up_window, text="Password", font=("Arial", 20), bg="#ffffff")
        sign_up_password_label.pack(pady=5)
        self.sign_up_password_entry = tk.Entry(sign_up_window, font=("Arial", 14), width=30, borderwidth=5, show="*")
        self.sign_up_password_entry.pack(pady=5)

        sign_up_button = tk.Button(sign_up_window, text="Sign Up", font=("Arial", 20), command=self.save_user)
        sign_up_button.pack(pady=20)

        # Back Button
        back_button = tk.Button(sign_up_window, text="Back", font=("Arial", 20), command=sign_up_window.destroy)
        back_button.pack(pady=10)

    def save_user(self):
        username = self.sign_up_username_entry.get()
        password = self.sign_up_password_entry.get()
        if username and password:
            self.users[username] = password
            messagebox.showinfo("Success", "User signed up successfully!")
        else:
            messagebox.showerror("Error", "Username and password cannot be empty!")

    def sign_in(self):
        username = self.user_entry_var.get()
        password = self.password_entry_var.get()
        if username in self.users and self.users[username] == password:
            self.open_main_window()
        else:
            self.error_label.config(text="Invalid username or password!")

    def open_main_window(self):
        open_window = tk.Toplevel(self.root)
        open_window.title("IN, OUT, INVENTORY")
        open_window.attributes('-fullscreen', True)
        open_window.resizable(True, True)

        # Background color instead of image
        open_window.configure(bg="#ffffff")
        
        new_window_back = tk.Button(open_window, text="<- BACK", font=("Roman", 20, "bold"), bg="#00CED1", fg="White", command=open_window.destroy, width=12)
        new_window_back.pack(anchor="w")

        new_window_in = tk.Button(open_window, text="   I N   ", font=("Times New Roman", 40, "bold"), bg="#00CED1", fg="White", command=self.window_in, width=12, height=2)
        new_window_in.pack(pady=50)
        
        new_window_sales = tk.Button(open_window, text="WEEKLY\n SALES", font=("Times New Roman", 30, "bold"), bg="#00CED1", fg="White", width=12, height=5, command=self.weekly_sales)
        new_window_sales.pack(side="left", pady=70, expand=True)
        
        new_window_sales = tk.Button(open_window, text="MONTHLY\n SALES", font=("Times New Roman", 30, "bold"), bg="#00CED1", fg="White", width=12, height=5, command=self.monthly_sales)
        new_window_sales.pack(side="right", pady=70, expand=True)

        new_window_inventory = tk.Button(open_window, text="INVENTORY", font=("Times New Roman", 40, "bold"), bg="#00CED1", fg="White", width=12, height=2, command=self.window_inventory)
        new_window_inventory.pack(pady=50)

        new_window_out = tk.Button(open_window, text="   OUT   ", font=("Times New Roman", 40, "bold"), bg="#00CED1", fg="White", width=12, height=2, command=self.window_out)
        new_window_out.pack(pady=50)

    def weekly_sales(self):
        pass

    def monthly_sales(self):
        pass

    def window_in(self):
        self.in_window = tk.Toplevel(self.root)
        self.in_window.title("IN WINDOW")
        self.in_window.attributes('-fullscreen', True)
        self.in_window.resizable(True, True)

        # Background color instead of image
        self.in_window.configure(bg="#ffffff")

        new_window_in_label = tk.Label(self.in_window, text="  I  N  ", font=("Times New Roman", 50, "bold"), width=20)
        new_window_in_label.pack(pady=30, side="top")

        new_window_in_type = tk.Label(self.in_window, text="TYPE", font=("Times New Roman", 35))
        new_window_in_type.pack(side="top", padx=5)

        self.new_window_in_type_entry = tk.Entry(self.in_window, fg="Black", font=("Times New Roman", 30), width=15)
        self.new_window_in_type_entry.pack(side="top", padx=5)

        new_window_in_quantity = tk.Label(self.in_window, text="QUANTITY", font=("Times New Roman", 35))
        new_window_in_quantity.pack(side="top")

        self.new_window_in_quantity_entry = tk.Entry(self.in_window, fg="Black", font=("Times New Roman", 30), width=15)
        self.new_window_in_quantity_entry.pack(side="top")

        new_window_in_price = tk.Label(self.in_window, text="PRICE", font=("Times New Roman", 35))
        new_window_in_price.pack(side="top")

        self.new_window_in_price_entry = tk.Entry(self.in_window, fg="Black", font=("Times New Roman", 30), width=15)
        self.new_window_in_price_entry.pack(side="top")

        new_window_in_name = tk.Label(self.in_window, text="NAME", font=("Times New Roman", 35))
        new_window_in_name.pack(side="top")

        self.new_window_in_name_entry = tk.Entry(self.in_window, fg="Black", font=("Times New Roman", 30), width=15)
        self.new_window_in_name_entry.pack(side="top")

        new_window_in_barcode = tk.Label(self.in_window, text="BARCODE", font=("Times New Roman", 35))
        new_window_in_barcode.pack(side="top")

        self.new_window_in_barcode_entry = tk.Entry(self.in_window, fg="Black", font=("Times New Roman", 30), width=15)
        self.new_window_in_barcode_entry.pack(side="top")
        
        new_window_in_done = tk.Button(self.in_window, text="DONE", font=("Times New Roman", 35), command=self.save_to_inventory)
        new_window_in_done.pack(side="left", expand=True)
        
        new_window_in_exit = tk.Button(self.in_window, text="EXIT", font=("Times New Roman", 35), command=self.in_window.destroy)
        new_window_in_exit.pack(side="right", expand=True)

    def save_to_inventory(self):
        item = {
            "Name": self.new_window_in_name_entry.get(),
            "Barcode": self.new_window_in_barcode_entry.get(),
            "Price": self.new_window_in_price_entry.get(),
            "Type": self.new_window_in_type_entry.get(),
            "Quantity": self.new_window_in_quantity_entry.get()
        }
        self.inventory_items.append(item)
        self.in_window.destroy()

    def window_inventory(self):
        self.inventory_window = tk.Toplevel(self.root)
        self.inventory_window.title("INVENTORY WINDOW")
        self.inventory_window.attributes('-fullscreen', True)
        self.inventory_window.configure(bg="#ffffff")
        self.inventory_window.resizable(True, True)

        # Inventory UI
        main_frame = tk.Frame(self.inventory_window)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Title
        title_label = tk.Label(main_frame, text="INVENTORY", bg='#add8e6', font=("Helvetica", 16, "bold"))
        title_label.pack(pady=10)

        # Back Button
        back_button = tk.Button(main_frame, text="Back", font=("Arial", 14), command=self.inventory_window.destroy)
        back_button.pack(pady=10)

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
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings")

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        self.tree.pack(fill=tk.BOTH, expand=True)

        # Load existing inventory items
        self.load_inventory_items()

    def load_inventory_items(self):
        for item in self.inventory_items:
            self.tree.insert("", "end", values=(item["Name"], item["Barcode"], item["Price"], item["Type"], item["Quantity"]))

    def window_out(self):
        open_window_out = tk.Toplevel(self.root)
        open_window_out.title("OUT WINDOW")
        open_window_out.attributes('-fullscreen', True)
        open_window_out.resizable(True, True)

        # Back Button
        back_button = tk.Button(open_window_out, text="Back", font=("Arial", 20), command=open_window_out.destroy)
        back_button.pack(pady=10)

        # Title Label
        title_label = tk.Label(open_window_out, text="OUT", font=("Times New Roman", 50, "bold"))
        title_label.pack(pady=30)

        # Table Frame
        table_frame = tk.Frame(open_window_out)
        table_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        columns = ("Name", "Barcode", "Price", "Type", "Quantity")
        self.tree_out = ttk.Treeview(table_frame, columns=columns, show="headings")

        for col in columns:
            self.tree_out.heading(col, text=col)
            self.tree_out.column(col, width=100)

        self.tree_out.pack(fill=tk.BOTH, expand=True)

        # Load existing inventory items into the out window
        self.load_inventory_items_out()

        # Check Out Button
        check_out_button = tk.Button(open_window_out, text="Check Out", font=("Arial", 20), command=self.check_out)
        check_out_button.pack(pady=10)

    def load_inventory_items_out(self):
        for item in self.inventory_items:
            self.tree_out.insert("", "end", values=(item["Name"], item["Barcode"], item["Price"], item["Type"], item["Quantity"]))

    def check_out(self):
        check_out_window = tk.Toplevel(self.root)
        check_out_window.title("Check Out")
        check_out_window.geometry("400x200")

        # Check Out Message
        check_out_message = tk.Label(check_out_window, text="The Item's are checked", font=("Arial", 20))
        check_out_message.pack(pady=30)

        # OK Button to close the check out window and clear inventory
        ok_button = tk.Button(check_out_window, text="OK", font=("Arial", 20), command=lambda: self.clear_inventory(check_out_window))
        ok_button.pack(pady=10)

    def clear_inventory(self, window):
        self.inventory_items.clear()
        for i in self.tree.get_children():
            self.tree.delete(i)
        for i in self.tree_out.get_children():
            self.tree_out.delete(i)
        window.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = MarketMate(root)
    root.mainloop()
