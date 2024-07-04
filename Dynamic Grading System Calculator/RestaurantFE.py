import tkinter as tk
from tkinter import ttk

class Order_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("650x625")
        self.root.title("Restaurant Order Management System")
        self.root.resizable(0, 0)

        label = tk.Label(root, text="Restaurant Order Management System", font=('Arial', 25))
        label.pack(padx=20, pady=20)

        labelframe = tk.LabelFrame(root, text="Select Option", font=('Arial', 20))
        labelframe.pack(fill="both", expand="yes", padx=20, pady=20)

        labelframe.columnconfigure(0, weight=1)

        b1 = tk.Button(labelframe, text="Add Order", font=('Arial', 20), command=self.open_add_order_window)
        b1.grid(row=0, column=0, sticky=tk.W+tk.E, pady=10)

        b2 = tk.Button(labelframe, text="Serve Order", font=('Arial', 20), command=self.open_serve_order_window)
        b2.grid(row=1, column=0, sticky=tk.W+tk.E, pady=10)

        b3 = tk.Button(labelframe, text="View Current Order", font=('Arial', 20), command=self.open_view_current_order_window)
        b3.grid(row=2, column=0, sticky=tk.W+tk.E, pady=10)

        b4 = tk.Button(labelframe, text="Check Order Pending", font=('Arial', 20), command=self.open_check_order_pending_window)
        b4.grid(row=3, column=0, sticky=tk.W+tk.E, pady=10)

        b5 = tk.Button(labelframe, text="Check If Stack is Full", font=('Arial', 20), command=self.open_check_if_stack_is_full_window)
        b5.grid(row=4, column=0, sticky=tk.W+tk.E, pady=10)

        b6 = tk.Button(labelframe, text="EXIT", font=('Arial', 20), command=self.root.destroy)
        b6.grid(row=5, column=0, sticky=tk.W+tk.E, pady=10)

    def open_add_order_window(self):
        add_order_window = tk.Toplevel(self.root)
        add_order_window.title("Add Order")
        add_order_window.geometry("400x300")

        label = tk.Label(add_order_window, text="Add Order", font=('Arial', 22))
        label.pack(pady=20)

        buttonframe = tk.LabelFrame(add_order_window)
        buttonframe.pack(fill='x', padx=20, pady=20)

        buttonframe.columnconfigure(0, weight=1)
        buttonframe.columnconfigure(1, weight=1)

        entry_label = tk.Label(buttonframe, text="Input Order:", font=('Arial', 15))
        entry_label.grid(row=0, column=0, columnspan=2, pady=5)

        entry = tk.Entry(buttonframe, font=('Arial', 15))
        entry.grid(row=1, column=0, columnspan=2, pady=5, padx=10, sticky=tk.W+tk.E)

        button1 = tk.Button(buttonframe, text="Confirm", font=('Arial', 20))
        button1.grid(row=2, column=0, sticky=tk.W+tk.E, padx=15, pady=5)

        button2 = tk.Button(buttonframe, text="Back", font=('Arial', 20), command=add_order_window.destroy)
        button2.grid(row=2, column=1, sticky=tk.W+tk.E, padx=15, pady=5)

    def confirm_add_order(self):
        pass

    def open_serve_order_window(self):
        serve_order_window = tk.Toplevel(self.root)
        serve_order_window.title("Serve Order")
        serve_order_window.geometry("400x300")

        label = tk.Label(serve_order_window, text="Serve Order", font=('Arial', 22))
        label.pack(pady=10)

        label1 = tk.Label(serve_order_window, text="Last input will appear", font=('Arial', 22))
        label1.pack(pady=30)

        buttonframe = tk.LabelFrame(serve_order_window)
        buttonframe.pack(fill='x', padx=20, pady=20)

        buttonframe.columnconfigure(0, weight=1)
        buttonframe.columnconfigure(1, weight=1)

        button1 = tk.Button(buttonframe, text="Confirm", font=('Arial', 20))
        button1.grid(row=2, column=0, sticky=tk.W+tk.E, padx=15, pady=5)

        button2 = tk.Button(buttonframe, text="Back", font=('Arial', 20), command=serve_order_window.destroy)
        button2.grid(row=2, column=1, sticky=tk.W+tk.E, padx=15, pady=5)

    def confirm_serve_order(self):
        pass

    def open_view_current_order_window(self):
        open_current_order_window = tk.Toplevel(self.root)
        open_current_order_window.title("View Current Order")
        open_current_order_window.geometry("400x300")

        open_current_order_window.columnconfigure(0, weight=1)

        label1 = tk.Label(open_current_order_window, text="View Current Order", font=('Arial', 25))
        label1.grid(row=0, column=0, pady=10, sticky=tk.N)

        label2 = tk.Label(open_current_order_window, text="Dito nakalagay yung current order", font=('Arial', 15))
        label2.grid(row=1, column=0, pady=10, sticky=tk.N)

        button = tk.Button(open_current_order_window, text="Back", font=('Arial', 20), command=open_current_order_window.destroy)
        button.grid(row=2, column=0, pady=10, sticky=tk.N)

    def open_check_order_pending_window(self):
        check_order_pending = tk.Toplevel(self.root)
        check_order_pending.title("Check Order Pending")
        check_order_pending.geometry("400x300")

        check_order_pending.columnconfigure(0, weight=1)

        label1 = tk.Label(check_order_pending, text="Check Order Pending", font=('Arial', 25))
        label1.grid(row=0, column=0, pady=10, sticky=tk.N)

        labelframe = tk.LabelFrame(check_order_pending, text="Pending Orders", font=('Arial', 20))
        labelframe.grid(row=1, column=0, padx=20, pady=20, sticky=tk.W+tk.E)

        labelframe.columnconfigure(0, weight=1)

        label2 = tk.Label(labelframe, text="Dito nakalagay yung mga pending orders", font=('Arial', 15))
        label2.grid(row=0, column=0, pady=20, sticky=tk.N)

        button = tk.Button(check_order_pending, text="Back", font=('Arial', 20), command=check_order_pending.destroy)
        button.grid(row=2, column=0, pady=10, sticky=tk.N)

    def open_check_if_stack_is_full_window(self):
        check_order_pending = tk.Toplevel(self.root)
        check_order_pending.title("Check If stack is Full")
        check_order_pending.geometry("400x300")

        check_order_pending.columnconfigure(0, weight=1)

        label1 = tk.Label(check_order_pending, text="Check Check if Stack is Full", font=('Arial', 23))
        label1.grid(row=0, column=0, pady=10, sticky=tk.N)

        labelframe = tk.LabelFrame(check_order_pending, text="", font=('Arial', 20))
        labelframe.grid(row=1, column=0, padx=20, pady=20, sticky=tk.W+tk.E)

        labelframe.columnconfigure(0, weight=1)

        label2 = tk.Label(labelframe, text="Order list is not full/ Order list is full", font=('Arial', 15))
        label2.grid(row=0, column=0, pady=20, sticky=tk.N)

        button = tk.Button(check_order_pending, text="Back", font=('Arial', 20), command=check_order_pending.destroy)
        button.grid(row=2, column=0, pady=10, sticky=tk.N)


if __name__ == "__main__":
    root = tk.Tk()
    app = Order_System(root)
    root.mainloop()