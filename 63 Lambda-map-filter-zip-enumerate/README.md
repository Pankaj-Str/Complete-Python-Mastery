# Python Functional Programming - Lambda, map(), filter(), zip(), enumerate() and Data Processing

## 1. Introduction

Python provides several built-in functions that make data processing easier, faster, and more readable.

In this tutorial, we will learn:

1. Lambda Function
2. `map()` Function
3. `filter()` Function
4. `zip()` Function
5. `enumerate()` Function
6. Processing Data Using `map()` and `filter()`
7. Real-world practical projects
8. Practice exercises with solutions

Real-world scenario:

Imagine you are working as a Junior Data Analyst in a company. You receive employee records, student marks, product prices, and sales data.

You need to:

- Calculate employee salaries.
- Filter students who passed an examination.
- Combine employee names with their salaries.
- Display records with serial numbers.
- Process thousands of records efficiently.

These Python functions help you perform these operations.

# PART 1: Lambda Function

## 2. What is a Lambda Function?

A lambda function is a small, anonymous function in Python.

Unlike a regular function, a lambda function does not require the `def` keyword or an explicit function name.

It is mainly used when you need a small function for a short period.

Syntax:

```
lambda arguments: expression
```

Where:

| Component  | Description                              |
| ---------- | ---------------------------------------- |
| `lambda`   | Keyword used to create a lambda function |
| arguments  | Input parameters                         |
| expression | Single expression that returns a result  |

### Step 1: Create a Normal Function

First, let's create a regular function that calculates the square of a number.

```
def square(num):    return num * numresult = square(5)print(result)
```

Output:

```
25
```

Explanation:

1. `def` creates a function.
2. `square` is the function name.
3. `num` is the parameter.
4. `return` sends the calculated result back.
5. `square(5)` calls the function.

### Step 2: Convert Normal Function into Lambda

Now, perform the same operation using lambda.

```
square = lambda num: num * numresult = square(5)print(result)
```

Output:

```
25
```

Both functions produce the same result.

### Step 3: Lambda with Multiple Arguments

A lambda function can accept multiple arguments.

Example 1: Addition

```
add = lambda a, b: a + bprint(add(10, 20))print(add(50, 30))
```

Output:

```
30
80
```

Example 2: Multiplication

```
multiply = lambda a, b: a * bprint(multiply(5, 4))
```

Output:

```
20
```

Example 3: Find Maximum Number

```
maximum = lambda a, b: a if a > b else bprint(maximum(10, 20))
```

Output:

```
20
```

### Step 4: Lambda with Conditional Statements

We can use conditional expressions inside lambda functions.

Example: Check Even or Odd

```
check = lambda num: "Even" if num % 2 == 0 else "Odd"print(check(10))print(check(7))print(check(25))
```

Output:

```
Even
Odd
Odd
```

Explanation:

- `%` is the modulus operator.
- If the remainder is `0`, the number is even.
- Otherwise, the number is odd.

### Step 5: Lambda with Strings

```
get_length = lambda name: len(name)print(get_length("Pankaj"))print(get_length("Python"))
```

Output:

```
6
6
```

### Step 6: Lambda with Lists

```
numbers = [1, 2, 3, 4, 5]square = lambda x: x * xresult = [square(x) for x in numbers]print(result)
```

Output:

```
[1, 4, 9, 16, 25]
```

### Step 7: Lambda with Sorting

One of the most useful applications of lambda is sorting complex data.

```
students = [    ("Amit", 85),    ("Rahul", 65),    ("Priya", 92),    ("Sneha", 75)]students.sort(key=lambda x: x[1])print(students)
```

Output:

```
[
    ('Rahul', 65),
    ('Sneha', 75),
    ('Amit', 85),
    ('Priya', 92)
]
```

Explanation:

- `students` contains tuples.
- `x` represents each tuple.
- `x[0]` represents the student name.
- `x[1]` represents the student marks.
- `key=lambda x: x[1]` sorts students based on marks.

For descending order:

```
students.sort(key=lambda x: x[1], reverse=True)print(students)
```

