import note_functions as nf
temp="123"
db = []
print("Hello frend")
while True:
    command=str(input("Print command \t[create_user] [create_user_note] [read_users] [read_user_notes] \n\t\t\t\t[update_user_note] [del_user_note] [del_user_notes] [exit] :"))
    if command=="create_user":
        name=input("Enter your name :")
        password=input("Enter your password :")
        nf.create_user(db,name,password)

    elif command == "create_user_note":
        note=input("Enter your note :")
        nf.create_user_note(db,name,password,note)

    elif command == "read_users":
        nf.read_users(db)
    elif command == "read_user_notes":
        name = input("What users notes you want read :")
        nf.read_user_notes(db,name)
    elif command == "update_user_note":
        new_note = input("Enter new note :")
        old_note = input("Enter old note :")
        try:
            nf.update_user_note(db,name,old_note,new_note)
        except:
            print("except !!!try again")
        finally: new_note = input("Enter new note :")
        old_note = input("Enter old note :")
        try:
            nf.update_user_note(db,name,old_note,new_note)
        except:
            print("except !!!again")
        finally:
            print("you got dont remember")

    elif command=="del_user_note":
        # (data_base, name, del_note, password)
        name = input("Attention!! Enter your name :")
        password = input("Attention!! Enter your password :")

        del_note = input(" Enter note to erase :")
        nf.del_user_note(db,name,del_note,password)
    elif command=="del_user_notes":

        name = input("Attention!! Enter your name :")
        password = input("Attention!! Enter your password :")
        yes=input(f"Attention!! {name} you want erase all your's notes - Yes/NO : ")
        if yes=="Yes":
            nf.del_user_notes_all(db,name,password)

        else:
            print("no deleted")

    elif command == "exit":
        break


