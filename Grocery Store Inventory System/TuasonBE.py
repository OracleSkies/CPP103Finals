import sqlite3

class DatabaseManagement:
    def __init__(self):
        self.connection = sqlite3.connect("ITEM_DATABASE.db")
        self.cursor = self.connection.cursor()

class DataManagement(DatabaseManagement):
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
        sql_command = "INSERT INTO ITEMS (barcode, brand_name, item_type, item_quantity, item_price) VALUES (?, ?, ?, ?, ?)"
        values = (self.barcode, self.brand_name, self.item_type, self.item_quantity, self.item_price)
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