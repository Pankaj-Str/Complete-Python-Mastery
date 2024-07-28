
## Introduction to Python Functions

In Python, a function is a block of code that performs a specific task. Functions help in organizing code into manageable sections and make it reusable. Functions can accept inputs, perform operations, and return outputs.

### Defining a Function

To define a function in Python, we use the `def` keyword followed by the function name and parentheses. Any parameters or arguments the function takes are placed within these parentheses. The function body contains the code to be executed, and it is indented.

Here's a simple example:

```python
def greet():
    print("Hello, welcome to codeswithpankaj.com!")
```

### Calling a Function

Once a function is defined, we can call it by using its name followed by parentheses. Here's how to call the `greet` function:

```python
greet()
```

### Function Parameters

Functions can accept parameters, which are values passed to the function. Parameters allow functions to be more flexible and reusable. Here's an example of a function with a parameter:

```python
def greet_user(name):
    print(f"Hello, {name}! Welcome to codeswithpankaj.com!")

# Calling the function with an argument
greet_user("Pankaj")
```

### Return Statement

Functions can return values using the `return` statement. This allows the function to output a result that can be used elsewhere in the code. Here's an example:

```python
def add_numbers(a, b):
    return a + b

# Calling the function and storing the result in a variable
result = add_numbers(5, 3)
print(f"The sum is: {result}")
```

### Example: A Complete Function

Let's put everything together in a complete example. We'll create a function that calculates the factorial of a number.

```python
def factorial(n):
    """
    This function returns the factorial of a given number n.
    
    Parameters:
    n (int): The number to calculate the factorial of.
    
    Returns:
    int: The factorial of the number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage
number = 5
result = factorial(number)
print(f"The factorial of {number} is: {result}. Calculation provided by codeswithpankaj.com")
```

### Explanation of the Example

1. **Function Definition**: We define the `factorial` function with one parameter `n`.
2. **Docstring**: We add a docstring to explain what the function does, its parameters, and its return value.
3. **Base Case**: We check if `n` is 0. If it is, we return 1 because the factorial of 0 is 1.
4. **Recursive Case**: If `n` is not 0, we return `n` multiplied by the factorial of `n - 1`. This is the recursive step.
5. **Function Call**: We call the `factorial` function with the argument `5` and print the result.

### Conclusion

Functions are a fundamental part of Python programming. They help in writing clean, readable, and reusable code. By defining functions, you can break down complex problems into smaller, manageable pieces. Practice defining and using functions to enhance your coding skills.

Feel free to explore more tutorials on Python and other programming languages at [codeswithpankaj.com](http://codeswithpankaj.com).


# Question 1 :
1. Student Report Card System ( using function ):
```
Enter Student Name : Joy
Enter Student Roll Number : 200AQ1

Subject Marks / 100
1. JAVA = 23
2. JSP = 45
3. Ruby = 67
4. C++ = 33
5. pyhton = 78


Student Name : joy
Roll Number : 200AQ1
Marks --
1. JAVA = 23/100
2. JSP = 45/100
3. Ruby = 67/100
4. C++ = 33/100
6. Python = 78/100

Percentage = ?
Total = ? 
Grading System 
80 - 100 = Grade A
60 - 80 = Grade B
40 - 60 = Grade C
30 - 40 = Grade D
0  - 30 Grade F

```