### Lambda vs Normal Function

| Normal Function                 | Lambda Function                         |
| ------------------------------- | --------------------------------------- |
| Uses `def`                      | Uses `lambda`                           |
| Has a function name             | Usually anonymous                       |
| Can contain multiple statements | Contains one expression                 |
| Uses explicit `return`          | Returns expression result automatically |
| Suitable for complex logic      | Suitable for short operations           |

When should you use lambda?

- Simple mathematical calculations.
- Sorting data.
- Short conditional operations.
- With `map()`, `filter()` and other functions.

# PART 2: map() Function

## 3. What is map()?

The `map()` function applies a given function to every element of an iterable, such as a list or tuple.

It returns a map iterator, which can be converted into a list, tuple, etc.

Syntax:

```
map(function, iterable)
```

| Parameter | Description                      |
| --------- | -------------------------------- |
| function  | Function to execute              |
| iterable  | List, tuple, or another iterable |

### Step 1: Without Using map()

Suppose we have a list of numbers and want to calculate the square of every number.

```
numbers = [1, 2, 3, 4, 5]result = []for num in numbers:    result.append(num * num)print(result)
```

Output:

```
[1, 4, 9, 16, 25]
```

Here, we use a `for` loop to process each element.

### Step 2: Using map()

Now let's perform the same operation using `map()`.

```
numbers = [1, 2, 3, 4, 5]def square(num):    return num * numresult = map(square, numbers)print(list(result))
```

Output:

```
[1, 4, 9, 16, 25]
```

Explanation:

1. `numbers` contains five elements.
2. `square()` calculates the square.
3. `map()` applies `square()` to every element.
4. `list()` converts the map iterator into a list.

### Step 3: Using map() with Lambda

We can simplify the previous example.

```
numbers = [1, 2, 3, 4, 5]result = map(lambda x: x * x, numbers)print(list(result))
```

Output:

```
[1, 4, 9, 16, 25]
```

### Step 4: Convert Strings into Uppercase

```
names = ["pankaj", "amit", "rahul", "priya"]result = map(lambda name: name.upper(), names)print(list(result))
```

Output:

```
['PANKAJ', 'AMIT', 'RAHUL', 'PRIYA']
```

### Step 5: Convert Celsius into Fahrenheit

Formula:

\\[ F = \frac{9}{5}C + 32 \\]

```
celsius = [0, 10, 20, 30, 40]fahrenheit = map(    lambda c: (c * 9/5) + 32,    celsius)print(list(fahrenheit))
```

Output:

```
[32.0, 50.0, 68.0, 86.0, 104.0]
```

### Step 6: map() with Multiple Iterables

The `map()` function can also accept multiple iterables when the supplied function accepts multiple arguments.

Example: Addition of Two Lists

```
list1 = [10, 20, 30, 40]list2 = [1, 2, 3, 4]result = map(lambda a, b: a + b, list1, list2)print(list(result))
```

Output:

```
[11, 22, 33, 44]
```

Explanation:

| List 1 | List 2 | Addition |
| ------ | ------ | -------- |
| 10     | 1      | 11       |
| 20     | 2      | 22       |
| 30     | 3      | 33       |
| 40     | 4      | 44       |

Important: When multiple iterables have different lengths, `map()` stops when the shortest iterable is exhausted.

### Step 7: Real-World Example – Calculate Employee Salary

Suppose we have employee basic salaries and need to calculate their salaries after adding a 10% increment.

```
salaries = [30000, 40000, 50000, 60000, 70000]updated_salaries = map(    lambda salary: salary + (salary * 0.10),    salaries)print(list(updated_salaries))
```

Output:

```
[33000.0, 44000.0, 55000.0, 66000.0, 77000.0]
```

Use cases of map():

- Data transformation.
- Salary calculations.
- Temperature conversion.
- String formatting.
- Mathematical operations.
- Processing records.

# PART 3: filter() Function

## 4. What is filter()?

The `filter()` function is used to filter elements from an iterable based on a condition.

