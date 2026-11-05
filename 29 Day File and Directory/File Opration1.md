
# File

**What is a File:**
A file is a named location on a storage medium, such as a hard drive or SSD, that stores information, usually in the form of text or binary data.

**Need of File:**
Files are essential for storing and retrieving data persistently. They provide a means for programs to read from and write to data even after the program has finished execution.

**Modes in File (Read, Write, Append):**
- **Read Mode ('r'):** Opens the file for reading. It is the default mode if no mode is specified.
  ```python
  with open('example.txt', 'r') as file:
      content = file.read()
      print(content)
  ```

- **Write Mode ('w'):** Opens the file for writing. If the file already exists, it truncates the file to zero length. If the file does not exist, it creates a new file.
  ```python
  with open('example.txt', 'w') as file:
      file.write('Hello, World!')
  ```

- **Append Mode ('a'):** Opens the file for appending. It doesn't truncate the file; instead, it appends data to the end.
  ```python
  with open('example.txt', 'a') as file:
      file.write('\nAppended content.')
  ```

**Methods in File Operations:**
- **`read(size)`:** Reads the specified number of bytes or the entire file if size is not provided.
  ```python
  with open('example.txt', 'r') as file:
      content = file.read(10)  # Reads the first 10 characters
  ```

- **`readline()`:** Reads a single line from the file.
  ```python
  with open('example.txt', 'r') as file:
      line = file.readline()
  ```

- **`write(data)`:** Writes the specified data to the file.
  ```python
  with open('example.txt', 'w') as file:
      file.write('Hello, World!')
  ```

- **`seek(offset, whence)`:** Moves the file cursor to a specified position. 'whence' can be 0 for the beginning, 1 for the current position, and 2 for the end.
  ```python
  with open('example.txt', 'r') as file:
      file.seek(5)  # Moves to the 5th byte in the file
  ```

These methods provide a basic overview of file operations in Python. Depending on the requirements, additional methods and techniques may be used.