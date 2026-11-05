import tkinter as tk

def calculate():
    try:
        num1 = float(entry1.get()) # 10
        num2 = float(entry2.get()) # 20
        op = operator.get() # + , - , * , / , Invalid
        
        if op == "+" : result = num1 + num2
        elif op == "-": result = num1 - num2
        elif op == "*": result = num1 * num2
        elif op == "/": result = num1 / num2 if num2 != 0 else "Error Do not Enter Zero"
        else :result = "invalid Data"
        label_result.config(text=f"Result : {result}")
    except ValueError:
        label_result.config(text="Enter Only Number")
        
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("500x500")

# row 0
tk.Label(root,text="Number 1 : ").grid(row=0,column=0,padx=5,pady=5,sticky="e")
entry1 = tk.Entry(root,width=15)
entry1.grid(row=0,column=1,padx=5,pady=5)           

# row 1
tk.Label(root,text="Number 2 : ").grid(row=1,column=0,padx=5,pady=5,sticky="e")
entry2 = tk.Entry(root,width=15)
entry2.grid(row=1,column=1,padx=5,pady=5) 

# row 3
tk.Label(root,text="Operator  : ").grid(row=2,column=0,padx=5,pady=5,sticky="e") 
operator = tk.StringVar(value="+")
tk.Radiobutton(root,text="+",variable=operator ,value="+").grid(row=2,column=1,sticky="w") 
tk.Radiobutton(root,text="-",variable=operator ,value="-").grid(row=2,column=1,sticky="e")
tk.Radiobutton(root,text="*",variable=operator ,value="*").grid(row=3,column=1,sticky="w")
tk.Radiobutton(root,text="/",variable=operator ,value="/").grid(row=3,column=1,sticky="e")    

# row 4
tk.Button(root,text="Calculate",command=calculate).grid(row=4,column=0,columnspan=2,pady=10)

# result 
label_result = tk.Label(root,text="Result = ",font=("Arial",20))
label_result.grid(row=5,column=0,columnspan=2)
root.mainloop()