It returns only those elements for which the given function evaluates to `True`.

Syntax:

```
filter(function, iterable)
```

| Parameter | Description                      |
| --------- | -------------------------------- |
| function  | Function containing a condition  |
| iterable  | List, tuple, or another iterable |

### Step 1: Without Using filter()

Suppose we want to extract even numbers from a list.

```
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]result = []for num in numbers:    if num % 2 == 0:        result.append(num)print(result)
```

Output:

```
[2, 4, 6, 8, 10]
```

### Step 2: Using filter()

```
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]def is_even(num):    return num % 2 == 0result = filter(is_even, numbers)print(list(result))
```

Output:

```
[2, 4, 6, 8, 10]
```

### Step 3: Using filter() with Lambda

```
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]result = filter(lambda x: x % 2 == 0, numbers)print(list(result))
```

Output:

```
[2, 4, 6, 8, 10]
```

### Step 4: Filter Odd Numbers

```
numbers = [10, 15, 20, 25, 30, 35, 40]result = filter(lambda x: x % 2 != 0, numbers)print(list(result))
```

Output:

```
[15, 25, 35]
```

### Step 5: Filter Numbers Greater Than 50

```
numbers = [10, 25, 45, 55, 65, 75, 85, 95]result = filter(lambda x: x > 50, numbers)print(list(result))
```

Output:

```
[55, 65, 75, 85, 95]
```

### Step 6: Filter Names Based on Length

```
names = [    "Amit",    "Pankaj",    "Rahul",    "Priya",    "Christopher"]result = filter(lambda name: len(name) > 5, names)print(list(result))
```

Output:

```
['Pankaj', 'Christopher']
```

### Step 7: Filter Students Who Passed

Suppose the passing marks are 40.

```
marks = [35, 85, 45, 25, 90, 30, 65, 55]result = filter(lambda x: x >= 40, marks)print(list(result))
```

Output:

```
[85, 45, 90, 65, 55]
```

### Step 8: Filter Employees Based on Salary

```
employees = [    {"name": "Amit", "salary": 25000},    {"name": "Rahul", "salary": 45000},    {"name": "Priya", "salary": 65000},    {"name": "Sneha", "salary": 35000}]result = filter(    lambda emp: emp["salary"] > 40000,    employees)for emp in result:    print(emp)
```

Output:

```
{'name': 'Rahul', 'salary': 45000}
{'name': 'Priya', 'salary': 65000}
```

Important: `filter()` selects existing elements. It does not modify the values of those elements.

# PART 4: zip() Function

## 5. What is zip()?

The `zip()` function combines two or more iterables element by element.

It creates pairs or groups of corresponding elements.

Syntax:

```
zip(iterable1, iterable2, ...)
```

### Step 1: Create Two Lists

```
names = ["Amit", "Rahul", "Priya"]marks = [85, 90, 95]result = zip(names, marks)print(list(result))
```

Output:

```
[
    ('Amit', 85),
    ('Rahul', 90),
    ('Priya', 95)
]
```

Explanation:

- First element of each list is combined.
- Second element of each list is combined.
- Third element of each list is combined.

### Step 2: Using zip() with Three Lists

```
names = ["Amit", "Rahul", "Priya"]marks = [85, 90, 95]subjects = ["Python", "Java", "SQL"]result = zip(names, marks, subjects)print(list(result))
```

Output:

```
[
    ('Amit', 85, 'Python'),
    ('Rahul', 90, 'Java'),
    ('Priya', 95, 'SQL')
]
```

### Step 3: Using zip() with a for Loop

```
names = ["Amit", "Rahul", "Priya"]marks = [85, 90, 95]for name, mark in zip(names, marks):    print(name, mark)
```

Output:

```
Amit 85
Rahul 90
Priya 95
```

### Step 4: Create a Dictionary Using zip()

This is one of the most useful applications of `zip()`.

```
keys = ["name", "age", "city"]values = ["Pankaj", 30, "Mumbai"]student = dict(zip(keys, values))print(student)
```

Output:

