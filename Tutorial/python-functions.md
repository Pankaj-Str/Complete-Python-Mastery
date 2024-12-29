# Python Functions

## Python Functions Tutorial

Welcome to this comprehensive tutorial on Python functions, brought to you by codeswithpankaj.com. In this tutorial, we will explore various aspects of functions in Python, covering their definition, usage, and practical examples. By the end of this tutorial, you will have a thorough understanding of how to use functions effectively in your Python programs.

### Table of Contents

1. Introduction to Functions
2. Defining a Function
3. Calling a Function
4. Function Arguments
   * Positional Arguments
   * Keyword Arguments
   * Default Arguments
   * Variable-length Arguments (\*args and \*\*kwargs)
5. Return Statement
6. Scope of Variables
   * Local Scope
   * Global Scope
   * Nonlocal Scope
7. Lambda Functions
8. Higher-Order Functions
9. Built-in Functions
10. Recursion
11. Function Annotations
12. Practical Examples
13. Common Pitfalls and Best Practices

***

### 1. Introduction to Functions

Functions are reusable blocks of code that perform a specific task. They help to modularize code, making it more readable, maintainable, and reusable. Functions can take inputs, process them, and return an output.

#### Why Functions are Important

Functions help to:

* Reduce code duplication
* Improve code organization
* Simplify code maintenance
* Enhance code readability

***

### 2. Defining a Function

A function is defined using the `def` keyword followed by the function name and parentheses `()`. The code block within every function starts with a colon `:` and is indented.

#### Syntax

```python
def function_name(parameters):
    # block of code
    return expression
```

#### Example

```python
# Defining a function
def greet():
    print("Hello, World!")

# Calling the function
greet()  # Output: Hello, World!
```

***

### 3. Calling a Function

To call a function, use the function name followed by parentheses. If the function has parameters, pass the arguments inside the parentheses.

#### Example

```python
# Function with parameters
def greet(name):
    print(f"Hello, {name}!")

# Calling the function with an argument
greet("Pankaj")  # Output: Hello, Pankaj!
```

***

### 4. Function Arguments

#### Positional Arguments

Positional arguments are passed to the function in the order in which they are defined.

```python
# Function with positional arguments
def add(a, b):
    return a + b

# Calling the function with positional arguments
result = add(5, 3)
print(result)  # Output: 8
```

#### Keyword Arguments

Keyword arguments are passed to the function by explicitly specifying the parameter names.

```python
# Function with keyword arguments
def greet(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")

# Calling the function with keyword arguments
greet(first_name="Pankaj", last_name="Kumar")  # Output: Hello, Pankaj Kumar!
```

#### Default Arguments

Default arguments are used to provide default values for parameters. If no argument is passed, the default value is used.

```python
# Function with default arguments
def greet(name="Guest"):
    print(f"Hello, {name}!")

# Calling the function without an argument
greet()  # Output: Hello, Guest!

# Calling the function with an argument
greet("Pankaj")  # Output: Hello, Pankaj!
```

#### Variable-length Arguments (\*args and \*\*kwargs)

Variable-length arguments allow you to pass an arbitrary number of arguments to a function.

**\*args**

`*args` is used to pass a non-keyworded, variable-length argument list.

```python
# Function with *args
def add(*args):
    result = 0
    for num in args:
        result += num
    return result

# Calling the function with variable-length arguments
print(add(1, 2, 3, 4))  # Output: 10
```

**\*\*kwargs**

`**kwargs` is used to pass a keyworded, variable-length argument list.

```python
# Function with **kwargs
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Calling the function with variable-length keyword arguments
display_info(name="Pankaj", age=30, city="Delhi")
# Output:
# name: Pankaj
# age: 30
# city: Delhi
```

***

### 5. Return Statement

The `return` statement is used to exit a function and return a value to the caller.

#### Example

```python
# Function with return statement
def add(a, b):
    return a + b

# Calling the function and storing the returned value
result = add(5, 3)
print(result)  # Output: 8
```

***

### 6. Scope of Variables

The scope of a variable determines where it can be accessed within the code.

#### Local Scope

Variables defined inside a function are in the local scope and can only be accessed within that function.

```python
# Local scope example
def my_function():
    local_var = "I am local"
    print(local_var)

my_function()  # Output: I am local
# print(local_var)  # This will cause an error as 'local_var' is not accessible outside the function
```

#### Global Scope

Variables defined outside any function are in the global scope and can be accessed from anywhere in the code.

```python
# Global scope example
global_var = "I am global"

def my_function():
    print(global_var)

my_function()  # Output: I am global
print(global_var)  # Output: I am global
```

#### Nonlocal Scope

The `nonlocal` keyword is used to work with variables inside nested functions, where the variable should not belong to the inner function.

