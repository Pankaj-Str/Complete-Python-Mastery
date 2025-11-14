import tkinter as tk
from tkinter import messagebox

class billingApp:
    def __init__(self,root):
        self.root = root
        self.root.title("Biiling System")
        self.root.geometry("520x720")
        self.root.resizable(False,False)
        
        # data 
        self.n = 0 # number of product
        self.product = [] #list of (name,price)
        self.gst = 0.0 # (0 if no GST)
        
        self.make_widgets()
        
        self.reset() # start
        
    def make_widgets(self):
        tk.Label(self.root,text="Biiling System",font=("Arial",18,"bold"),fg="#EDE6E6").pack(pady=15)
            
        self.lbl_instr = tk.Label(self.root,text="",font=("Helvetica",12),fg="#2980b9",wraplength=460,justify="center") 
        self.lbl_instr.pack(pady=10)
            
        # entry box 
            
        self.entry = tk.Entry(self.root,font=("Helvetica",12),justify="center",width=30)
            
        self.entry.pack(pady=12)
        self.entry.focus_set()
        self.entry.bind("<Return>",lambda e : self.next_step())
            
        # submit button
        self.btn_next = tk.Button(self.root,text="Submit",font=("Arial",18,"bold"),bg="#27ae60",fg="white",width=15,command=self.next_step)
            
        self.btn_next.pack(pady=8)
            
        # bill Display
        self.txt_bill = tk.Text(self.root,height=20,width=55,font=("Courier",11),state="disabled",bg="#f8f9fa",relief="flat")
            
        #self.txt_bill.pack(pady=20, **pad)
            
        # new button 
        self.btn_new = tk.Button(self.root,text="new bill",font=("Arial",18,"bold"),bg="#27ae60",fg="white",width=15,command=self.reset)
            
            
    def reset(self):
        # print bill 
        self.n = 0
        self.product = []
        self.gst = 0.0
        self.step = 0   # 0 ask size , 1......n
        self.clear_bill()
        self.btn_next.config(text="Submit")
        self.btn_new.pack_forget()
        self.show_step()   

            
    def clear_bill(self):
       self.txt_bill.config(state="normal")
       self.txt_bill.delete("1.0",tk.END)
       self.txt_bill.config(state="disabled")
       
       
    def show_step(self):
        if self.step == 0:
            self.lbl_instr.config(text="Enter Product List Size ...")
        elif 1 <= self.step <= self.n:
            self.lbl_instr.config(text=f"Enter Product {self.step} - ")
        elif self.n < self.step <= 2 * self.n:
            idx = self.step - self.n - 1
            name = self.product[idx][0]
            self.lbl_instr.config(text=f"Enter {name} Price - ")
        elif self.step == 2 * self.n + 1:
            self.lbl_instr.config(text="Do You Want to add GST [Y/N]") 
        elif self.step == 2 * self.n + 2:
            self.lbl_instr.config(text="Enter GST")
        self.entry.delete(0,tk.END)
        self.entry.focus_set()           
    
    def next_step(self):
        txt = self.entry.get().strip()
        if not txt:
            messagebox.showwarning("Empty","please fill the field")
        
        try:
            if self.step == 0:
                self.n = int(txt)
                if self.n <= 0:
                    raise ValueError
                self.step = 1
                self.show_step()
                
            elif 1 <= self.step <= self.n:
                name = txt.title()
                self.product.append([name,0])
                self.step += 1
                if self.step > self.n:
                    self.step = self.n + 1 
                self.show_step()       
                
        except ValueError:
            messagebox.showerror("Invalid Input","plz enter valid number (Y/N for GST)")            
    
    
          
if __name__ == "__main__":
    root = tk.Tk()
    app = billingApp(root)
    root.mainloop()