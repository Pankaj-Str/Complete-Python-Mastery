# Python Files and Directories

## Python Files and Directories Tutorial

Welcome to this comprehensive tutorial on Python files and directories, brought to you by codeswithpankaj.com. In this tutorial, we will explore various aspects of file handling and directory management in Python, covering their definition, usage, and practical examples. By the end of this tutorial, you will have a thorough understanding of how to work with files and directories effectively in your Python programs.

### Table of Contents

1. Introduction to File Handling
2. Opening and Closing Files
3. Reading and Writing Files
   * Reading Files
   * Writing Files
   * Appending to Files
4. Working with File Paths
5. File Methods
6. Introduction to Directories
7. Creating and Removing Directories
8. Listing Directory Contents
9. Practical Examples
10. Common Pitfalls and Best Practices

***

### 1. Introduction to File Handling

File handling is an essential part of programming, allowing you to store and retrieve data from files. Python provides a simple and efficient way to handle files using built-in functions and methods.

#### Why File Handling is Important

File handling is crucial for:

* Storing data persistently
* Reading and writing data to files
* Managing and organizing data
* Interacting with external data sources

***

### 2. Opening and Closing Files

Files can be opened using the `open()` function, which returns a file object. It is important to close files after performing operations to free up system resources.

#### Syntax

```python
file = open("filename", "mode")
file.close()
```

#### Modes for Opening Files

* `'r'`: Read mode (default)
* `'w'`: Write mode
* `'a'`: Append mode
* `'b'`: Binary mode
* `'+'`: Read and write mode

#### Example

```python
# Opening and closing a file
file = open("example.txt", "r")
print(file.read())
file.close()
```

#### Using `with` Statement

The `with` statement is used to wrap the execution of a block of code with methods defined by a context manager. This ensures that the file is properly closed after its suite finishes, even if an exception is raised.

```python
# Using with statement to open and close a file
with open("example.txt", "r") as file:
    print(file.read())
```

***

### 3. Reading and Writing Files

#### Reading Files

**`read()`**

Reads the entire file.

```python
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```

**`readline()`**

Reads a single line from the file.

```python
with open("example.txt", "r") as file:
    line = file.readline()
    print(line)
```

**`readlines()`**

Reads all the lines in a file and returns them as a list.

```python
with open("example.txt", "r") as file:
    lines = file.readlines()
    print(lines)
```

#### Writing Files

**`write()`**

Writes a string to the file.

```python
with open("example.txt", "w") as file:
    file.write("Hello, World!")
```

#### Appending to Files

**`append()`**

Appends a string to the end of the file.

```python
with open("example.txt", "a") as file:
    file.write("\nHello, again!")
```

***

### 4. Working with File Paths

Python provides the `os` and `pathlib` modules for working with file paths.

#### Using `os` Module

**`os.path.join()`**

Joins one or more path components.

```python
import os

path = os.path.join("folder", "example.txt")
print(path)  # Output: folder/example.txt
```

**`os.path.exists()`**

Checks if a path exists.

```python
if os.path.exists("example.txt"):
    print("File exists")
else:
    print("File does not exist")
```

#### Using `pathlib` Module

The `pathlib` module provides an object-oriented interface for working with file paths.

```python
from pathlib import Path

path = Path("folder/example.txt")

if path.exists():
    print("File exists")
else:
    print("File does not exist")
```

***

### 5. File Methods

#### `tell()`

Returns the current file position.

```python
with open("example.txt", "r") as file:
    print(file.tell())
```

#### `seek()`

Changes the file position.

```python
with open("example.txt", "r") as file:
    file.seek(5)
    print(file.read())
```

#### `truncate()`

Resizes the file to the specified size.

```python
with open("example.txt", "a") as file:
    file.truncate(10)
```

***

### 6. Introduction to Directories

Directories are used to organize files into a hierarchical structure. Python provides the `os` and `pathlib` modules for directory management.

#### Why Directory Management is Important

Directory management is crucial for:

* Organizing files systematically
* Managing large datasets
* Improving data retrieval efficiency
* Creating a structured file system

***

### 7. Creating and Removing Directories

#### Creating Directories

**`os.mkdir()`**

Creates a single directory.

```python
import os

os.mkdir("new_folder")
```

**`os.makedirs()`**

Creates directories recursively.

```python
os.makedirs("parent_folder/child_folder")
```

#### Removing Directories

**`os.rmdir()`**

Removes a single directory.

```python
os.rmdir("new_folder")
```

**`os.removedirs()`**

Removes directories recursively.

```python
os.removedirs("parent_folder/child_folder")
```

***

### 8. Listing Directory Contents

#### `os.listdir()`

Lists the contents of a directory.

```python
import os

contents = os.listdir("folder")
print(contents)
```

#### `os.scandir()`

Returns an iterator of `os.DirEntry` objects corresponding to the entries in the directory.

```python
with os.scandir("folder") as entries:
    for entry in entries:
        print(entry.name)
```

#### Using `pathlib` Module

**`Path.iterdir()`**

Returns an iterator of `Path` objects representing the contents of the directory.

```python
from pathlib import Path

path = Path("folder")

for entry in path.iterdir():
    print(entry.name)
```

***

### 9. Practical Examples

#### Example 1: Copying a File

```python
import shutil

def copy_file(src, dst):
    shutil.copy(src, dst)
    print(f"File copied from {src} to {dst}")

copy_file("example.txt", "example_copy.txt")
```

#### Example 2: Moving a File

```python
import shutil

def move_file(src, dst):
    shutil.move(src, dst)
    print(f"File moved from {src} to {dst}")

move_file("example.txt", "new_folder/example.txt")
```

#### Example 3: Deleting a File

```python
import os

def delete_file(path):
    if os.path.exists(path):
        os.remove(path)
        print(f"File {path} deleted")
    else:
        print(f"File {path} does not exist")

delete_file("example.txt")
```

***

### 10. Common Pitfalls and Best Practices

#### Pitfalls

1. **Forgetting to Close Files**: Always close files to free up system resources.
2. **Incorrect File Paths**: Ensure that file paths are correct to avoid `FileNotFoundError`.
3. **Ignoring File Exceptions**: Handle exceptions to avoid program crashes.

#### Best Practices

1. **Use `with` Statement**: Use the `with` statement to ensure files are properly closed.
2. **Validate File Paths**: Always validate file paths before performing operations.
3. **Handle Exceptions Gracefully**: Use try-except blocks to handle exceptions.

```python
# Good example with with statement and exception handling
try:
    with open("example.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(f"An error occurred: {e}")
```

***

This concludes our detailed tutorial on Python files and directories. We hope you found this tutorial helpful and informative. For more tutorials and resources, visit codeswithpankaj.com. Happy coding!
