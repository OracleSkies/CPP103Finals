import tkinter as tk

def confirm_button_click():
    # Handle Confirm button click here
    pass

def back_button_click():
    # Handle Back button click here
    pass

root = tk.Tk()
root.title("IN")
root.configure(bg='cadetblue2')
labels = ["Name", "Barcode", "Price", "Type", "Quantity"]
entry_widgets = []

for label_text in labels:
    label = tk.Label(root, text=label_text, background='cadetblue2', foreground='white', font= 'bold')
    label.pack(anchor="w") 
    entry = tk.Entry(root, bg="darkturquoise")  
    entry.pack(fill="both", expand=True)  
    entry_widgets.append(entry)


confirm_button = tk.Button(root, text="Confirm", command=confirm_button_click, bg="chartreuse3")
confirm_button.pack(side="right")

back_button = tk.Button(root, text="Back", command=back_button_click, bg="darkolivegreen2")
back_button.pack(side="right")

root.mainloop()  