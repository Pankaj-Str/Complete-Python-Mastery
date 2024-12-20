
### 1. Iterating Over a List

```python
# List of numbers
numbers = [1, 2, 3, 4, 5]

# Using a for loop to iterate over the list of numbers
for num in numbers:
    print(num)
```

**Explanation:** This loop prints each number in the `numbers` list.

### 2. Iterating Over a String

```python
# String
text = "Hello"

# Using a for loop to iterate over each character in the string
for char in text:
    print(char)
```

**Explanation:** This loop prints each character in the `text` string.

### 3. Using `range()` Function

```python
# Using the range() function to generate a sequence of numbers
for i in range(5):
    print(i)
```

**Explanation:** This loop prints numbers from 0 to 4.

### 4. Iterating Over a Dictionary

```python
# Dictionary of fruits and their colors
fruits = {"apple": "red", "banana": "yellow", "grape": "purple"}

# Using a for loop to iterate over dictionary keys
for fruit in fruits:
    print(fruit, fruits[fruit])
```

**Explanation:** This loop prints each fruit and its corresponding color.

### 5. Nested For Loop

```python
# Nested for loop to print a multiplication table
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i * j}")
    print("-" * 10)  # Separator between tables
```

**Explanation:** This loop prints a multiplication table from 1 to 5.

### 6. Iterating Over a List of Tuples

```python
# List of tuples
points = [(1, 2), (3, 4), (5, 6)]

# Using a for loop to iterate over the list of tuples
for x, y in points:
    print(f"x: {x}, y: {y}")
```

**Explanation:** This loop prints each tuple's elements.

### 7. List Comprehension

```python
# Using a for loop in a list comprehension to create a new list
squares = [x**2 for x in range(10)]
print(squares)
```

**Explanation:** This creates a list of squares of numbers from 0 to 9.

### 8. Iterating Over a Set

```python
# Set of unique numbers
unique_numbers = {1, 2, 3, 4, 5}

# Using a for loop to iterate over the set
for num in unique_numbers:
    print(num)
```

**Explanation:** This loop prints each unique number in the set.

### 9. Breaking Out of a Loop

```python
# Using a for loop with a break statement
for i in range(10):
    if i == 5:
        break
    print(i)
```

**Explanation:** This loop prints numbers from 0 to 4 and breaks when `i` equals 5.

### 10. Continue Statement

```python
# Using a for loop with a continue statement
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
```

**Explanation:** This loop prints only the odd numbers from 0 to 9, skipping even numbers.

### 11. Enumerate Function

```python
# List of names
names = ["Alice", "Bob", "Charlie"]

# Using enumerate to get index and value
for index, name in enumerate(names):
    print(f"Index: {index}, Name: {name}")
```

**Explanation:** This loop prints each name along with its index in the list.

### 12. Zip Function

```python
# Two lists
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

# Using zip to iterate over two lists simultaneously
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
```

**Explanation:** This loop prints names and their corresponding ages.

### 13. Iterating in Reverse

```python
# List of numbers
numbers = [1, 2, 3, 4, 5]

# Using a for loop to iterate over the list in reverse
for num in reversed(numbers):
    print(num)
```

**Explanation:** This loop prints the numbers in reverse order.

### 14. Iterating Over a Dictionary with Items

```python
# Dictionary of fruits and their colors
fruits = {"apple": "red", "banana": "yellow", "grape": "purple"}

# Using a for loop to iterate over dictionary items
for fruit, color in fruits.items():
    print(f"The color of {fruit} is {color}")
```

**Explanation:** This loop prints each fruit and its corresponding color.

### 15. Iterating Over a Nested List

```python
# Nested list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Using a nested for loop to iterate over a nested list
for row in matrix:
    for num in row:
        print(num, end=' ')
    print()
```

**Explanation:** This loop prints each number in the nested list (matrix) in a matrix format.

### 16. Using For Loop with Else

```python
# Using a for loop with an else clause
for i in range(5):
    print(i)
else:
    print("Loop finished")
```

**Explanation:** This loop prints numbers from 0 to 4 and then prints "Loop finished".

### 17. Iterating Over a File

```python
# Writing some lines to a file
with open("example.txt", "w") as file:
    file.write("Line 1\nLine 2\nLine 3\n")

# Using a for loop to iterate over each line in a file
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())
```

**Explanation:** This loop prints each line from the file `example.txt`.

### 18. Using a For Loop with a Dictionary Comprehension

```python
# Dictionary of fruits and their prices
fruit_prices = {"apple": 1.2, "banana": 0.5, "cherry": 2.5}

# Using a for loop in a dictionary comprehension to create a new dictionary
discounted_prices = {fruit: price * 0.9 for fruit, price in fruit_prices.items()}
print(discounted_prices)
```

**Explanation:** This creates a new dictionary with discounted prices for each fruit.

### 19. Iterating Over a List with a Condition

```python
# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Using a for loop to print only even numbers
for num in numbers:
    if num % 2 == 0:
        print(num)
```

**Explanation:** This loop prints only the even numbers from the list.

### 20. Using For Loop to Create a Set

```python
# List of numbers with duplicates
numbers = [1, 2, 2, 3, 4, 4, 5]

# Using a for loop to create a set with unique numbers
unique_numbers = {num for num in numbers}
print(unique_numbers)
```

**Explanation:** This creates a set of unique numbers from the list.
