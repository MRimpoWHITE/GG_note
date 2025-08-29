# import tkinter as tk
# from tkinter import filedialog, Text
# import os

# def add_note():
#     note = entry.get()
#     if note:
#         listbox.insert(tk.END, note)
#         entry.delete(0, tk.END)

# root = tk.Tk()
# root.title("GG_note")

# canvas =tk.Canvas(root, height=700, width=700, bg="#ffffff")
# canvas.pack(side=tk.RIGHT , fill="both",expand=True )

# entry = tk.Entry(root, width=40)

# entry.pack()

# btn = tk.Button(root, text="Create Your Journey", command=add_note)
# btn.pack()

# listbox = tk.Listbox(root, width=50, height=20)
# listbox.pack(expand=True, fill="both" )

# root.mainloop()




import customtkinter as ctk

ctk.set_appearance_mode("dark")      #กำหนด ธีม light , dark , system
ctk.set_default_color_theme("blue")    # ธีมสี

app = ctk.CTk()
app.title("GG_List Note")
app.geometry("400x400")

app.mainloop()