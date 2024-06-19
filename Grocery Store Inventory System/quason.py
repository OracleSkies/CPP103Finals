import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime, timedelta

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

        self.main_frame = tk.Frame(root, bg="#000029")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.create_login_screen()

        # Inventory list to hold items
        self.inventory_items = []

        # Sales records
        self.sales_records = []

        # Dictionary to hold users
        self.users = {}

    def create_login_screen(self):
        self.clear_screen()

        # Title Label
        self.log_in_text = tk.Label(self.main_frame, text="  MARKETMATE  ", font=("Times", 80, "bold"), fg="white", bg="#000029")
        self.log_in_text.pack(pady=60)

        # Placeholder for logo (just a label with text)
        self.image_label_left = tk.Label(self.main_frame, text="LOGO", bg="blue3", width=20, height=10, font=("Arial", 20, "bold"), fg="white")
        self.image_label_left.pack(side="left", fill="none", expand=True)

        self.image_label_right = tk.Label(self.main_frame, text="LOGO", bg="blue3", width=20, height=10, font=("Arial", 20, "bold"), fg="white")
        self.image_label_right.pack(side="right", fill="none", expand=True)

        # Login Text
        self.login_text = tk.Label(self.main_frame, text="   LOG IN   ", font=("Times", 50, "bold"), fg="white", bg="#000029")
        self.login_text.pack(pady=30)

        # Username Entry
        self.user_entry_var = tk.StringVar()
        self.username_label = tk.Label(self.main_frame, text=" Username ", font=("Roboto", 30), fg="white", bg="#000150")
        self.username_label.pack(pady=5)
        self.username_entry = tk.Entry(self.main_frame, textvariable=self.user_entry_var, font=("Arial", 14), width=30, borderwidth=5)
        self.username_entry.pack(pady=5)

        # Password Entry
        self.password_entry_var = tk.StringVar()
        self.password_label = tk.Label(self.main_frame, text=" Password ", font=("Roboto", 30), fg="white", bg="#000150")
        self.password_label.pack(pady=5)
        self.password_entry = tk.Entry(self.main_frame, textvariable=self.password_entry_var, font=("Arial", 14), width=30, borderwidth=5, show="*")
        self.password_entry.pack(pady=5)

        # Error Label
        self.error_label = tk.Label(self.main_frame, text="", font=("Arial", 14), fg="red", bg="#000029")
        self.error_label.pack(pady=10)

        # Button Frame to hold Sign In and Sign Up buttons
        button_frame = tk.Frame(self.main_frame, bg="#000029")
        button_frame.pack(pady=10)

        # Sign In Button
        self.sign_in_button = tk.Button(button_frame, text="Sign In", font=("Roboto", 20), width=10, borderwidth=3, command=self.sign_in)
        self.sign_in_button.pack(side="left", padx=10)

        # Sign Up Button
        self.sign_up_button = tk.Button(button_frame, text="Sign Up", font=("Roboto", 20), width=10, borderwidth=3, command=self.create_sign_up_screen)
        self.sign_up_button.pack(side="left", padx=10)

    def create_sign_up_screen(self):
        self.clear_screen()

        sign_up_label = tk.Label(self.main_frame, text="Sign Up", font=("Arial", 30), bg="#ffffff")
        sign_up_label.pack(pady=20)

        sign_up_username_label = tk.Label(self.main_frame, text="Username", font=("Arial", 20), bg="#ffffff")
        sign_up_username_label.pack(pady=5)
        self.sign_up_username_entry = tk.Entry(self.main_frame, font=("Arial", 14), width=30, borderwidth=5)
        self.sign_up_username_entry.pack(pady=5)

        sign_up_password_label = tk.Label(self.main_frame, text="Password", font=("Arial", 20), bg="#ffffff")
        sign_up_password_label.pack(pady=5)
        self.sign_up_password_entry = tk.Entry(self.main_frame, font=("Arial", 14), width=30, borderwidth=5, show="*")
        self.sign_up_password_entry.pack(pady=5)

        sign_up_button = tk.Button(self.main_frame, text="Sign Up", font=("Arial", 20), command=self.save_user)
        sign_up_button.pack(pady=20)

        # Back Button
        back_button = tk.Button(self.main_frame, text="Back", font=("Arial", 20), command=self.create_login_screen)
        back_button.pack(pady=10)

    def save_user(self):
        username = self.sign_up_username_entry.get()
        password = self.sign_up_password_entry.get()
        if username and password:
            self.users[username] = password
            messagebox.showinfo("Success", "User signed up successfully!")
            self.create_login_screen()
        else:
            messagebox.showerror("Error", "Username and password cannot be empty!")

    def sign_in(self):
        username = self.user_entry_var.get()
        password = self.password_entry_var.get()
        if username in self.users and self.users[username] == password:
            self.create_main_menu()
        else:
            self.error_label.config(text="Invalid username or password!")

    def create_main_menu(self):
        self.clear_screen()

        new_window_back = tk.Button(self.main_frame, text="<- BACK", font=("Roman", 20, "bold"), bg="#00CED1", fg="White", command=self.create_login_screen, width=12)
        new_window_back.pack(anchor="w")

        new_window_in = tk.Button(self.main_frame, text="   I N   ", font=("Times New Roman", 40, "bold"), bg="#00CED1", fg="White", command=self.create_in_window, width=12, height=2)
        new_window_in.pack(pady=50)

        new_window_sales = tk.Button(self.main_frame, text="WEEKLY\n SALES", font=("Times New Roman", 30, "bold"), bg="#00CED1", fg="White", width=12, height=5, command=self.create_weekly_sales_window)
        new_window_sales.pack(side="left", pady=70, expand=True)

        new_window_sales = tk.Button(self.main_frame, text="MONTHLY\n SALES", font=("Times New Roman", 30, "bold"), bg="#00CED1", fg="White", width=12, height=5, command=self.create_monthly_sales_window)
        new_window_sales.pack(side="right", pady=70, expand=True)

        new_window_inventory = tk.Button(self.main_frame, text="INVENTORY", font=("Times New Roman", 40, "bold"), bg="#00CED1", fg="White", width=12, height=2, command=self.create_inventory_window)
        new_window_inventory.pack(pady=50)

        new_window_out = tk.Button(self.main_frame, text="   OUT   ", font=("Times New Roman", 40, "bold"), bg="#00CED1", fg="White", width=12, height=2, command=self.create_out_window)
        new_window_out.pack(pady=50)

    def create_weekly_sales_window(self):
        self.clear_screen()

        # Title
        title_label = tk.Label(self.main_frame, text="Weekly Sales", font=("Times New Roman", 40, "bold"))
        title_label.pack(pady=30)

        # Table Frame
        table_frame = tk.Frame(self.main_frame)
        table_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        columns = ("Name", "Barcode", "Price", "Type", "Quantity", "Date")
        self.weekly_sales_tree = ttk.Treeview(table_frame, columns=columns, show="headings")

        for col in columns:
            self.weekly_sales_tree.heading(col, text=col)
            self.weekly_sales_tree.column(col, width=100)

        self.weekly_sales_tree.pack(fill=tk.BOTH, expand=True)

        # Back Button
        back_button = tk.Button(self.main_frame, text="Back", font=("Arial", 20), command=self.create_main_menu)
        back_button.pack(pady=10)

        self.load_weekly_sales()

    def load_weekly_sales(self):
        one_week_ago = datetime.now() - timedelta(days=7)
        for record in self.sales_records:
            sale_date = datetime.strptime(record["Date"], "%Y-%m-%d %H:%M:%S")
            if sale_date >= one_week_ago:
                self.weekly_sales_tree.insert("", "end", values=(record["Name"], record["Barcode"], record["Price"], record["Type"], record["Quantity"], record["Date"]))

    def create_monthly_sales_window(self):
        self.clear_screen()

        # Title
        title_label = tk.Label(self.main_frame, text="Monthly Sales", font=("Times New Roman", 40, "bold"))
        title_label.pack(pady=30)

        # Table Frame
        table_frame = tk.Frame(self.main_frame)
        table_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        columns = ("Name", "Barcode", "Price", "Type", "Quantity", "Date")
        self.monthly_sales_tree = ttk.Treeview(table_frame, columns=columns, show="headings")

        for col in columns:
            self.monthly_sales_tree.heading(col, text=col)
            self.monthly_sales_tree.column(col, width=100)

        self.monthly_sales_tree.pack(fill=tk.BOTH, expand=True)

        # Back Button
        back_button = tk.Button(self.main_frame, text="Back", font=("Arial", 20), command=self.create_main_menu)
        back_button.pack(pady=10)

        self.load_monthly_sales()

    def load_monthly_sales(self):
        one_month_ago = datetime.now() - timedelta(days=30)
        for record in self.sales_records:
            sale_date = datetime.strptime(record["Date"], "%Y-%m-%d %H:%M:%S")
            if sale_date >= one_month_ago:
                self.monthly_sales_tree.insert("", "end", values=(record["Name"], record["Barcode"], record["Price"], record["Type"], record["Quantity"], record["Date"]))

    def create_in_window(self):
        self.clear_screen()

        new_window_in_text = tk.Label(self.main_frame, text="I N", font=("Times New Roman", 80, "bold"))
        new_window_in_text.pack(pady=50)

        new_window_in_type = tk.Label(self.main_frame, text="TYPE", font=("Times New Roman", 35))
        new_window_in_type.pack(side="top")

        self.new_window_in_type_entry = tk.Entry(self.main_frame, fg="Black", font=("Times New Roman", 30), width=15)
        self.new_window_in_type_entry.pack(side="top")

        new_window_in_quantity = tk.Label(self.main_frame, text="QUANTITY", font=("Times New Roman", 35))
        new_window_in_quantity.pack(side="top")

        self.new_window_in_quantity_entry = tk.Entry(self.main_frame, fg="Black", font=("Times New Roman", 30), width=15)
        self.new_window_in_quantity_entry.pack(side="top")

        new_window_in_price = tk.Label(self.main_frame, text="PRICE", font=("Times New Roman", 35))
        new_window_in_price.pack(side="top")

        self.new_window_in_price_entry = tk.Entry(self.main_frame, fg="Black", font=("Times New Roman", 30), width=15)
        self.new_window_in_price_entry.pack(side="top")

        new_window_in_name = tk.Label(self.main_frame, text="NAME", font=("Times New Roman", 35))
        new_window_in_name.pack(side="top")

        self.new_window_in_name_entry = tk.Entry(self.main_frame, fg="Black", font=("Times New Roman", 30), width=15)
        self.new_window_in_name_entry.pack(side="top")

        new_window_in_barcode = tk.Label(self.main_frame, text="BARCODE", font=("Times New Roman", 35))
        new_window_in_barcode.pack(side="top")

        self.new_window_in_barcode_entry = tk.Entry(self.main_frame, fg="Black", font=("Times New Roman", 30), width=15)
        self.new_window_in_barcode_entry.pack(side="top")

        new_window_in_done = tk.Button(self.main_frame, text="DONE", font=("Times New Roman", 35), command=self.save_to_inventory)
        new_window_in_done.pack(side="left", expand=True)

        new_window_in_exit = tk.Button(self.main_frame, text="BACK", font=("Times New Roman", 35), command=self.create_main_menu)
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
        self.create_main_menu()

    def create_inventory_window(self):
        self.clear_screen()

        # Inventory UI
        main_frame = tk.Frame(self.main_frame, bg="#ffffff")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Title
        title_label = tk.Label(main_frame, text="INVENTORY", bg='#add8e6', font=("Helvetica", 16, "bold"))
        title_label.pack(pady=10)

        # Back Button
        back_button = tk.Button(main_frame, text="Back", font=("Arial", 14), command=self.create_main_menu)
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

    def create_out_window(self):
        self.clear_screen()

        # Title Label
        title_label = tk.Label(self.main_frame, text="OUT", font=("Times New Roman", 50, "bold"))
        title_label.pack(pady=30)

        # Table Frame
        table_frame = tk.Frame(self.main_frame)
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
        check_out_button = tk.Button(self.main_frame, text="Check Out", font=("Arial", 20), command=self.check_out)
        check_out_button.pack(pady=10)

        # Back Button
        back_button = tk.Button(self.main_frame, text="Back", font=("Arial", 20), command=self.create_main_menu)
        back_button.pack(pady=10)

    def load_inventory_items_out(self):
        for item in self.inventory_items:
            self.tree_out.insert("", "end", values=(item["Name"], item["Barcode"], item["Price"], item["Type"], item["Quantity"]))

    def check_out(self):
        selected_items = self.tree_out.selection()
        for selected_item in selected_items:
            values = self.tree_out.item(selected_item, "values")
            item = {
                "Name": values[0],
                "Barcode": values[1],
                "Price": values[2],
                "Type": values[3],
                "Quantity": values[4],
                "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            self.sales_records.append(item)
            self.tree_out.delete(selected_item)
            self.remove_from_inventory(item["Barcode"])
        
        messagebox.showinfo("Success", "Items checked out successfully!")
        self.create_main_menu()

    def remove_from_inventory(self, barcode):
        for item in self.inventory_items:
            if item["Barcode"] == barcode:
                self.inventory_items.remove(item)
                break

    def clear_screen(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = MarketMate(root)
    root.mainloop()
