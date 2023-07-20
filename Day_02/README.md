# 1 Python Comments 

Comments are used to add explanatory notes or annotations within the code. They are ignored by the Python interpreter and have no impact on the execution of the program. Comments are useful for documenting code, providing context, and making it easier for other developers (including yourself) to understand the code.

Python supports two types of comments:

1. Single-line comments: These comments start with the `#` symbol and extend till the end of the line. Anything after the `#` symbol on the same line is considered a comment.

   Example:
   ```python
   # This is a single-line comment
   x = 10  # Assigning a value to x
   ```

2. Multi-line comments (docstrings): These comments can span multiple lines and are enclosed within triple quotes (`'''` or `"""`). While multi-line comments are not strictly treated as comments by the interpreter, they are commonly used to provide documentation for functions, classes, and modules.

   Example:
   ```python
   '''
   This is a multi-line comment or a docstring.
   It can span multiple lines and is commonly used
   to document functions, classes, or modules.
   '''
   def add(a, b):
       '''
       This function adds two numbers and returns the result.
       '''
       return a + b
   ```

Comments are an important aspect of coding as they improve code readability, maintainability, and collaboration among developers. They help in understanding the purpose and functionality of code segments, making it easier to debug and modify the code in the future.

------------------------------------

# 2 Python Variables

Variables are used to store and manipulate data. They act as containers for holding values of different types, such as numbers, strings, lists, or objects. Unlike some other programming languages, Python is dynamically typed, which means you don't need to explicitly declare the type of a variable. The type is inferred based on the value assigned to it.

To create a variable in Python, you need to follow these rules:

1. Choose a name for the variable: The name should be descriptive and indicate the purpose of the variable.
2. Assign a value to the variable: Use the assignment operator (`=`) to assign a value to the variable.

Here are some examples of creating variables in Python:

```python
# Assigning an integer value to a variable
age = 25

# Assigning a string value to a variable
name = "John Doe"

# Assigning a floating-point value to a variable
pi = 3.14

# Assigning a boolean value to a variable
is_valid = True

# Assigning a list to a variable
numbers = [1, 2, 3, 4, 5]
```

Variables can be updated by assigning new values to them:

```python
age = 25  # Initial value
age = 30  # Updated value
```

Python variables are dynamically typed, which means you can assign a value of a different type to an existing variable:

```python
x = 5  # Integer
x = "Hello"  # String
```

Variables in Python are case-sensitive, meaning `myVar` and `myvar` are considered different variables. It's good practice to use lowercase letters and underscores (`snake_case`) for variable names.

Using variables allows you to store and manipulate data throughout your program, making it more flexible and adaptable to different scenarios.

# 3 Python Constants

In Python, constants are values that do not change during the execution of a program. They are typically used to represent fixed and unchanging values, such as mathematical constants or configuration settings. Although Python does not have built-in support for defining constants, it is a common convention to use uppercase letters and underscores to indicate that a variable should be treated as a constant.

Here's an example of defining constants in Python:

```python
PI = 3.14159
MAX_VALUE = 100
CONFIG_FILE_PATH = "/path/to/config.ini"
```

By convention, these variables are named using uppercase letters, which helps distinguish them from regular variables. However, it's important to note that Python does not enforce the immutability of these variables, so they can be reassigned a new value. The naming convention is mainly a convention followed by developers to indicate that the variable should not be modified.

Using constants in your code can enhance readability and maintainability, as it allows you to use meaningful names for fixed values rather than using hard-coded values directly in your code. It also makes it easier to update these values in a single place if they need to be changed in the future.

# 4 Python Literals

literals are the literal representations of values in the code. They are fixed values that are directly used within the program without any computation or evaluation. Python supports various types of literals, including:

1. Numeric Literals:
   - Integer literals: Whole numbers without a fractional part, such as `42`, `0`, or `-10`.
   - Floating-point literals: Numbers with a decimal point or exponent notation, such as `3.14`, `-2.5`, or `1e-5`.
   - Complex literals: Numbers with a real and imaginary part, such as `2+3j` or `-1+2j`.

2. String Literals:
   - Enclosed within single quotes (`'...'`) or double quotes (`"..."`), such as `'Hello'` or `"Python"`.

3. Boolean Literals:
   - Representing the truth values `True` and `False`.

