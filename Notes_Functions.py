def load_Hotels():
    with open(f"{Current_User_Name}/{Current_Country}_Hotels", 'r+') as Notes_load:
        Data = Notes_load.read()
        Notes_Text.delete(1.0, tk.END)
        Notes_Text.insert(tk.END, Data)
        print(Current_Country)
        print(Current_User_Name)

def load_Restraunts():
    with open(f"{Current_User_Name}/{Current_Country}_Restraunts", 'r+') as Notes_load:
        Data = Notes_load.read()
        Notes_Text.delete(1.0, tk.END)
        Notes_Text.insert(tk.END, Data)
        print(Current_Country)
        print(Current_User_Name)