# Python Operators Tutorial

Welcome to this comprehensive tutorial on Python Operators, brought to you by codeswithpankaj.com. In this tutorial, we will delve into various types of operators in Python, covering their syntax, usage, and practical examples. By the end of this tutorial, you will have a thorough understanding of how to use operators effectively in your Python programs.

## Table of Contents

1. Introduction to Operators
2. Arithmetic Operators
3. Comparison Operators
4. Logical Operators
5. Bitwise Operators
6. Assignment Operators
7. Identity Operators
8. Membership Operators
9. Operator Precedence
10. Practical Examples

---

## 1. Introduction to Operators

Operators are special symbols or keywords in Python that perform operations on variables and values. Python provides a variety of operators, each serving a specific purpose. These operators can be categorized into several types based on their functionality.

### Types of Operators

1. Arithmetic Operators
2. Comparison Operators
3. Logical Operators
4. Bitwise Operators
5. Assignment Operators
6. Identity Operators
7. Membership Operators

---

## 2. Arithmetic Operators

Arithmetic operators are used to perform mathematical operations such as addition, subtraction, multiplication, division, and more.

### List of Arithmetic Operators

| Operator | Description            | Example         |
|----------|------------------------|-----------------|
| `+`      | Addition               | `a + b`         |
| `-`      | Subtraction            | `a - b`         |
| `*`      | Multiplication         | `a * b`         |
| `/`      | Division               | `a / b`         |
| `%`      | Modulus                | `a % b`         |
| `**`     | Exponentiation         | `a ** b`        |
| `//`     | Floor Division         | `a // b`        |

### Examples

```python
# Addition
a = 10
b = 5
result = a + b
print(result)  # Output: 15

# Subtraction
result = a - b
print(result)  # Output: 5

# Multiplication
result = a * b
print(result)  # Output: 50

# Division
result = a / b
print(result)  # Output: 2.0

# Modulus
result = a % b
print(result)  # Output: 0

# Exponentiation
result = a ** b
print(result)  # Output: 100000

# Floor Division
result = a // b
print(result)  # Output: 2
```

---

## 3. Comparison Operators

Comparison operators are used to compare two values. They return either `True` or `False` based on the comparison result.

### List of Comparison Operators

| Operator | Description                  | Example     |
|----------|------------------------------|-------------|
| `==`     | Equal to                     | `a == b`    |
| `!=`     | Not equal to                 | `a != b`    |
| `>`      | Greater than                 | `a > b`     |
| `<`      | Less than                    | `a < b`     |
| `>=`     | Greater than or equal to     | `a >= b`    |
| `<=`     | Less than or equal to        | `a <= b`    |

### Examples

```python
a = 10
b = 5

# Equal to
result = (a == b)
print(result)  # Output: False

# Not equal to
result = (a != b)
print(result)  # Output: True

# Greater than
result = (a > b)
print(result)  # Output: True

# Less than
result = (a < b)
print(result)  # Output: False

# Greater than or equal to
result = (a >= b)
print(result)  # Output: True

# Less than or equal to
result = (a <= b)
print(result)  # Output: False
```

---

## 4. Logical Operators

Logical operators are used to combine conditional statements. They include `and`, `or`, and `not`.

### List of Logical Operators

| Operator | Description                  | Example              |
|----------|------------------------------|----------------------|
| `and`    | Returns True if both statements are true | `a and b`           |
| `or`     | Returns True if one of the statements is true | `a or b`         |
| `not`    | Reverses the result, returns False if the result is true | `not a` |

### Examples

```python
a = True
b = False

# Logical AND
result = a and b
print(result)  # Output: False

# Logical OR
result = a or b
print(result)  # Output: True

# Logical NOT
result = not a
print(result)  # Output: False
```

---

## 5. Bitwise Operators

Bitwise operators are used to perform bit-level operations on integers. They include `&`, `|`, `^`, `~`, `<<`, and `>>`.

### List of Bitwise Operators

