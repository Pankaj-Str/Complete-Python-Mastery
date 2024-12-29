# Python if-else

## Python if-else Tutorial

Welcome to this comprehensive tutorial on Python if-else statements, brought to you by codeswithpankaj.com. In this tutorial, we will explore various aspects of if-else statements in Python, covering their syntax, usage, and practical examples. By the end of this tutorial, you will have a thorough understanding of how to use if-else statements effectively in your Python programs.

### Table of Contents

1. Introduction to if-else Statements
2. Basic if Statement
3. if-else Statement
4. if-elif-else Statement
5. Nested if Statements
6. Conditional Expressions (Ternary Operator)
7. Flowchart
8. Practical Examples
9. Common Pitfalls and Best Practices

***

### 1. Introduction to if-else Statements

If-else statements are used to perform different actions based on different conditions. They are fundamental in controlling the flow of a program, allowing you to execute certain parts of the code based on specific conditions.

#### Why if-else Statements are Important

If-else statements enable decision-making in programs, allowing for dynamic and responsive code execution based on varying inputs and conditions.

***

### 2. Basic if Statement

The `if` statement evaluates a condition, and if the condition is true, it executes a block of code.

#### Syntax

```python
if condition:
    # block of code to be executed if the condition is true
```

#### Example

```python
# Basic if statement example
x = 10
if x > 5:
    print("x is greater than 5")  # Output: x is greater than 5
```

***

### 3. if-else Statement

The `if-else` statement provides an alternative block of code that executes if the condition is false.

#### Syntax

```python
if condition:
    # block of code to be executed if the condition is true
else:
    # block of code to be executed if the condition is false
```

#### Example

```python
# if-else statement example
x = 4
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")  # Output: x is not greater than 5
```

***

### 4. if-elif-else Statement

The `if-elif-else` statement allows you to check multiple conditions, executing different blocks of code depending on which condition is true.

#### Syntax

```python
if condition1:
    # block of code to be executed if condition1 is true
elif condition2:
    # block of code to be executed if condition2 is true
else:
    # block of code to be executed if neither condition1 nor condition2 is true
```

#### Example

```python
# if-elif-else statement example
x = 10
if x < 5:
    print("x is less than 5")
elif x == 10:
    print("x is 10")  # Output: x is 10
else:
    print("x is greater than 5 and not equal to 10")
```

***

### 5. Nested if Statements

You can use nested if statements to check multiple conditions in a more complex way. An if statement inside another if statement is called a nested if statement.

#### Syntax

```python
if condition1:
    # block of code to be executed if condition1 is true
    if condition2:
        # block of code to be executed if condition2 is true
```

#### Example

```python
# Nested if statement example
x = 10
y = 20
if x > 5:
    if y > 15:
        print("x is greater than 5 and y is greater than 15")  # Output: x is greater than 5 and y is greater than 15
```

***

### 6. Conditional Expressions (Ternary Operator)

Conditional expressions, also known as ternary operators, provide a concise way to perform an if-else statement in a single line of code.

#### Syntax

```python
variable = value_if_true if condition else value_if_false
```

#### Example

```python
# Ternary operator example
x = 10
result = "x is greater than 5" if x > 5 else "x is not greater than 5"
print(result)  # Output: x is greater than 5
```

***

### 7. Flowchart

Below is a flowchart that visually represents the structure of if-else statements.



1. **Start**: Begin the process.
2. **Condition**: Evaluate the condition.
3. **True**: If the condition is true, execute the block of code under the `if` statement.
4. **False**: If the condition is false, execute the block of code under the `else` statement (if present).
5. **End**: The process ends.

***

### 8. Practical Examples

#### Example 1: Checking Even or Odd Number

```python
# Check if a number is even or odd
num = 7
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")  # Output: 7 is odd
```

#### Example 2: Grade Classification

```python
# Grade classification based on score
score = 85
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'
print(f"Grade: {grade}")  # Output: Grade: B
```

#### Example 3: Password Validation

```python
# Password validation
password = "securepassword"
if len(password) < 8:
    print("Password is too short")
elif not any(char.isdigit() for char in password):
    print("Password should have at least one numeral")
elif not any(char.isupper() for char in password):
    print("Password should have at least one uppercase letter")
else:
    print("Password is valid")  # Output: Password is valid
```

***

### 9. Common Pitfalls and Best Practices

#### Pitfalls

1. **Incorrect Indentation**: Python relies on indentation to define blocks of code. Ensure proper indentation to avoid syntax errors.
2. **Overcomplicating Conditions**: Keep conditions simple and readable. Complex conditions can be hard to debug.
3. **Neglecting Edge Cases**: Always consider and handle edge cases in your conditions.

#### Best Practices

1. **Use Descriptive Conditions**: Write conditions that are easy to understand.
2. **Avoid Deep Nesting**: Minimize the use of nested if statements to improve code readability.
3. **Use elif for Multiple Conditions**: Use `elif` instead of multiple `if` statements for clarity and efficiency.

```python
# Good example with descriptive conditions and elif
age = 25
if age < 18:
    print("Minor")
elif 18 <= age < 65:
    print("Adult")  # Output: Adult
else:
    print("Senior")
```

***

This concludes our detailed tutorial on Python if-else statements. We hope you found this tutorial helpful and informative. For more tutorials and resources, visit codeswithpankaj.com. Happy coding!