```
{
    'name': 'Pankaj',
    'age': 30,
    'city': 'Mumbai'
}
```

### Step 5: zip() with Different Lengths

By default, `zip()` stops when the shortest iterable is exhausted.

```
names = ["Amit", "Rahul", "Priya", "Sneha"]marks = [85, 90, 95]result = zip(names, marks)print(list(result))
```

Output:

```
[
    ('Amit', 85),
    ('Rahul', 90),
    ('Priya', 95)
]
```

Notice that `Sneha` is not included because there is no corresponding mark.

### Step 6: Using zip_longest()

If you want to include all elements, use `zip_longest()` from the `itertools` module.

```
from itertools import zip_longestnames = ["Amit", "Rahul", "Priya", "Sneha"]marks = [85, 90, 95]result = zip_longest(names, marks, fillvalue="Not Available")print(list(result))
```

Output:

```
[
    ('Amit', 85),
    ('Rahul', 90),
    ('Priya', 95),
    ('Sneha', 'Not Available')
]
```

Use cases of zip():

- Combining student names and marks.
- Combining employee names and salaries.
- Creating dictionaries.
- Combining product names and prices.
- Processing multiple datasets together.

# PART 5: enumerate() Function

## 6. What is enumerate()?

The `enumerate()` function adds a counter to an iterable.

It returns an iterator containing pairs of:

1. Index (counter).
2. Corresponding element.

Syntax:

```
enumerate(iterable, start=0)
```

| Parameter | Description                   |
| --------- | ----------------------------- |
| iterable  | List, tuple, string, etc.     |
| start     | Starting index (default is 0) |

### Step 1: Without enumerate()

Suppose we want to display student names with serial numbers.

```
students = ["Amit", "Rahul", "Priya", "Sneha"]count = 0for student in students:    print(count, student)    count += 1
```

Output:

```
0 Amit
1 Rahul
2 Priya
3 Sneha
```

### Step 2: Using enumerate()

```
students = ["Amit", "Rahul", "Priya", "Sneha"]result = enumerate(students)print(list(result))
```

Output:

```
[
    (0, 'Amit'),
    (1, 'Rahul'),
    (2, 'Priya'),
    (3, 'Sneha')
]
```

### Step 3: Using enumerate() with a for Loop

```
students = ["Amit", "Rahul", "Priya", "Sneha"]for index, student in enumerate(students):    print(index, student)
```

Output:

```
0 Amit
1 Rahul
2 Priya
3 Sneha
```

### Step 4: Change the Starting Index

By default, the index starts from 0.

But we can change it using the `start` parameter.

```
students = ["Amit", "Rahul", "Priya", "Sneha"]for index, student in enumerate(students, start=1):    print(index, student)
```

Output:

```
1 Amit
2 Rahul
3 Priya
4 Sneha
```

### Step 5: enumerate() with Strings

```
name = "Python"for index, char in enumerate(name):    print(index, char)
```

Output:

```
0 P
1 y
2 t
3 h
4 o
5 n
```

### Step 6: enumerate() with a List of Dictionaries

```
employees = [    {"name": "Amit", "salary": 30000},    {"name": "Rahul", "salary": 45000},    {"name": "Priya", "salary": 55000}]for sr_no, employee in enumerate(employees, start=1):    print(        sr_no,        employee["name"],        employee["salary"]    )
```

Output:

```
1 Amit 30000
2 Rahul 45000
3 Priya 55000
```

Use cases of enumerate():

- Displaying serial numbers.
- Generating numbered reports.
- Tracking records.
- Processing CSV data.
- Displaying student or employee lists.

# PART 6: Process Data Using map() and filter()

## 7. What is Data Processing?

Data processing means collecting, transforming, filtering, and organizing data to obtain meaningful information.

In Python, `map()` and `filter()` are frequently used together to process datasets.

Let's understand this using a real-world business scenario.

## Business Scenario: Student Result Management System

Imagine you are working as a Data Analyst in an educational institute.

You have received student marks and need to:

