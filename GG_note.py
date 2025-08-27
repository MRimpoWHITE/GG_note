import tkinter as tk

def add_note():
    note = entry.get()
    if note:
        listbox.insert(tk.END, note)
        entry.delete(0, tk.END)

root = tk.Tk()
root.title("GG_note")

entry = tk.Entry(root, width=40)
entry.pack()

btn = tk.Button(root, text="Capture Your Spark", command=add_note)
btn.pack()

listbox = tk.Listbox(root, width=50, height=10)
listbox.pack()

root.mainloop()
