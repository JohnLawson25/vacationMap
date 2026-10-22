import tkinter as tk
from PIL import Image, ImageTk

current_image_index = 0


def Gallery_Popup():
    global image_list
    global image_paths
    global gallery_popup
    gallery_popup = tk.Toplevel()
    gallery_popup.geometry('800x600')

    image_paths = ["Ferrari.jpg", "McLaren.jpeg", "Alpine.jpeg"]
    image_list = []

    for path in image_paths:
        img = Image.open(path)
        img = img.resize((600, 400))  # Resize as needed
        image_list.append(ImageTk.PhotoImage(img))


    Gallery_label = tk.Label(gallery_popup, image=image_list[0])
    Gallery_label.pack()

    def next_image():
        global current_image_index
        current_image_index = (current_image_index + 1) % len(image_list)
        Gallery_label.config(image=image_list[current_image_index])

    def previous_image():
        global current_image_index
        current_image_index = (current_image_index - 1) % len(image_list)
        Gallery_label.config(image=image_list[current_image_index])

    # Gallery Buttons
    next_button = tk.Button(gallery_popup, text="next", command=next_image)
    next_button.pack(side=tk.RIGHT)
    previous_button = tk.Button(gallery_popup, text="previous", command=previous_image)
    previous_button.pack(side=tk.LEFT)

