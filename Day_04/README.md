# Operators

Python provides a wide range of operators that allow you to perform various operations on values and variables. Here are some of the most commonly used operators in Python:

1. Arithmetic Operators:
   - Addition: `+`
   - Subtraction: `-`
   - Multiplication: `*`
   - Division: `/`
   - Modulo (Remainder): `%`
   - Exponentiation: `**`
   - Floor Division: `//`
     
  


   ```python
   x = 10
   y = 3

   print(x + y)   # Output: 13
   print(x - y)   # Output: 7
   print(x * y)   # Output: 30
   print(x / y)   # Output: 3.3333333333333335
   print(x % y)   # Output: 1
   print(x ** y)  # Output: 1000
   print(x // y)  # Output: 3
   ```

2. Comparison Operators:
   - Equal to: `==`
   - Not equal to: `!=`
   - Greater than: `>`
   - Less than: `<`
   - Greater than or equal to: `>=`
   - Less than or equal to: `<=`


   ```python
   x = 5
   y = 3

   print(x == y)  # Output: False
   print(x != y)  # Output: True
   print(x > y)   # Output: True
   print(x < y)   # Output: False
   print(x >= y)  # Output: True
   print(x <= y)  # Output: False
   ```

3. Assignment Operators:
   - Assignment: `=`
   - Addition assignment: `+=`
   - Subtraction assignment: `-=`
   - Multiplication assignment: `*=`
   - Division assignment: `/=`
   - Modulo assignment: `%=`
   - Exponentiation assignment: `**=`
   - Floor division assignment: `//=`


   ```python
   x = 10

   x += 5  # Equivalent to x = x + 5
   print(x)  # Output: 15

   x **= 2  # Equivalent to x = x ** 2
   print(x)  # Output: 225
   ```

4. Logical Operators:
   - Logical AND: `and`
   - Logical OR: `or`
   - Logical NOT: `not`


   ```python
   x = 5
   y = 3
   z = 7

   print(x > y and x < z)  # Output: True
   print(x > y or x > z)   # Output: True
   print(not x > y)        # Output: False
   ```

5. Membership Operators:
   - `in`: Evaluates if a value is present in a sequence.
   - `not in`: Evaluates if a value is not present in a sequence.


   ```python
   fruits = ['apple', 'banana', 'orange']

   print('banana' in fruits)       # Output: True
   print('grape' not in fruits)    # Output: True
   ```

6. Identity Operators:
   - `is`: Evaluates if two variables refer to the same object.
   - `is not`: Evaluates if two variables do not refer to the same object.


   ```python
   x = [1, 2, 3]
   y = [1, 2, 3]
   z = x

   print(x is y)       # Output: False
   print(x is not y)   # Output: True
   print(x is z)       # Output: True
   ```

These are just a few examples of the operators available in Python. Operators allow you to perform various computations and comparisons, and they play a crucial role in writing expressive and efficient code.
