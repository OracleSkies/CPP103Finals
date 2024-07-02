import tkinter as tk
from tkinter import ttk

class SortingApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x200")
        self.root.title("Sorting Method")

        label = tk.Label(root, text="Sorting Method", font=('Arial', 25))
        label.pack(padx=20, pady=20)

        start_button = tk.Button(root, text="Start", font=('Arial', 35), command=self.open_menu_window)
        start_button.pack(pady=20)

    def open_menu_window(self):
        menu_window = tk.Toplevel(self.root)
        menu_window.title("Menu Options")
        menu_window.geometry("300x450")

        label = tk.Label(menu_window, text="Select Sorting Method", font=('Arial', 22))
        label.pack(pady=20)

        buttonframe = tk.Frame(menu_window)
        buttonframe.pack(fill='y')

        buttonframe.columnconfigure(0, weight=1)

        b1 = tk.Button(buttonframe, text="Bubble Sort", font=('Arial', 20), command=self.open_array_window)
        b1.grid(row=0, column=0, sticky=tk.W+tk.E)

        b2 = tk.Button(buttonframe, text="Selection Sort", font=('Arial', 20), command=self.open_array_window)
        b2.grid(row=1, column=0, sticky=tk.W+tk.E)

        b3 = tk.Button(buttonframe, text="Insertion Sort", font=('Arial', 20), command=self.open_array_window)
        b3.grid(row=2, column=0, sticky=tk.W+tk.E)

        b4 = tk.Button(buttonframe, text="Merge Sort", font=('Arial', 20), command=self.open_array_window)
        b4.grid(row=3, column=0, sticky=tk.W+tk.E)

        b5 = tk.Button(buttonframe, text="Quick Sort", font=('Arial', 20), command=self.open_array_window)
        b5.grid(row=4, column=0, sticky=tk.W+tk.E)

        b6 = tk.Button(buttonframe, text="Back", font=('Arial', 20), command=menu_window.destroy)
        b6.grid(row=4, column=0, sticky=tk.W+tk.E)

    def open_array_window(self):
        array_window = tk.Toplevel(self.root)
        array_window.title("Array Lists")
        array_window.geometry("300x450")

        label = tk.Label(array_window, text="Select Array Lists", font=('Arial', 22))
        label.pack(pady=20)

        buttonframe = tk.Frame(array_window)
        buttonframe.pack(fill='y')

        buttonframe.columnconfigure(0, weight=1)

        button1 = tk.Button(buttonframe, text="Array 1", font=('Arial', 20), command=self.array1)
        button1.grid(row=0, column=0, sticky=tk.W+tk.E)

        button2 = tk.Button(buttonframe, text="Array 2", font=('Arial', 20), command=self.array2)
        button2.grid(row=1, column=0, sticky=tk.W+tk.E)

        button3 = tk.Button(buttonframe, text="Array 3", font=('Arial', 20), command=self.array3)
        button3.grid(row=2, column=0, sticky=tk.W+tk.E)

        button4 = tk.Button(buttonframe, text="Array 4", font=('Arial', 20), command=self.array4)
        button4.grid(row=3, column=0, sticky=tk.W+tk.E)

        button5 = tk.Button(buttonframe, text="Array 5", font=('Arial', 20), command=self.array5)
        button5.grid(row=4, column=0, sticky=tk.W+tk.E)

        button6 = tk.Button(buttonframe, text="Back", font=('Arial', 20), command=array_window.destroy)
        button6.grid(row=6, column=0, sticky=tk.W+tk.E)

    def array1(self):
        unsorted_array1_window = tk.Toplevel(self.root)
        unsorted_array1_window.title("Array 1")
        unsorted_array1_window.geometry("300x400")

        label = tk.Label(unsorted_array1_window, text="Array 1: [3, 1, 2]", font=('Arial', 22))
        label.pack(pady=20)

        label = tk.Label(unsorted_array1_window, text="Sort Array?", font=('Arial', 22))
        label.pack(pady=30)

        buttonframe = tk.Frame(unsorted_array1_window)
        buttonframe.pack(fill='y')

        buttonframe.columnconfigure(0, weight=1)

        b1 = tk.Button(buttonframe, text="Yes", font=('Arial', 20), command=self.sorted_array1_window)
        b1.grid(row=0, column=0, sticky=tk.W+tk.E)

        b2 = tk.Button(buttonframe, text="Back", font=('Arial', 20), command=unsorted_array1_window.destroy)
        b2.grid(row=1, column=0, sticky=tk.W+tk.E)


    def array2(self):
        unsorted_array2_window = tk.Toplevel(self.root)
        unsorted_array2_window.title("Array 2")
        unsorted_array2_window.geometry("300x400")

        label = tk.Label(unsorted_array2_window, text="Array 2: [5, 3, 8, 1, 2]", font=('Arial', 22))
        label.pack(pady=20)

        label = tk.Label(unsorted_array2_window, text="Sort Array?", font=('Arial', 22))
        label.pack(pady=30)

        buttonframe = tk.Frame(unsorted_array2_window)
        buttonframe.pack(fill='y')

        buttonframe.columnconfigure(0, weight=1)

        b1 = tk.Button(buttonframe, text="Yes", font=('Arial', 20), command=self.sorted_array2_window)
        b1.grid(row=0, column=0, sticky=tk.W+tk.E)

        b2 = tk.Button(buttonframe, text="Back", font=('Arial', 20), command=unsorted_array2_window.destroy)
        b2.grid(row=1, column=0, sticky=tk.W+tk.E)

    def array3(self):
        unsorted_array3_window = tk.Toplevel(self.root)
        unsorted_array3_window.title("Array 3")
        unsorted_array3_window.geometry("500x400")

        label = tk.Label(unsorted_array3_window, text="Array 3: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]", font=('Arial', 22))
        label.pack(pady=20)

        label = tk.Label(unsorted_array3_window, text="Sort Array?", font=('Arial', 22))
        label.pack(pady=30)

        buttonframe = tk.Frame(unsorted_array3_window)
        buttonframe.pack(fill='y')

        buttonframe.columnconfigure(0, weight=1)

        b1 = tk.Button(buttonframe, text="Yes", font=('Arial', 20), command=self.sorted_array3_window)
        b1.grid(row=0, column=0, sticky=tk.W+tk.E)

        b2 = tk.Button(buttonframe, text="Back", font=('Arial', 20), command=unsorted_array3_window.destroy)
        b2.grid(row=1, column=0, sticky=tk.W+tk.E)

    def array4(self):
        unsorted_array4_window = tk.Toplevel(self.root)
        unsorted_array4_window.title("Array 4")
        unsorted_array4_window.geometry("700x400")

        label = tk.Label(unsorted_array4_window, text="Array 4: [15, 1, 10, 12, 5, 8, 3, 9, 7, 6, 2, 11, 14, 13, 4]", font=('Arial', 22))
        label.pack(pady=20)

        label = tk.Label(unsorted_array4_window, text="Sort Array?", font=('Arial', 22))
        label.pack(pady=30)

        buttonframe = tk.Frame(unsorted_array4_window)
        buttonframe.pack(fill='y')

        buttonframe.columnconfigure(0, weight=1)

        b1 = tk.Button(buttonframe, text="Yes", font=('Arial', 20), command=self.sorted_array4_window)
        b1.grid(row=0, column=0, sticky=tk.W+tk.E)

        b2 = tk.Button(buttonframe, text="Back", font=('Arial', 20), command=unsorted_array4_window.destroy)
        b2.grid(row=1, column=0, sticky=tk.W+tk.E)

    def array5(self):
        unsorted_array5_window = tk.Toplevel(self.root)
        unsorted_array5_window.title("Array 5")
        unsorted_array5_window.geometry("950x400")

        label = tk.Label(unsorted_array5_window, text="Array 5: [20, 18, 15, 16, 14, 13, 12, 10, 9, 7, 8, 6, 5, 4, 3, 2, 1, 11, 19, 17]", font=('Arial', 22))
        label.pack(pady=20)

        label = tk.Label(unsorted_array5_window, text="Sort Array?", font=('Arial', 22))
        label.pack(pady=30)

        buttonframe = tk.Frame(unsorted_array5_window)
        buttonframe.pack(fill='y')

        buttonframe.columnconfigure(0, weight=1)

        b1 = tk.Button(buttonframe, text="Yes", font=('Arial', 20), command=self.sorted_array5_window)
        b1.grid(row=0, column=0, sticky=tk.W+tk.E)

        b2 = tk.Button(buttonframe, text="Back", font=('Arial', 20), command=unsorted_array5_window.destroy)
        b2.grid(row=1, column=0, sticky=tk.W+tk.E)

    def sorted_array1_window(self):
        sorted_array1_window = tk.Toplevel(self.root)
        sorted_array1_window.title("Array 1")
        sorted_array1_window.geometry("300x400")

        label = tk.Label(sorted_array1_window, text="Sorted Array 1", font=('Arial', 22))
        label.pack(pady=20)

        buttonframe = tk.Frame(sorted_array1_window)
        buttonframe.pack(fill='y')

        buttonframe.columnconfigure(0, weight=1)

        back_button1 = tk.Button(buttonframe, text="Back", font=('Arial', 20), command=sorted_array1_window.destroy)
        back_button1.grid(row=1, column=0, sticky=tk.W+tk.E)

    def sorted_array2_window(self):
        sorted_array2_window = tk.Toplevel(self.root)
        sorted_array2_window.title("Array 2")
        sorted_array2_window.geometry("300x400")

        label = tk.Label(sorted_array2_window, text="Sorted Array 2", font=('Arial', 22))
        label.pack(pady=20)

        buttonframe = tk.Frame(sorted_array2_window)
        buttonframe.pack(fill='y')

        buttonframe.columnconfigure(0, weight=1)

        back_button2 = tk.Button(buttonframe, text="Back", font=('Arial', 20), command=sorted_array2_window.destroy)
        back_button2.grid(row=1, column=0, sticky=tk.W+tk.E)

    def sorted_array3_window(self):
        sorted_array3_window = tk.Toplevel(self.root)
        sorted_array3_window.title("Array 3")
        sorted_array3_window.geometry("500x400")

        label = tk.Label(sorted_array3_window, text="Array 1: [3, 1, 2]", font=('Arial', 22))
        label.pack(pady=20)

        buttonframe = tk.Frame(sorted_array3_window)
        buttonframe.pack(fill='y')

        buttonframe.columnconfigure(0, weight=1)

        back_button3 = tk.Button(buttonframe, text="Back", font=('Arial', 20), command=sorted_array3_window.destroy)
        back_button3.grid(row=1, column=0, sticky=tk.W+tk.E)

    def sorted_array4_window(self):
        sorted_array4_window = tk.Toplevel(self.root)
        sorted_array4_window.title("Array 4")
        sorted_array4_window.geometry("700x400")

        label = tk.Label(sorted_array4_window, text="Array 1: [3, 1, 2]", font=('Arial', 22))
        label.pack(pady=20)

        buttonframe = tk.Frame(sorted_array4_window)
        buttonframe.pack(fill='y')

        buttonframe.columnconfigure(0, weight=1)

        back_button4 = tk.Button(buttonframe, text="Back", font=('Arial', 20), command=sorted_array4_window.destroy)
        back_button4.grid(row=1, column=0, sticky=tk.W+tk.E)

    def sorted_array5_window(self):
        sorted_array5_window = tk.Toplevel(self.root)
        sorted_array5_window.title("Array 5")
        sorted_array5_window.geometry("950x400")

        label = tk.Label(sorted_array5_window, text="Array 1: [3, 1, 2]", font=('Arial', 22))
        label.pack(pady=20)

        buttonframe = tk.Frame(sorted_array5_window)
        buttonframe.pack(fill='y')

        buttonframe.columnconfigure(0, weight=1)

        back_button5 = tk.Button(buttonframe, text="Back", font=('Arial', 20), command=sorted_array5_window.destroy)
        back_button5.grid(row=1, column=0, sticky=tk.W+tk.E)

        

if __name__ == "__main__":
    root = tk.Tk()
    app = SortingApp(root)
    root.mainloop()
