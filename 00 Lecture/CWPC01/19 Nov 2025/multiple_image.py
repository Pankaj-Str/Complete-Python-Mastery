import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Multiple Images Example")
root.geometry("600x600")


# function to load and resize image 
def load_image(path, width, height):
    img = Image.open(path)
    img = img.resize((width, height), Image.Resampling.LANCZOS) # Use LANCZOS for high-quality downsampling 
    return ImageTk.PhotoImage(img)


# Load multiple images
image01 = load_image("/Users/pankajchouhan/github/Complete-Python-Mastery/00 Lecture/CWPC01/19 Nov 2025/image/book.png", 150, 150)
image02 = load_image("/Users/pankajchouhan/github/Complete-Python-Mastery/00 Lecture/CWPC01/19 Nov 2025/image/img01.jpg", 150, 150)

# create labels to display images
tk.Label(root , image=image01, bd=2 , relief="solid").pack(pady=10)
tk.Label(root , image=image02, bd=2 , relief="solid").pack(pady=10)

# keep references to images
root.image01 = image01
root.image02 = image02

root.mainloop()