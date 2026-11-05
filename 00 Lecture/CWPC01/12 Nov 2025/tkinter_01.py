import tkinter as tk

root = tk.Tk()
root.title("Welcome Bords widgets")
root.geometry("500x400")

label = tk.Label(root,text='Hello Word',font=("Arial",30),fg="blue",bg="yellow")
label.pack(pady=20)

def on_button_click():
    print("button Clicked!")
    
button = tk.Button(root,text="click Me",width=10,height=2,command=on_button_click)
button.pack(pady=10)  

entry = tk.Entry(root,width=30,show="*")
entry.pack(pady=10)
entry.insert(0,"Enter Text here ....")

text = tk.Text(root,height=5,width=40)
text.pack(pady=10)
text.insert(tk.END,"this is multi-line text .....")



root.mainloop()