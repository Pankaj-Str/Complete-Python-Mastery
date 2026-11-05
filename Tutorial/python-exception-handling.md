# Python Exception Handling

## Python Exception Handling

Welcome to [codeswithpankaj.com](https://codeswithpankaj.com)! In this tutorial, we will explore the concept of exception handling in Python. We'll cover what exceptions are, how to handle them, and provide detailed examples to illustrate its application.

### Table of Contents

1. Introduction to Exceptions
2. Why Use Exception Handling?
3. Types of Exceptions
4. The `try` and `except` Blocks
5. Handling Multiple Exceptions
6. The `else` and `finally` Blocks
7. Raising Exceptions
8. Custom Exceptions
9. Practical Examples
10. Summary

### 1. Introduction to Exceptions

#### What are Exceptions?

Exceptions are events that occur during the execution of a program that disrupt the normal flow of instructions. They are typically errors that need to be addressed to prevent the program from crashing.

#### Key Points

* Exceptions indicate errors and exceptional conditions in the program.
* Python provides a robust mechanism to handle exceptions gracefully.

### 2. Why Use Exception Handling?

* **Prevent Crashes:** Exception handling prevents the program from terminating unexpectedly.
* **Debugging:** It helps in debugging by providing detailed error messages.
* **Graceful Degradation:** It allows the program to continue execution or fail gracefully.

### 3. Types of Exceptions

Python has many built-in exceptions, such as:

* `SyntaxError`
* `TypeError`
* `IndexError`
* `KeyError`
* `ValueError`
* `ZeroDivisionError`

### 4. The `try` and `except` Blocks

#### Basic Exception Handling

The `try` block allows you to test a block of code for errors. The `except` block lets you handle the error.

```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

### 5. Handling Multiple Exceptions

You can handle multiple exceptions by specifying multiple `except` blocks.

```python
try:
    x = int("abc")
except ValueError:
    print("ValueError occurred")
except TypeError:
    print("TypeError occurred")
```

#### Using a Single `except` Block for Multiple Exceptions

```python
try:
    x = int("abc")
except (ValueError, TypeError) as e:
    print(f"An error occurred: {e}")
```

### 6. The `else` and `finally` Blocks

#### The `else` Block

The `else` block is executed if no exceptions are raised in the `try` block.

```python
try:
    x = int("10")
except ValueError:
    print("ValueError occurred")
else:
    print("No error occurred")
```

#### The `finally` Block

The `finally` block is executed regardless of whether an exception occurs or not.

```python
try:
    x = int("10")
except ValueError:
    print("ValueError occurred")
finally:
    print("This will always be executed")
```

### 7. Raising Exceptions

You can raise an exception using the `raise` statement.

```python
def check_age(age):
    if age < 18:
        raise ValueError("Age must be at least 18")
    return "Age is valid"

try:
    print(check_age(16))
except ValueError as e:
    print(e)
```

### 8. Custom Exceptions

You can create custom exceptions by defining a new class that inherits from the built-in `Exception` class.

```python
class CustomError(Exception):
    pass

def check_value(value):
    if value < 0:
        raise CustomError("Value must be non-negative")

try:
    check_value(-1)
except CustomError as e:
    print(e)
```

### 9. Practical Examples

#### Example 1: Handling File Operations

```python
try:
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found")
else:
    print(content)
finally:
    print("File operation complete")
```

#### Example 2: Division Function with Exception Handling

```python
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "Invalid input type"
    else:
        return result
    finally:
        print("Division operation complete")

print(divide(10, 2))
print(divide(10, 0))
print(divide(10, "a"))
```

#### Example 3: Custom Exception in User Input Validation

```python
class InvalidInputError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def get_positive_number():
    try:
        number = int(input("Enter a positive number: "))
        if number <= 0:
            raise InvalidInputError("The number must be positive")
        return number
    except ValueError:
        return "Invalid input type"
    except InvalidInputError as e:
        return e.message

print(get_positive_number())
```

### 10. Summary

In this tutorial, we explored the concept of exception handling in Python, its importance, and how to implement it using `try`, `except`, `else`, and `finally` blocks. We also covered raising exceptions, creating custom exceptions, and practical examples to illustrate the application of exception handling. Exception handling is a powerful feature that enhances code robustness, readability, and maintainability.

For more tutorials and in-depth explanations, visit [codeswithpankaj.com](https://codeswithpankaj.com)!

***

This tutorial provides a comprehensive overview of Python exception handling, detailing each topic and subtopic with examples and explanations. For more such tutorials, keep following [codeswithpankaj.com](https://codeswithpankaj.com)!
