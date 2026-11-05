## Topic
```
1. Python File Operation
2. Python Directory
3. Python Exception
4. Python Exception Handling
5. Python User-defined Exception
```
# File operations

File operations in Python involve reading from and writing to files. 
Python provides built-in functions and methods to handle file-related operations. Here's a brief overview of some common file operations:

**1. Opening a File:**
You can use the built-in `open()` function to open a file. It takes two arguments: the file path and the mode (read, write, append, etc.).

```python
# Opening a file in read mode
file = open("example.txt", "r")

# Opening a file in write mode
file = open("output.txt", "w")

# Opening a file in append mode
file = open("log.txt", "a")
```

**2. Reading from a File:**
Once a file is opened in read mode, you can use various methods to read its contents.

- `read()`: Reads the entire content of the file as a string.
- `readline()`: Reads a single line from the file.
- `readlines()`: Reads all lines and returns a list of lines.

```python
# Reading the entire content of a file
content = file.read()

# Reading a single line from a file
line = file.readline()

# Reading all lines from a file
lines = file.readlines()
```

**3. Writing to a File:**
When a file is opened in write mode, you can use the `write()` method to write content to the file.

```python
file.write("Hello, world!\n")
file.write("This is a new line.")
```

**4. Appending to a File:**
In append mode, you can use the `write()` method to add content to the end of the file without overwriting the existing content.

```python
file.write("Appending this line.")
```

**5. Closing a File:**
It's important to close the file after you're done using it to free up system resources.

```python
file.close()
```

**6. Using `with` Statement (Context Managers):**
A better way to work with files is using the `with` statement, which ensures that the file is properly closed when you're done with it.

```python
with open("example.txt", "r") as file:
    content = file.read()
    # Do something with the content

# File is automatically closed when the block is exited
```

**7. File Modes:**
There are various modes you can use when opening a file:
- `"r"`: Read (default mode).
- `"w"`: Write (creates a new file or overwrites an existing file).
- `"a"`: Append (creates a new file or appends to an existing file).
- `"b"`: Binary mode (for non-text files like images, videos, etc.).
- `"x"`: Exclusive creation (fails if the file already exists).
- `"t"`: Text mode (default mode, for text files).


## Examples of reading from and writing to a file using Python


**Reading from a File:**

Let's say you have a file named "example.txt" with the following content:

```
Hello, this is an example file.
It contains multiple lines.
We will read it using Python.
```

You can read the content of this file using the following code:

```python
# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```

Output:
```
Hello, this is an example file.
It contains multiple lines.
We will read it using Python.
```

**Writing to a File:**

Let's say you want to write some content to a file named "output.txt":

```python
# Writing to a file
with open("output.txt", "w") as file:
    file.write("This is the first line.\n")
    file.write("This is the second line.")
```

After running this code, a file named "output.txt" will be created with the following content:

```
This is the first line.
This is the second line.
```

**Appending to a File:**

If you want to add more content to the file without overwriting the existing content, you can use append mode:

```python
# Appending to a file
with open("output.txt", "a") as file:
    file.write("\nThis is an appended line.")
```

After running this code, the "output.txt" file will look like this:

```
This is the first line.
This is the second line.
This is an appended line.
```
---- 
# **1. Python Directory:**

In Python, a directory (also known as a folder) is a way to organize and store files. Python provides a module called `os` (Operating System Interface) that allows you to work with directories and perform various operations on them. Here are some common tasks related to directories using the `os` module:

**1. Creating a Directory:**
You can create a new directory using the `os.mkdir()` function.

```python
import os

# Creating a directory
os.mkdir("my_directory")
```

**2. Checking if a Directory Exists:**
You can check if a directory exists using the `os.path.exists()` function.

```python
import os

if os.path.exists("my_directory"):
    print("Directory exists")
else:
    print("Directory does not exist")
```

**3. Listing Contents of a Directory:**
To list the contents of a directory, you can use the `os.listdir()` function.

```python
import os

contents = os.listdir("my_directory")
print("Directory contents:", contents)
```

**4. Renaming a Directory:**
You can rename a directory using the `os.rename()` function.

```python
import os

os.rename("my_directory", "new_directory")
```

