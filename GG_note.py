import customtkinter as ctk
from customtkinter import *
from CTkListbox import *

ctk.set_appearance_mode("dark")      #กำหนด ธีม light , dark , system
ctk.set_default_color_theme("blue")    # ธีมสี

app = ctk.CTk()
app.title("GG_List Note")
app.geometry("400x400")

tasks = []

# ----------------------
# function
# ----------------------

def add_task():
    task = entry.get()
    if task != "" :
        tasks.append(task)
        listbox.insert(END, task)
        entry.delete(0, END )    

def delete_task():
    selected = listbox.curselection()
    if selected is not None :
        index = selected
        print(index)
        listbox.delete(index)
        tasks.pop(index)

# ----------------------
# Widgets
# ----------------------       

frame1 = ctk.CTkFrame(app)
frame1.pack(pady=20, padx=20, fill="both", expand=True)

entry = ctk.CTkEntry(frame1, placeholder_text="Name Your Journey")
entry.pack(pady=10, fill="x")

add_button = ctk.CTkButton(frame1, text="Add", command=add_task)
add_button.pack(pady=5)

del_button = ctk.CTkButton(frame1, text="Delete", command=delete_task)
del_button.pack(pady=5)





listbox = CTkListbox(frame1, height=200)
listbox.pack(pady=10, fill="both", expand=True)


# ----------------------
# Run app
# ----------------------


app.mainloop()