| Operator | Description                  | Example     |
|----------|------------------------------|-------------|
| `&`      | Bitwise AND                  | `a & b`     |
| `|`      | Bitwise OR                   | `a | b`     |
| `^`      | Bitwise XOR                  | `a ^ b`     |
| `~`      | Bitwise NOT                  | `~a`        |
| `<<`     | Bitwise left shift           | `a << b`    |
| `>>`     | Bitwise right shift          | `a >> b`    |

### Examples

```python
a = 10  # Binary: 1010
b = 4   # Binary: 0100

# Bitwise AND
result = a & b
print(result)  # Output: 0

# Bitwise OR
result = a | b
print(result)  # Output: 14

# Bitwise XOR
result = a ^ b
print(result)  # Output: 14

# Bitwise NOT
result = ~a
print(result)  # Output: -11

# Bitwise left shift
result = a << 1
print(result)  # Output: 20

# Bitwise right shift
result = a >> 1
print(result)  # Output: 5
```

---

## 6. Assignment Operators

Assignment operators are used to assign values to variables. They include `=`, `+=`, `-=`, `*=`, `/=`, `%=`, `**=`, and `//=`.
 
### List of Assignment Operators

| Operator | Description                  | Example     |
|----------|------------------------------|-------------|
| `=`      | Assign                      | `a = 10`    |
| `+=`     | Add and assign              | `a += 5`    |
| `-=`     | Subtract and assign         | `a -= 5`    |
| `*=`     | Multiply and assign         | `a *= 5`    |
| `/=`     | Divide and assign           | `a /= 5`    |
| `%=`     | Modulus and assign          | `a %= 5`    |
| `**=`    | Exponentiation and assign   | `a **= 5`   |
| `//=`    | Floor division and assign   | `a //= 5`   |

### Examples

```python
a = 10

# Assign
a = 5
print(a)  # Output: 5

# Add and assign
a += 5
print(a)  # Output: 10

# Subtract and assign
a -= 5
print(a)  # Output: 5

# Multiply and assign
a *= 2
print(a)  # Output: 10

# Divide and assign
a /= 2
print(a)  # Output: 5.0

# Modulus and assign
a %= 3
print(a)  # Output: 2.0

# Exponentiation and assign
a **= 3
print(a)  # Output: 8.0

# Floor division and assign
a //= 2
print(a)  # Output: 4.0
```

---

## 7. Identity Operators

Identity operators are used to compare the memory locations of two objects. They include `is` and `is not`.

### List of Identity Operators

| Operator | Description                  | Example     |
|----------|------------------------------|-------------|
| `is`     | Returns True if both variables are the same object | `a is b`    |
| `is not` | Returns True if both variables are not the same object | `a is not b` |

### Examples

```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]

# is operator
result = (a is b)
print(result)  # Output: True

# is not operator
result = (a is not c)
print(result)  # Output: True
```

---

## 8. Membership Operators

Membership operators are used to test if a sequence contains a specified value. They include `in` and `not in`.

### List of Membership Operators

| Operator | Description                  | Example     |
|----------|------------------------------|-------------|
| `in`     | Returns True if a sequence contains a

 specified value | `a in b`    |
| `not in` | Returns True if a sequence does not contain a specified value | `a not in b` |

### Examples

```python
a = [1, 2, 3, 4, 5]
b = 3
c = 6

# in operator
result = (b in a)
print(result)  # Output: True

# not in operator
result = (c not in a)
print(result)  # Output: True
```

---

## 9. Operator Precedence

Operator precedence determines the order in which operations are performed in an expression. Operators with higher precedence are evaluated before those with lower precedence.

### List of Operator Precedence

The following table lists the operators in descending order of precedence:

