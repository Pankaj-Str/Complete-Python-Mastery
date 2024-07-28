### Student Report Card System Assignment

#### Objective:
Create a Python program to manage a student report card system using functions. The program should take the student's name, roll number, and marks for five subjects, calculate the total marks, percentage, and assign a grade based on the marks.

#### Assignment Questions:

**Question 1: Basic Student Report Card System**

1. **Input Student Details:**
    - Student Name
    - Student Roll Number

2. **Input Marks for Subjects:**
    - JAVA
    - JSP
    - Ruby
    - C++
    - Python

3. **Calculate and Display:**
    - Total Marks
    - Percentage
    - Grade

4. **Grading System:**
    - 80 - 100: Grade A
    - 60 - 80: Grade B
    - 40 - 60: Grade C
    - 30 - 40: Grade D
    - 0 - 30: Grade F

### Features to Implement:
- **Function for Inputting Student Details**: Create a function that prompts the user to enter the student's name and roll number.
- **Function for Inputting Marks**: Create a function that prompts the user to enter marks for each subject.
- **Function for Calculating Total and Percentage**: Create a function that calculates the total marks and percentage.
- **Function for Assigning Grade**: Create a function that assigns a grade based on the percentage.
- **Function for Displaying the Report Card**: Create a function that prints the student details, marks, total, percentage, and grade.

### Example Output:

```
Enter Student Name: Joy
Enter Student Roll Number: 200AQ1

Enter marks for the following subjects out of 100:
JAVA: 23
JSP: 45
Ruby: 67
C++: 33
Python: 78

Student Report Card
-------------------
Student Name: Joy
Roll Number: 200AQ1
Marks:
1. JAVA = 23/100
2. JSP = 45/100
3. Ruby = 67/100
4. C++ = 33/100
5. Python = 78/100

Total Marks: 246
Percentage: 49.2%
Grade: C
```

**Question 2: Enhanced Student Report Card System**

1. **Add Student Class and Section:**
    - Student Class
    - Student Section

2. **Attendance Record:**
    - Total Classes
    - Classes Attended
    - Attendance Percentage

3. **Comments Section:**
    - Teacher's Comments
    - Parent's Signature

4. **Enhanced Output Format:**
    - Display the report card in a clear format.
    - Include the school name, address, and a logo if available.

### Additional Features to Implement:
- **Function for Inputting Class and Section**: Create a function that prompts the user to enter the student's class and section.
- **Function for Inputting Attendance**: Create a function that prompts the user to enter the total classes and classes attended.
- **Function for Calculating Attendance Percentage**: Create a function that calculates the attendance percentage.
- **Function for Inputting Comments and Signature**: Create a function that allows the teacher to input comments and provides a space for the parent's signature.
- **Enhanced Display Function**: Modify the display function to include the new details and format them neatly.

### Example Output with Enhanced Features:

```
Enter Student Name: Joy
Enter Student Roll Number: 200AQ1
Enter Student Class: 10
Enter Student Section: A

Enter marks for the following subjects out of 100:
JAVA: 23
JSP: 45
Ruby: 67
C++: 33
Python: 78

Enter Attendance Details:
Total Classes: 180
Classes Attended: 160

Enter Teacher's Comments: Needs improvement in JAVA and C++.

Student Report Card
-------------------
School: XYZ School
Address: 123 Main St, Anytown

Student Name: Joy
Roll Number: 200AQ1
Class: 10
Section: A

Marks:
1. JAVA = 23/100
2. JSP = 45/100
3. Ruby = 67/100
4. C++ = 33/100
5. Python = 78/100

Total Marks: 246
Percentage: 49.2%
Grade: C

Attendance Record:
Total Classes: 180
Classes Attended: 160
Attendance Percentage: 88.89%

Comments:
Teacher's Comments: Needs improvement in JAVA and C++.
Parent's Signature: ___________________
```

**Question 3: Advanced Features for Student Report Card System**

1. **Manage Multiple Students:**
    - Allow input for multiple students.
    - Provide an option to search for a student by name or roll number.

2. **Export Report Card:**
    - Add a feature to export the report card to a PDF file.

3. **User Interface:**
    - Create a simple text-based menu for navigating the system.
    - Provide options to add, view, update, and delete student records.

### Features to Implement:
- **Function for Managing Multiple Students**: Create a function to store multiple student records and allow searching by name or roll number.
- **Function for Exporting to PDF**: Use a library like `fpdf` to create and export the report card to a PDF file.
- **Menu Interface**: Create a menu interface to allow users to navigate through different options like adding, viewing, updating, and deleting student records.

### Example of Menu Interface:

```
Student Report Card System
--------------------------
1. Add Student
2. View Student
3. Update Student
4. Delete Student
5. Export Report Card to PDF
6. Exit

Enter your choice: 
```

### Example Python Code for Basic Functionality:

```python
def input_student_details():
    name = input("Enter Student Name: ")
    roll_number = input("Enter Student Roll Number: ")
    return name, roll_number

def input_marks(subjects):
    marks = {}
    print("\nEnter marks for the following subjects out of 100:")
    for subject in subjects:
        while True:
            try:
                mark = int(input(f"{subject}: "))
                if 0 <= mark <= 100:
                    marks[subject] = mark
                    break
                else:
                    print("Marks should be between 0 and 100. Please try again.")
            except ValueError:
                print("Invalid input. Please enter an integer value.")
    return marks

def calculate_total_and_percentage(marks):
    total = sum(marks.values())
    percentage = total / len(marks)
    return total, percentage

def assign_grade(percentage):
    if percentage >= 80:
        return 'A'
    elif percentage >= 60:
        return 'B'
    elif percentage >= 40:
        return 'C'
    elif percentage >= 30:
        return 'D'
    else:
        return 'F'

def display_report_card(name, roll_number, marks, total, percentage, grade):
    print("\nStudent Report Card")
    print("-------------------")
    print(f"Student Name: {name}")
    print(f"Roll Number: {roll_number}")
    print("Marks:")
    for subject, mark in marks.items():
        print(f"{subject} = {mark}/100")
    print(f"\nTotal Marks: {total}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")

def main():
    subjects = ["JAVA", "JSP", "Ruby", "C++", "Python"]
    name, roll_number = input_student_details()
    marks = input_marks(subjects)
    total, percentage = calculate_total_and_percentage(marks)
    grade = assign_grade(percentage)
    display_report_card(name, roll_number, marks, total, percentage, grade)

if __name__ == "__main__":
    main()
```

This assignment helps students understand how to modularize code using functions, handle user inputs, perform calculations, and display formatted outputs.