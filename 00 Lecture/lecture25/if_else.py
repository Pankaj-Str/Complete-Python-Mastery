# age = int(input('Enter Your Age ..'))
# voting 
#if age >= 18:
#    print("Done - vote....")
#else:
#    print("not Done - vote....")


passenger_age = int(input('Enter Passenger Age - '))
ticket_confirmed = True

if passenger_age >= 25 and ticket_confirmed:
    print('Passenger Eligible for Travel')
else:
    print('Passenger not Eligible for Travel')


# ---------------

# Python if, if-else, if-elif-else, Nested if and Ternary Operator

# 1. Simple if Statement

age = 20

if age >= 18:
    print("Eligible for Voting")


# 2. if-else Statement

num = 10

if num > 0:
    print("Positive Number")
else:
    print("Negative Number")


# 3. Even or Odd

num = 15

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")


# 4. Pass or Fail

marks = 65

if marks >= 35:
    print("Pass")
else:
    print("Fail")


# 5. if-elif-else Statement

marks = 85

if marks >= 90:
    print("Grade A+")

elif marks >= 80:
    print("Grade A")

elif marks >= 70:
    print("Grade B")

elif marks >= 60:
    print("Grade C")

elif marks >= 35:
    print("Grade D")

else:
    print("Fail")


# 6. Greatest Number Between Two Numbers

a = 100
b = 200

if a > b:
    print("A is Greater")
elif b > a:
    print("B is Greater")
else:
    print("Both Numbers are Equal")


# 7. Greatest Number Among Three Numbers

a = 100
b = 200
c = 150

if a > b and a > c:
    print("A is Greatest")

elif b > a and b > c:
    print("B is Greatest")

elif c > a and c > b:
    print("C is Greatest")

else:
    print("Two or More Numbers are Equal")


# 8. Positive, Negative or Zero

num = 0

if num > 0:
    print("Positive Number")

elif num < 0:
    print("Negative Number")

else:
    print("Zero")


# 9. Nested if Statement

age = 25
has_license = True

if age >= 18:

    if has_license:
        print("You Can Drive")
    else:
        print("You Need a Driving License")

else:
    print("You Are Not Eligible")


# 10. Login System

username = "admin"
password = "12345"

if username == "admin":

    if password == "12345":
        print("Login Successful")
    else:
        print("Incorrect Password")

else:
    print("Invalid Username")


# 11. Leap Year

year = 2024

if year % 400 == 0:
    print("Leap Year")

elif year % 100 == 0:
    print("Not a Leap Year")

elif year % 4 == 0:
    print("Leap Year")

else:
    print("Not a Leap Year")


# 12. Vowel or Consonant

char = "a"

if char.lower() in "aeiou":
    print("Vowel")
else:
    print("Consonant")


# 13. Divisible by 5

num = 25

if num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not Divisible by 5")


# 14. Discount Calculation

amount = 5000

if amount >= 10000:
    discount = amount * 0.20

elif amount >= 5000:
    discount = amount * 0.10

elif amount >= 2000:
    discount = amount * 0.05

else:
    discount = 0

final_amount = amount - discount

print("Original Amount:", amount)
print("Discount:", discount)
print("Final Amount:", final_amount)


# 15. Simple Calculator

a = 20
b = 10
operator = "+"

if operator == "+":
    print("Addition:", a + b)

elif operator == "-":
    print("Subtraction:", a - b)

elif operator == "*":
    print("Multiplication:", a * b)

elif operator == "/":

    if b != 0:
        print("Division:", a / b)
    else:
        print("Cannot Divide by Zero")

else:
    print("Invalid Operator")


# 16. Ternary Operator

age = 20

result = "Eligible" if age >= 18 else "Not Eligible"

print(result)


# 17. Electricity Bill Calculation

units = 250

if units <= 100:
    bill = units * 3

elif units <= 200:
    bill = (100 * 3) + ((units - 100) * 5)

else:
    bill = (100 * 3) + (100 * 5) + ((units - 200) * 8)

print("Electricity Bill:", bill)


# 18. Check Number Range

num = 45

if num >= 1 and num <= 10:
    print("Number is between 1 and 10")

elif num >= 11 and num <= 50:
    print("Number is between 11 and 50")

elif num >= 51 and num <= 100:
    print("Number is between 51 and 100")

else:
    print("Number is outside the given ranges")