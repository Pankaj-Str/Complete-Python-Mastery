# Python Operators

a = 10
b = 3

# 1. Arithmetic Operators

print("Arithmetic Operators")

print(a + b)    # Addition
print(a - b)    # Subtraction
print(a * b)    # Multiplication
print(a / b)    # Division
print(a // b)   # Floor Division
print(a % b)    # Modulus
print(a ** b)   # Exponentiation


# 2. Assignment Operators

print("\nAssignment Operators")

x = 10

x += 5
print(x)

x -= 2
print(x)

x *= 2
print(x)

x /= 2
print(x)

x //= 2
print(x)

x %= 3
print(x)

x **= 2
print(x)


# 3. Comparison Operators

print("\nComparison Operators")

a = 10
b = 5

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)


# 4. Logical Operators

print("\nLogical Operators")

age = 25
salary = 50000

print(age >= 18 and salary >= 30000)
print(age >= 18 or salary >= 60000)
print(not(age >= 18))


# 5. Bitwise Operators

print("\nBitwise Operators")

a = 10
b = 3

print(a & b)    # AND
print(a | b)    # OR
print(a ^ b)    # XOR
print(~a)       # NOT
print(a << 1)   # Left Shift
print(a >> 1)   # Right Shift


# 6. Membership Operators

print("\nMembership Operators")

languages = ["Python", "Java", "C++"]

print("Python" in languages)
print("PHP" not in languages)


# 7. Identity Operators

print("\nIdentity Operators")

list1 = [10, 20, 30]
list2 = [10, 20, 30]
list3 = list1

print(list1 is list2)
print(list1 is list3)

print(list1 == list2)
print(list1 is not list2)


# 8. Assignment Bitwise Operators

print("\nBitwise Assignment Operators")

x = 10

x &= 3
print(x)

x = 10
x |= 3
print(x)

x = 10
x ^= 3
print(x)

x = 10
x <<= 1
print(x)

x = 10
x >>= 1
print(x)