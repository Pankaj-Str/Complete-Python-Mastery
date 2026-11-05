import tkinter as tk
from PIL import Image, ImageTk # for image handling (pillow = pip install pillow)

root = tk.Tk()
root.title("Image Example")
root.geometry("400x400")
root.config(bg="#f0f0f0")

# step 1 using label image 

Image  = Image.open("/Users/pankajchouhan/github/Complete-Python-Mastery/00 Lecture/CWPC01/19 Nov 2025/image/book.png")
photo = ImageTk.PhotoImage(Image)

# add text label
tk.Label(root, text="Book Image Example", bg="#f0f0f0", font=("Arial", 16)).pack(pady=10)

label = tk.Label(root, image=photo, bg="#f0f0f0")
label.image_names = photo  # keep a reference!
label.pack(pady=20) 

root.mainloop()

