import tkinter as tk
from tkinter import filedialog, Text
import os

def add_note():
    note = entry.get()
    if note:
        listbox.insert(tk.END, note)
        entry.delete(0, tk.END)

root = tk.Tk()
root.title("GG_note")

canvas =tk.Canvas(root, height=700, width=700, bg="#ffffff")
canvas.pack(side=tk.RIGHT)

entry = tk.Entry(root, width=40)
entry.pack()

btn = tk.Button(root, text="Capture Your Spark", command=add_note)
btn.pack()

listbox = tk.Listbox(root, width=50, height=20)
listbox.pack(side=tk.RIGHT)

root.mainloop()
