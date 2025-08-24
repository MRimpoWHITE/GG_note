import json

notes = []


def save_notes():
    with open("note/notes.json", "w", encoding="utf-8") as f:
        json.dump(notes, f, ensure_ascii=False)

def load_notes():
    try:
        with open("note/notes.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    
def show_notes():
    if not notes:
        print("\nNo notes available.")
    else:
        print("\n=== Here you go ===")
        for i, note in enumerate(notes, 1):
            print(f"{i}. {note}")
        print("===================")

def add_note():
    note = input("\nEnter your note: ")
    notes.append(note)
    save_notes()

def delete_note():
    show_notes()
    num = int(input("\nEnter the number of the note to delete: "))
    if 1 <= num <= len(notes):
        notes.pop(num - 1)
        save_notes()
    else:
        print("No Note number detect.")

notes = load_notes()


while True:
    print("\n=========================")
    print("---- GG_Notes -----")
    print("1. View Your Vault")
    print("2. Capture Your Spark")   
    print("3. Purge the Record")
    print("4. Eject Now")
    print("=========================\n")
    choice = input("Make Your Move : ")    
    

    if choice == '1':
        show_notes()
    elif choice == '2':
        add_note()
    elif choice == '3':
        delete_note()
    elif choice == '4':
        print("=========================")
        print("Bye for Now.")
        break
    else : 
        print("\nCan you read Bro? \n type again!")