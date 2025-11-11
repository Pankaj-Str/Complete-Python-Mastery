# label , button , entry , text

import tkinter as tk
from tkinter import messagebox


def submit_data():
    name = entry.get()
    notes = text.get("1.0","end").strip()
    if name:
        messagebox.showinfo("Success",f"Hello {name} \n Notes : {notes or 'None'}")
    else:
        messagebox.showwarning("Error","Name is required !")

root = tk.Tk()
root.title("Demo")
root.geometry("400x300")
root.configure(padx=15,pady=15)

# 1 label + Entry (Name)
tk.Label(root,text="Your Name :",font=("Arial",15)).grid(row=0,column=0,sticky="e",pady=5)
entry = tk.Entry(root,width=30)
entry.grid(row=0,column=1,pady=5)

# label + text (Notes)
tk.Label(root,text="Notes :",font=("Arial",15)).grid(row=1,column=0,sticky="ne",pady=5)
text = tk.Text(root,height=8,width=38)
text.grid(row=1,column=1,pady=5)
text.insert("1.0","Type Multiple line here .....")

# button 
tk.Button(root,text="Submit",command=submit_data,bg="lightblue").grid(row=2,column=0,columnspan=2,padx=15)




root.mainloop()       