1. Store student records.
2. Calculate grades.
3. Filter students who passed.
4. Calculate bonus marks.
5. Generate a final report.

### Step 1: Create Student Data

```
students = [    {"name": "Amit", "marks": 85},    {"name": "Rahul", "marks": 35},    {"name": "Priya", "marks": 92},    {"name": "Sneha", "marks": 45},    {"name": "Vikas", "marks": 28},    {"name": "Neha", "marks": 75}]print(students)
```

Our dataset contains six students.

### Step 2: Extract Student Marks Using map()

We want to extract only the marks from the student records.

```
marks = map(    lambda student: student["marks"],    students)print(list(marks))
```

Output:

```
[85, 35, 92, 45, 28, 75]
```

### Step 3: Filter Students Who Passed

Assume the passing marks are 40.

```
passed_students = filter(    lambda student: student["marks"] >= 40,    students)print(list(passed_students))
```

Output:

```
[
    {'name': 'Amit', 'marks': 85},
    {'name': 'Priya', 'marks': 92},
    {'name': 'Sneha', 'marks': 45},
    {'name': 'Neha', 'marks': 75}
]
```

### Step 4: Calculate Bonus Marks Using map()

Suppose the institute gives five bonus marks to every student who passes.

```
passed_students = list(filter(    lambda student: student["marks"] >= 40,    students))updated_students = map(    lambda student: {        "name": student["name"],        "marks": student["marks"],        "bonus_marks": student["marks"] + 5    },    passed_students)print(list(updated_students))
```

Output:

```
[
    {'name': 'Amit', 'marks': 85, 'bonus_marks': 90},
    {'name': 'Priya', 'marks': 92, 'bonus_marks': 97},
    {'name': 'Sneha', 'marks': 45, 'bonus_marks': 50},
    {'name': 'Neha', 'marks': 75, 'bonus_marks': 80}
]
```

### Step 5: Calculate Grades Using map()

Let's assign grades based on the final marks.

| Marks        | Grade |
| ------------ | ----- |
| 90 and above | A+    |
| 80–89        | A     |
| 70–79        | B     |
| 60–69        | C     |
| 40–59        | D     |
| Below 40     | Fail  |

```
def calculate_grade(marks):    if marks >= 90:        return "A+"    elif marks >= 80:        return "A"    elif marks >= 70:        return "B"    elif marks >= 60:        return "C"    elif marks >= 40:        return "D"    else:        return "Fail"grades = map(    lambda student: calculate_grade(student["marks"]),    students)print(list(grades))
```

Output:

```
['A', 'Fail', 'A+', 'D', 'Fail', 'B']
```

### Step 6: Complete Data Processing Pipeline

Now let's combine `filter()` and `map()` in a single program.

Business requirement:

- Select students who scored at least 40 marks.
- Add five bonus marks.
- Calculate the final grade.
- Display the final student report.

```
students = [    {"name": "Amit", "marks": 85},    {"name": "Rahul", "marks": 35},    {"name": "Priya", "marks": 92},    {"name": "Sneha", "marks": 45},    {"name": "Vikas", "marks": 28},    {"name": "Neha", "marks": 75}]# Function to calculate gradedef calculate_grade(marks):    if marks >= 90:        return "A+"    elif marks >= 80:        return "A"    elif marks >= 70:        return "B"    elif marks >= 60:        return "C"    elif marks >= 40:        return "D"    else:        return "Fail"# Step 1: Filter passed studentspassed_students = filter(    lambda student: student["marks"] >= 40,    students
```

Output:

```
STUDENT RESULT REPORT
-----------------------------------------------------------------
1 Amit 85 90 A+
2 Priya 92 97 A+
3 Sneha 45 50 D
4 Neha 75 80 A
```

Understanding the complete pipeline:

Original Student Dataset

6 student records

filter()

Select students with marks >= 40

map()

Add 5 bonus marks

map()

Calculate final grades

Final Result Report

4 processed student records

# PART 7: Real-World Practical Examples

## 8. Practical Example 1 – Employee Salary Processing

Problem statement:

