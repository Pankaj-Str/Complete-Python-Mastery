# Data Types and Other Basic Elements in Python

Welcome to **codeswithpankaj.com** ! In this tutorial, we will explore Python's data types, how to classify data, and other fundamental elements of a Python program. By the end, you'll have a solid understanding of Python's building blocks.

***

### **Part 1: Comments in Python**

#### What Are Comments?

Comments are used to explain code and make it easier to read. Python ignores comments during execution.

#### Types of Comments:

1.  **Single-line Comments**\
    Use the `#` symbol to write single-line comments.

    ```python
    # This is a single-line comment
    print("Hello, CodesWithPankaj!")  # This prints a message
    ```
2.  **Multi-line Comments**\
    Use triple quotes (`'''` or `"""`) for multi-line comments.

    ```python
    """
    This is a multi-line comment.
    It can span multiple lines.
    """
    print("Welcome to codeswithpankaj.com!")
    ```

***

### **Part 2: Values and Data Types**

#### What Are Data Types?

Data types define the kind of data a variable can hold. Python supports several built-in data types.

***

#### **1. Numeric Data Types**

**Integer (`int`)**

*   Whole numbers (positive or negative).

    ```python
    age = 25
    print(type(age))  # Output: <class 'int'>
    ```

**Floating-point (`float`)**

*   Numbers with decimals.

    ```python
    price = 19.99
    print(type(price))  # Output: <class 'float'>
    ```

**Complex Numbers (`complex`)**

*   Numbers with real and imaginary parts.

    ```python
    num = 3 + 4j
    print(type(num))  # Output: <class 'complex'>
    ```

***

#### **2. Boolean Data Type**

*   Represents `True` or `False`.

    ```python
    is_valid = True
    print(type(is_valid))  # Output: <class 'bool'>
    ```

***

#### **3. Compound Data Types**

**List**

*   Ordered and mutable collection.

    ```python
    fruits = ["apple", "banana", "cherry"]
    print(type(fruits))  # Output: <class 'list'>
    ```

**Tuple**

*   Ordered and immutable collection.

    ```python
    coordinates = (10, 20)
    print(type(coordinates))  # Output: <class 'tuple'>
    ```

**String**

*   Sequence of characters.

    ```python
    name = "Pankaj"
    print(type(name))  # Output: <class 'str'>
    ```

***

#### **4. Dictionary Data Type**

*   Stores data in key-value pairs.

    ```python
    user = {"name": "Pankaj", "age": 30}
    print(type(user))  # Output: <class 'dict'>
    ```

***

#### **5. Set Data Type**

*   Unordered collection of unique elements.

    ```python
    numbers = {1, 2, 3, 3, 4}
    print(numbers)  # Output: {1, 2, 3, 4}
    print(type(numbers))  # Output: <class 'set'>
    ```

***

### **Part 3: Other Basic Elements of Python Program**

#### **1. Identifiers**

* Names used to identify variables, functions, or other elements.
*   Rules for identifiers:

    * Must start with a letter or underscore.
    * Can contain letters, digits, and underscores.
    * Case-sensitive.

    ```python
    _name = "CodesWithPankaj"
    user1 = "John"
    ```

***

#### **2. Keywords**

* Reserved words in Python with predefined meanings.
*   Examples: `if`, `else`, `for`, `while`, `True`, `False`, etc.

    ```python
    # Correct usage of a keyword
    if True:
        print("This is a keyword example")
    ```

***

### List of Python Keywords

Python has a specific set of keywords that are reserved and have predefined meanings. They should not be used as variable names. Here's a basic list of Python keywords:

* `False`
* `None`
* `True`
* `and`
* `as`
* `assert`
* `async`
* `await`
* `break`
* `class`
* `continue`
* `def`
* `del`
* `elif`
* `else`
* `except`
* `finally`
* `for`
* `from`
* `global`
* `if`
* `import`
* `in`
* `is`
* `lambda`
* `nonlocal`
* `not`
* `or`
* `pass`
* `raise`
* `return`
* `try`
* `while`
* `with`
* `yield`

To obtain the most up-to-date list of Python keywords, you can use the `keyword` module:

```python
import keyword
print(keyword.kwlist)
```

#### **3. Variables**

* Containers for storing data values.
* Python is dynamically typed, so you don’t need to declare the type explicitly.

**Variable Declaration**

```python
name = "Pankaj"
age = 30
is_active = True
```

**Multiple Assignments**

```python
x, y, z = 10, 20, 30
```

**Reassigning Variables**

```python
x = 100  # x now holds a new value
```

**Type Checking**

Use the `type()` function to check the type of a variable.

```python
print(type(name))  # Output: <class 'str'>
print(type(age))   # Output: <class 'int'>
```

***

### **Examples Summary**

| **Concept**          | **Example Code**                        | **Output**              |
| -------------------- | --------------------------------------- | ----------------------- |
| Integer Data Type    | `x = 5; print(type(x))`                 | `<class 'int'>`         |
| List Data Type       | `lst = [1, 2, 3]; print(type(lst))`     | `<class 'list'>`        |
| Boolean Data Type    | `flag = True; print(type(flag))`        | `<class 'bool'>`        |
| Dictionary Data Type | `d = {"key": "value"}; print(type(d))`  | `<class 'dict'>`        |
| Variable Declaration | `name = "Pankaj"; print(name)`          | `Pankaj`                |
| Checking Keywords    | `import keyword; print(keyword.kwlist)` | List of Python keywords |

***

### **Conclusion**

Python's data types and basic elements form the foundation for programming. Understanding these concepts is essential for building complex programs. Keep practicing, and stay tuned to **codeswithpankaj.com** for more tutorials!

Happy Coding! 🚀
