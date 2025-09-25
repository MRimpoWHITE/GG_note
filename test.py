import customtkinter as ctk
from customtkinter import *
from CTkListbox import *
import os










#====================หน้าต่างโปรแกรม================================================================

class GG_NoteApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("GG Note")     #ชื่อโปรแกรม
        self.geometry("1000x520")      #ขนาดหน้าต่าง  
        ctk.set_appearance_mode("dark")      #เลือก ธีม
        ctk.set_default_color_theme("blue")
        
        #ตั้งค่า grid หลัก 
        self.grid_columnconfigure(0, weight=0)  # ซ้าย fixed (หรือ 1 ถ้าอยากให้ขยายทั้งคู่)
        self.grid_columnconfigure(1, weight=1)  # ขวาขยายเต็ม
        self.grid_rowconfigure(0, weight=1)    # ขยาย vertically   

        # Create Frame ซ้าย
        self.createnote_frame = ctk.CTkFrame(self, width=350)
        self.createnote_frame.grid(row=0, column=0, sticky="nsew")

        self.createnote_frame.grid_rowconfigure(0, weight=0)
        self.createnote_frame.grid_rowconfigure(1, weight=1)  # ปรับ row 0 ให้ขยาย (แทน row 1)
        self.createnote_frame.grid_columnconfigure(0, weight=1)  # entry ขยาย
        self.createnote_frame.grid_columnconfigure(1, weight=0)  # button fixed
        
        #สร้างโน๊ต
        self.createnote_label = ctk.CTkEntry(self.createnote_frame, placeholder_text="Name Your Journey....", width=250)  # ลบ width เพื่อให้ขยาย
        self.createnote_label.grid(row=0, column=0, padx=10, pady=10, sticky="ew")  # ew เพื่อขยายแนวนอน

        #ปุ่มแอดโน๊ต
        self.add_button = ctk.CTkButton(self.createnote_frame, width=50,text="Add Note") #, command=self.add_note
        self.add_button.grid(row=0, column=1, pady=10, padx=10)  # เพิ่ม padx ให้ห่างนิด
        
        #หน้าต่างเลือกโน๊ต
        self.note_list = CTkListbox(self.createnote_frame)
        self.note_list.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        
        

        # Create the NOTE FRAME
        self.note_frame = ctk.CTkFrame(self)
        self.note_frame.grid(row=0, column=1, sticky="nsew")

        self.note_frame.grid_rowconfigure(0, weight=1)  # เพิ่มเพื่อให้ textbox ขยาย vertically
        self.note_frame.grid_columnconfigure(0, weight=1)  # เพิ่มเพื่อให้ textbox ขยาย horizontally

        self.note_text = ctk.CTkTextbox(self.note_frame)
        self.note_text.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        #self.note_text.insert("1.0", "Write Your Story....")

if __name__ == "__main__":
    app = GG_NoteApp()
    app.mainloop()