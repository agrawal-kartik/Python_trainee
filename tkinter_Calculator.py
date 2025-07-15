import tkinter as tk
from tkinter import messagebox

def add_numbers():
    """Addition"""
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result = num1 + num2
        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers in both fields.")

def subtract_numbers():
    """Subtraction"""
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result = num1 - num2
        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers in both fields.")

def Multiply_numbers():
    """Mulpication"""
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result = num1 * num2
        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers in both fields.")

def Divide_numbers():
    """Division"""
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result = num1 / num2
        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers in both fields.")

def Exponetial_numbers():
    """Exponetial"""
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result = num1 ** num2
        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers in both fields.")

def Remainder_numbers():
    """Remainder"""
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result = num1 % num2
        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers in both fields.")


root = tk.Tk()
root.title("Calculator")

label_num1 = tk.Label(root, text="First Number:")
label_num1.grid(row=0, column=0, padx=10, pady=5, sticky="w")

entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1, padx=10, pady=5)

label_num2 = tk.Label(root, text="Second Number:")
label_num2.grid(row=1, column=0, padx=10, pady=5, sticky="w")

entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1, padx=10, pady=5)

button_add = tk.Button(root, text="Add", command=add_numbers)
button_add.grid(row=2, column=0)

button_add = tk.Button(root, text="Substract", command=subtract_numbers)
button_add.grid(row=2, column=1)

button_add = tk.Button(root, text="Multiply", command=Multiply_numbers)
button_add.grid(row=2, column=2)

button_add = tk.Button(root, text="Divide", command=Divide_numbers)
button_add.grid(row=2, column=3)

button_add = tk.Button(root, text="Exponential", command=Exponetial_numbers)
button_add.grid(row=2, column=4)

button_add = tk.Button(root, text="Remainder", command=Remainder_numbers)
button_add.grid(row=2, column=5)

label_result = tk.Label(root, text="Result:")
label_result.grid(row=8, column=0, columnspan=2)

root.mainloop()