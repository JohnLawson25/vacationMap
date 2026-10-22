import plotly.io as pio
import plotly.express as px
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import pandas as pd
import sys
import os
import json
from Load_Profile_Pic import load_profile_pic
import shutil
from tkinter import filedialog
from Open_Func import open_file_dialog
from pathlib import Path


#Variables
filename = ""
current_country = ""
global User_Data
User_Data = {}
List = []
global Profile_label
global new_data
new_data = {'country': [], 'value': []}
global data
data = {"country": [], "value": []}
country_list = []
Country_pick = []
global Current_Country



user_name = "Jinkens"
global Current_User_Name
Current_User_Name = ""
Directory_name = user_name
current_image_index = 0
from Pic_Gallery import Gallery_Popup
Profile_img = Image.open("Profile_pic4.png")
User_countries = ['country', 'value']
title_text = "Start your Adventure"
Map_label = None

def Make_Map(content):
    df = pd.DataFrame(content)
    df.columns = ['country', 'value']
    #print(df.columns)
    print(len(df.columns))

    fig = px.choropleth(df,
                        locations='country',
                        locationmode='country names',  # or 'ISO-3' if using ISO codes
                        color='value',
                        #hover_name='country',
                        color_continuous_scale=px.colors.sequential.Plasma)

    pio.write_image(fig, "new_image.png")
    #update_image()

# Popup to add country - update List + Note fields + Adds country to Map
def popup():
    Popup = tk.Toplevel()
    Popup.geometry('315x120')

    label = tk.Label(Popup, text="Add a Country: ")
    label.grid(row=1, column=1)

    entry = tk.Entry(Popup)
    entry.grid(row=2, column=2)

    Popup_Submit = tk.Button(Popup, text="Add Country", command=lambda: [get_input(), update_image()])
    Popup_Submit.grid(row=3, column=0)


    def get_input():
        user_input = entry.get()
        Country_pick.append(user_input)
        List.delete(0, tk.END)  # Clear all existing items
        for item in Country_pick:
            List.insert(tk.END, item)  # Insert new items

        data['country'].append(user_input)
        data['value'].append(15)
        print(data['country'], " ", data['value'])
        with open(f"{user_name}/{user_input}", "w+") as N:
            N.write("Work it out ")
            # Notes.config(text=N.read())
            N.close()

        print(data['country'])
        print(data['value'])
        Make_Map(data)
        Popup.destroy()


def update_image():
    global Map_label
    global Map
    # Load the new image (replace 'start_image.png' with your image path)
    new_image = Image.open("new_image.png")
    Map = ImageTk.PhotoImage(new_image)
    Map_label.config(image=Map)
    Map_label.image = Map


def load_text_file_into_label():
    with open(f"{user_name}/Country_notes.txt", 'r') as Notes_file:
        content = Notes_file.read()
        Notes_Text.delete("1.0", tk.END)
        Notes_Text.insert(tk.END, content)

def load_Hotel_file_into_label():
    with open(f"{user_name}/Hotel.txt", 'r') as Notes_file:
        content = Notes_file.read()
        Notes_Text.delete("1.0", tk.END)
        Notes_Text.insert(tk.END, content)

def load_Restraunt_file_into_label():
    with open(f"{user_name}/Restraunt.txt", 'r') as Notes_file:
        content = Notes_file.read()
        Notes_Text.delete("1.0", tk.END)
        Notes_Text.insert(tk.END, content)

# Get country name + load notes when click on list
def load_txt_on_listbox_click(event):
    CN = List.curselection()

    index = CN[0]
    # Get the text of the selected item (which should be the filename)
    global filename
    filename = List.get(index)
    global Current_Country
    Current_Country = filename
    print(filename)

    for i in CN:
        if i >= 0:
            print("Yes!")
            with open(filename, 'r+') as Notes_load:
                Data = Notes_load.read()
                Notes_Text.delete(1.0, tk.END)
                Notes_Text.insert(tk.END, Data)

def Upload_Pics():
    """Opens a file dialog and prints the selected file path."""
    file_path = filedialog.askopenfilename(
        title="Select a file",
        initialdir="/",  # Optional: Set initial directory
        filetypes=(("Text files", "*.txt"), ("All files", "*.*"))  # Optional: Filter file types
    )
    print(file_path)
    #try:
    dir_name = f"{user_name}/Pics"
    os.mkdir(dir_name)
    print(f"File {dir_name} created successfully")
    #except FileExistsError:
        #print(f"{dir_name} already exists")
    shutil.copy(file_path, dir_name )



#Assign User name to profile



