import tkinter as tk
import sqlite3

# Initialize the main window
root = tk.Tk()
root.title("Inventory Management")
root.geometry("500x350")

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

def confirm_addition():
    # Insert data into the database and close the confirmation dialog
    insert_data()
    dialog.destroy()

def cancel_addition():
    # Close the main window
    root.destroy()

def show_confirmation_dialog():
    global dialog
    # Create a new top-level window for the confirmation dialog
    dialog = tk.Toplevel(root)
    dialog.title("Confirm Addition")
    dialog.geometry("300x150")

    # Create frame for dialog box
    dialog_frame = tk.Frame(dialog)
    dialog_frame.pack(pady=20)

    # Add dialog text
    dialog_label = tk.Label(dialog_frame, text="ADD PRODUCT TO THE INVENTORY?", font=("Arial", 14))
    dialog_label.pack()

    # Create frame for buttons
    button_frame = tk.Frame(dialog)
    button_frame.pack(pady=10)

    # Add 'Yes' button
    yes_button = tk.Button(button_frame, text="YES", command=confirm_addition)
    yes_button.grid(row=0, column=0, padx=10)

    # Add 'No' button
    no_button = tk.Button(button_frame, text="NO", command=dialog.destroy)
    no_button.grid(row=0, column=1)

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
backButton = tk.Button(bottomFrame, text="BACK", command=cancel_addition)
backButton.pack(side=tk.LEFT, padx=10)

confirmButton = tk.Button(bottomFrame, text="CONFIRM", command=show_confirmation_dialog)
confirmButton.pack(side=tk.LEFT)

root.mainloop()
