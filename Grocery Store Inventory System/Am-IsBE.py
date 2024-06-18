import tkinter as tk
import sqlite3

# Function to insert data into the database
def insert_data():
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()
    
    # Create table if it doesn't exist
    c.execute('''CREATE TABLE IF NOT EXISTS inventory
                 (name text, price real, type text, quantity integer, barcode text)''')

    # Insert a row of data
    c.execute("INSERT INTO inventory VALUES (?, ?, ?, ?, ?)",
              (nameEntry.get(), priceEntry.get(), typeEntry.get(), quantityEntry.get(), barcodeEntry.get()))

    # Save (commit) the changes and close the connection
    conn.commit()
    conn.close()

# Initialize the main window
root = tk.Tk()
root.title("IN")
root.geometry("400x300")

# Create frames for each section
topFrame = tk.Frame(root)
topFrame.pack(side=tk.TOP, fill=tk.X, pady=10)

middleFrame = tk.Frame(root)
middleFrame.pack(fill=tk.X, pady=10)

barcodeFrame = tk.Frame(root)
barcodeFrame.pack(fill=tk.X, pady=10)

bottomFrame = tk.Frame(root)
bottomFrame.pack(side=tk.BOTTOM, fill=tk.X, pady=10)

# Add widgets to the top frame
nameLabel = tk.Label(topFrame, text="Name")
nameLabel.pack(side=tk.LEFT)

nameEntry = tk.Entry(topFrame)
nameEntry.pack(side=tk.LEFT)

priceLabel = tk.Label(topFrame, text="Price")
priceLabel.pack(side=tk.LEFT)

priceEntry = tk.Entry(topFrame)
priceEntry.pack(side=tk.LEFT)

# Add widgets to the middle frame
typeLabel = tk.Label(middleFrame, text="Type")
typeLabel.pack(side=tk.LEFT)

typeEntry = tk.Entry(middleFrame)
typeEntry.pack(side=tk.LEFT)

quantityLabel = tk.Label(middleFrame, text="Quantity")
quantityLabel.pack(side=tk.LEFT)

quantityEntry = tk.Entry(middleFrame)
quantityEntry.pack(side=tk.LEFT)

# Add widgets to the barcode frame
barcodeLabel = tk.Label(barcodeFrame, text="Barcode")
barcodeLabel.pack(side=tk.LEFT)

barcodeEntry = tk.Entry(barcodeFrame)
barcodeEntry.pack(side=tk.LEFT)

# Add widgets to the bottom frame
backButton = tk.Button(bottomFrame, text="BACK")
backButton.pack(side=tk.LEFT, padx=10)

confirmButton = tk.Button(bottomFrame, text="CONFIRM", command=insert_data)
confirmButton.pack(side=tk.LEFT)

root.mainloop()
