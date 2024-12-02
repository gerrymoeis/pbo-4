import tkinter as tk
from tkinter import messagebox

class BankAccount:
    def __init__(self):
        self.___balance = 0 # Private attribute

    def get_balance(self):
        return self.___balance

    def deposit(self, amount):
        if amount > 0:
            self.___balance += amount
        else:
            raise ValueError("Invalid deposit amount!")
    
    def reset_balance(self):
        self.___balance = 0
    
def add_balance():
    try:
        amount = int(entry_amount.get())
        account.deposit (amount)
        label_balance.config(text=f"Balance: {account.get_balance()}", font=("Arial", 20))
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def reset():
    try:
        account.reset_balance()
        label_balance.config(text=f"Balance: {account.get_balance()}", font=("Arial", 20))
        entry_amount.delete(0, tk.END)
        entry_amount.insert(0, 0)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# GUI Tkinter
root = tk.Tk()
root.title("Bank Toyyib")

account = BankAccount()
label_balance = tk.Label(root, text=f"Balance: {account.get_balance()}", font=("Arial", 20))
label_balance.pack()

entry_amount = tk.Entry(root, font=("Arial", 20))
entry_amount.pack()

button_deposit = tk.Button(root, text="Deposit", command=add_balance, font=("Arial", 20))
button_deposit.pack()

reset_button = tk.Button(root, text="Reset", command=reset, font=("Arial", 20))
reset_button.pack()

root.mainloop()