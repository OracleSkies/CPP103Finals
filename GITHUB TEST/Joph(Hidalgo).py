#joph
import tkinter as tk
from tkinter import messagebox


    
def open_in_window():
    
    
        
    openIN = tk.Toplevel(root)
    openIN.title("IN WINDOW")
    openIN.geometry("1000x800")
    openIN.configure(bg='dark slate blue')
   

    
    
    openIN_username = tk.Label(openIN, text = "Username", font = ('Times New Roman', 15), height= 2,width=7 ,bg = "aquamarine2")
    openIN_username.pack(pady=10)
    
    openIN_username_entry = tk.Entry(openIN)
    openIN_username_entry.pack(pady=5)
    
    openIN_password = tk.Label(openIN, text = "Password", font = ("Times New Roman",15),height= 2,width= 7,bg ="aquamarine2")
    openIN_password.pack(pady = 10)
    
    openIN_password_entry = tk.Entry(openIN, show = '*')
    openIN_password_entry.pack(pady =5)
    
    sign_in_button = tk.Button(openIN, text = "Sign IN", font = ("Helvictica", 16), height = 2, width = 7, bg = "green")
    sign_in_button.pack(pady=50)

    

def open_inventory_window():
    open_inventory = tk.Toplevel(root)
    open_inventory.title('INVENTORY')
    open_inventory.geometry("1000x800")
    open_inventory.configure(bg = 'light blue')
    
    
    
    
    
def open_out_window():
    openOut = tk.Toplevel(root)
    openOut.title('OUT')
    openOut.geometry('1000x800')
    openOut.configure(bg= 'light blue')  
    
    
root= tk.Tk()
root.title("MAIN WINDOW")
root.geometry("1000x800")
root.configure(bg='light blue')  

main_buttonIN = tk.Button(root, text = "IN", font = ('Times New Roman' , 20), height= 8, width= 20, command= open_in_window, bg= 'light blue')
main_buttonIN.pack()
main_button_INVENTORY = tk.Button(root, text = "INVENTORY", font = ('Times New Roman' , 20), height= 8, width= 20, command= open_inventory_window, bg = 'light blue')
main_button_INVENTORY.pack()
main_buttonOUT = tk.Button(root, text = "OUT", font = ('Times New Roman' , 20), height= 8, width= 20, command= open_out_window, bg = 'light blue')
main_buttonOUT.pack()






root.mainloop()
