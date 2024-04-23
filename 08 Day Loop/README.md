
# Mastering Loops in Python

Loops are a crucial concept in programming, allowing you to execute a block of code repeatedly. In Python, there are two main types of loops: `for` loops and `while` loops. Understanding how to use loops efficiently is essential for writing concise and effective code.

## The `for` Loop

The `for` loop in Python is used to iterate over a sequence (such as a list, tuple, string, or range) and execute a block of code for each item in the sequence. The basic syntax is as follows:

```python
for item in sequence:
    # Code to be executed for each item
```

### Example 1: Iterating Over a List

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(f"I like {fruit}s")
```

In this example, the `for` loop iterates over the elements in the `fruits` list, and the code inside the loop is executed for each item.

### Example 2: Using `range` for Numeric Iteration

```python
for i in range(5):
    print(f"Current number: {i}")
```

Here, the `range(5)` generates a sequence of numbers from 0 to 4, and the loop iterates through them.

## The `while` Loop

The `while` loop is used to repeatedly execute a block of code as long as a specified condition is true. The syntax is as follows:

```python
while condition:
    # Code to be executed as long as the condition is true
```

### Example: Countdown Using a `while` Loop

```python
count = 5

while count > 0:
    print(count)
    count -= 1

print("Blastoff!")
```

In this example, the `while` loop continues to execute as long as the `count` is greater than 0, printing the countdown and decrementing the count in each iteration.

## Controlling Loops with `break` and `continue`

### `break` Statement

The `break` statement is used to exit a loop prematurely. It is often used when a certain condition is met, and the loop needs to terminate immediately.

```python
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 3:
        break
    print(num)
```

In this example, the loop breaks when the value of `num` is 3, preventing the remaining numbers from being printed.

### `continue` Statement

The `continue` statement is used to skip the rest of the code inside the loop for the current iteration and move to the next iteration.

```python
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 3:
        continue
    print(num)
```

Here, the loop continues to the next iteration without printing anything when the value of `num` is 3.

-----
# A nested for loop

A nested for loop in Python is a loop inside another loop. This is useful when you need to iterate over elements in a nested data structure, like a list of lists or a 2D array. The syntax for a nested for loop looks like this:

```python
for outer_variable in outer_sequence:
    # Outer loop code

    for inner_variable in inner_sequence:
        # Inner loop code
```

Here's a simple example of a nested for loop that iterates over a 2D list:

```python
# 2D list (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Nested for loop to iterate over each element in the matrix
for row in matrix:
    for element in row:
        print(element, end=' ')
    print()  # Move to the next line after each row
```

Output:
```
1 2 3 
4 5 6 
7 8 9 
```

In this example, the outer loop iterates over each row of the matrix, and the inner loop iterates over each element in the current row.

--- 
Example of a nested for loop that prints a simple multiplication table:

```python
# Multiplication table example
for i in range(1, 6):  # Outer loop for rows
    for j in range(1, 11):  # Inner loop for columns
        result = i * j
        print(f'{i} * {j} = {result}', end='\t')
    print()  # Move to the next line after each row
```

Output:
```
1 * 1 = 1	1 * 2 = 2	1 * 3 = 3	1 * 4 = 4	1 * 5 = 5	1 * 6 = 6	1 * 7 = 7	1 * 8 = 8	1 * 9 = 9	1 * 10 = 10	
2 * 1 = 2	2 * 2 = 4	2 * 3 = 6	2 * 4 = 8	2 * 5 = 10	2 * 6 = 12	2 * 7 = 14	2 * 8 = 16	2 * 9 = 18	2 * 10 = 20	
3 * 1 = 3	3 * 2 = 6	3 * 3 = 9	3 * 4 = 12	3 * 5 = 15	3 * 6 = 18	3 * 7 = 21	3 * 8 = 24	3 * 9 = 27	3 * 10 = 30	
4 * 1 = 4	4 * 2 = 8	4 * 3 = 12	4 * 4 = 16	4 * 5 = 20	4 * 6 = 24	4 * 7 = 28	4 * 8 = 32	4 * 9 = 36	4 * 10 = 40	
5 * 1 = 5	5 * 2 = 10	5 * 3 = 15	5 * 4 = 20	5 * 5 = 25	5 * 6 = 30	5 * 7 = 35	5 * 8 = 40	5 * 9 = 45	5 * 10 = 50	
```

In this example, the outer loop iterates over the rows (from 1 to 5), and the inner loop iterates over the columns (from 1 to 10). The result is the multiplication table up to 5x10.

---

### Example of a nested for loop that prints a pattern of asterisks in a right-angled triangle:

```python
# Asterisk pattern example
rows = 5

for i in range(1, rows + 1):  # Outer loop for rows
    for j in range(1, i + 1):  # Inner loop for columns
        print('*', end=' ')
    print()  # Move to the next line after each row
```

Output:
```
* 
* * 
* * * 
* * * * 
* * * * * 
```

In this example, the outer loop iterates over the rows (from 1 to 5), and the inner loop iterates over the columns for each row. The `print('* ', end=' ')` statement prints an asterisk with a space after it, and the inner loop prints the required number of asterisks for each row.

## Conclusion

Loops are indispensable tools in Python programming, providing a way to execute repetitive tasks efficiently. Whether you need to iterate over a sequence or execute code while a condition is true, mastering `for` and `while` loops is essential for writing expressive and powerful Python code. Practice and experiment with loops to enhance your programming skills and solve a wide range of problems in a more automated and elegant way.


