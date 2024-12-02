import tkinter as tk
from tkinter import messagebox

def divide_numbers():
    try:
        num1 = int (entry_num1.get())
        num2 = int (entry_num2.get())
        result = num1 / num2
        label_result.config(text=f"Result: {result}", font=("Arial", 20))

    except ZeroDivisionError:
        messagebox.showerror("Error", "Division by zero is not allowed.")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

def reset():
    try:
        label_result.config(text="Result: ", font=("Arial", 20))
        
        entry_num1.delete(0, tk.END)
        entry_num1.insert(0, 0)

        entry_num2.delete(0, tk.END)
        entry_num2.insert(0, 0)
    except ValueError as e:
        messagebox.showerror("Error", str(e))


root = tk.Tk()
root.title("Bagi Membagi")

tk.Label(root, text="Number 1:", font=("Arial", 20)).pack()
entry_num1 = tk.Entry(root, font=("Arial", 20))
entry_num1.pack()

tk.Label(root, text="Number 2:", font=("Arial", 20)).pack()
entry_num2 = tk.Entry(root, font=("Arial", 20))
entry_num2.pack()

button_divide = tk.Button(root, text="Divide", command=divide_numbers, font=("Arial", 20))
button_divide.pack()

label_result = tk.Label(root, text="Result: ", font=("Arial", 20))
label_result.pack()

reset_button = tk.Button(root, text="Reset", command=reset, font=("Arial", 20))
reset_button.pack()

root.mainloop()