A company wants to increase employee salaries by 15% and display only employees whose updated salaries are greater than ₹40,000.

### Complete Code

```
employees = [    {"name": "Amit", "salary": 25000},    {"name": "Rahul", "salary": 35000},    {"name": "Priya", "salary": 45000},    {"name": "Sneha", "salary": 55000},    {"name": "Vikas", "salary": 30000}]# Increase salary by 15%updated_employees = map(    lambda emp: {        "name": emp["name"],        "salary": emp["salary"] * 1.15    },    employees)# Filter salary greater than 40000filtered_employees = filter(    lambda emp: emp["salary"] > 40000,    updated_employees)# Display reportfor emp in filtered_employees:    print(emp)
```

Output:

```
{'name': 'Priya', 'salary': 51750.0}
{'name': 'Sneha', 'salary': 63250.0}
```

## 9. Practical Example 2 – Product Price Management

Problem statement:

An online shopping company wants to:

- Store product names and prices.
- Increase product prices by 10%.
- Filter products with updated prices above ₹1,000.
- Display the final product report.

```
products = [    ("Laptop", 50000),    ("Mouse", 500),    ("Keyboard", 1500),    ("Monitor", 12000),    ("USB Cable", 200)]# Update product pricesupdated_products = map(    lambda p: (p[0], p[1] * 1.10),    products)# Filter products above 1000filtered_products = filter(    lambda p: p[1] > 1000,    updated_products)# Display resultfor product, price in filtered_products:    print(        f"Product: {product}, Updated Price: ₹{price:.2f}"    )
```

Output:

```
Product: Laptop, Updated Price: ₹55000.00
Product: Keyboard, Updated Price: ₹1650.00
Product: Monitor, Updated Price: ₹13200.00
```

## 10. Practical Example 3 – Sales Data Analysis

Problem statement:

A company has recorded its daily sales. You need to:

- Increase each sales amount by 10%.
- Filter sales greater than ₹5,000.
- Display the sales with serial numbers.

```
sales = [2000, 4500, 6000, 8000, 3000, 10000, 12000]# Increase sales by 10%updated_sales = map(    lambda x: x * 1.10,    sales)# Filter sales above 5000filtered_sales = filter(    lambda x: x > 5000,    updated_sales)# Display reportfor index, amount in enumerate(filtered_sales, start=1):    print(f"Sale {index}: ₹{amount:.2f}")
```

Output:

```
Sale 1: ₹6600.00
Sale 2: ₹8800.00
Sale 3: ₹11000.00
Sale 4: ₹13200.00
```

# PART 8: Difference Between map(), filter(), zip() and enumerate()

## 11. Comparison Table

| Function      | Purpose                           | Example        |
| ------------- | --------------------------------- | -------------- |
| `map()`       | Transform every element           | Square numbers |
| `filter()`    | Select elements using a condition | Even numbers   |
| `zip()`       | Combine multiple iterables        | Names + marks  |
| `enumerate()` | Add index to elements             | Serial numbers |
| `lambda`      | Create a short anonymous function | Addition       |

### Quick Example

```
numbers = [1, 2, 3, 4, 5]# map()print(list(map(lambda x: x * 2, numbers)))# filter()print(list(filter(lambda x: x > 2, numbers)))# enumerate()print(list(enumerate(numbers)))# zip()names = ["Amit", "Rahul", "Priya"]marks = [85, 90, 95]print(list(zip(names, marks)))
```

Output:

```
[2, 4, 6, 8, 10]

[3, 4, 5]

[(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]

[('Amit', 85), ('Rahul', 90), ('Priya', 95)]
```

# PART 9: Important Concepts and Common Mistakes

## 12. Understanding Iterators

The `map()`, `filter()`, `zip()` and `enumerate()` functions return iterators.

An iterator provides elements one at a time when requested.

Example:

```
numbers = [1, 2, 3, 4, 5]result = map(lambda x: x * 2, numbers)print(result)
```

Output (representation may vary):

```
<map object at 0x...>
```

Why don't we see the actual values?

