Student_name = ?
Java_marks = ?
c_marks = ?
science = ?
maths = ?
english = ?
total = ?
per = ?


#Per range  | grade
#90 - 100        A
#75 - 89         B
#60 - 74         C
#40 - 59         D
#Below 40        Fail

marks = int(input("Enter Your Marks - "))
# check grade
if marks >= 90 and marks <= 100:
    print("Grade - A")
elif marks >= 75 and marks <= 89:
    print("Grade - B")
elif marks >=60 and marks <= 74:
    print("Grade - C")
elif marks >=40 and marks <= 59:
    print("Grade - D")
elif marks < 40 and marks >= 0:
    print("Fail")
else:
    print("Invalid Marks entered")
