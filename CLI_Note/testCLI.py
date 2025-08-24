import json , os

notes = []

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "notes.json")

def save_notes():
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(notes, f, ensure_ascii=False)

def load_notes():
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    
notes = load_notes()
    
def show_notes():
    if not notes:
        print("\n   No notes available.")
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
    if len(notes) >= 1:
        num = int(input("\nEnter the number of the note to delete: "))
        if 1 <= num <= len(notes):
            notes.pop(num - 1)
            save_notes()
            print("\n     Note Deleted.")
        else:
            print("\n     No Note Number Detect.")


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
        input("\nTap Enter to Reboot the Hub...")
    elif choice == '2':
        add_note()
    elif choice == '3':
        delete_note()
    elif choice == '4':
        print("=========================")
        print("      Bye for Now       .")
        print("=========================")
        break
    else : 
        print("\nCan you read Bro? \n type again!")

    