Because `map()` returns an iterator rather than a list.

To see the values:

```
print(list(result))
```

Output:

```
[2, 4, 6, 8, 10]
```

## 13. Important: Iterators Can Be Exhausted

Once you consume an iterator, you cannot reuse it to retrieve the same values.

```
numbers = [1, 2, 3, 4]result = map(lambda x: x * 2, numbers)print(list(result))print(list(result))
```

Output:

```
[2, 4, 6, 8]

[]
```

The second result is empty because the iterator has already been consumed.

Solution: Create a new iterator whenever you need to process the original data again, or store the results in a list.

## 14. map() vs List Comprehension

Both can transform data.

Using map():

```
numbers = [1, 2, 3, 4, 5]result = list(map(lambda x: x * 2, numbers))print(result)
```

Using list comprehension:

```
numbers = [1, 2, 3, 4, 5]result = [x * 2 for x in numbers]print(result)
```

Both produce:

```
[2, 4, 6, 8, 10]
```

Which one should you use?

- Use `map()` when applying an existing function to every element.
- Use list comprehension when transformation and filtering are easier to understand together.
- Choose readability rather than assuming one is always faster.

# PART 10: Practice Exercises for Students

Hands-on Practice

Try solving these exercises yourself before checking the solutions.

## Exercise 1: Lambda Function

Create a lambda function to calculate:

1. Square of a number.
2. Cube of a number.
3. Addition of two numbers.
4. Check whether a number is positive or negative.
5. Find the largest of two numbers.

## Exercise 2: map() Function

Given the following list:

```
numbers = [10, 20, 30, 40, 50]
```

Perform these operations:

1. Multiply every number by 2.
2. Calculate the square of every number.
3. Convert all numbers into strings.
4. Add 100 to every number.
5. Calculate 18% GST on every price.

## Exercise 3: filter() Function

Given the following list:

```
numbers = [12, 15, 20, 25, 30, 35, 40, 45, 50]
```

Perform these operations:

1. Extract even numbers.
2. Extract odd numbers.
3. Extract numbers greater than 25.
4. Extract numbers divisible by 5.
5. Extract numbers between 20 and 40.

## Exercise 4: zip() Function

Create three lists:

```
names = ["Amit", "Rahul", "Priya", "Sneha"]marks = [85, 90, 75, 95]subjects = ["Python", "Java", "SQL", "MongoDB"]
```

Perform these operations:

1. Combine names and marks.
2. Combine all three lists.
3. Create a dictionary using names and marks.
4. Display each student's name and subject.

## Exercise 5: enumerate() Function

Given:

```
courses = [    "Python",    "Java",    "Machine Learning",    "Data Science",    "SQL"]
```

Perform these operations:

1. Display each course with an index.
2. Start indexing from 1.
3. Display only courses at even indexes.
4. Generate a numbered course list.

## Exercise 6: Data Processing Project

Student Performance Analysis

Create a Python program that:

1. Stores 10 student records.
2. Extracts student marks using `map()`.
3. Filters students who scored 50 or above using `filter()`.
4. Adds 5 bonus marks to passed students using `map()`.
5. Calculates grades.
6. Displays the final result using `enumerate()`.
7. Combines student names and grades using `zip()`.

# PART 11: Solutions to Selected Exercises

## Solution 1: Lambda Functions

```
# Squaresquare = lambda x: x ** 2# Cubecube = lambda x: x ** 3# Additionadd = lambda a, b: a + b# Positive or Negativecheck = lambda x: "Positive" if x >= 0 else "Negative"# Largest numbermaximum = lambda a, b: a if a > b else bprint(square(5))print(cube(3))print(add(10, 20))print(check(-5))print(maximum(10, 20))
```

Output:

```
25
27
30
Negative
20
```

## Solution 2: map()

```
numbers = [10, 20, 30, 40, 50]# Multiply by 2print(list(map(lambda x: x * 2, numbers)))# Squareprint(list(map(lambda x: x ** 2, numbers)))# Convert into stringsprint(list(map(str, numbers)))# Add 100print(list(map(lambda x: x + 100, numbers)))# Calculate GSTprint(list(map(lambda x: x * 0.18, numbers)))
```

