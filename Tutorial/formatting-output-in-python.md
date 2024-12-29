# Formatting Output in Python

#### **Formatting Output in Python**

In Python, formatting output allows you to present data in a readable and structured way. There are several methods for formatting output in Python, which can be useful for making your program’s output more user-friendly. Let’s explore the most common methods.

***

### **1. Using f-strings (Formatted String Literals)**

Introduced in Python 3.6, f-strings are the most modern and efficient way to format strings. You can embed expressions inside string literals using curly braces `{}` and prefix the string with `f`.

#### **Syntax:**

```python
f"string {expression}"
```

#### **Example:**

```python
name = "Pankaj"
age = 25
print(f"My name is {name}, and I am {age} years old.")
```

**Output:**

```
My name is Pankaj, and I am 25 years old.
```

#### **Advantages of f-strings:**

* More readable and concise.
* Allows expressions inside the curly braces, such as calculations or function calls.

**Example with expressions:**

```python
x = 10
y = 5
print(f"The sum of {x} and {y} is {x + y}.")
```

**Output:**

```
The sum of 10 and 5 is 15.
```

***

### **2. Using `str.format()` Method**

The `str.format()` method allows you to format strings by inserting placeholders in the string and passing values to these placeholders.

#### **Syntax:**

```python
"string {} {}".format(value1, value2)
```

#### **Example:**

```python
name = "Pankaj"
age = 25
print("My name is {}, and I am {} years old.".format(name, age))
```

**Output:**

```
My name is Pankaj, and I am 25 years old.
```

#### **Using Indexes and Named Placeholders:**

You can also specify the position of the arguments using indexes or name them.

**Example with indexes:**

```python
print("My name is {0}, and I am {1} years old. {0} is learning Python.".format(name, age))
```

**Output:**

```
My name is Pankaj, and I am 25 years old. Pankaj is learning Python.
```

**Example with named placeholders:**

```python
print("My name is {name}, and I am {age} years old.".format(name="Pankaj", age=25))
```

**Output:**

```
My name is Pankaj, and I am 25 years old.
```

***

### **3. Using `%` Formatting (Old Style)**

This method is an older way to format strings in Python. It is similar to the `printf()` function in C. Although it is still widely used, it is generally recommended to use f-strings or `str.format()` for better readability.

#### **Syntax:**

```python
"string % (value1, value2)"
```

#### **Example:**

```python
name = "Pankaj"
age = 25
print("My name is %s, and I am %d years old." % (name, age))
```

**Output:**

```
My name is Pankaj, and I am 25 years old.
```

#### **Common Format Specifiers:**

* `%s` for strings.
* `%d` for integers.
* `%f` for floating-point numbers.

**Example with floating-point number:**

```python
pi = 3.14159
print("The value of pi is approximately %.2f." % pi)
```

**Output:**

```
The value of pi is approximately 3.14.
```

***

### **4. Controlling Width and Alignment**

You can control the width and alignment of the output using formatting techniques.

#### **1. Right-aligning text**

Use `>` to right-align text in a field of a given width.

**Example:**

```python
name = "Pankaj"
print(f"{name:>10}")  # Right-align with a width of 10
```

**Output:**

```
    Pankaj
```

#### **2. Left-aligning text**

Use `<` to left-align text in a field of a given width.

**Example:**

```python
name = "Pankaj"
print(f"{name:<10}")  # Left-align with a width of 10
```

**Output:**

```
Pankaj    
```

#### **3. Center-aligning text**

Use `^` to center-align text in a field of a given width.

**Example:**

```python
name = "Pankaj"
print(f"{name:^10}")  # Center-align with a width of 10
```

**Output:**

```
  Pankaj  
```

***

### **5. Formatting Numbers**

You can format numbers in Python to control decimal places, add commas for thousands, or represent them in scientific notation.

#### **1. Controlling Decimal Places**

Use `:.nf` to control the number of decimal places, where `n` is the number of decimal places you want.

**Example:**

```python
pi = 3.141592653589793
print(f"Value of pi to 3 decimal places: {pi:.3f}")
```

**Output:**

```
Value of pi to 3 decimal places: 3.142
```

#### **2. Adding Commas for Thousands**

Use `:,` to format numbers with commas as thousands separators.

**Example:**

```python
number = 1000000
print(f"Number with commas: {number:,}")
```

**Output:**

```
Number with commas: 1,000,000
```

***

### **6. Combining Multiple Formatting Techniques**

You can combine different formatting techniques in a single string.

#### **Example:**

```python
name = "Pankaj"
age = 25
pi = 3.14159
print(f"Name: {name:<10} Age: {age:>5} Pi: {pi:.2f}")
```

**Output:**

```
Name: Pankaj     Age:    25 Pi: 3.14
```

***

### **Conclusion**

Python offers several ways to format output, from the modern f-strings to the older `%` formatting. The most commonly recommended and efficient approach is using **f-strings**, as they are easier to read and allow for complex expressions. However, depending on your needs, you can also use `str.format()` or `%` formatting.

Here’s a quick summary:

* **f-strings** (recommended): `f"Hello, {name}"`
* **`str.format()`**: `"Hello, {}".format(name)`
* **Old style (`%`)**: `"Hello, %s" % name`

Happy Coding at **codeswithpankaj.com**! 🚀
