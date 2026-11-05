# Assignment 1: Basic Arithmetic Operations
num1 = 10
num2 = 5
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)

# Assignment 2: Temperature Converter
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)

# Assignment 3: String Concatenation
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = first_name + " " + last_name
print("Full Name:", full_name)

# Assignment 4: BMI Calculator
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height * height)
print("Your BMI is:", bmi)

# Assignment 5: Area of a Triangle
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area = (base * height) / 2
print("Area of the triangle:", area)

# Assignment 6: Age Calculator
birth_year = int(input("Enter your birth year: "))
current_year = 2024
age = current_year - birth_year
print("Your age is:", age)

# Assignment 7: Even or Odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# Assignment 8: Grade Calculator
test1 = int(input("Enter score for test 1 (out of 100): "))
test2 = int(input("Enter score for test 2 (out of 100): "))
test3 = int(input("Enter score for test 3 (out of 100): "))
average_score = (test1 + test2 + test3) / 3
print("Average score:", average_score)
if average_score >= 90:
    print("Grade: A")
elif average_score >= 80:
    print("Grade: B")
elif average_score >= 70:
    print("Grade: C")
elif average_score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# Assignment 9: Simple Interest Calculator
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time in years: "))
simple_interest = (principal * rate * time) / 100
print("Simple Interest:", simple_interest)

# Assignment 10: Quadratic Equation Solver
import cmath

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Calculate discriminant
d = (b ** 2) - (4 * a * c)

# Find two solutions
sol1 = (-b - cmath.sqrt(d)) / (2 * a)
sol2 = (-b + cmath.sqrt(d)) / (2 * a)

print("The solutions are {0} and {1}".format(sol1, sol2))
