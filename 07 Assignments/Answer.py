# 1. Grade Classifier
exam_score = int(input("Enter your exam score: "))
if exam_score >= 90:
    print("Your grade is A.")
elif exam_score >= 80:
    print("Your grade is B.")
elif exam_score >= 70:
    print("Your grade is C.")
elif exam_score >= 60:
    print("Your grade is D.")
else:
    print("Your grade is F.")

# 2. Number Comparison
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 > num2:
    print(num1, "is greater than", num2)
elif num1 < num2:
    print(num2, "is greater than", num1)
else:
    print("Both numbers are equal.")

# 3. Leap Year Checker
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

# 4. Number Sign Checker
number = int(input("Enter a number: "))
if number > 0:
    print(number, "is a positive number.")
elif number < 0:
    print(number, "is a negative number.")
else:
    print("The number is zero.")

# 5. Vowel Checker
character = input("Enter a character: ")
if character.lower() in ['a', 'e', 'i', 'o', 'u']:
    print("'", character, "' is a vowel.")
else:
    print("'", character, "' is a consonant.")

# 6. Age Classifier
age = int(input("Enter your age: "))
if age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
else:
    print("You are an adult.")

# 7. Odd or Even Checker
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is an even number.")
else:
    print(num, "is an odd number.")

# 8. Triangle Type Classifier (Assuming sides are entered in ascending order)
side1 = int(input("Enter the length of side 1: "))
side2 = int(input("Enter the length of side 2: "))
side3 = int(input("Enter the length of side 3: "))
if side1 == side2 == side3:
    print("This is an equilateral triangle.")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("This is an isosceles triangle.")
else:
    print("This is a scalene triangle.")

# 9. Temperature Adviser
temperature = float(input("Enter the current temperature (in Celsius): "))
if temperature < 10:
    print("It's cold outside. You should wear a coat.")
elif temperature < 20:
    print("It's cool outside. You can wear a jacket.")
else:
    print("It's warm outside. You can wear a t-shirt.")

# 10. Number Range Checker
number = int(input("Enter a number: "))
if 1 <= number <= 100:
    print("The number", number, "falls within the range of 1 to 100.")
else:
    print("The number", number, "is not within the range of 1 to 100.")
