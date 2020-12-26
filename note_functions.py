# Create user

def create_user(data_base, name,password):

    l = list()
    l.insert(0, name)
    l.insert(1, password)
    data_base.append(l)
    # print(l)
    return data_base

#Create note
def create_user_note(data_base, name,password, note):
    for i in range(len(data_base)):
        if data_base[i][0] == name and data_base[i][1] == password:
            data_base[i].append(note)
            # print(data_base)
            break

    return note

#Read Users
def read_users(data_base):
    print('User ID\t\tUser Name')
    for i in range(0,len(data_base)):
        print(f'\t{i}\t\t{data_base[i][0]}')

def read_user_notes(data_base, name):

    print('User ID\t\tUser Name\t\tNotes')
    for i in range(len(data_base)):
        if data_base[i][0] == name:
            for j in range(2, len(data_base[i])):
             print(f'\t{i}\t\t{data_base[i][0]}\t\t\t\t{data_base[i][j]}')






#Update Note
def update_user_note(data_base,name,old_note,new_note):

        for i in range(len(data_base)):
            if data_base[i][0] == name:
                for j in range(1, len(data_base[i])):
                    if data_base[i][j] == old_note:
                        data_base[i][j] = new_note
                        # print(data_base)

                        return new_note



def del_user_note(data_base,name,del_note,password):

        for i in range(len(data_base)):
            if data_base[i][0] == name and data_base[i][1] == password:
                for j in range(1, len(data_base[i])):
                    if data_base[i][j] == del_note:
                        del data_base[i][j]
                        # data_base[i][j] = ""
                        # print(data_base)
                        return data_base


def del_user_notes_all(data_base, name, password):
    for i in range(len(data_base)):
        if data_base[i][0] == name and data_base[i][1] == password:
            for j in range(1, len(data_base[i])):
                for j in range(1, len(data_base[i])):
                  del data_base[i][2:]

                # print(data_base)
                return data_base
