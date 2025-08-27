import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
apps = []


def addApp():
    
    for widget in frame.winfo_children():
        widget.destroy()
    
    filename = filedialog.askopenfilename(initialdir="", title="Select File",
                                          filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app , fg="#00FF1E", bg="#747474")
        label.pack()
        
def runApps():
    for app in apps:
        os.startfile(app)
        
def deleteApps():
    
    for widget in frame.winfo_children():
        widget.destroy()


root.title("GG_Note :D")
           
canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File", padx=10, 
                     pady=5, fg="white", bg="#263D42", command=addApp)      #fg = font bg
openFile.pack()


runApps = tk.Button(root, text="Run Apps", padx=10, 
                     pady=5, fg="white", bg="#263D42", command=runApps)
runApps.pack()

delApps = tk.Button(root, text="Delete Apps", padx=10, 
                     pady=5, fg="white", bg="#263D42", command=deleteApps)
delApps.pack()

root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')