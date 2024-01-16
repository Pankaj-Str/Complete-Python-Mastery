## Primitive Types

# Python Variables

In Python, variables are used to store data values. They provide a way to name and reference data, making it easier to work with information in your programs.

## Variable Naming Rules

- Variable names can contain letters, numbers, and underscores.
- Variable names must start with a letter or an underscore.
- Variable names are case-sensitive (`myVar` and `myvar` are different variables).
- Avoid using Python reserved keywords (e.g., `if`, `while`, `for`) as variable names.

## Variable Assignment

In Python, you assign a value to a variable using the assignment operator `=`. Here's an example:

```python
age = 25
name = "Alice"
```

## Variable Data Types

Python is dynamically typed, which means you don't need to specify a variable's data type explicitly. The interpreter determines the data type based on the assigned value. Common data types include:

- `int`: Integer numbers (e.g., `42`, `-10`).
- `float`: Floating-point numbers (e.g., `3.14`, `-0.5`).
- `str`: Strings (e.g., `"Hello, World!"`, `'Python'`).
- `bool`: Boolean values (`True` or `False`).
- `list`, `tuple`, `set`, `dict`: Data structures to store multiple values.

## Variable Reassignment

You can change the value of a variable by assigning a new value to it:

```python
x = 10
x = 20  # Reassigning the value of x to 20
```

## Variable Conventions

Following naming conventions improves code readability:

- Use descriptive names (`name` instead of `n`, `counter` instead of `c`).
- Use lowercase letters for variable names (`my_variable`).
- For multi-word variable names, use underscores or camelCase (`user_name` or `userName`).

## Variable Scope

A variable's scope defines where it can be accessed. Variables can have local or global scope:

- **Local**: Defined within a function and accessible only inside that function.
- **Global**: Defined outside any function and accessible throughout the program.

```python
def my_function():
    local_var = 10  # Local variable

global_var = 20  # Global variable
```

## Constants

Though Python doesn't have true constants, conventionally, variables in ALL_CAPS are treated as constants and shouldn't be changed after being assigned.

```python
PI = 3.14159
```


# Python Variable Names

In Python, variable names play a crucial role in writing clear, readable, and maintainable code. Choosing meaningful and consistent variable names is essential for communicating the purpose and intent of your code to others.

## Naming Rules and Conventions

1. Variable names must start with a letter (a-z, A-Z) or an underscore (`_`).
2. Subsequent characters can be letters, digits (0-9), or underscores.
3. Variable names are case-sensitive (`myVar` and `myvar` are different).
4. Avoid using Python reserved keywords (e.g., `if`, `while`, `for`) as variable names.
5. Use descriptive names that convey the purpose of the variable (`counter` instead of `c`).
6. Separate words in variable names using underscores (`user_name`) or use camelCase (`userName`).
7. Follow a consistent naming style throughout your codebase.

## Naming Styles

1. **Snake Case**: Words are separated by underscores. Commonly used in Python.
   - Example: `user_age`, `total_students`

2. **Camel Case**: Words are concatenated without spaces, and each word's first letter (except the first one) is capitalized.
   - Example: `userName`, `totalStudents`

3. **Pascal Case**: Similar to camel case, but the first letter is also capitalized.
   - Example: `UserName`, `TotalStudents`

4. **UPPERCASE**: Used for constants or variables with a fixed value that should not be changed.
   - Example: `PI`, `MAX_VALUE`

## Choosing Meaningful Names

- Use names that describe the purpose of the variable.
- Avoid using vague names like `data`, `value`, or single letters like `x`, `i`.
- Be consistent in your naming choices across your codebase.

## Avoiding Ambiguous Names

- Choose variable names that are not easily confused with existing functions or types.
- Avoid using similar names with different casing (e.g., `user_name` vs. `userName`).

## Examples

```python
# Good examples
user_name = "Alice"
total_students = 100
is_valid = True

# Avoid ambiguous or unclear names
n = 5  # Not clear
x = "hello"  # Not descriptive
```





Question 1 : Create a student marksheet program output like this 
```yaml

-- input Section 
1. Enter Student Name : Ravi
2. Enter Roll Number : RAVI009912
3. Enter Class : MCA
4. Enter JAVA Marks : 56
5. Enter C++ Marks : 89
6. Enter Python Marks : 12
7. Enter Ruby Marks : 56
8. Enter SQL Marks : 78

-- Output Section
Student Name : Ravi
Roll Number : RAVI009912
Class : MCA
Enter JAVA Marks : 56/100
C++ Marks : 89/100
Python Marks : 12/100
Ruby Marks : 56/100
SQL Marks : 78/100
   total = ?
   Per % = ?%
```
Question 2. Write a  Program to Print an Integer (Entered by the User) <br> <br>
Question 3. Write a  Program to Add Two Integers (Entered by the User) <br> <br>
Question 4. Write a  Program to Multiply two Floating Point Numbers (Entered by the User) <br> <br>





