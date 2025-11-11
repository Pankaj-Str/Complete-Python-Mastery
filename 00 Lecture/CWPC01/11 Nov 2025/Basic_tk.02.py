import tkinter as tk
from tkinter import messagebox

def submit():
    name = entry_name.get()
    if name:
        messagebox.showinfo("Greeting",f"hello{name}")
    else:
        messagebox.showwarning("Empty","please type your name.")
        
root = tk.Tk()

root.title("Hello Welcome to codes with pankaj")
root.geometry("400x300")

tk.Label(root,text="Your Name : ").pack(padx=5)
entry_name = tk.Entry(root,width=30)
entry_name.pack(padx=5)

tk.Button(root,text="Say hello",command=submit).pack(pady=10)
root.mainloop()