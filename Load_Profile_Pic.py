import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def load_profile_pic():
    global Profile_label
    """Opens a file dialog and prints the selected file path."""
    file_path = filedialog.askopenfilename(
        title="Select a file",
        initialdir="/",  # Optional: Set initial directory
        filetypes=(("Text files", "*.txt"), ("All files", "*.*")) # Optional: Filter file types
    )
    print(file_path)

    global Profile_label
    # Load the new image (replace 'start_image.png' with your image path)
    user_pic = Image.open("start_image.png")
    Profile_Pic = ImageTk.PhotoImage(user_pic)
    Profile_label.config(image=Profile_Pic)
    Profile_label.image = Profile_Pic