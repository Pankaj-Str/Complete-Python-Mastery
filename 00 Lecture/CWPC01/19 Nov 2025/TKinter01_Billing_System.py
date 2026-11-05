import tkinter as tk
from tkinter import messagebox

class billingApp:
    def __init__(self,root):
        self.root = root
        self.root.title("Biiling System")
        self.root.geometry("520x780")
        self.root.resizable(False,False)
        # set background color
        self.root.config(bg="#dfe6e9")
        
        # data 
        self.n = 0 # number of product
        self.product = [] #list of (name,price)
        self.gst = 0.0 # (0 if no GST)
        
        # add custom fonts and colors here
        self.font_title = ("Arial",18,"bold")
        self.color_title = "#4D3737"
        self.label_font = ("Helvetica",12)
        self.label_color = "#2980b9"
        self.entry_font = ("Helvetica",12)
        self.btn_font = ("Arial",18,"bold")
        self.btn_bg = "#27ae60"
        self.btn_fg = "white"
        self.txt_bg = "#97adc3"
        
        self.make_widgets() # GUI elements 
        
        self.reset() # start
        
    def make_widgets(self):
        
        #pad = dict(padx=10,pady=8)
        
        header = tk.Frame(self.root,bg="#b2bec3",height=60)
        header.pack(fill="x")
        header.pack_propagate(False)
        
        tk.Label(header,text="Billing System",font=("Arial",22,"bold"),fg="white",bg="#2d3436").pack(pady=5)
        
       
        
        # instructions and entry
        
        
        # titel
        tk.Label(self.root,text="Biiling System",font=("Arial",18,"bold"),fg="#4D3737").pack(pady=2)
        
        # label change every step   
            
        self.lbl_instr = tk.Label(self.root,text="",font=("Helvetica",12),fg="#2980b9",wraplength=460,justify="center") 
        self.lbl_instr.pack(pady=10)
            
        # entry box 
            
        self.entry = tk.Entry(self.root,font=("Helvetica",12),justify="center",width=30)
            
        self.entry.pack(pady=12)
        self.entry.focus_set()
        self.entry.bind("<Return>",lambda e : self.next_step())
            
        
        # submit button style
        
        btn_style = {
            "font":("Arial",18,"bold"),
            "bg":"#27ae60",
            "fg":"white",
            "width":15
        }
        
        self.btn_next = tk.Button(self.root,text="Submit",activebackground="#00b894",activeforeground="white", **btn_style, command=self.next_step)
            
        self.btn_next.pack(pady=8)
            
        # bill Display
        self.txt_bill = tk.Text(self.root,height=20,width=55,font=("Courier",11),state="disabled",bg="#97adc3",relief="flat")
            
        self.txt_bill.pack(pady=20,padx=10)
            
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
            return
        
        try:
            # project list size 
            if self.step == 0:
                self.n = int(txt)
                if self.n <= 0:
                    raise ValueError
                self.step = 1
                self.show_step()
                
            elif 1 <= self.step <= self.n: # product names..
                name = txt.title()
                self.product.append([name,0])
                self.step += 1
                if self.step > self.n:
                    self.step = self.n + 1 
                self.show_step()     
                
                # product price...  
            elif self.n < self.step <= 2 * self.n: 
                price = int(txt.replace("/-","").split()[0])
                idx = self.step - self.n - 1
                self.product[idx][1] = price
                self.step += 1
                if self.step > 2 * self.n:
                    self.step = 2 * self.n + 1
                self.show_step()
                
            # GST Y/N    
            elif self.step == 2 * self.n+1:
                ch = txt.upper()
                if ch == 'Y':
                    self.step += 1
                    self.show_step()
                elif ch == "N":
                    self.generate_bill()
                else:
                    raise ValueError  
                
            # add GST percent 
            elif self.step == 2 * self.n + 2:
                self.gst = float(txt) 
                self.generate_bill()        
                
        except ValueError:
            messagebox.showerror("Invalid Input","plz enter valid number (Y/N for GST)")
        except Exception as e:
            messagebox.showerror("Error",str(e))                
    
    def generate_bill(self):
        # build and diplay the final bill print 
        subtotal = sum(p[1] for p in self.product)
        
        lines = []
        for i ,(name,price) in enumerate(self.product,1):
            lines.append(f"{i}. {name} = {price}")
        
        lines.append("-" * 19)
        lines.append(f"total = {subtotal}")
        if self.gst > 0:
            gst_amt = subtotal * self.gst / 100
            final = subtotal + gst_amt
            lines.append(f"GST = {self.gst}%")
            lines.append("-"*19)
            lines.append(f"final total = {final:0f}/-")
        else:
            lines.append(f"final total without GST : = {subtotal}/-")
        lines.append("-"*19)
        
        
        # ---- show 
        self.txt_bill.config(state="normal")
        self.txt_bill.delete("1.0",tk.END)
        for line in lines:
            self.txt_bill.insert(tk.END,line + "\n")
        self.txt_bill.config(state="disabled")
        
        # --- finish
        self.lbl_instr.config(text="ill generated ! click to new bill start again...")
        self.btn_next.config(state="disabled")
        self.btn_next.pack_forget()
        self.btn_new.pack(pady=10)
    
# run ----              
          
if __name__ == "__main__":
    root = tk.Tk()
    app = billingApp(root)
    root.mainloop()