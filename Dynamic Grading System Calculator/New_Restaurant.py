import tkinter as tk
from tkinter import ttk

class OrderSystem:
    def __init__(self):
        self.orders = []
    
    def isEmpty(self): # Check if the stack is empty
        return len(self.orders) == 0
    
    def push(self,item):#Add an item to the top of the stack
        self.orders.append(item)

    def pop(self):
        if self.isEmpty():
            raise IndexError("Pop from an empty stack")
        return self.orders.pop()
    
    def peek(self):
        if self.isEmpty():
            raise IndexError("Peek from an empty stack")
        return self.orders[-1]
    
    def size(self):
        return len(self.orders)
    
    def __str__(self):
        return str(self.orders)
    
class OrderGUI:
    def __init__(self, root):
        #main window where users will choose option for order system
        self.root = root
        self.root.geometry("650x625")
        self.root.title("Restaurant Order Management System")
        self.root.resizable(0, 0)
        self.root.configure(bg='midnight blue')
        self.order = OrderSystem()
        

        label = tk.Label(root, text="Restaurant Order Management System", font=('Arial', 25), bg='midnight blue', fg='white')
        label.pack(padx=20, pady=20)

        labelframe = tk.LabelFrame(root, text="Select Option", font=('Arial', 20), bg='midnight blue', fg='white')
        labelframe.pack(fill="both", expand="yes", padx=20, pady=20)

        labelframe.columnconfigure(0, weight=1)

        #buttons for choosing
        b1 = tk.Button(labelframe, text="Add Order", font=('Arial', 20), bg="royalblue3", fg="white", command=self.open_add_order_window)
        b1.grid(row=0, column=0, sticky=tk.W+tk.E, pady=10)

        b2 = tk.Button(labelframe, text="Serve Order", font=('Arial', 20), bg="royalblue3", fg="white", command=self.open_serve_order_window)
        b2.grid(row=1, column=0, sticky=tk.W+tk.E, pady=10)

        b3 = tk.Button(labelframe, text="View Current Order", font=('Arial', 20), bg="royalblue3", fg="white", command=self.open_view_current_order_window)
        b3.grid(row=2, column=0, sticky=tk.W+tk.E, pady=10)

        b4 = tk.Button(labelframe, text="Check Order Pending", font=('Arial', 20), bg="royalblue3", fg="white", command=self.open_check_order_pending_window)
        b4.grid(row=3, column=0, sticky=tk.W+tk.E, pady=10)

        b5 = tk.Button(labelframe, text="Check If Stack is Full", font=('Arial', 20), bg="royalblue3", fg="white", command=self.open_check_if_stack_is_full_window)
        b5.grid(row=4, column=0, sticky=tk.W+tk.E, pady=10)

        b6 = tk.Button(labelframe, text="EXIT", font=('Arial', 20), bg="royalblue3", fg="white", command=self.root.destroy)
        b6.grid(row=5, column=0, sticky=tk.W+tk.E, pady=10)

    #new pop-up window for adding order
    def open_add_order_window(self):
        self.add_order_window = tk.Toplevel(self.root)
        self.add_order_window.title("Add Order")
        self.add_order_window.geometry("400x300")
        self.add_order_window.configure(bg='midnight blue')

        self.label = tk.Label(self.add_order_window, text="Add Order", font=('Arial', 22), bg='midnight blue', fg='white')
        self.label.pack(pady=20)

        self.buttonframe = tk.LabelFrame(self.add_order_window, bg='royalblue3')
        self.buttonframe.pack(fill='x', padx=20, pady=20)

        self.buttonframe.columnconfigure(0, weight=1)
        self.buttonframe.columnconfigure(1, weight=1)

        #user input for adding order
        self.orderLabel = tk.Label(self.buttonframe, text="Input Order:", font=('Arial', 15), bg='royalblue3', fg='white')
        self.orderLabel.grid(row=0, column=0, columnspan=2, pady=5)

        self.orderEntry = tk.Entry(self.buttonframe, font=('Arial', 15), bg='white', fg='black')
        self.orderEntry.grid(row=1, column=0, columnspan=2, pady=5, padx=10, sticky=tk.W+tk.E)

        self.serveButton = tk.Button(self.buttonframe, text="Confirm", font=('Arial', 20), bg='royalblue3', fg='white', command = self.confirm_add_order)
        self.serveButton.grid(row=2, column=0, sticky=tk.W+tk.E, padx=15, pady=5)

        self.backButton = tk.Button(self.buttonframe, text="Back", font=('Arial', 20), bg='royalblue3', fg='white', command=self.add_order_window.destroy)
        self.backButton.grid(row=2, column=1, sticky=tk.W+tk.E, padx=15, pady=5)

    def confirm_add_order(self):
        orderToPush = self.orderEntry.get()
        self.order.push(orderToPush)

    #new pop-up window for serving order
    def open_serve_order_window(self):
        self.serve_order_window = tk.Toplevel(self.root)
        self.serve_order_window.title("Serve Order")
        self.serve_order_window.geometry("400x300")
        self.serve_order_window.configure(bg='midnight blue')

        serveLabel = tk.Label(self.serve_order_window, text="Serve Current Order", font=('Arial', 22), bg='midnight blue', fg='white')
        serveLabel.pack(pady=10)

        #label where the last input will appear
        #peek muna
        self.currentOrder = self.order.peek()

        label1 = tk.Label(self.serve_order_window, text= f"The current order is {self.currentOrder}", font=('Arial', 22), bg='midnight blue', fg='white')
        label1.pack(pady=30)

        self.buttonframe = tk.LabelFrame(self.serve_order_window, bg='royalblue3')
        self.buttonframe.pack(fill='x', padx=20, pady=20)

        self.buttonframe.columnconfigure(0, weight=1)
        self.buttonframe.columnconfigure(1, weight=1)

        serveButton = tk.Button(self.buttonframe, text="Serve", font=('Arial', 20), bg='royalblue3', fg='white', command = self.confirm_serve_order)
        serveButton.grid(row=2, column=0, sticky=tk.W+tk.E, padx=15, pady=5)

        backButton = tk.Button(self.buttonframe, text="Back", font=('Arial', 20), bg='royalblue3', fg='white', command=self.serve_order_window.destroy)
        backButton.grid(row=2, column=1, sticky=tk.W+tk.E, padx=15, pady=5)

    def confirm_serve_order(self):
        self.order.pop() 
        #==== Need Error Handling ======
        pass

    #new pop-up window for viewing current order
    def open_view_current_order_window(self):
        open_current_order_window = tk.Toplevel(self.root)
        open_current_order_window.title("View Current Order")
        open_current_order_window.geometry("400x300")
        open_current_order_window.configure(bg='midnight blue')

        open_current_order_window.columnconfigure(0, weight=1)
        

        self.currentOrder = self.order.peek()
        #display the current order
        label1 = tk.Label(open_current_order_window, text="View Current Order", font=('Arial', 25), bg='midnight blue', fg='white')
        label1.grid(row=0, column=0, pady=10, sticky=tk.N)

        label2 = tk.Label(open_current_order_window, text=f"The current order is {self.currentOrder}", font=('Arial', 15), bg='midnight blue', fg='white')
        label2.grid(row=1, column=0, pady=10, sticky=tk.N)

        button = tk.Button(open_current_order_window, text="Back", font=('Arial', 20), bg='royalblue3', fg='white', command=open_current_order_window.destroy)
        button.grid(row=2, column=0, pady=10, sticky=tk.N)

    #new pop-up window for checking pending orders
    def open_check_order_pending_window(self):
        check_order_pending = tk.Toplevel(self.root)
        check_order_pending.title("Check Order Pending")
        check_order_pending.geometry("400x300")
        check_order_pending.configure(bg='midnight blue')

        check_order_pending.columnconfigure(0, weight=1)

        label1 = tk.Label(check_order_pending, text="Check Order Pending", font=('Arial', 25), bg='midnight blue', fg='white')
        label1.grid(row=0, column=0, pady=10, sticky=tk.N)

        labelframe = tk.LabelFrame(check_order_pending, bg='royalblue3')
        labelframe.grid(row=1, column=0, padx=20, pady=20, sticky=tk.W+tk.E)

        labelframe.columnconfigure(0, weight=1)

        #display the pending orders that is pending
        label2 = tk.Label(labelframe, text="Dito nakalagay yung mga pending orders", font=('Arial', 15), bg='royalblue3', fg='white')
        label2.grid(row=0, column=0, pady=20, sticky=tk.N)

        button = tk.Button(check_order_pending, text="Back", font=('Arial', 20), bg='royalblue3', fg='white', command=check_order_pending.destroy)
        button.grid(row=2, column=0, pady=10, sticky=tk.N)

    #new pop-up window for checking if stack is full
    def open_check_if_stack_is_full_window(self):
        check_order_pending = tk.Toplevel(self.root)
        check_order_pending.title("Check If Stack is Full")
        check_order_pending.geometry("400x300")
        check_order_pending.configure(bg='midnight blue')

        check_order_pending.columnconfigure(0, weight=1)

        #display if the stack is full or not
        label1 = tk.Label(check_order_pending, text="Check if Stack is Full", font=('Arial', 23), bg='midnight blue', fg='white')
        label1.grid(row=0, column=0, pady=10, sticky=tk.N)

        labelframe = tk.LabelFrame(check_order_pending, bg='royalblue3')
        labelframe.grid(row=1, column=0, padx=20, pady=20, sticky=tk.W+tk.E)

        labelframe.columnconfigure(0, weight=1)

        label2 = tk.Label(labelframe, text="Order list is not full/ Order list is full", font=('Arial', 15), bg='royalblue3', fg='white')
        label2.grid(row=0, column=0, pady=20, sticky=tk.N)

        button = tk.Button(check_order_pending, text="Back", font=('Arial', 20), bg='royalblue3', fg='white', command=check_order_pending.destroy)
        button.grid(row=2, column=0, pady=10, sticky=tk.N)


if __name__ == "__main__":
    root = tk.Tk()
    app = OrderGUI(root)
    root.mainloop()
