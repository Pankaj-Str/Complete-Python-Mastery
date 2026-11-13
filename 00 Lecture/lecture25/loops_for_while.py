# Python Loops: for loop, while loop, nested loop, break, continue, pass

# 1. Simple For Loop

for i in range(1, 6):
    print(i)


# 2. For Loop with Range

for i in range(1, 11):
    print(i)


# 3. Print Even Numbers

for i in range(1, 21):
    if i % 2 == 0:
        print(i)


# 4. Print Odd Numbers

for i in range(1, 21):
    if i % 2 != 0:
        print(i)


# 5. Print Multiplication Table

num = 5

for i in range(1, 11):
    print(num, "x", i, "=", num * i)


# 6. Sum of First 10 Natural Numbers

total = 0

for i in range(1, 11):
    total += i

print("Sum:", total)


# 7. Iterate Over a String

name = "Python"

for char in name:
    print(char)


# 8. Iterate Over a List

languages = ["Python", "Java", "C++", "JavaScript"]

for language in languages:
    print(language)


# 9. Iterate Over a Dictionary

student = {
    "name": "Pankaj",
    "age": 30,
    "course": "Python"
}

for key, value in student.items():
    print(key, ":", value)


# 10. Simple While Loop

i = 1

while i <= 5:
    print(i)
    i += 1


# 11. Print Numbers in Reverse

i = 10

while i >= 1:
    print(i)
    i -= 1


# 12. Sum of Numbers Using While Loop

i = 1
total = 0

while i <= 10:
    total += i
    i += 1

print("Total:", total)


# 13. Break Statement

for i in range(1, 11):

    if i == 5:
        break

    print(i)


# 14. Continue Statement

for i in range(1, 11):

    if i == 5:
        continue

    print(i)


# 15. Pass Statement

for i in range(1, 6):

    if i == 3:
        pass

    print(i)


# 16. Nested For Loop

for i in range(1, 4):

    for j in range(1, 4):
        print(i, j)


# 17. Star Pattern

for i in range(1, 6):

    for j in range(i):
        print("*", end=" ")

    print()


# 18. Number Pattern

for i in range(1, 6):

    for j in range(1, i + 1):
        print(j, end=" ")

    print()


# 19. Factorial Using For Loop

num = 5
fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial:", fact)


# 20. Reverse a Number

num = 12345
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

print("Reverse:", reverse)


# 21. Count Digits in a Number

num = 12345
count = 0

while num > 0:
    count += 1
    num //= 10

print("Total Digits:", count)


# 22. Fibonacci Series

a = 0
b = 1

for i in range(10):
    print(a, end=" ")
    a, b = b, a + b

print()


# 23. Prime Number Check

num = 17
count = 0

for i in range(1, num + 1):

    if num % i == 0:
        count += 1

if count == 2:
    print("Prime Number")
else:
    print("Not a Prime Number")


# 24. Multiplication Tables Using Nested Loop

for i in range(1, 6):

    for j in range(1, 11):
        print(i, "x", j, "=", i * j)

    print("----------------")


# 25. Else with For Loop

for i in range(1, 6):
    print(i)

else:
    print("Loop Completed")


# 26. Else with While Loop

i = 1

while i <= 5:
    print(i)
    i += 1

else:
    print("While Loop Completed")