```python
# Nonlocal scope example
def outer_function():
    nonlocal_var = "I am nonlocal"

    def inner_function():
        nonlocal nonlocal_var
        nonlocal_var = "Modified nonlocal"
    
    inner_function()
    print(nonlocal_var)

outer_function()  # Output: Modified nonlocal
```

***

### 7. Lambda Functions

Lambda functions are small anonymous functions defined using the `lambda` keyword. They can have any number of arguments but only one expression.

#### Syntax

```python
lambda arguments: expression
```

#### Example

```python
# Lambda function example
add = lambda a, b: a + b

# Calling the lambda function
result = add(5, 3)
print(result)  # Output: 8
```

***

### 8. Higher-Order Functions

Higher-order functions are functions that can take other functions as arguments or return them as results.

#### Example

```python
# Higher-order function example
def apply_function(func, value):
    return func(value)

# Defining a function to be passed as an argument
def square(x):
    return x * x

# Calling the higher-order function
result = apply_function(square, 5)
print(result)  # Output: 25
```

***

### 9. Built-in Functions

Python provides a wide range of built-in functions that can be used to perform various tasks.

#### Common Built-in Functions

* `len()`: Returns the length of an object
* `max()`: Returns the largest item
* `min()`: Returns the smallest item
* `sum()`: Sums the items of an iterable
* `abs()`: Returns the absolute value of a number
* `sorted()`: Returns a sorted list

#### Examples

```python
# Using built-in functions
numbers = [1, 2, 3, 4, 5]

print(len(numbers))  # Output: 5
print(max(numbers))  # Output: 5
print(min(numbers))  # Output: 1
print(sum(numbers))  # Output: 15
print(abs(-10))      # Output: 10
print(sorted(numbers, reverse=True))  # Output: [5, 4, 3, 2, 1]
```

***

### 10. Recursion

Recursion is a process where a function calls itself as a subroutine. It allows the function to be repeated several times as it can call itself during its execution.

#### Example

```python
# Recursive function example: factorial
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Calling the recursive function
result = factorial(5)
print(result)  # Output: 120
```

#### Advantages of Recursion

* Simplifies code for complex problems
* Reduces the need for loop constructs

#### Disadvantages of Recursion

* Can lead to high memory usage
* Risk of infinite recursion if the base case is not properly defined

***

### 11. Function Annotations

Function annotations provide a way of associating various parts of a function with arbitrary python expressions at compile time. They are used to add metadata to function arguments and return values.

#### Syntax

```python
def function_name(parameter: annotation) -> return_annotation:
    # block of code
```

#### Example

```python
# Function with annotations
def add(a: int, b: int) -> int:
    return a + b

# Calling the function
result = add(5, 3)
print(result)  # Output: 8

# Checking the annotations
print(add.__annotations__)  # Output: {'a': <class 'int'>, '

b': <class 'int'>, 'return': <class 'int'>}
```

***

### 12. Practical Examples

#### Example 1: Prime Number Checker

```python
# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Calling the function
number = 29
print(f"Is {number} a prime number? {is_prime(number)}")  # Output: Is 29 a prime number? True
```

#### Example 2: Fibonacci Sequence Generator

```python
# Function to generate Fibonacci sequence up to n terms
def fibonacci(n):
    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Calling the function
print(fibonacci(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

#### Example 3: Sorting a List of Tuples

```python
# Function to sort a list of tuples based on the second element
def sort_tuples(tuples_list):
    return sorted(tuples_list, key=lambda x: x[1])

# Calling the function
tuples = [(1, 'b'), (2, 'a'), (3, 'c')]
print(sort_tuples(tuples))  # Output: [(2, 'a'), (1, 'b'), (3, 'c')]
```

***

### 13. Common Pitfalls and Best Practices

#### Pitfalls

1. **Unintended Variable Scope**: Be cautious of variable scope to avoid unintended behavior.
2. **Incorrect Argument Passing**: Ensure correct order and types of arguments are passed to functions.
3. **Missing Return Statements**: Remember to use return statements to return values from functions.

#### Best Practices

1. **Use Descriptive Names**: Use meaningful names for functions and variables to improve code readability.
2. **Keep Functions Short and Focused**: Write functions that perform a single task for better modularity and maintainability.
3. **Utilize Function Annotations**: Use annotations to provide additional information about function parameters and return values.

```python
# Good example with descriptive names and function annotations
def calculate_area(radius: float) -> float:
    PI = 3.14159
    return PI * (radius ** 2)

# Calling the function
print(calculate_area(5))  # Output: 78.53975
```

***

This concludes our detailed tutorial on Python functions. We hope you found this tutorial helpful and informative. For more tutorials and resources, visit codeswithpankaj.com. Happy coding!
