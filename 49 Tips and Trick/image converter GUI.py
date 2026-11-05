import tkinter as tk
from tkinter import filedialog
from PIL import Image
import os

class ImageConverterApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Image Converter")
        self.geometry("400x200")
        
        self.input_dir = ""
        self.output_dir = ""
        
        self.create_widgets()
    
    def create_widgets(self):
        # Input directory
        self.input_label = tk.Label(self, text="Input Directory:")
        self.input_label.grid(row=0, column=0)
        
        self.input_entry = tk.Entry(self, width=30)
        self.input_entry.grid(row=0, column=1)
        
        self.input_button = tk.Button(self, text="Browse", command=self.browse_input)
        self.input_button.grid(row=0, column=2)
        
        # Output directory
        self.output_label = tk.Label(self, text="Output Directory:")
        self.output_label.grid(row=1, column=0)
        
        self.output_entry = tk.Entry(self, width=30)
        self.output_entry.grid(row=1, column=1)
        
        self.output_button = tk.Button(self, text="Browse", command=self.browse_output)
        self.output_button.grid(row=1, column=2)
        
        # Format selection
        self.format_label = tk.Label(self, text="Output Format:")
        self.format_label.grid(row=2, column=0)
        
        self.format_var = tk.StringVar(self)
        self.format_var.set(".jpg")  # Default format
        self.format_dropdown = tk.OptionMenu(self, self.format_var, ".jpg", ".png", ".bmp", ".tiff")
        self.format_dropdown.grid(row=2, column=1)
        
        # Convert button
        self.convert_button = tk.Button(self, text="Convert", command=self.convert_images)
        self.convert_button.grid(row=3, column=1)
        
    def browse_input(self):
        self.input_dir = filedialog.askdirectory()
        self.input_entry.delete(0, tk.END)
        self.input_entry.insert(0, self.input_dir)
    
    def browse_output(self):
        self.output_dir = filedialog.askdirectory()
        self.output_entry.delete(0, tk.END)
        self.output_entry.insert(0, self.output_dir)
    
    def convert_images(self):
        if not self.input_dir or not self.output_dir:
            tk.messagebox.showerror("Error", "Please select input and output directories.")
            return
        
        format_selected = self.format_var.get()
        
        for filename in os.listdir(self.input_dir):
            if filename.endswith((".jpg", ".jpeg", ".png", ".bmp", ".tiff")):
                input_path = os.path.join(self.input_dir, filename)
                output_path = os.path.join(self.output_dir, filename.replace(".", "_converted."))
                
                try:
                    with Image.open(input_path) as img:
                        img.save(output_path, format=format_selected)
                except Exception as e:
                    tk.messagebox.showerror("Error", f"Failed to convert {filename}: {str(e)}")
        
        tk.messagebox.showinfo("Success", "Image conversion completed.")

if __name__ == "__main__":
    app = ImageConverterApp()
    app.mainloop()
