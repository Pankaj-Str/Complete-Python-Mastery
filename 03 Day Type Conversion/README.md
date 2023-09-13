# Python Type Conversion 

Type conversion refers to the process of converting one data type into another. Python provides built-in functions that allow you to perform type conversion.

Here are some commonly used type conversion functions in Python:

1. `int()`: Converts a value into an integer. For example:
   ```python
   num_str = "10"
   num_int = int(num_str)
   print(num_int)  # Output: 10
   ```

2. `float()`: Converts a value into a floating-point number. For example:
   ```python
   num_str = "3.14"
   num_float = float(num_str)
   print(num_float)  # Output: 3.14
   ```

3. `str()`: Converts a value into a string. For example:
   ```python
   num_int = 42
   num_str = str(num_int)
   print(num_str)  # Output: "42"
   ```

4. `list()`, `tuple()`, `set()`: Convert a value into a list, tuple, or set, respectively. For example:
   ```python
   num_str = "12345"
   num_list = list(num_str)
   num_tuple = tuple(num_str)
   num_set = set(num_str)
   print(num_list)  # Output: ['1', '2', '3', '4', '5']
   print(num_tuple)  # Output: ('1', '2', '3', '4', '5')
   print(num_set)  # Output: {'1', '2', '3', '4', '5'}
   ```

5. `bool()`: Converts a value into a boolean. For example:
   ```python
   num = 42
   bool_val = bool(num)
   print(bool_val)  # Output: True
   ```

These are just a few examples of type conversion functions available in Python. Depending on your needs, you may need to use additional functions or techniques to convert between specific data types.

-------------------------

# Python Basic Input and Output 

We can use the built-in functions `input()` and `print()` for basic input and output operations, respectively. Here's how you can use them:

1. Input:
   The `input()` function is used to receive input from the user. It takes an optional prompt as an argument and returns the user's input as a string.

   ```python
   name = input("Enter your name: ")
   print("Hello, " + name + "!")  # Output: Hello, <name>!
   ```

   In the example above, the user is prompted to enter their name. The input is stored in the `name` variable, and then it is printed along with a greeting.

2. Output:
   The `print()` function is used to display output on the console. It can accept one or more arguments and prints them to the console.

   ```python
   print("Hello, World!")  # Output: Hello, World!
   ```

   In the example above, the string "Hello, World!" is printed to the console.

   You can also print variables and combine them with strings using the string concatenation (`+`) operator or formatted string literals (f-strings):

   ```python
   name = "Alice"
   age = 25
   print("Name: " + name + ", Age: " + str(age))  # Output: Name: Alice, Age: 25

   print(f"Name: {name}, Age: {age}")  # Output: Name: Alice, Age: 25
   ```

   In the first example, the variables `name` and `age` are concatenated with the strings using the `+` operator. In the second example, the variables are directly inserted into the string using curly braces (`{}`) inside an f-string.

Remember that `input()` returns the user's input as a string, so if you want to work with other data types, you'll need to perform type conversion as necessary.

These are the basic input and output operations in Python. You can use them to interact with users and display information on the console.
