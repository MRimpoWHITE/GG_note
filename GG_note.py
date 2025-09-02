import customtkinter as ctk
from customtkinter import *
from CTkListbox import *


ctk.set_appearance_mode("dark")      #เลือก ธีม
ctk.set_default_color_theme("blue")    

app = ctk.CTk()
app.title("GG_List Note")
app.geometry("1000x520")

app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(0, weight=1)

note_names = []
notes = []

# --------------------
# Save Note as File
# --------------------









# -------------
# function
# -------------

placeholder = "Write Your Story...."

def add_note():
    note_name = entry.get()
    if note_name != "":
        note_names.append(note_name)
        notes.append("")
        listbox.insert(END, note_name)
        entry.delete(0, END)

def delete_task():
    selected = listbox.curselection()
    if selected is not None and selected !="":
        index =  int(selected)
        listbox.delete(index)
        note_names.pop(index)  # ต้อง cast เป็น int ด้วย
        note_text.delete("1.0", "end")   # ล้างช่อง note ด้วย
        
def show_task(event):
    selected = listbox.curselection()
    if selected is not None and selected !="":
        index = int(selected)
        note_text.delete("1.0", "end")
        note_text.insert("1.0", notes[index])
        
        if notes[index].strip() == "":
            note_text.insert("1.0", placeholder, "placeholder")
            note_text.tag_add("placeholder", "1.0", "end")
        # else:
        #     note_text.insert("1.0", notes[index])
        
        print(note_names[index])
        print(notes[index])

def save_task():
    selected = listbox.curselection()
    if selected is not None and selected !="":
        index = int(selected)
        new_text = note_text.get("1.0", "end-1c")
        notes[index] = new_text
        print("note_saved")
    
        
# ----------------------
# Placeholder functions
# ----------------------
        
def clear_placeholder(event):                             
    if note_text.get("1.0", "end-1c") == placeholder:
        note_text.delete("1.0", "end")
        note_text.tag_remove("placeholder", "1.0", "end")
        
def add_placeholder(event):
    if note_text.get("1.0", "end-1c").strip()== "":
        note_text.insert("1.0", placeholder, "placeholder")
        note_text.tag_add("placeholder", "1.0", "end")


# ----------------------
# Widgets    // Frame 1
# ----------------------       

frame1 = ctk.CTkFrame(app, width=60)
frame1.grid(row=0, column=0, pady=20, padx=20, sticky="nsew")

entry = ctk.CTkEntry(frame1, placeholder_text="Name Your Journey")
entry.pack(pady=10, fill="x")

add_button = ctk.CTkButton(frame1, text="Capture Your Spark", command=add_note)
add_button.pack(pady=5)

del_button = ctk.CTkButton(frame1, text="Purge the Record", command=delete_task)
del_button.pack(pady=5)

listbox = CTkListbox(frame1)
listbox.pack(pady=10, fill="both", expand=True)
listbox.bind("<<ListboxSelect>>", show_task)

# ----------------------
# Widgets    // Frame 2
# ----------------------    

frame2 = ctk.CTkFrame(app)
frame2.grid(row=0, column=1, pady=20, padx=20, sticky="nsew")

# ---------------------
# Note     // Frame 2
# ---------------------

note_text = ctk.CTkTextbox(frame2)
note_text.pack(pady=10, fill="both", expand=True)
# ตั้งค่า tag สำหรับ placeholder
note_text.tag_config("placeholder", foreground="gray")   #เปลี่ยนสี
note_text.insert("1.0", placeholder, "placeholder")
note_text.tag_add("placeholder", "1.0", "end")
# bind event focus
note_text.bind("<FocusIn>", clear_placeholder)          
note_text.bind("<FocusOut>", add_placeholder)          


save_button = ctk.CTkButton(frame2, text="Save", command=save_task)
save_button.pack(pady=5)

# -------------
# Run app
# -------------

app.mainloop()
