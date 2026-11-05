import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Multiple Images Example")
root.geometry("600x600")


def on_click():
    label.config(text="Button Clicked!")
    
    
# load image for button 
btn_img = Image.open("/Users/pankajchouhan/github/Complete-Python-Mastery/00 Lecture/CWPC01/19 Nov 2025/image/book.png").resize((100, 100), Image.Resampling.LANCZOS)
btn_photo = ImageTk.PhotoImage(btn_img)

# create a image button 
Image_button = tk.Button(root, image=btn_photo, command=on_click , borderwidth=2)
Image_button.image = btn_photo  # keep a reference!
Image_button.pack(pady=20)

# label to show click result
label = tk.Label(root, text="Click the Button Above", font=("Arial", 14))
label.pack(pady=10)

root.mainloop()

    