# How you can create a PDF file using the `reportlab` library:

### Code Example
```python
from reportlab.pdfgen import canvas

def create_pdf(file_path, text):
    # Create a canvas to write the PDF
    c = canvas.Canvas(file_path)
    
    # Set the title of the PDF
    c.setTitle("Sample PDF")
    
    # Write text at a specific position (x, y)
    c.drawString(100, 750, text)
    
    # Save the PDF file
    c.save()

# Specify the file path and text content
file_path = "output.pdf"
text_content = "Hello, this is a sample PDF created using Python!"

# Create the PDF
create_pdf(file_path, text_content)

print(f"PDF file '{file_path}' created successfully!")
```

### Steps to Run the Code
1. Install the `reportlab` library if you don't already have it:
   ```bash
   pip install reportlab
   ```
2. Copy and paste the code into a Python script (e.g., `create_pdf.py`).
3. Run the script:
   ```bash
   python create_pdf.py
   ```
4. A file named `output.pdf` will be created in the same directory. You can open it to see the text.