**5. Deleting a Directory:**
To delete an empty directory, you can use the `os.rmdir()` function.

```python
import os

os.rmdir("new_directory")
```

**6. Recursive Directory Deletion:**
If you want to delete a directory and all its contents (including subdirectories), you can use the `shutil.rmtree()` function from the `shutil` module.

```python
import shutil

shutil.rmtree("my_directory")
```
Certainly! Here are some commonly used methods from the `os` module to work with directories in Python, along with examples for each method:

**1. `os.mkdir(path)` - Creating a Directory:**

This method creates a new directory at the specified path.

```python
import os

# Create a new directory named "my_folder"
os.mkdir("my_folder")
```

**2. `os.path.exists(path)` - Checking if a Directory Exists:**

This method checks if the directory at the specified path exists.

```python
import os

if os.path.exists("my_folder"):
    print("Directory exists")
else:
    print("Directory does not exist")
```

**3. `os.listdir(path)` - Listing Contents of a Directory:**

This method returns a list of all items (files and directories) within the specified directory.

```python
import os

contents = os.listdir("my_folder")
print("Directory contents:", contents)
```

**4. `os.rename(old_path, new_path)` - Renaming a Directory:**

This method renames a directory from `old_path` to `new_path`.

```python
import os

os.rename("my_folder", "new_folder")
```

**5. `os.rmdir(path)` - Deleting an Empty Directory:**

This method removes an empty directory at the specified path.

```python
import os

os.rmdir("new_folder")
```

**6. `shutil.rmtree(path)` - Recursive Directory Deletion:**

This method deletes a directory and its contents (including subdirectories).

```python
import shutil

shutil.rmtree("my_folder")
```

**7. `os.getcwd()` - Getting the Current Working Directory:**

This method returns the current working directory.

```python
import os

current_dir = os.getcwd()
print("Current working directory:", current_dir)
```

# **2. Python Exception:**

Exceptions in Python are events that occur during the execution of a program and disrupt the normal flow of instructions. When an exception occurs, the program terminates unless the exception is caught and handled using exception handling mechanisms.

**3. Python Exception Handling:**

Exception handling is the process of dealing with exceptions that occur during the execution of a program. It prevents the program from crashing and allows you to handle errors gracefully. The `try` and `except` blocks are used for exception handling.

```python
try:
    # Code that might raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Handling a specific exception
    print("Division by zero error")
except Exception as e:
    # Handling other exceptions
    print("An error occurred:", e)
else:
    # Executed if no exception occurs
    print("No exceptions")
finally:
    # Always executed, regardless of whether an exception occurred
    print("Cleaning up")
```

**4. Python User-defined Exception:**

Exception handling in Python is a crucial concept that allows you to gracefully handle errors that might occur during the execution of your code. It helps prevent your program from crashing and allows you to provide alternative actions or error messages when things go wrong.

The main components of exception handling in Python are the `try`, `except`, `else`, and `finally` blocks.

**1. `try` and `except` Blocks:**
The `try` block is used to enclose the code that might raise an exception. If an exception occurs within the `try` block, it is caught and handled in the corresponding `except` block.

```python
try:
    # Code that might raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Handling the specific exception
    print("Cannot divide by zero")
except Exception as e:
    # Handling other exceptions
    print("An error occurred:", e)
```

In this example, a `ZeroDivisionError` occurs because of dividing by zero. It is caught and handled in the `except` block.

**2. `else` Block:**
The `else` block is executed only if no exceptions occur within the `try` block. It's often used for code that should run when no exceptions are raised.

```python
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input: not a number")
else:
    print("Entered number:", num)
```


**3. `finally` Block:**

The `finally` block is used to define cleanup code that should be executed regardless of whether an exception occurred or not. It's commonly used to release resources or perform clean-up tasks.

```python
try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found")
else:
    print("Content:", content)
finally:
    file.close()  # Ensure the file is closed no matter what
```

Here, the `finally` block ensures that the opened file is closed, even if an exception occurs.

**4. Multiple `except` Blocks:**
You can have multiple `except` blocks to handle different types of exceptions.

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
except ArithmeticError:
    print("Arithmetic error occurred")
except Exception as e:
    print("An error occurred:", e)
```



