# Exception handling in Python

Exception handling in Python is a crucial aspect of writing robust and reliable code. It allows you to gracefully handle errors, exceptions, and unexpected conditions that may occur during program execution. Let's explore the key concepts related to exception handling in Python:

1. **What is an Exception?**

   An exception is an event that occurs during the execution of a program and disrupts the normal flow of the program's instructions. Exceptions can occur for various reasons, such as division by zero, invalid input, or attempting to access a non-existent file. In Python, exceptions are raised using the `raise` keyword and can be caught and handled using `try` and `except` blocks.

2. **Handle Errors with Try and Except:**

   The `try` and `except` blocks are used to catch and handle exceptions in Python. The code within the `try` block is executed, and if an exception occurs, the corresponding `except` block is executed to handle the exception gracefully.

   Example:

   ```python
   try:
       # Code that may raise an exception
       x = 10 / 0
   except ZeroDivisionError:
       # Handle the ZeroDivisionError exception
       print("Division by zero is not allowed.")
   ```

3. **Multiple Tries and Excepts:**

   You can have multiple `try` and `except` blocks to handle different types of exceptions independently. This allows you to provide specific error-handling logic for various exceptions.

   Example:

   ```python
   try:
       x = int(input("Enter a number: "))
       result = 10 / x
   except ZeroDivisionError:
       print("Division by zero is not allowed.")
   except ValueError:
       print("Invalid input. Please enter a valid number.")
   ```

4. **User-Defined Exception:**

   You can create your own custom exceptions in Python by defining new exception classes. These custom exceptions can be raised and caught like built-in exceptions.

   Example of defining and raising a custom exception:

   ```python
   class CustomError(Exception):
       pass

   def validate_age(age):
       if age < 0:
           raise CustomError("Age cannot be negative.")

   try:
       user_age = int(input("Enter your age: "))
       validate_age(user_age)
       print(f"Your age is {user_age}.")
   except CustomError as ce:
       print(f"Custom Error: {ce}")
   ```

   In this example, we define a custom exception class `CustomError` and raise it in the `validate_age` function when an invalid age is detected.

Exception handling is essential for writing robust and reliable code in Python. It helps you gracefully handle errors, provide informative error messages, and ensure that your program can recover or terminate gracefully when exceptions occur.