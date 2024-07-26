### Introduction to Variables in Python

Variables are fundamental to programming. They are used to store data values. In Python, variables are created by assigning a value to them. Python is dynamically typed, which means you don’t need to declare the type of the variable beforehand. The type is inferred from the value assigned.

### Creating Variables

To create a variable in Python, simply assign a value to a variable name using the `=` operator.

```python
# Creating variables
name = "John Doe"
age = 25
height = 5.9
is_student = True
```

In the example above:
- `name` is a string variable.
- `age` is an integer variable.
- `height` is a floating-point variable.
- `is_student` is a boolean variable.

### Variable Naming Rules

1. **Names can include letters, numbers, and underscores (`_`).**
2. **Names must start with a letter or an underscore.**
3. **Names cannot start with a number.**
4. **Names are case-sensitive.**
5. **Avoid using Python reserved keywords as variable names (e.g., `if`, `else`, `for`).**

**Examples of valid variable names:**
```python
my_variable = 10
variable_2 = 20
_variable = 30
```

**Examples of invalid variable names:**
```python
2variable = 10  # Starts with a number
my-variable = 20  # Contains a hyphen
```

### Data Types

In Python, the most common data types for variables include:

1. **Integer (`int`)** - Represents whole numbers.
   ```python
   age = 30
   ```

2. **Floating-point (`float`)** - Represents decimal numbers.
   ```python
   height = 5.9
   ```

3. **String (`str`)** - Represents a sequence of characters.
   ```python
   name = "Alice"
   ```

4. **Boolean (`bool`)** - Represents `True` or `False`.
   ```python
   is_student = True
   ```

5. **List** - A collection of items.
   ```python
   numbers = [1, 2, 3, 4, 5]
   ```

6. **Dictionary** - A collection of key-value pairs.
   ```python
   person = {"name": "Bob", "age": 30}
   ```

### Type Checking

You can check the type of a variable using the `type()` function.

```python
x = 10
print(type(x))  # Output: <class 'int'>

y = 5.7
print(type(y))  # Output: <class 'float'>
```

### Variable Reassignment

Variables in Python are dynamically typed, so you can change the type of a variable by reassigning it.

```python
x = 10          # x is an integer
x = "Hello"     # x is now a string
```

### Multiple Variable Assignment

You can assign multiple variables in a single line.

```python
x, y, z = 5, 10, 15
```

### Swapping Variables

Python allows you to swap values between variables easily.

```python
a = 5
b = 10
a, b = b, a  # Now a is 10 and b is 5
```

### Constants

In Python, constants are usually declared in uppercase and are not enforced by the language, but it's a convention to indicate that their values should not change.

```python
PI = 3.14159
```

### Conclusion

Variables are a crucial part of Python programming. They allow you to store and manipulate data in your programs. Understanding how to create and use variables effectively will help you write more efficient and readable code.

For more tutorials and coding tips, visit [codeswithpankaj.com](https://codeswithpankaj.com).