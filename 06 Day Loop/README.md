
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

## Conclusion

Loops are indispensable tools in Python programming, providing a way to execute repetitive tasks efficiently. Whether you need to iterate over a sequence or execute code while a condition is true, mastering `for` and `while` loops is essential for writing expressive and powerful Python code. Practice and experiment with loops to enhance your programming skills and solve a wide range of problems in a more automated and elegant way.

## Question - 

1. Write a  Program to Calculate the Sum of Natural Numbers ?
   
   ```

   Example : 
   Enter Start Number : 1
   Enter End Number : 10
   
   -----------------
   total sum of 1 to 10 = 55
   ----------------- 

   ```
2. Write a  Program to Generate Multiplication Table ?

    ```

    Enter print Table Number : 2
    
    2 x 1  = 2
    2 x 2  = 4
    .
    .
    2 x 10 = 20

    ```
3. Write a  Program to Display count of Alphabets in to String 
   
   ```
      Enter Word : p4n.in

      total = count of Alphabets : 6

   ```
4. Write a  Program to Count Number of Digits in an Integer

   ```
      Enter Number : 4567
      Count Number : total Digits : 4 

   ```
5. Write a  Program to Reverse a Number

   ```
      Enter Number : 4569
      Reverse Number : 9654 

   ```
   