4. None Literal:
   - Representing the absence of a value, using the keyword `None`.

5. List Literals:
   - Ordered collections of items enclosed within square brackets (`[...]`), such as `[1, 2, 3]` or `['apple', 'banana', 'cherry']`.

6. Tuple Literals:
   - Similar to lists but enclosed within parentheses (`(...)`), such as `(1, 2, 3)` or `('apple', 'banana', 'cherry')`.

7. Dictionary Literals:
   - Unordered collections of key-value pairs enclosed within curly braces (`{...}`), such as `{'name': 'John', 'age': 30}`.

8. Set Literals:
   - Unordered collections of unique elements enclosed within curly braces (`{...}`) or using the `set(...)` constructor, such as `{1, 2, 3}` or `set([1, 2, 3])`.

9. Boolean Literals:
   - Representing the truth values `True` and `False`.

These are some of the most common types of literals in Python. Literals provide a convenient way to represent constant values directly in the code, making it more readable and expressive.

-------------------
# 5 Python Data Types

Data types define the kind of values that can be stored and manipulated by variables. Python is a dynamically typed language, which means you don't need to declare the data type explicitly. The interpreter infers the type based on the value assigned to a variable. Here are some common data types in Python:

1. Numeric Types:
   - Integer (`int`): Whole numbers without a fractional part, such as `42` or `-10`.
   - Floating-Point (`float`): Numbers with a decimal point or exponent notation, such as `3.14` or `-2.5`.
   - Complex (`complex`): Numbers with both a real and imaginary part, such as `2+3j`.

2. Text Type:
   - String (`str`): Ordered sequences of characters, such as `'Hello'` or `"Python"`.

3. Sequence Types:
   - List (`list`): Ordered collections of items, which can be of different data types, enclosed within square brackets (`[...]`), such as `[1, 2, 3]` or `['apple', 'banana', 'cherry']`.
   - Tuple (`tuple`): Similar to lists but immutable, enclosed within parentheses (`(...)`), such as `(1, 2, 3)` or `('apple', 'banana', 'cherry')`.

4. Mapping Type:
   - Dictionary (`dict`): Unordered collections of key-value pairs enclosed within curly braces (`{...}`), such as `{'name': 'John', 'age': 30}`.

5. Set Types:
   - Set (`set`): Unordered collections of unique elements enclosed within curly braces (`{...}`), such as `{1, 2, 3}`.

6. Boolean Type:
   - Boolean (`bool`): Represents truth values, either `True` or `False`.

7. None Type:
   - None (`None`): Represents the absence of a value.

These are some of the built-in data types provided by Python. Additionally, Python allows you to define and work with custom data types using classes and objects. Understanding the data types is crucial for writing correct and efficient code, as it determines how the values are stored, manipulated, and interact with each other.


---------------
Here are some examples of using different data types in Python:

1. Numeric Types:

```python
# Integer
x = 42
y = -10

# Floating-Point
pi = 3.14
temperature = -2.5

# Complex
z = 2 + 3j
```

2. Text Type:

```python
message = 'Hello, World!'
name = "Alice"
```

3. Sequence Types:

```python
# List
numbers = [1, 2, 3, 4, 5]
fruits = ['apple', 'banana', 'cherry']

# Tuple
coordinates = (10, 20)
colors = ('red', 'green', 'blue')
```

4. Mapping Type:

```python
student = {
    'name': 'John',
    'age': 25,
    'grade': 'A'
}
```

5. Set Type:

```python
numbers = {1, 2, 3, 4, 5}
unique_letters = set('hello')
```

6. Boolean Type:

```python
is_valid = True
is_empty = False
```

7. None Type:

```python
result = None
```

These examples demonstrate the usage of different data types in Python. Remember that Python is dynamically typed, so you can assign values of different types to variables. The data type of a variable is determined by the value assigned to it.

-------------------

Question 1 : Create a student marksheet program output like this 


### Student MarkSheet
----
#### input Section 

1. Enter Student Name : Ravi
2. Enter Roll Number : RAVI009912
3. Enter Class : MCA
4. Enter JAVA Marks : 56
5. Enter C++ Marks : 89
6. Enter Python Marks : 12
7. Enter Ruby Marks : 56
8. Enter SQL Marks : 78

   #### total = ?
   #### Per % = ?