## Solution 3: filter()

```
numbers = [12, 15, 20, 25, 30, 35, 40, 45, 50]# Even numbersprint(list(filter(lambda x: x % 2 == 0, numbers)))# Odd numbersprint(list(filter(lambda x: x % 2 != 0, numbers)))# Greater than 25print(list(filter(lambda x: x > 25, numbers)))# Divisible by 5print(list(filter(lambda x: x % 5 == 0, numbers)))# Between 20 and 40print(list(filter(lambda x: 20 <= x <= 40, numbers)))
```

## Solution 4: zip()

```
names = ["Amit", "Rahul", "Priya", "Sneha"]marks = [85, 90, 75, 95]subjects = ["Python", "Java", "SQL", "MongoDB"]# Combine names and marksprint(list(zip(names, marks)))# Combine three listsprint(list(zip(names, marks, subjects)))# Create dictionaryprint(dict(zip(names, marks)))# Display name and subjectfor name, subject in zip(names, subjects):    print(name, subject)
```

## Solution 5: enumerate()

```
courses = [    "Python",    "Java",    "Machine Learning",    "Data Science",    "SQL"]# Index from 0for index, course in enumerate(courses):    print(index, course)# Index from 1for index, course in enumerate(courses, start=1):    print(index, course)# Courses at even indexesfor index, course in enumerate(courses):    if index % 2 == 0:        print(course)
```

# PART 12: Final Interview Questions

## 15. Frequently Asked Questions

Q1. What is a lambda function in Python?

A lambda function is an anonymous function created using the `lambda` keyword. It supports a single expression and returns its evaluated result.

Q2. What is the difference between lambda and def?

`def` creates a regular named function that can contain multiple statements, whereas `lambda` creates a small anonymous function with one expression.

Q3. What is the purpose of map()?

`map()` applies a given function to every element of an iterable and returns an iterator.

Q4. What is the purpose of filter()?

`filter()` selects elements from an iterable based on a condition.

Q5. What is the difference between map() and filter()?

`map()` transforms elements, whereas `filter()` selects elements based on a condition.

Q6. What does zip() do?

`zip()` combines corresponding elements from multiple iterables into tuples.

Q7. What is enumerate()?

`enumerate()` adds a counter to an iterable and returns index-element pairs.

Q8. What is the default starting index of enumerate()?

The default starting index is 0.

Q9. Can map() work with multiple lists?

Yes. `map()` accepts multiple iterables if the supplied function accepts the corresponding number of arguments.

Q10. What happens when two lists have different lengths in zip()?

By default, `zip()` stops when the shortest iterable is exhausted.

Q11. Can we use lambda with filter()?

Yes. Lambda functions are frequently used with `filter()` to write short filtering conditions.

Q12. What is lazy evaluation in map() and filter()?

They produce iterators, so their elements are calculated when requested rather than all being stored immediately in a list.

# PART 13: Summary – Complete Revision

| Topic           | Main Purpose                  | Example                             |
| --------------- | ----------------------------- | ----------------------------------- |
| Lambda          | Anonymous function            | `lambda x: x * 2`                   |
| map()           | Transform data                | `map(str, numbers)`                 |
| filter()        | Filter data                   | `filter(lambda x: x > 10, numbers)` |
| zip()           | Combine data                  | `zip(names, marks)`                 |
| enumerate()     | Add index                     | `enumerate(names, start=1)`         |
| Data Processing | Transform and filter datasets | `map()` + `filter()`                |

## Recommended Learning Order

1. Lambda Function

   Learn anonymous functions and expressions.
2. map() Function

   Learn how to transform every element.
3. filter() Function

   Learn how to select records based on conditions.
4. zip() Function

   Learn how to combine multiple datasets.
5. enumerate() Function

   Learn how to generate indexes and serial numbers.
6. Real-World Data Processing

   Combine all concepts in practical projects.

