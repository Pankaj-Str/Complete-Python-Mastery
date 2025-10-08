# Functions

Functions are fundamental building blocks in Python programming. They allow you to encapsulate reusable code, improve modularity, and make your programs more organized and efficient. This tutorial will cover the key aspects of functions in Python, from basics to more advanced concepts, with detailed explanations and examples. We'll assume you have a basic understanding of Python syntax.

All examples are written in Python 3.x, which is the standard as of 2025. You can copy and paste them into a Python interpreter or script to test them.

## 1. Defining and Calling Functions

### Defining a Function
In Python, you define a function using the `def` keyword, followed by the function name, parentheses for parameters, and a colon. The function body is indented.

```python
def greet():
    print("Hello, World!")
```

- `def`: Keyword to define the function.
- `greet`: Function name (should be descriptive and follow snake_case convention).
- `()`: Parentheses for parameters (empty here since no parameters).
- Indented block: The code that runs when the function is called.

### Calling a Function
To execute the function, call it by its name followed by parentheses.

```python
greet()  # Output: Hello, World!
```

If you don't call the function, nothing happens—it's just defined.

### Example with Parameters
Functions can take inputs called parameters.

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!
```

Here, `name` is a parameter, and `"Alice"` is an argument passed when calling.

## 2. Function Arguments

Python supports flexible argument passing. Let's break it down.

### Positional Arguments
Arguments are passed in the order of parameters.

```python
def add(a, b):
    print(a + b)

add(5, 3)  # Output: 8
```

### Default Arguments
You can provide default values for parameters. If no argument is passed, the default is used.

```python
def greet(name="World"):
    print(f"Hello, {name}!")

greet()        # Output: Hello, World!
greet("Bob")   # Output: Hello, Bob!
```

Defaults must come after non-default parameters in the definition.

### Keyword Arguments
Pass arguments by specifying the parameter name. Order doesn't matter.

```python
def introduce(name, age):
    print(f"{name} is {age} years old.")

introduce(age=30, name="Charlie")  # Output: Charlie is 30 years old.
```

This is useful for clarity, especially with many parameters.

### Variable-Length Arguments
For arbitrary numbers of arguments:

- `*args`: For non-keyword variable arguments (as a tuple).

```python
def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    print(total)

sum_numbers(1, 2, 3)       # Output: 6
sum_numbers(4, 5, 6, 7)    # Output: 22
```

- `**kwargs`: For keyword variable arguments (as a dictionary).

```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="David", age=25, city="New York")
# Output:
# name: David
# age: 25
# city: New York
```

You can combine them: `def func(pos1, pos2=def_val, *args, **kwargs)`.

### Argument Unpacking
Use `*` for iterables and `**` for dictionaries when passing arguments.

```python
nums = [1, 2, 3]
sum_numbers(*nums)  # Equivalent to sum_numbers(1, 2, 3)

info = {"name": "Eve", "age": 28}
print_info(**info)  # Passes as keyword arguments
```

## 3. Return Statement

Functions can return values using `return`. Without it, the function returns `None` by default.

```python
def multiply(x, y):
    return x * y

result = multiply(4, 5)
print(result)  # Output: 20
```

- You can return multiple values as a tuple.

```python
def get_stats(numbers):
    return sum(numbers), min(numbers), max(numbers)

total, minimum, maximum = get_stats([10, 20, 30])
print(total, minimum, maximum)  # Output: 60 10 30
```

- Early return: Use `return` to exit early.

```python
def check_even(num):
    if num % 2 == 0:
        return True
    return False  # Or just 'return num % 2 == 0' in one line
```

## 4. Scope of Variables (Local vs Global)

Scope determines where a variable is accessible.

### Local Variables
Defined inside a function; accessible only within it.

```python
def local_example():
    local_var = "I'm local!"
    print(local_var)

local_example()  # Output: I'm local!
# print(local_var)  # Error: NameError, local_var not defined outside
```

### Global Variables
Defined outside functions; accessible everywhere, but to modify inside a function, use `global`.

```python
global_var = "I'm global!"

def read_global():
    print(global_var)  # Works without 'global'

def modify_global():
    global global_var
    global_var = "Modified global!"

read_global()       # Output: I'm global!
modify_global()
print(global_var)   # Output: Modified global!
```

### Nonlocal (for Nested Functions)
In nested functions, use `nonlocal` to modify variables from the enclosing scope.

```python
def outer():
    x = "outer"
    def inner():
        nonlocal x
        x = "modified"
    inner()
    print(x)  # Output: modified

outer()
```

Avoid overusing globals; prefer passing arguments.

## 5. Recursive Functions

A function that calls itself. Useful for problems like factorials or tree traversals. Needs a base case to avoid infinite recursion.

```python
def factorial(n):
    if n == 0 or n == 1:  # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive call

print(factorial(5))  # Output: 120 (5*4*3*2*1)
```

- Python has a recursion limit (default ~1000) to prevent stack overflow.

```python
import sys
print(sys.getrecursionlimit())  # Typically 1000
```

For deep recursion, consider iterative alternatives.

### Example: Fibonacci Sequence

```python
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))  # Output: 8 (0,1,1,2,3,5,8)
```

This is inefficient for large n due to repeated calculations; memoization (e.g., with `@lru_cache`) can optimize it.

## 6. Anonymous Functions (Lambda)

Lambda functions are small, nameless functions defined with `lambda`. Useful for short operations, often with higher-order functions.

Syntax: `lambda arguments: expression`

```python
add = lambda x, y: x + y
print(add(2, 3))  # Output: 5
```

- Single expression only; no statements.
- Often used inline.

### Example with Sorting

```python
points = [(1, 2), (3, 1), (5, 0)]
points.sort(key=lambda p: p[1])  # Sort by y-coordinate
print(points)  # Output: [(5, 0), (3, 1), (1, 2)]
```

## 7. map(), filter(), reduce()

These are higher-order functions for functional programming styles. They take a function and an iterable.

### map()
Applies a function to each item in an iterable, returns a map object (convert to list).

```python
numbers = [1, 2, 3, 4]
squared = map(lambda x: x**2, numbers)
print(list(squared))  # Output: [1, 4, 9, 16]
```

With multiple iterables:

```python
a = [1, 2]
b = [3, 4]
sums = map(lambda x, y: x + y, a, b)
print(list(sums))  # Output: [4, 6]
```

### filter()
Filters items based on a function that returns True/False.

```python
numbers = [1, 2, 3, 4, 5, 6]
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))  # Output: [2, 4, 6]
```

### reduce()
From `functools` module; applies a function cumulatively to items, reducing to a single value.

```python
from functools import reduce

numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 24 (1*2*3*4)
```

With initial value:

```python
sum_with_init = reduce(lambda x, y: x + y, numbers, 10)
print(sum_with_init)  # Output: 20 (10+1+2+3+4)
```

These functions promote concise, expressive code. For large datasets, consider generators to save memory.

## Best Practices and Tips
- Keep functions short and focused (single responsibility).
- Use descriptive names.
- Document with docstrings: `"""Description"""` inside the function.
- Handle errors with try-except if needed.
- For performance, profile recursive or higher-order functions.
- Python functions are first-class: You can pass them as arguments, return them, etc.

```python
def apply_func(func, value):
    return func(value)

print(apply_func(lambda x: x*2, 5))  # Output: 10
```

