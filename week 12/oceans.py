import os
import tkinter as tk
from tkinter import messagebox

# Build the path from this file's location so it works from any folder
FILENAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "oceans.txt")


def load_oceans(filename):
    # Returns a sorted list of ocean names, or raises ValueError with a message.
    try:
        with open(filename, "r", encoding="utf-8-sig") as f:
            lines = f.readlines()
    except FileNotFoundError:
        raise ValueError("File 'oceans.txt' not found.\nPut it in the same folder as oceans.py.")
    except PermissionError:
        raise ValueError("No permission to read 'oceans.txt'.")
    except UnicodeDecodeError:
        raise ValueError("'oceans.txt' is not a valid text file.")
    except OSError:
        raise ValueError("Could not read 'oceans.txt'.")

    names = []
    for line in lines:
        name = line.strip()
        if name and name.lower() not in [n.lower() for n in names]:
            names.append(name)

    if not names:
        raise ValueError("'oceans.txt' contains no oceans.")

    return sorted(names, key=str.lower)


def show_oceans():
    # Runs when the button is clicked: read the file, then fill the blank box.
    try:
        oceans = load_oceans(FILENAME)
    except ValueError as err:
        messagebox.showerror("File Error", str(err))
        listbox.delete(0, tk.END)   # leave the box blank
        return

    # Clear old items so repeated clicks don't create duplicates
    listbox.delete(0, tk.END)
    for ocean in oceans:
        listbox.insert(tk.END, ocean)

  
root = tk.Tk()
root.title("Oceans")
root.columnconfigure(0, weight=1)

# ---- 1. Label ----
tk.Label(root, text="Oceans").grid(row=0, column=0, pady=(10, 2))

# ---- 2. Blank box (list box + scrollbar) ----
list_frame = tk.Frame(root)
list_frame.grid(row=1, column=0, padx=60, pady=5)

scrollbar = tk.Scrollbar(list_frame, orient="vertical", width=14)
listbox = tk.Listbox(list_frame, height=4, width=12,
                     exportselection=False,
                     activestyle="underline",
                     selectbackground="#0078d7",
                     selectforeground="white",
                     yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

listbox.grid(row=0, column=0)
scrollbar.grid(row=0, column=1, sticky="ns")

# ---- 3. Button ----
tk.Button(root, text="Show Oceans", command=show_oceans).grid(
    row=2, column=0, pady=(5, 10))

root.mainloop()