def Save_User_Notes():
    Text_content = Notes_Text.get("1.0", "end-1c")
    with open(f"{user_name}/{current_country}{filename}", "w") as F:
        F.write(Text_content)
        F.close()

def start_new_data():
    global User_Data
    global new_data
    Make_Map(new_data)

def load_data_profile():
    global User_Data
    global data
    Make_Map(data)


def create_new_directory():

    # 1. Ask the user for the parent folder
    parent_dir = filedialog.askdirectory(title='Select Parent Folder')
    try:
        dir_name = f"{parent_dir}/{user_name}"
        os.mkdir(dir_name)
        print(f"File {dir_name} created successfully")
    except FileExistsError:
        print(f"{dir_name} already exists")

def create_new_dir_simple():
    global user_name
    try:
        dir_name = f"{user_name}"
        os.mkdir(dir_name)
        print(f"File {dir_name} created successfully")
    except FileExistsError:
        print(f"{dir_name} already exists")


def save_file_dialog():
    # Define file types for the dialog
    filetypes = (
        ('Text files', '*.txt'),
        ('All files', '*.*')
    )

    # asksaveasfile returns an opened file object
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",  # Default extension if user doesn't specify
        filetypes=filetypes,
        title="Save File As"
    )
    # User selected a file, now you can save your data to 'filepath'
    dir_name = f"{user_name}"
    try:
        os.mkdir(dir_name)
        print(f"File {dir_name} created successfully")
        with open(file_path, "w") as f:
            f.write(f"{data}")
    except FileExistsError:
        print(f"{dir_name} already exists")
        with open(file_path, "w") as f:
            f.write(f"{data}")
    print(f"File saved to: {file_path}")


# What needs saved?
# country names list to reproduce map + Color code
# Profile Name
# link to photos and notes through profile name on save.

def load_file_dialog():
    global List

    # Define file types for the dialog
    filetypes = (
        ('Text files', '*.txt'),
        ('All files', '*.*')
    )

    # asksaveasfile returns an opened file object
    file_path = filedialog.askopenfilename(
        defaultextension=".txt",  # Default extension if user doesn't specify
        filetypes=filetypes,
        title="Load Profile"
    )
    # User selected a file, now you can extract data 'filepath'
    global User_countries
    global title_text
    with open(file_path, "r") as f:
        content = json.load(f)

    nations = content['country']
    for i in nations:
        List.insert(0, i)

    proj = Path(file_path)
    proj_name = proj.parts[-2]
    print(content)
    Make_Map(content)
    update_image()

    Title_Label.config(text=f"{proj_name}'s World Travel Map")

    #notes : Check some notes on my Test}



    print(f"File loaded from: {file_path}")



#Menubar
def open_file():
    print("Open File clicked")

def save_file():
    print("Save File clicked")
    save_file_dialog()

def exit_app():
    root.quit()

#def open_main_app():
    #splash_root.destroy()  # Close the splash screen

#Initalize GUI Window
root = tk.Tk()
#global user_name
my_string_var = tk.StringVar(root)
root.title("World Skratch Map")
root.geometry("1200x600")
user_name = "Jinkens"

def User_name_popup():
    global user_name

    UN_popup = tk.Toplevel()
    UN_popup.geometry('315x120')

    UNlabel = tk.Label(UN_popup, text="Enter Name: ")
    UNlabel.grid(row=1, column=1)

    UNentry = tk.Entry(UN_popup)
    UNentry.grid(row=2, column=2)

    UN_popup_submit = tk.Button(UN_popup, text="Submit", command=lambda: [get_username()])
    UN_popup_submit.grid(row=3, column=0)

    def get_username():
        global user_name
        user_name = UNentry.get()
        print(user_name)
        UN_popup.destroy()
        print("Printing from Level 2 inside")
        Title_Label.config(text=f"{user_name}'s World Adventure")
        #return user_name
        print(user_name)
        create_new_dir_simple()

def Upload_Profile_Pic():
    """Opens a file dialog and prints the selected file path."""
    profile_path = filedialog.askopenfilename(
        title="Select a file",
        initialdir="/",  # Optional: Set initial directory
        filetypes=(("Text files", "*.txt"), ("All files", "*.*"))  # Optional: Filter file types
    )

    dir_name = f"{user_name}/ProfilePics"
    try:
        os.mkdir(dir_name)
        print(f"File {dir_name} created successfully")
        shutil.copy(profile_path, dir_name)
    except FileExistsError:
        print(f"{dir_name} already exists")
        shutil.copy(profile_path, dir_name)

    def set_profile_pic():
        newProfile_img = Image.open(profile_path)
        #resize
        resize_img = newProfile_img.resize((286, 200), Image.LANCZOS)
        pro_img = ImageTk.PhotoImage(resize_img)
        print(profile_path)
        Profile_label.config(image=pro_img)
        Profile_label.image_ref = pro_img
    set_profile_pic()


