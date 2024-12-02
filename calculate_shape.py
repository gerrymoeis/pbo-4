import tkinter as tk
from tkinter import messagebox
from math import pi

class Shape:
    def area(self):
        return "Not implemented"
    def perimeter(self):
        return "Not implemented"

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

class Circle(Shape):
    def __init__(self, radius): 
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * pi * self.radius


root = tk.Tk()
root.title("Kalkulasi Bentuk2")

shape_var = tk.StringVar(value="Rectangle")

tk.Radiobutton (root, text="Rectangle", variable=shape_var, value="Rectangle", font=("Arial", 20)).pack()
tk.Radiobutton (root, text="Circle", variable=shape_var, value="Circle", font=("Arial", 20)).pack()

tk.Label(root, text="Parameter 1:", font=("Arial", 20)).pack()
entry_param1 = tk.Entry(root, font=("Arial", 20))
entry_param1.pack()

tk.Label(root, text="Parameter 2 (if Rectangle):", font=("Arial", 20)).pack()
entry_param2 = tk.Entry(root, font=("Arial", 20))
entry_param2.pack()

def calculate():
    try:
        shape_type = shape_var.get()
        if shape_type == "Rectangle":
            shape = Rectangle(int(entry_param1.get()), int(entry_param2.get()))
        elif shape_type == "Circle":
            shape = Circle(int (entry_param1.get()))
        else:
            raise ValueError("Invalid shape")
        
        label_result.config(text=f"Area: {shape.area()}, Perimeter: {shape.perimeter()}", font=("Arial", 20))
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def reset():
    try:
        label_result.config(text="Area:, Perimeter: ", font=("Arial", 20))
        
        entry_param1.delete(0, tk.END)
        entry_param1.insert(0, 0)

        entry_param2.delete(0, tk.END)
        entry_param2.insert(0, 0)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

button_calculate = tk.Button(root, text="Calculate", command=calculate)
button_calculate.pack()

label_result = tk.Label(root, text="Area:, Perimeter: ", font=("Arial", 20))
label_result.pack()

reset_button = tk.Button(root, text="Reset", command=reset, font=("Arial", 20))
reset_button.pack()

root.mainloop()