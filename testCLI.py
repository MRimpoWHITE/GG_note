notes = []

def show_notes():
    if not notes:
        print("No notes available.")
    else:
        for i, note in enumerate(notes, 1):
            print(f"{i}. {note}")

def add_note(note):
    note = input("Enter your note: \n")
    notes.append(note)

def delete_note():
    show_notes()
    num = int(input("Enter the number of the note to delete: \n"))
    if 1 <= num <= len(notes):
        notes.pop(num - 1)
    else:
        print("Invalid note number.")


while True:
    print("---- GG_Notes -----")
    print("1. View Your Vault")
    print("2. Capture Your Spark")   
    print("3. Purge the Record")
    print("4. Eject Now")

    choice = input("Make Your Move : \n")    
