import tkinter as tk
from tkinter import ttk

class StudentMarksheet:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Marksheet")

        # Student Information
        self.student_name = tk.StringVar()
        self.roll_number = tk.StringVar()

        # Marks
        self.subject_marks = {
            "Math": tk.DoubleVar(),
            "English": tk.DoubleVar(),
            "Science": tk.DoubleVar(),
            # Add more subjects as needed
        }

        # GUI Components
        self.create_student_info_section()
        self.create_marks_section()
        self.create_display_section()

    def create_student_info_section(self):
        frame_info = ttk.LabelFrame(self.root, text="Student Information")
        frame_info.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        ttk.Label(frame_info, text="Student Name:").grid(row=0, column=0, sticky="w", pady=5)
        ttk.Entry(frame_info, textvariable=self.student_name).grid(row=0, column=1, padx=5)

        ttk.Label(frame_info, text="Roll Number:").grid(row=1, column=0, sticky="w", pady=5)
        ttk.Entry(frame_info, textvariable=self.roll_number).grid(row=1, column=1, padx=5)

    def create_marks_section(self):
        frame_marks = ttk.LabelFrame(self.root, text="Subject Marks")
        frame_marks.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        row_counter = 0
        for subject, marks_var in self.subject_marks.items():
            ttk.Label(frame_marks, text=f"{subject}:").grid(row=row_counter, column=0, sticky="w", pady=5)
            ttk.Entry(frame_marks, textvariable=marks_var).grid(row=row_counter, column=1, padx=5)
            row_counter += 1

    def create_display_section(self):
        frame_display = ttk.LabelFrame(self.root, text="Display")
        frame_display.grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky="w")

        ttk.Button(frame_display, text="Show Marksheet", command=self.show_marksheet).grid(row=0, column=0, pady=10)
        self.marksheet_display = tk.Text(frame_display, height=10, width=30)
        self.marksheet_display.grid(row=1, column=0, padx=5)

    def show_marksheet(self):
        student_name = self.student_name.get()
        roll_number = self.roll_number.get()

        if student_name and roll_number:
            marksheet_text = f"Student Name: {student_name}\nRoll Number: {roll_number}\n\n"
            for subject, marks_var in self.subject_marks.items():
                marks = marks_var.get()
                marksheet_text += f"{subject}: {marks:.2f}\n"

            self.marksheet_display.delete("1.0", tk.END)  # Clear previous content
            self.marksheet_display.insert(tk.END, marksheet_text)
        else:
            self.marksheet_display.delete("1.0", tk.END)
            self.marksheet_display.insert(tk.END, "Please enter student information.")

if __name__ == "__main__":
    root = tk.Tk()
    marksheet_app = StudentMarksheet(root)
    root.mainloop()