#Menubar
menubar = tk.Menu(root)
root.config(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)

profile_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Profile", menu=profile_menu)

file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=create_new_directory)
file_menu.add_separator()

profile_menu.add_command(label="Change Name", command=User_name_popup)
profile_menu.add_command(label="Load Profile Pic", command=User_name_popup)

#Title Bar
#global user_name
Title_Label = tk.Label(root, text="World Adventure Map", font=("Arial", 20, "bold"))
Title_Label.place(x=50, y=0)

#Load Map Image
Map = Image.open("start_image.png")
Map_image = ImageTk.PhotoImage(Map)
#global Map_label
Map_label = tk.Label(root, image=Map_image)
Map_label.place(x=0, y=30)

#global Profile_img
Profile_pic = ImageTk.PhotoImage(Profile_img)
Profile_label = tk.Label(root, image=Profile_pic)
Profile_label.place(x=800 , y=0)

#Frame to hold Notes ect.
frame = tk.Frame(root, bg='lightblue', height = 1100, width=600)
frame.place(x=800, y=300)

frame_Buttons = tk.Frame(root, bg='lightblue')
frame_Buttons.place(x=800, y=200)

#Buttons

Load_profile_button = tk.Button(root, text="Load Pic", command=Upload_Profile_Pic)
Load_profile_button.place(x=1000, y=0)

Add_button = tk.Button(root, text="Add County", command=popup)
Add_button.place(x=315, y =520 )

load_Button = tk.Button(root, text="Load Map", command=lambda: [load_file_dialog()])
load_Button.place(x=315, y=480)

Save_Button = tk.Button(root, text="Save Project", command=save_file_dialog)
Save_Button.place(x=315, y=440)

Upload_Pic_Button = tk.Button(root, text="Upload Picture", command=Upload_Pics)
Upload_Pic_Button.place(x=315, y=400)

Save_Notes = tk.Button(frame, text="Save Notes", command=Save_User_Notes)
Save_Notes.pack(side=tk.BOTTOM)

Notes_Button = tk.Button(frame_Buttons, text="Country Notes", command=load_text_file_into_label)
Notes_Button.pack(side=tk.LEFT)

Pics_Button = tk.Button(frame_Buttons, text="Pictures", command=Gallery_Popup)
Pics_Button.pack(side=tk.LEFT)

Hotel_Button = tk.Button(frame_Buttons, text='Hotels', command=load_Hotel_file_into_label)
Hotel_Button.pack(side=tk.LEFT)

Restraunts_Button = tk.Button(frame_Buttons, text='Restraunts', command=load_Restraunt_file_into_label)
Restraunts_Button.pack(side=tk.LEFT)

#Country Listbox
#global List
List = tk.Listbox(root)
for item in country_list:
    List.insert(tk.END, item)
List.bind('<Double-1>', load_txt_on_listbox_click)
List.place(x= 400, y=407)


#Country Notes Title label
Notes_title = tk.Label(frame, text='Country Notes: ')
Notes_title.pack(side=tk.TOP)


#Notes TextBox to replace label
global Notes_Text
Notes_Text = tk.Text(frame, height= 15, width = 40)
load_text_file_into_label()
Notes_Text.pack()


root.mainloop()

# # Create the splash screen window
# splash_root = tk.Tk()
# splash_root.title("Loading...")
# splash_root.geometry("300x150")
# splash_root.overrideredirect(True)  # Remove window decorations for a cleaner splash screen
#
# # Center the splash screen (optional)
# screen_width = splash_root.winfo_screenwidth()
# screen_height = splash_root.winfo_screenheight()
# x = (screen_width // 2) - (300 // 2)
# y = (screen_height // 2) - (150 // 2)
# splash_root.geometry(f"800x550")
#
# title = Image.open("benefits-seeing-world.jpg")
# splash_img =  ImageTk.PhotoImage(title)
#
# splash_label = tk.Label(splash_root,image=splash_img)
# splash_label.place(x=0, y=0)
#
# splash_start_Button = tk.Button(splash_root, text="New Map", command=lambda: [start_new_data(), open_main_app()])
# splash_start_Button.pack(pady=20)
#
# splash_load_Button = tk.Button(splash_root, text="Load Map", command=lambda: [load_file_dialog(), open_main_app()])
# splash_load_Button.pack(pady=20)
#
# # Schedule the main window to open after a delay (e.g., 2000 milliseconds = 2 seconds)
# #splash_root.after(2000, open_main_window)
#
# splash_root.mainloop()
