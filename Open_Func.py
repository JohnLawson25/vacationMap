from tkinter import filedialog

def open_file_dialog():
    global data
    global Current_User_Name
    """Opens a file dialog and prints the selected file path."""
    file_path = filedialog.askopenfilename(
        title="Select a file",
        initialdir="/",  # Optional: Set initial directory
        filetypes=(("Text files", "*.txt"), ("All files", "*.*")) # Optional: Filter file types
    )
    print(file_path)
    sub = "/"
    _, _, D_name = file_path.rpartition(sub)

    print(D_name)

    my_string = D_name
    delimiter = "."
    f_name = my_string.split(delimiter)[0]

    Current_User_Name = f_name
    file_path = f"{f_name}/{D_name}"  # '..' moves up one directory

    try:
        with open(file_path, 'r') as f:
            content = f.read()
            print(data)
            # data.update(content)
            new_dic = json.loads(content)
            print(new_dic)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")

    data.update(new_dic)
    print(data)
    Make_Map(data)