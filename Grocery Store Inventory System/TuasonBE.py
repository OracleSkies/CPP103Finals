import sqlite3

class database_management:
    def __init__(self):
        self.connection = sqlite3.connect("ITEM_DATABASE.db")
        self.cursor = self.connection.cursor()

class data_management(database_management):

    def __init__(self,barcode, brand_name, item_type, item_quantity, item_price):
        super().__init__()
        self.barcode = barcode
        self.brand_name = brand_name
        self.item_type = item_type
        self.item_quantity = item_quantity
        self.item_price = item_price

    def insert_Inventory_In_Data(self):
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS ITEMS ( id INTEGER PRIMARY KEY,\
                            barcode INTEGER,\
                            brand_name TEXT,\
                            item_type TEXT,\
                            item_quantity INTEGER,\
                            item_price INTEGER)""")
        sqlcommand = "INSERT INTO ITEMS (barcode, brand_name, item_type, item_quantity, item_price) VALUES (?, ?, ?, ?, ?)"
        values = (self.barcode, self.brand_name, self.item_type, self.item_quantity, self.item_price)
        self.cursor.execute(sqlcommand, values)
        self.connection.commit()  
    
    
"""class edit:
    def __init__(self,cursor):
        self.cursor = cursor
    
    def delete_row(self,Barcode):
        
        cursor.execute("DELETE FROM ITEMS WHERE BARCODE = ?",(Barcode,))
        if self.cursor.rowcount == 0:
            print("None removed")
        else:
            print(f"Item{barcode},removed")
        connection.commit()  

"""
    

        


"""print("Input data")
user = user_input(cursor)

item_inserted = user.input_data()
user.insertion(item_inserted)

print("Remove data")
remove_barcode = int(input("Enter barcode to remove: "))


editor = edit(cursor)
editor.delete_row(remove_barcode)


connection.close()"""