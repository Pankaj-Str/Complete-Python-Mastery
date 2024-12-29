# Python Math

## Python Math

Welcome to [codeswithpankaj.com](https://codeswithpankaj.com)! In this tutorial, we will explore the `math` module in Python. We'll cover how to perform various mathematical operations, work with constants, and provide detailed examples to illustrate their application.

### Table of Contents

1. Introduction to the `math` Module
2. Common Mathematical Functions
3. Trigonometric Functions
4. Logarithmic and Exponential Functions
5. Special Functions
6. Mathematical Constants
7. Practical Examples
8. Summary

### 1. Introduction to the `math` Module

#### What is the `math` Module?

The `math` module in Python provides access to various mathematical functions and constants. It includes functions for arithmetic operations, trigonometry, logarithms, and more.

#### Key Points

* The `math` module contains a wide range of mathematical functions.
* It provides access to mathematical constants like `pi` and `e`.

### 2. Common Mathematical Functions

#### Example: Using Basic Mathematical Functions

```python
import math

# Absolute value
print(math.fabs(-5))  # Output: 5.0

# Square root
print(math.sqrt(16))  # Output: 4.0

# Power
print(math.pow(2, 3))  # Output: 8.0

# Floor and Ceiling
print(math.floor(4.7))  # Output: 4
print(math.ceil(4.3))   # Output: 5

# Factorial
print(math.factorial(5))  # Output: 120
```

### 3. Trigonometric Functions

#### Example: Using Trigonometric Functions

```python
import math

# Sine, Cosine, and Tangent
print(math.sin(math.pi / 2))  # Output: 1.0
print(math.cos(0))            # Output: 1.0
print(math.tan(math.pi / 4))  # Output: 1.0

# Inverse Trigonometric Functions
print(math.asin(1))  # Output: 1.5707963267948966 (pi/2)
print(math.acos(1))  # Output: 0.0
print(math.atan(1))  # Output: 0.7853981633974483 (pi/4)

# Hyperbolic Functions
print(math.sinh(1))  # Output: 1.1752011936438014
print(math.cosh(1))  # Output: 1.5430806348152437
print(math.tanh(1))  # Output: 0.7615941559557649
```

### 4. Logarithmic and Exponential Functions

#### Example: Using Logarithmic and Exponential Functions

```python
import math

# Natural logarithm
print(math.log(10))  # Output: 2.302585092994046

# Logarithm base 10
print(math.log10(10))  # Output: 1.0

# Exponential function
print(math.exp(2))  # Output: 7.38905609893065

# Power function (equivalent to ** operator)
print(math.pow(2, 3))  # Output: 8.0
```

### 5. Special Functions

#### Example: Using Special Functions

```python
import math

# Gamma function
print(math.gamma(5))  # Output: 24.0

# Error function
print(math.erf(1))  # Output: 0.8427007929497149

# Complementary error function
print(math.erfc(1))  # Output: 0.15729920705028513
```

### 6. Mathematical Constants

#### Example: Using Mathematical Constants

```python
import math

# Pi
print(math.pi)  # Output: 3.141592653589793

# Euler's number (e)
print(math.e)  # Output: 2.718281828459045

# Tau (2*pi)
print(math.tau)  # Output: 6.283185307179586

# Infinity
print(math.inf)  # Output: inf

# Not a Number (NaN)
print(math.nan)  # Output: nan
```

### 7. Practical Examples

#### Example 1: Calculating the Area of a Circle

```python
import math

def area_of_circle(radius):
    return math.pi * math.pow(radius, 2)

radius = 5
print(f"Area of circle with radius {radius}: {area_of_circle(radius)}")
```

#### Example 2: Calculating Compound Interest

```python
import math

def compound_interest(principal, rate, time):
    return principal * math.pow((1 + rate / 100), time)

principal = 1000
rate = 5
time = 2
print(f"Compound Interest: {compound_interest(principal, rate, time)}")
```

#### Example 3: Solving a Quadratic Equation

```python
import math

def solve_quadratic(a, b, c):
    discriminant = math.pow(b, 2) - 4 * a * c
    if discriminant < 0:
        return "No real roots"
    elif discriminant == 0:
        root = -b / (2 * a)
        return f"One root: {root}"
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return f"Two roots: {root1} and {root2}"

a, b, c = 1, -3, 2
print(solve_quadratic(a, b, c))
```

### 8. Summary

In this tutorial, we explored the `math` module in Python, its importance, and how to use its functions and constants. We covered common mathematical functions, trigonometric functions, logarithmic and exponential functions, special functions, and mathematical constants. We also provided practical examples to illustrate the application of the `math` module. The `math` module is a powerful tool for performing mathematical operations in Python.

For more tutorials and in-depth explanations, visit [codeswithpankaj.com](https://codeswithpankaj.com)!

***

This tutorial provides a comprehensive overview of Python's `math` module, detailing each topic and subtopic with examples and explanations. For more such tutorials, keep following [codeswithpankaj.com](https://codeswithpankaj.com)!
