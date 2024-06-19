import sqlite3
from tkinter import messagebox

class DatabaseManagement:
    def __init__(self):
        self.connection = sqlite3.connect("ITEM_DATABASE.db")
        self.cursor = self.connection.cursor()
    
class LoginSystem(DatabaseManagement):
    def __init__(self, login_username, login_password):
        super().__init__()
        self.login_username = login_username
        self.login_password = login_password
    
    def login_Account(self):
        sqlCommand = "SELECT * FROM users WHERE username = ? AND password = ?"
        account = (self.login_username, self.login_password)
        self.cursor.execute(sqlCommand, account)
        result = self.cursor.fetchone()
        if result:
            messagebox.showinfo("User log in","Account successfully logged in")
            return True
        else:
            messagebox.showinfo("User log in","Account not found")
            return False

class Registration_System(DatabaseManagement):
    def __init__(self, reg_Username, reg_Password):
        super().__init__()
        self.reg_Username = reg_Username
        self.reg_Password = reg_Password

    def register_Account(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users(\
                            id INTEGER PRIMARY KEY,\
                            username TEXT,\
                            password TEXT NOT NULL)")
        sqlCommand = "INSERT INTO users (username, password) VALUES (?, ?)"
        values = (self.reg_Username, self.reg_Password)
        self.cursor.execute(sqlCommand,values)
        self.connection.commit()
        messagebox.showinfo("Account Registration", "Account Successfully Registered!")
        
        
class InventoryManagement(DatabaseManagement):
    def __init__(self, barcode, brand_name, item_type, item_quantity, item_price):
        super().__init__()
        self.barcode = barcode
        self.brand_name = brand_name
        self.item_type = item_type
        self.item_quantity = item_quantity
        self.item_price = item_price

    def create_items_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS ITEMS (
                               id INTEGER PRIMARY KEY,
                               barcode INTEGER,
                               brand_name TEXT,
                               item_type TEXT,
                               item_quantity INTEGER,
                               item_price INTEGER)""")
        self.connection.commit()

    def insert_inventory(self):
        sql_command = "INSERT INTO ITEMS (brand_name, barcode, item_price, item_type, item_quantity) VALUES (?, ?, ?, ?, ?)"
        values = (self.brand_name, self.barcode, self.item_price, self.item_type, self.item_quantity)
        #name barcode price type quantity
        self.cursor.execute(sql_command, values)
        self.connection.commit()

    def delete_inventory(self, barcode):
        self.cursor.execute("DELETE FROM ITEMS WHERE barcode = ?", (barcode,))
        self.connection.commit()

class OutWindow(DatabaseManagement):
    def __init__(self):
        super().__init__()

    def print_items(self):
        self.cursor.execute("SELECT * FROM ITEMS")
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)

def main():
    print("Input data")
    barcode = int(input("Enter barcode: "))
    brand_name = input("Enter brand name: ")
    item_type = input("Enter item type: ")
    item_quantity = int(input("Enter item quantity: "))
    item_price = int(input("Enter item price: "))

    data_manager = DataManagement(barcode, brand_name, item_type, item_quantity, item_price)
    data_manager.create_items_table()  
    data_manager.insert_inventory()  

    print("Remove data")
    remove_barcode = int(input("Enter barcode to remove: "))
    data_manager.delete_inventory(remove_barcode)

    out_window = OutWindow()
    out_window.print_items()

    data_manager.connection.close()

if __name__ == "__main__":
    main()