| Precedence | Operator        | Description               |
|------------|-----------------|---------------------------|
| 1          | `()`            | Parentheses               |
| 2          | `**`            | Exponentiation            |
| 3          | `+`, `-`        | Unary plus and minus      |
| 4          | `*`, `/`, `%`, `//` | Multiplication, Division, Modulus, Floor Division |
| 5          | `+`, `-`        | Addition, Subtraction     |
| 6          | `<<`, `>>`      | Bitwise shift operators   |
| 7          | `&`             | Bitwise AND               |
| 8          | `^`             | Bitwise XOR               |
| 9          | `|`             | Bitwise OR                |
| 10         | `==`, `!=`, `>`, `<`, `>=`, `<=` | Comparison operators |
| 11         | `not`           | Logical NOT               |
| 12         | `and`           | Logical AND               |
| 13         | `or`            | Logical OR                |

### Examples

```python
# Example of operator precedence
a = 10
b = 5
c = 2

result = a + b * c
print(result)  # Output: 20, because b * c is evaluated first

result = (a + b) * c
print(result)  # Output: 30, because parentheses have the highest precedence
```

---

## 10. Practical Examples

### Example 1: Arithmetic Operations

```python
# Basic arithmetic operations
a = 15
b = 4

addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
modulus = a % b
exponentiation = a ** b
floor_division = a // b

print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")
print(f"Modulus: {modulus}")
print(f"Exponentiation: {exponentiation}")
print(f"Floor Division: {floor_division}")
```

### Example 2: Comparison and Logical Operations

```python
# Comparison and logical operations
a = 10
b = 20

is_equal = (a == b)
is_not_equal = (a != b)
is_greater = (a > b)
is_less = (a < b)
is_greater_equal = (a >= b)
is_less_equal = (a <= b)

logical_and = (a < b) and (b > 15)
logical_or = (a < b) or (b < 15)
logical_not = not (a < b)

print(f"Is Equal: {is_equal}")
print(f"Is Not Equal: {is_not_equal}")
print(f"Is Greater: {is_greater}")
print(f"Is Less: {is_less}")
print(f"Is Greater or Equal: {is_greater_equal}")
print(f"Is Less or Equal: {is_less_equal}")
print(f"Logical AND: {logical_and}")
print(f"Logical OR: {logical_or}")
print(f"Logical NOT: {logical_not}")
```

### Example 3: Bitwise Operations

```python
# Bitwise operations
a = 10  # Binary: 1010
b = 4   # Binary: 0100

bitwise_and = a & b
bitwise_or = a | b
bitwise_xor = a ^ b
bitwise_not = ~a
bitwise_left_shift = a << 2
bitwise_right_shift = a >> 2

print(f"Bitwise AND: {bitwise_and}")
print(f"Bitwise OR: {bitwise_or}")
print(f"Bitwise XOR: {bitwise_xor}")
print(f"Bitwise NOT: {bitwise_not}")
print(f"Bitwise Left Shift: {bitwise_left_shift}")
print(f"Bitwise Right Shift: {bitwise_right_shift}")
```

### Example 4: Assignment Operations

```python
# Assignment operations
a = 5
print(f"Initial value of a: {a}")

a += 2
print(f"After a += 2: {a}")

a -= 1
print(f"After a -= 1: {a}")

a *= 3
print(f"After a *= 3: {a}")

a /= 2
print(f"After a /= 2: {a}")

a %= 3
print(f"After a %= 3: {a}")

a **= 2
print(f"After a **= 2: {a}")

a //= 2
print(f"After a //= 2: {a}")
```

### Example 5: Identity and Membership Operations

```python
# Identity and membership operations
a = [1, 2, 3]
b = a
c = [1, 2, 3]

is_identity = (a is b)
is_not_identity = (a is not c)

membership_in = (2 in a)
membership_not_in = (4 not in a)

print(f"Is Identity: {is_identity}")
print(f"Is Not Identity: {is_not_identity}")
print(f"Membership In: {membership_in}")
print(f"Membership Not In: {membership_not_in}")
```

---

This concludes our detailed tutorial on Python Operators. We hope you found this tutorial helpful and informative. For more tutorials and resources, visit codeswithpankaj.com. Happy coding!
