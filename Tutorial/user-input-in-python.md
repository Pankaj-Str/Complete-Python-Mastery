# User Input in Python

User input in Python refers to the process of accepting data from the user during program execution. This allows the program to interact with the user dynamically. Python provides the `input()` function to take input from the user. Let's dive into the details of how to handle user input in Python.

***

### **1. Using the `input()` Function**

The `input()` function is used to take input from the user. By default, the input taken from the user is always treated as a string, even if the user enters numbers.

#### **Syntax:**

```python
input(prompt)
```

* **prompt**: A string that is displayed to the user as a prompt before accepting the input. It is optional but highly recommended to provide a prompt to guide the user.

#### **Example 1: Basic User Input**

```python
name = input("Enter your name: ")
print(f"Hello, {name}!")
```

**Output:**

```
Enter your name: Pankaj
Hello, Pankaj!
```

In this example:

* The program asks the user to enter their name.
* The input is stored in the variable `name`.
* The program then prints a greeting message with the entered name.

***

### **2. Input as String**

By default, the `input()` function always returns the data as a **string**. If the user enters numbers, they will still be returned as a string.

#### **Example 2: Input as String**

```python
age = input("Enter your age: ")
print(f"Your age is {age}")
```

**Output:**

```
Enter your age: 25
Your age is 25
```

In this example, even though the user enters a number, it is stored as a string. To perform mathematical operations on the input, we need to convert it to the appropriate type.

***

### **3. Converting Input to Other Data Types**

Since the input from the `input()` function is always a string, we may need to convert it to other data types such as integers or floating-point numbers to perform calculations or other operations.

#### **1. Converting Input to Integer (`int()`)**

To convert the user input to an integer, use the `int()` function.

#### **Example 3: Converting Input to Integer**

```python
age = input("Enter your age: ")
age = int(age)  # Convert string input to integer
print(f"Next year, you will be {age + 1} years old.")
```

**Output:**

```
Enter your age: 25
Next year, you will be 26 years old.
```

In this example, the user enters their age as a string, which is then converted to an integer using `int()`. The program calculates the next age and prints the result.

#### **2. Converting Input to Float (`float()`)**

To convert the user input to a floating-point number, use the `float()` function.

#### **Example 4: Converting Input to Float**

```python
price = input("Enter the price of the item: ")
price = float(price)  # Convert string input to float
print(f"The price of the item after tax is {price * 1.05}")
```

**Output:**

```
Enter the price of the item: 100.50
The price of the item after tax is 105.525
```

Here, the user enters the price of an item as a string, which is converted to a float using `float()`. The program calculates the price after adding a 5% tax.

***

### **4. Handling Invalid Input**

If the user enters something that cannot be converted to the desired data type (for example, entering a non-numeric value when you expect an integer), it will result in a **ValueError**. To handle this, you can use **exception handling** with `try` and `except`.

#### **Example 5: Handling Invalid Input with `try-except`**

```python
try:
    age = input("Enter your age: ")
    age = int(age)  # Attempt to convert to integer
    print(f"Your age next year will be {age + 1}")
except ValueError:
    print("Invalid input! Please enter a valid number.")
```

**Output (Valid Input):**

```
Enter your age: 25
Your age next year will be 26
```

**Output (Invalid Input):**

```
Enter your age: twenty-five
Invalid input! Please enter a valid number.
```

In this example:

* The program tries to convert the user input to an integer.
* If the conversion fails (for example, if the user enters text like "twenty-five"), a `ValueError` is raised.
* The program catches the error and prints an error message asking for valid input.

***

### **5. Input with Default Values**

Sometimes, you might want to provide a default value if the user does not enter anything. You can do this by checking if the input is empty and assigning a default value.

#### **Example 6: Input with Default Value**

```python
name = input("Enter your name (press Enter to skip): ")
if not name:  # If the input is empty
    name = "Guest"
print(f"Hello, {name}!")
```

**Output (With Input):**

```
Enter your name (press Enter to skip): Pankaj
Hello, Pankaj!
```

**Output (Without Input):**

```
Enter your name (press Enter to skip): 
Hello, Guest!
```

Here, if the user presses Enter without typing anything, the `name` variable is assigned the default value "Guest".

***

### **6. Multiple Inputs on One Line**

If you want to accept multiple inputs from the user on the same line, you can use the `split()` method to split the input string into a list.

#### **Example 7: Multiple Inputs on One Line**

```python
x, y = input("Enter two numbers separated by space: ").split()
x = int(x)
y = int(y)
print(f"The sum of {x} and {y} is {x + y}")
```

**Output:**

```
Enter two numbers separated by space: 10 20
The sum of 10 and 20 is 30
```

In this example:

* The user is prompted to enter two numbers separated by a space.
* The `split()` method splits the input into two parts, and each part is converted to an integer.
* The program calculates and prints the sum of the two numbers.

***

### **Conclusion**

Handling user input is a crucial part of making interactive Python programs. The key steps are:

* Use the `input()` function to take input.
* Convert input to the required data type using functions like `int()`, `float()`, etc.
* Handle invalid input using `try-except` blocks.
* Optionally, provide default values or accept multiple inputs on the same line.

Mastering user input will allow you to create dynamic and responsive programs. Happy coding at **codeswithpankaj.com**! 🚀
