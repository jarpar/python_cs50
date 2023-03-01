# Calculator with GUI in Python

import tkinter as tk


# Define functions for the basic math operations
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


# Create the GUI window
root = tk.Tk()
root.title("Calculator")

# Create the entry fields for the user to input numbers and select operation
num1_entry = tk.Entry(root, width=10)
num1_entry.grid(row=0, column=0, padx=5, pady=5)

operation_label = tk.Label(root, text="Operation:")
operation_label.grid(row=0, column=1, padx=5, pady=5)

operation_options = ["+", "-", "*", "/"]
operation_var = tk.StringVar(root)
operation_var.set("+")
operation_dropdown = tk.OptionMenu(root, operation_var, *operation_options)
operation_dropdown.grid(row=0, column=2, padx=5, pady=5)

num2_entry = tk.Entry(root, width=10)
num2_entry.grid(row=0, column=3, padx=5, pady=5)

result_label = tk.Label(root, text="Result:")
result_label.grid(row=1, column=0, padx=5, pady=5)

result_entry = tk.Entry(root, width=10, state="readonly")
result_entry.grid(row=1, column=1, columnspan=3, padx=5, pady=5)


# Define the function to perform the calculation
def calculate():
    num1 = float(num1_entry.get())
    num2 = float(num2_entry.get())
    operation = operation_var.get()

    if operation == "+":
        result = add(num1, num2)
    elif operation == "-":
        result = subtract(num1, num2)
    elif operation == "*":
        result = multiply(num1, num2)
    elif operation == "/":
        result = divide(num1, num2)
    else:
        result = "Invalid input"

    result_entry.configure(state="normal")
    result_entry.delete(0, tk.END)
    result_entry.insert(0, result)
    result_entry.configure(state="readonly")


# Create the button to perform the calculation
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=2, column=0, columnspan=4, padx=5, pady=5)

root.mainloop()
