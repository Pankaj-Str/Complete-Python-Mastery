# Type Conversion in Python

#### **Type Conversion in Python**

Type conversion in Python refers to the process of converting one data type to another. Python provides two types of type conversion:

1. **Implicit Type Conversion** (also known as **type coercion**)
2. **Explicit Type Conversion** (also known as **type casting**)

Let’s explore both with examples.

***

### **1. Implicit Type Conversion (Type Coercion)**

Python automatically converts one data type to another when required, without needing the programmer to specify the conversion. This typically happens when you perform operations involving different data types.

#### **Example:**

```python
# Implicit Type Conversion Example
a = 10         # Integer
b = 5.5        # Float

# Python automatically converts the integer to float
result = a + b
print(result)  # Output: 15.5
print(type(result))  # Output: <class 'float'>
```

In the above example, the integer `a` is automatically converted to a float when added to the float `b`, resulting in a float output.

***

### **2. Explicit Type Conversion (Type Casting)**

Explicit type conversion occurs when you manually convert one data type to another using Python’s built-in functions like `int()`, `float()`, `str()`, etc.

#### **Common Type Conversion Functions:**

* **`int()`**: Converts a value to an integer.
* **`float()`**: Converts a value to a float.
* **`str()`**: Converts a value to a string.
* **`bool()`**: Converts a value to a boolean (True or False).

***

#### **Example 1: Converting String to Integer**

```python
# Converting string to integer
num_str = "25"
num_int = int(num_str)  # Converts the string to an integer
print(num_int)  # Output: 25
print(type(num_int))  # Output: <class 'int'>
```

In this example, the string `"25"` is converted to the integer `25`.

***

#### **Example 2: Converting Integer to Float**

```python
# Converting integer to float
num_int = 10
num_float = float(num_int)  # Converts the integer to a float
print(num_float)  # Output: 10.0
print(type(num_float))  # Output: <class 'float'>
```

Here, the integer `10` is explicitly converted to a float `10.0`.

***

#### **Example 3: Converting Float to Integer**

```python
# Converting float to integer
num_float = 10.75
num_int = int(num_float)  # Converts the float to an integer
print(num_int)  # Output: 10
print(type(num_int))  # Output: <class 'int'>
```

In this case, the float `10.75` is converted to the integer `10`. Note that the decimal part is truncated (not rounded).

***

#### **Example 4: Converting Integer to String**

```python
# Converting integer to string
num_int = 50
num_str = str(num_int)  # Converts the integer to a string
print(num_str)  # Output: "50"
print(type(num_str))  # Output: <class 'str'>
```

Here, the integer `50` is converted to the string `"50"`.

***

#### **Example 5: Converting String to Float**

```python
# Converting string to float
num_str = "20.5"
num_float = float(num_str)  # Converts the string to a float
print(num_float)  # Output: 20.5
print(type(num_float))  # Output: <class 'float'>
```

The string `"20.5"` is converted to the float `20.5`.

***

#### **Example 6: Boolean Conversion**

```python
# Converting other data types to boolean
num = 0
str_val = ""
list_val = []

# False values
print(bool(num))  # Output: False
print(bool(str_val))  # Output: False
print(bool(list_val))  # Output: False

# Non-zero values
num = 10
str_val = "Hello"
list_val = [1, 2, 3]

print(bool(num))  # Output: True
print(bool(str_val))  # Output: True
print(bool(list_val))  # Output: True
```

In Python, the following values are considered **False** when converted to boolean:

* `0` (integer)
* `0.0` (float)
* `""` (empty string)
* `[]` (empty list)
* `None`

All other values are considered **True**.

***

### **Conclusion**

Type conversion is an essential concept in Python. Understanding when and how to convert between data types helps you avoid errors and allows you to manipulate data effectively.

* **Implicit Type Conversion** happens automatically by Python when necessary.
* **Explicit Type Conversion** requires you to use built-in functions to convert data types manually.

Keep practicing these conversions to build a strong foundation for your Python programs. Happy Coding at **codeswithpankaj.com**! 🚀
