
# Assignment

| **Assignment**                               | **Task**                                                                                                                                                                                                                                      |
|---------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **1. Basic Arithmetic Operations**           | Write a Python script that declares two variables, num1 and num2, assigns them with integer values, and then performs basic arithmetic operations such as addition, subtraction, multiplication, and division using these variables. |
| **2. Temperature Converter**                | Create a Python program that prompts the user to enter a temperature in Celsius, stores it in a variable, and then converts it to Fahrenheit using the formula `(Celsius * 9/5) + 32`. Display the result.                                 |
| **3. String Concatenation**                 | Write a Python script that declares two string variables and concatenates them together. Prompt the user to enter their first name and last name separately, then concatenate them and print out the full name.                        |
| **4. BMI Calculator**                       | Develop a Python program that calculates Body Mass Index (BMI). Prompt the user to enter their weight in kilograms and height in meters. Calculate BMI using the formula `BMI = weight / (height * height)`. Print out the BMI.          |
| **5. Area of a Triangle**                   | Write a Python program that calculates the area of a triangle. Prompt the user to enter the base and height of the triangle. Use the formula `Area = (base * height) / 2` and display the result.                                          |
| **6. Age Calculator**                       | Create a Python script that prompts the user to enter their birth year and stores it in a variable. Calculate the user's age based on the current year and print out the result.                                                                |
| **7. Even or Odd**                          | Write a Python program that prompts the user to enter an integer and checks whether it's even or odd. Print out the result.                                                                                                                 |
| **8. Grade Calculator**                     | Develop a Python script that takes in the scores of three tests (out of 100) and stores them in variables. Calculate the average score and print it out. Then, based on the average score, assign a letter grade (A, B, C, D, or F) and print it out.                                                   |
| **9. Simple Interest Calculator**           | Create a Python program that calculates simple interest. Prompt the user to enter principal amount, rate of interest, and time (in years). Calculate simple interest using the formula `Simple Interest = (principal * rate * time) / 100` and display the result.                                               |
| **10. Quadratic Equation Solver**          | Write a Python script that solves a quadratic equation. Prompt the user to enter the coefficients a, b, and c of the quadratic equation ax^2 + bx + c = 0. Calculate the roots of the equation using the quadratic formula and print out the results. Make sure to handle cases where the discriminant is negative. |


# Question and Answers

1. **Purpose of declaring variables in Python:**
   Variables in Python are used to store data values for later use in the program. They provide a way to label and manipulate data in a meaningful way, making code more readable and easier to understand. Declaring variables allows programmers to assign values, perform operations, and manipulate data within the program.

2. **How to declare a variable in Python:**
   In Python, you declare a variable by simply assigning a value to it using the assignment operator (`=`). For example:
   ```python
   my_variable = 10
   ```

3. **Changing the value of a variable:**
   Yes, you can change the value of a variable after it has been declared by assigning a new value to it. For example:
   ```python
   my_variable = 10
   my_variable = 20  # Changing the value of my_variable
   ```

4. **Naming conventions for variables in Python:**
   - Variable names should be descriptive and indicative of their purpose.
   - They can contain letters (both lowercase and uppercase), digits, and underscores (_), but cannot start with a digit.
   - Variable names are case-sensitive.
   - It's recommended to use lowercase letters for variable names, with underscores to separate words for readability (e.g., `my_variable`).

5. **Difference between local and global variables in Python:**
   - **Local variables:** Local variables are defined within a function and are only accessible within that function's scope.
   - **Global variables:** Global variables are defined outside of any function and can be accessed and modified throughout the entire program.
   ```python
   global_variable = 10  # Global variable

   def my_function():
       local_variable = 20  # Local variable
       print(global_variable)  # Accessing global variable

   my_function()
   ```

6. **Deleting a variable in Python:**
   You can delete a variable using the `del` statement followed by the variable name. For example:
   ```python
   my_variable = 10
   del my_variable
   ```

7. **Variable scope in Python:**
   Variable scope refers to the area of the program where a variable is accessible. In Python, variables have either local or global scope. Local variables are accessible only within the function where they are defined, while global variables are accessible throughout the entire program.

8. **Role of data types in Python variables:**
   Data types define the type of data that a variable can store and the operations that can be performed on it. Python is dynamically typed, meaning you don't need to explicitly declare the data type of a variable. Data types in Python include integers, floats, strings, lists, tuples, dictionaries, etc.

9. **Checking the type of a variable in Python:**
   You can check the type of a variable using the `type()` function. For example:
   ```python
   my_variable = 10
   print(type(my_variable))  # Output: <class 'int'>
   ```

10. **Dynamic typing in Python and its impact on variables:**
    Dynamic typing in Python means that you don't need to explicitly declare the data type of a variable. Variables can dynamically change their type based on the assigned value. This provides flexibility but requires careful attention to variable types to avoid unexpected behaviors or errors during runtime.
