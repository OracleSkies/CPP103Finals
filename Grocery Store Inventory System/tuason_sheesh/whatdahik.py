import sqlite3

connection = sqlite3.connect("ITEM_DATABASE.db")
cursor = connection.cursor()


cursor.execute(""" CREATE TABLE IF NOT EXISTS ITEMS ( barcode INTEGER PRIMARY KEY,brand_name TEXT,item_type TEXT,item_quantity INTEGER,item_price INTEGER)""")

class user_input:

    def __init__(self,cursor):
        self.cursor = cursor
        

    def insertion(self,data_input):
        items = "INSERT INTO ITEMS (barcode, brand_name, item_type, item_quantity, item_price) VALUES (?, ?, ?, ?, ?)"
        cursor.execute(items, data_input)
        connection.commit()  

    def input_data(self):
        Barcode = int(input("Enter barcode: "))
        Brand_name = input("Enter brand name: ")
        Item_type = input("Enter item type: ")
        Item_quantity = int(input("Enter quantity: "))
        Item_price = int(input("Enter price: "))
        
        data = (Barcode, Brand_name, Item_type, Item_quantity, Item_price)
        return data
    
    
class edit:
    def __init__(self,cursor):
        self.cursor = cursor
    
    def delete_row(self,Barcode):
        
        cursor.execute("DELETE FROM ITEMS WHERE BARCODE = ?",(Barcode,))
        if self.cursor.rowcount == 0:
            print("None removed")
        else:
            print(f"Item{barcode},removed")
        connection.commit()  


    

        


print("Input data")
user = user_input(cursor)

item_inserted = user.input_data()
user.insertion(item_inserted)

print("Remove data")
remove_barcode = int(input("Enter barcode to remove: "))


editor = edit(cursor)
editor.delete_row(remove_barcode)


connection.close()