import tkinter as tk
from tkinter import messagebox
import math


def read_numbers():
    # Returns (a, b) as floats, or None (after showing a pop-up) if invalid.
    first = entry_first.get().strip()
    second = entry_second.get().strip()

    # Blank check
    if first == "" and second == "":
        messagebox.showerror("Input Error", "Both boxes are blank.\nPlease enter two numbers.")
        result.set("")
        entry_first.focus_set()
        return None
    if first == "":
        messagebox.showerror("Input Error", "The first number is blank.\nPlease enter a number.")
        result.set("")
        entry_first.focus_set()
        return None
    if second == "":
        messagebox.showerror("Input Error", "The second number is blank.\nPlease enter a number.")
        result.set("")
        entry_second.focus_set()
        return None

    # Letters / symbols check
    try:
        a = float(first)
    except ValueError:
        messagebox.showerror("Input Error",
                             "The first number '" + first + "' is not a valid number.\n"
                             "Please enter digits only (for example 4 or -2.5).")
        result.set("")
        entry_first.focus_set()
        return None

    try:
        b = float(second)
    except ValueError:
        messagebox.showerror("Input Error",
                             "The second number '" + second + "' is not a valid number.\n"
                             "Please enter digits only (for example 10 or 3.14).")
        result.set("")
        entry_second.focus_set()
        return None

    # float() accepts "nan" and "inf", so reject those too
    if not (math.isfinite(a) and math.isfinite(b)):
        messagebox.showerror("Input Error", "Please enter normal numbers (not nan or inf).")
        result.set("")
        return None

    return a, b


def fmt(value):
    # Show 14 instead of 14.0
    if value == int(value):
        return str(int(value))
    return str(round(value, 6))


def show(label, value):
    if not math.isfinite(value):
        messagebox.showerror("Calculation Error", "The result is too large to display.")
        result.set("")
    else:
        result.set(label + ": " + fmt(value))


def add():
    nums = read_numbers()
    if nums:
        show("Sum", nums[0] + nums[1])


def subtract():
    nums = read_numbers()
    if nums:
        show("Difference", nums[0] - nums[1])


def multiply():
    nums = read_numbers()
    if nums:
        show("Product", nums[0] * nums[1])


root = tk.Tk()
root.title("Calculator")

# ---- Labels ----
tk.Label(root, text="First\nnumber:").grid(row=0, column=0)
tk.Label(root, text="Second\nnumber:").grid(row=0, column=2)

# ---- Entry boxes (user input) ----
entry_first = tk.Entry(root, width=8)
entry_first.grid(row=1, column=0, padx=5)
entry_second = tk.Entry(root, width=8)
entry_second.grid(row=1, column=2, padx=5)

# ---- Buttons ----
tk.Button(root, text="+", width=3, command=add).grid(row=0, column=1, padx=10, pady=2)
tk.Button(root, text="-", width=3, command=subtract).grid(row=1, column=1, pady=2)
tk.Button(root, text="x", width=3, command=multiply).grid(row=2, column=1, pady=2)

# ---- Read-only Entry (result display) ----
result = tk.StringVar()
entry_result = tk.Entry(root, textvariable=result, width=25,
                        state="readonly", justify="center")
entry_result.grid(row=3, column=0, columnspan=3, pady=8, padx=5)

root.mainloop()