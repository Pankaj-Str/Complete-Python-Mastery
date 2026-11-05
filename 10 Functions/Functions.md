

# Functions in Python

## What is a Function in Python?

A **function** is a block of reusable code that performs a specific task.
Instead of writing the same code again and again, we write it once inside a function and call it whenever needed.

### Why use functions?

* Code reuse
* Better readability
* Easy debugging
* Modular programming

---

## 1. Built-in Functions

Python provides many **ready-made functions**.

### Examples:

```python
print("Hello Python")
len("Python")
type(10)
sum([1, 2, 3])
```

---

## 2. User-Defined Functions

Functions created by the programmer.

### Syntax:

```python
def function_name():
    code
```

### Example:

```python
def greet():
    print("Welcome to Python")

greet()
```

---

## 3. Function with Parameters

Parameters allow passing data to a function.

### Example:

```python
def greet(name):
    print("Hello", name)

greet("Pankaj")
```

---

## 4. Function with Return Value

A function can **return a result** using `return`.

### Example:

```python
def add(a, b):
    return a + b

result = add(10, 20)
print(result)
```

---

## 5. Function with Multiple Parameters

You can pass more than one parameter.

### Example:

```python
def student(name, age):
    return name, age

print(student("Rahul", 21))
```

---

## 6. Default Parameter Function

Default values are used if no argument is provided.

### Example:

```python
def greet(name="Student"):
    print("Hello", name)

greet()
greet("Amit")
```

---

## 7. Keyword Arguments

Arguments passed using parameter names.

### Example:

```python
def employee(name, salary):
    print(name, salary)

employee(salary=50000, name="Ravi")
```

---

## 8. Arbitrary Arguments (*args)

Used when the number of arguments is unknown.

### Example:

```python
def total(*numbers):
    print(sum(numbers))

total(10, 20, 30, 40)
```

---

## 9. Arbitrary Keyword Arguments (**kwargs)

Used for key-value arguments.

### Example:

```python
def details(**info):
    print(info)

details(name="Pankaj", course="Python", exp=10)
```

---

## 10. Lambda (Anonymous) Function

A function without a name, written in one line.

### Syntax:

```python
lambda arguments: expression
```

### Example:

```python
square = lambda x: x * x
print(square(5))
```

---

## 11. Recursive Function

A function that **calls itself**.

### Example:

```python
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
```

---

## 12. Nested Function

A function inside another function.

### Example:

```python
def outer():
    def inner():
        print("Inside inner function")
    inner()

outer()
```

---

## 13. Function with Docstring

Docstring explains what the function does.

### Example:

```python
def add(a, b):
    """This function adds two numbers"""
    return a + b

print(add.__doc__)
```

---

## 14. Pass Statement in Function

Used when function body is empty.

### Example:

```python
def future_function():
    pass
```

---

## 15. Function Calling Another Function

One function can call another.

### Example:

```python
def add(a, b):
    return a + b

def calculate():
    print(add(5, 10))

calculate()
```

---

## Summary Table

| Function Type | Purpose                  |
| ------------- | ------------------------ |
| Built-in      | Predefined by Python     |
| User-defined  | Created by programmer    |
| Parameters    | Accept input             |
| Return        | Send output              |
| Default       | Use default value        |
| *args         | Multiple values          |
| **kwargs      | Key-value pairs          |
| Lambda        | One-line function        |
| Recursive     | Calls itself             |
| Nested        | Function inside function |

---


