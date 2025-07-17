
# Python Loops
**Website**: [www.codeswithpankaj.com](http://www.codeswithpankaj.com)  
**Author**: Pankaj Chouhan

Welcome to *Codes With Pankaj*! In this tutorial, we’ll explore Python loops, a fundamental concept that lets you repeat tasks efficiently in your code. Whether you’re printing numbers or processing data, loops make your life as a coder easier. Let’s dive in step by step!

---

## Table of Contents
1. [What Are Loops?](#what-are-loops)
2. [Types of Loops in Python](#types-of-loops)
3. [The `for` Loop](#for-loop)
   - Step 1: Understanding the `for` Loop
   - Step 2: Syntax and Example
   - Step 3: Using `range()`
   - Step 4: Looping Through Lists
4. [The `while` Loop](#while-loop)
   - Step 5: Understanding the `while` Loop
   - Step 6: Syntax and Example
5. [Loop Control Statements](#loop-control)
   - Step 7: Using `break`
   - Step 8: Using `continue`
6. [Practice Exercises](#practice-exercises)
7. [What’s Next?](#whats-next)

---

## What Are Loops?
A loop in programming allows you to repeat a block of code multiple times. Imagine you want to print "Hello, Pankaj!" 5 times. Writing `print("Hello, Pankaj!")` five times is tedious. Loops let you do this with just a few lines of code!

In Python, there are two main types of loops:
- **`for` loop**: Used when you know how many times you want to repeat something.
- **`while` loop**: Used when you want to repeat until a condition is met.

Let’s explore both with simple examples.

---

## Types of Loops in Python
Python offers two primary loops:
1. **`for` loop**: Iterates over a sequence (like a list, string, or range of numbers).
2. **`while` loop**: Repeats as long as a condition is true.

We’ll break down each loop with examples you can try yourself.

---

## The `for` Loop
### Step 1: Understanding the `for` Loop
The `for` loop is perfect for repeating tasks a specific number of times or iterating over items in a sequence (like a list or string).

### Step 2: Syntax and Example
Here’s the basic syntax of a `for` loop:

```python
for variable in sequence:
    # Code block to repeat
```

**Example**: Print numbers 1 to 5.

```python
for num in [1, 2, 3, 4, 5]:
    print(num)
```

**Output**:
```
1
2
3
4
5
```

In this example:
- `num` is the loop variable that takes each value in the list `[1, 2, 3, 4, 5]`.
- The `print(num)` statement runs for each value of `num`.

### Step 3: Using `range()`
The `range()` function generates a sequence of numbers, making it super useful with `for` loops.

**Example**: Print numbers 0 to 4.

```python
for i in range(5):
    print(i)
```

**Output**:
```
0
1
2
3
4
```

**Explanation**:
- `range(5)` generates numbers from 0 to 4 (5 numbers total, starting at 0).
- You can also specify a start and end: `range(1, 6)` gives 1 to 5.

Try this:
```python
for i in range(1, 6):
    print(f"Number: {i}")
```

**Output**:
```
Number: 1
Number: 2
Number: 3
Number: 4
Number: 5
```

### Step 4: Looping Through Lists
You can loop through any list, not just numbers.

**Example**: Print each fruit in a list.

```python
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"I love {fruit}!")
```

**Output**:
```
I love apple!
I love banana!
I love orange!
```

**Tip**: The loop variable (`fruit`) takes each item in the list one by one.

---

## The `while` Loop
### Step 5: Understanding the `while` Loop
The `while` loop keeps running as long as a condition is true. It’s great when you don’t know how many times you’ll need to loop.

### Step 6: Syntax and Example
Here’s the syntax:

```python
while condition:
    # Code block to repeat
```

**Example**: Print numbers 1 to 5.

```python
count = 1
while count <= 5:
    print(count)
    count += 1
```

**Output**:
```
1
2
3
4
5
```

**Explanation**:
- `count = 1` sets the starting value.
- The loop runs while `count <= 5` is true.
- `count += 1` increases `count` by 1 each time to avoid an infinite loop.

**Warning**: Always ensure the condition will eventually become false, or you’ll get an infinite loop!

Try this:
```python
number = 10
while number > 0:
    print(f"Countdown: {number}")
    number -= 2
```

**Output**:
```
Countdown: 10
Countdown: 8
Countdown: 6
Countdown: 4
Countdown: 2
```

---

## Loop Control Statements
Sometimes, you want to control how a loop behaves. Python provides two useful statements: `break` and `continue`.

### Step 7: Using `break`
The `break` statement stops the loop immediately.

**Example**: Stop the loop when you find a specific number.

```python
for i in range(1, 10):
    if i == 5:
        break
    print(i)
```

**Output**:
```
1
2
3
4
```

**Explanation**: The loop stops when `i` equals 5, so 5 and higher numbers aren’t printed.

### Step 8: Using `continue`
The `continue` statement skips the rest of the current loop iteration and moves to the next one.

**Example**: Skip printing even numbers.

```python
for i in range(1, 6):
    if i % 2 == 0:
        continue
    print(f"Odd number: {i}")
```

**Output**:
```
Odd number: 1
Odd number: 3
Odd number: 5
```

**Explanation**: When `i` is even (divisible by 2), `continue` skips the `print` statement.

---

## Practice Exercises
Ready to test your skills? Try these exercises and check your answers on [www.codeswithpankaj.com](http://www.codeswithpankaj.com)!

1. **Exercise 1**: Write a `for` loop to print all even numbers from 2 to 10.
2. **Exercise 2**: Use a `while` loop to print "Hello, Pankaj!" 3 times.
3. **Exercise 3**: Write a `for` loop that stops when it reaches the number 7 (use `break`).
4. **Exercise 4**: Write a loop that skips printing the number 4 (use `continue`).

**Sample Solution (Exercise 1)**:
```python
for i in range(2, 11, 2):
    print(i)
```

**Output**:
```
2
4
6
8
10
```

Visit [www.codeswithpankaj.com](http://www.codeswithpankaj.com) for solutions to all exercises!

---


### Notes for Beginners
- **Try it yourself**: Copy the code examples into a Python editor (like IDLE, VS Code, or an online editor like Replit) and run them.
- **Experiment**: Change numbers or conditions in the examples to see what happens.
- **Ask for help**: If you’re stuck, leave a comment on our website or join the *Codes With Pankaj* community!

---
