# Python Functional Programming

## Lambda Functions, map(), filter(), zip(), enumerate(), and real-world data processing with practical examples.

---

## Table of Contents

1. Introduction to Functional Programming
2. Lambda Function
3. map() Function
4. filter() Function
5. zip() Function
6. enumerate() Function
7. Process Data Using map() and filter()
8. Real-World Practical Examples
9. Understanding Python Iterators
10. map() vs filter() vs List Comprehension
11. Common Mistakes
12. Practice Exercises
13. Exercise Solutions
14. Mini Projects
15. Interview Questions
16. Conclusion

---

# 1. Introduction to Functional Programming

Functional programming is a programming approach in which functions are used to process and transform data.

Python supports functional programming through several built-in functions.

The important functions covered in this tutorial are:

| Function | Description |
|---|---|
| lambda | Creates anonymous functions |
| map() | Transforms every element |
| filter() | Filters elements based on conditions |
| zip() | Combines multiple iterables |
| enumerate() | Adds an index to iterable elements |

### Why Do We Need These Functions?

Consider a business scenario.

You are working as a Junior Data Analyst in an IT company.

You receive the following employee salary data:

```python
salaries = [25000, 30000, 45000, 55000, 65000]
```

Your requirements are:

1. Increase employee salaries by 10%.
2. Filter salaries greater than ₹40,000.
3. Combine employee names with salaries.
4. Display records with serial numbers.

Python provides these functions to make such operations easier.

---

# 2. Lambda Function

## 2.1 What is a Lambda Function?

A lambda function is an anonymous function in Python.

It is created using the `lambda` keyword instead of `def`.

Lambda functions are useful when we need a small function for a short operation.

### Syntax

```python
lambda arguments: expression
```

### Example 1: Normal Function

```python
def square(num):
    return num * num

result = square(5)

print(result)
```

Output:

```text
25
```

### Example 2: Lambda Function

```python
square = lambda num: num * num

print(square(5))
```

Output:

```text
25
```

### Explanation

- `lambda` creates an anonymous function.
- `num` is the parameter.
- `num * num` is the expression.
- The expression result is returned automatically.

## 2.2 Lambda with One Argument

```python
double = lambda x: x * 2

print(double(10))
print(double(20))
print(double(30))
```

Output:

```text
20
40
60
```

## 2.3 Lambda with Multiple Arguments

```python
add = lambda a, b: a + b

print(add(10, 20))
print(add(50, 30))
```

Output:

```text
30
80
```

### Multiplication

```python
multiply = lambda a, b: a * b

print(multiply(5, 4))
```

Output:

```text
20
```

### Division

```python
divide = lambda a, b: a / b

print(divide(20, 5))
```

Output:

```text
4.0
```

## 2.4 Lambda with Conditional Expressions

Lambda functions support conditional expressions.

### Example: Even or Odd

```python
check = lambda x: "Even" if x % 2 == 0 else "Odd"

print(check(10))
print(check(15))
```

Output:

```text
Even
Odd
```

### Example: Positive or Negative

```python
check = lambda x: "Positive" if x > 0 else "Negative or Zero"

print(check(10))
print(check(-5))
print(check(0))
```

Output:

```text
Positive
Negative or Zero
Negative or Zero
```

## 2.5 Lambda with Strings

```python
name_length = lambda name: len(name)

print(name_length("Pankaj"))
print(name_length("Python"))
```

Output:

```text
6
6
```

### Convert String into Uppercase

```python
convert = lambda name: name.upper()

print(convert("python programming"))
```

Output:

```text
PYTHON PROGRAMMING
```

## 2.6 Lambda with Lists

```python
numbers = [1, 2, 3, 4, 5]

square = lambda x: x ** 2

result = [square(x) for x in numbers]

print(result)
```

Output:

```text
[1, 4, 9, 16, 25]
```

## 2.7 Lambda with Sorting

Lambda functions are frequently used with the `sort()` and `sorted()` functions.

```python
students = [
    ("Amit", 85),
    ("Rahul", 65),
    ("Priya", 92),
    ("Sneha", 75)
]

students.sort(key=lambda x: x[1])

print(students)
```

Output:

```text
[
    ('Rahul', 65),
    ('Sneha', 75),
    ('Amit', 85),
    ('Priya', 92)
]
```

### Descending Order

```python
students.sort(key=lambda x: x[1], reverse=True)

print(students)
```

## 2.8 Lambda with Dictionary

```python
employees = [
    {"name": "Amit", "salary": 30000},
    {"name": "Rahul", "salary": 50000},
    {"name": "Priya", "salary": 40000}
]

result = sorted(
    employees,
    key=lambda emp: emp["salary"]
)

print(result)
```

Output:

```text
[
    {'name': 'Amit', 'salary': 30000},
    {'name': 'Priya', 'salary': 40000},
    {'name': 'Rahul', 'salary': 50000}
]
```

### Important Points

- Lambda functions can accept multiple arguments.
- Lambda functions contain one expression.
- Lambda functions return their expression result automatically.
- They are useful with map(), filter(), and sorted().

---

# 3. map() Function

## 3.1 What is map()?

The `map()` function applies a given function to every element of an iterable.

It returns a map iterator.

### Syntax

```python
map(function, iterable)
```

Parameters:

| Parameter | Description |
|---|---|
| function | Function to apply |
| iterable | List, tuple, or another iterable |

## 3.2 Without Using map()

Calculate the square of every number.

```python
numbers = [1, 2, 3, 4, 5]

result = []

for num in numbers:
    result.append(num * num)

print(result)
```

Output:

```text
[1, 4, 9, 16, 25]
```

## 3.3 Using map() with a Normal Function

```python
numbers = [1, 2, 3, 4, 5]

def square(num):
    return num * num

result = map(square, numbers)

print(list(result))
```

Output:

```text
[1, 4, 9, 16, 25]
```

## 3.4 Using map() with Lambda

```python
numbers = [1, 2, 3, 4, 5]

result = map(lambda x: x * x, numbers)

print(list(result))
```

Output:

```text
[1, 4, 9, 16, 25]
```

## 3.5 Multiply Every Number by 2

```python
numbers = [10, 20, 30, 40, 50]

result = map(lambda x: x * 2, numbers)

print(list(result))
```

Output:

```text
[20, 40, 60, 80, 100]
```

## 3.6 Convert Strings into Uppercase

```python
names = ["pankaj", "amit", "rahul", "priya"]

result = map(lambda name: name.upper(), names)

print(list(result))
```

Output:

```text
['PANKAJ', 'AMIT', 'RAHUL', 'PRIYA']
```

## 3.7 Convert Celsius into Fahrenheit

Formula:

F = (C × 9/5) + 32

```python
celsius = [0, 10, 20, 30, 40]

fahrenheit = map(
    lambda c: (c * 9/5) + 32,
    celsius
)

print(list(fahrenheit))
```

Output:

```text
[32.0, 50.0, 68.0, 86.0, 104.0]
```

## 3.8 map() with Multiple Iterables

The map() function supports multiple iterables.

### Example: Addition of Two Lists

```python
list1 = [10, 20, 30, 40]

list2 = [1, 2, 3, 4]

result = map(lambda a, b: a + b, list1, list2)

print(list(result))
```

Output:

```text
[11, 22, 33, 44]
```

### Example: Multiplication of Two Lists

```python
list1 = [2, 3, 4, 5]

list2 = [10, 20, 30, 40]

result = map(lambda a, b: a * b, list1, list2)

print(list(result))
```

Output:

```text
[20, 60, 120, 200]
```

## 3.9 Employee Salary Increment Using map()

```python
salaries = [30000, 40000, 50000, 60000]

updated_salaries = map(
    lambda salary: salary + (salary * 0.10),
    salaries
)

print(list(updated_salaries))
```

Output:

```text
[33000.0, 44000.0, 55000.0, 66000.0]
```

### Use Cases of map()

- Data transformation.
- Mathematical calculations.
- Salary processing.
- String conversion.
- Data cleaning.
- Temperature conversion.

---

# 4. filter() Function

## 4.1 What is filter()?

The `filter()` function selects elements from an iterable based on a given condition.

It returns only the elements for which the condition evaluates to True.

### Syntax

```python
filter(function, iterable)
```

## 4.2 Without Using filter()

Extract even numbers from a list.

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = []

for num in numbers:

    if num % 2 == 0:
        result.append(num)

print(result)
```

Output:

```text
[2, 4, 6, 8, 10]
```

## 4.3 Using filter() with Normal Function

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def is_even(num):
    return num % 2 == 0

result = filter(is_even, numbers)

print(list(result))
```

Output:

```text
[2, 4, 6, 8, 10]
```

## 4.4 Using filter() with Lambda

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = filter(lambda x: x % 2 == 0, numbers)

print(list(result))
```

Output:

```text
[2, 4, 6, 8, 10]
```

## 4.5 Filter Odd Numbers

```python
numbers = [10, 15, 20, 25, 30, 35, 40]

result = filter(lambda x: x % 2 != 0, numbers)

print(list(result))
```

Output:

```text
[15, 25, 35]
```

## 4.6 Filter Numbers Greater Than 50

```python
numbers = [10, 25, 45, 55, 65, 75, 85, 95]

result = filter(lambda x: x > 50, numbers)

print(list(result))
```

Output:

```text
[55, 65, 75, 85, 95]
```

## 4.7 Filter Names Based on Length

```python
names = [
    "Amit",
    "Pankaj",
    "Rahul",
    "Priya",
    "Christopher"
]

result = filter(lambda name: len(name) > 5, names)

print(list(result))
```

Output:

```text
['Pankaj', 'Christopher']
```

## 4.8 Filter Students Who Passed

```python
marks = [35, 85, 45, 25, 90, 30, 65, 55]

result = filter(lambda x: x >= 40, marks)

print(list(result))
```

Output:

```text
[85, 45, 90, 65, 55]
```

## 4.9 Filter Employee Records

```python
employees = [
    {"name": "Amit", "salary": 25000},
    {"name": "Rahul", "salary": 45000},
    {"name": "Priya", "salary": 65000},
    {"name": "Sneha", "salary": 35000}
]

result = filter(
    lambda emp: emp["salary"] > 40000,
    employees
)

for emp in result:
    print(emp)
```

Output:

```text
{'name': 'Rahul', 'salary': 45000}
{'name': 'Priya', 'salary': 65000}
```

### Use Cases of filter()

- Extracting passed students.
- Filtering employees.
- Selecting products by price.
- Extracting even and odd numbers.
- Filtering customer records.
- Data analysis.

---

# 5. zip() Function

## 5.1 What is zip()?

The zip() function combines corresponding elements from two or more iterables.

It returns an iterator containing tuples.

### Syntax

```python
zip(iterable1, iterable2, ...)
```

## 5.2 Combine Two Lists

```python
names = ["Amit", "Rahul", "Priya"]

marks = [85, 90, 95]

result = zip(names, marks)

print(list(result))
```

Output:

```text
[('Amit', 85), ('Rahul', 90), ('Priya', 95)]
```

## 5.3 Combine Three Lists

```python
names = ["Amit", "Rahul", "Priya"]

marks = [85, 90, 95]

subjects = ["Python", "Java", "SQL"]

result = zip(names, marks, subjects)

print(list(result))
```

Output:

```text
[
    ('Amit', 85, 'Python'),
    ('Rahul', 90, 'Java'),
    ('Priya', 95, 'SQL')
]
```

## 5.4 Using zip() with a for Loop

```python
names = ["Amit", "Rahul", "Priya"]

marks = [85, 90, 95]

for name, mark in zip(names, marks):

    print(name, mark)
```

Output:

```text
Amit 85
Rahul 90
Priya 95
```

## 5.5 Create a Dictionary Using zip()

```python
keys = ["name", "age", "city"]

values = ["Pankaj", 30, "Mumbai"]

student = dict(zip(keys, values))

print(student)
```

Output:

```text
{'name': 'Pankaj', 'age': 30, 'city': 'Mumbai'}
```

## 5.6 zip() with Different Lengths

By default, zip() stops when the shortest iterable is exhausted.

```python
names = ["Amit", "Rahul", "Priya", "Sneha"]

marks = [85, 90, 95]

result = zip(names, marks)

print(list(result))
```

Output:

```text
[
    ('Amit', 85),
    ('Rahul', 90),
    ('Priya', 95)
]
```

## 5.7 zip_longest()

To include all elements, use zip_longest() from itertools.

```python
from itertools import zip_longest

names = ["Amit", "Rahul", "Priya", "Sneha"]

marks = [85, 90, 95]

result = zip_longest(
    names,
    marks,
    fillvalue="Not Available"
)

print(list(result))
```

Output:

```text
[
    ('Amit', 85),
    ('Rahul', 90),
    ('Priya', 95),
    ('Sneha', 'Not Available')
]
```

### Use Cases of zip()

- Combining student names and marks.
- Combining employee names and salaries.
- Creating dictionaries.
- Combining product names and prices.
- Combining multiple datasets.

---

# 6. enumerate() Function

## 6.1 What is enumerate()?

The enumerate() function adds a counter to an iterable.

It returns index-element pairs.

### Syntax

```python
enumerate(iterable, start=0)
```

| Parameter | Description |
|---|---|
| iterable | List, tuple, string, etc. |
| start | Starting index, default 0 |

## 6.2 Without Using enumerate()

```python
students = ["Amit", "Rahul", "Priya", "Sneha"]

count = 0

for student in students:

    print(count, student)

    count += 1
```

Output:

```text
0 Amit
1 Rahul
2 Priya
3 Sneha
```

## 6.3 Using enumerate()

```python
students = ["Amit", "Rahul", "Priya", "Sneha"]

result = enumerate(students)

print(list(result))
```

Output:

```text
[
    (0, 'Amit'),
    (1, 'Rahul'),
    (2, 'Priya'),
    (3, 'Sneha')
]
```

## 6.4 enumerate() with a for Loop

```python
students = ["Amit", "Rahul", "Priya", "Sneha"]

for index, student in enumerate(students):

    print(index, student)
```

## 6.5 Change the Starting Index

```python
students = ["Amit", "Rahul", "Priya", "Sneha"]

for index, student in enumerate(students, start=1):

    print(index, student)
```

Output:

```text
1 Amit
2 Rahul
3 Priya
4 Sneha
```

## 6.6 enumerate() with Strings

```python
name = "Python"

for index, char in enumerate(name):

    print(index, char)
```

Output:

```text
0 P
1 y
2 t
3 h
4 o
5 n
```

## 6.7 enumerate() with Dictionary Records

```python
employees = [
    {"name": "Amit", "salary": 30000},
    {"name": "Rahul", "salary": 45000},
    {"name": "Priya", "salary": 55000}
]

for sr_no, employee in enumerate(employees, start=1):

    print(
        sr_no,
        employee["name"],
        employee["salary"]
    )
```

Output:

```text
1 Amit 30000
2 Rahul 45000
3 Priya 55000
```

### Use Cases of enumerate()

- Generating serial numbers.
- Displaying student lists.
- Processing employee records.
- Generating numbered reports.
- Tracking iterable elements.

---

# 7. Process Data Using map() and filter()

## 7.1 What is Data Processing?

Data processing is the process of transforming, filtering, organizing, and analyzing raw data to obtain meaningful information.

Python provides map() and filter() to simplify data processing.

## Business Scenario: Student Result Management System

An educational institute wants to process student records.

Requirements:

1. Store student records.
2. Extract student marks.
3. Filter students who passed.
4. Add bonus marks.
5. Calculate grades.
6. Generate a final result report.

## Step 1: Create Student Dataset

```python
students = [
    {"name": "Amit", "marks": 85},
    {"name": "Rahul", "marks": 35},
    {"name": "Priya", "marks": 92},
    {"name": "Sneha", "marks": 45},
    {"name": "Vikas", "marks": 28},
    {"name": "Neha", "marks": 75}
]

print(students)
```

## Step 2: Extract Student Marks Using map()

```python
marks = map(
    lambda student: student["marks"],
    students
)

print(list(marks))
```

Output:

```text
[85, 35, 92, 45, 28, 75]
```

## Step 3: Filter Passed Students

Passing marks are 40.

```python
passed_students = filter(
    lambda student: student["marks"] >= 40,
    students
)

print(list(passed_students))
```

Output:

```text
[
    {'name': 'Amit', 'marks': 85},
    {'name': 'Priya', 'marks': 92},
    {'name': 'Sneha', 'marks': 45},
    {'name': 'Neha', 'marks': 75}
]
```

## Step 4: Add Bonus Marks Using map()

```python
passed_students = list(
    filter(
        lambda student: student["marks"] >= 40,
        students
    )
)

updated_students = map(
    lambda student: {
        "name": student["name"],
        "marks": student["marks"],
        "bonus_marks": student["marks"] + 5
    },
    passed_students
)

print(list(updated_students))
```

## Step 5: Calculate Grades

Grade criteria:

| Marks | Grade |
|---|---|
| 90 and above | A+ |
| 80–89 | A |
| 70–79 | B |
| 60–69 | C |
| 40–59 | D |
| Below 40 | Fail |

```python
def calculate_grade(marks):

    if marks >= 90:
        return "A+"

    elif marks >= 80:
        return "A"

    elif marks >= 70:
        return "B"

    elif marks >= 60:
        return "C"

    elif marks >= 40:
        return "D"

    else:
        return "Fail"
```

## Step 6: Complete Data Processing Program

```python
students = [
    {"name": "Amit", "marks": 85},
    {"name": "Rahul", "marks": 35},
    {"name": "Priya", "marks": 92},
    {"name": "Sneha", "marks": 45},
    {"name": "Vikas", "marks": 28},
    {"name": "Neha", "marks": 75}
]


# Function to calculate grade
def calculate_grade(marks):

    if marks >= 90:
        return "A+"

    elif marks >= 80:
        return "A"

    elif marks >= 70:
        return "B"

    elif marks >= 60:
        return "C"

    elif marks >= 40:
        return "D"

    else:
        return "Fail"


# Step 1: Filter passed students
passed_students = filter(
    lambda student: student["marks"] >= 40,
    students
)


# Step 2: Add bonus marks
updated_students = map(
    lambda student: {
        "name": student["name"],
        "original_marks": student["marks"],
        "final_marks": student["marks"] + 5
    },
    passed_students
)


# Step 3: Calculate grades
final_result = map(
    lambda student: {
        **student,
        "grade": calculate_grade(student["final_marks"])
    },
    updated_students
)


# Step 4: Display final report
print("STUDENT RESULT REPORT")
print("-" * 65)

for index, student in enumerate(final_result, start=1):

    print(
        index,
        student["name"],
        student["original_marks"],
        student["final_marks"],
        student["grade"]
    )
```

Output:

```text
STUDENT RESULT REPORT
-----------------------------------------------------------------
1 Amit 85 90 A+
2 Priya 92 97 A+
3 Sneha 45 50 D
4 Neha 75 80 A
```

### Understanding the Data Processing Pipeline

```text
Original Student Dataset
          |
          v
       filter()
          |
          v
   Passed Students
          |
          v
        map()
          |
          v
     Add Bonus Marks
          |
          v
        map()
          |
          v
    Calculate Grades
          |
          v
     enumerate()
          |
          v
     Final Report
```

---

# 8. Real-World Practical Examples

## Practical 1: Employee Salary Processing

Business Requirement:

- Increase salary by 15%.
- Filter employees with salaries above ₹40,000.
- Display updated salary details.

```python
employees = [
    {"name": "Amit", "salary": 25000},
    {"name": "Rahul", "salary": 35000},
    {"name": "Priya", "salary": 45000},
    {"name": "Sneha", "salary": 55000},
    {"name": "Vikas", "salary": 30000}
]


# Increase salary by 15%
updated_employees = map(
    lambda emp: {
        "name": emp["name"],
        "salary": emp["salary"] * 1.15
    },
    employees
)


# Filter employees
filtered_employees = filter(
    lambda emp: emp["salary"] > 40000,
    updated_employees
)


# Display result
for emp in filtered_employees:

    print(emp)
```

## Practical 2: Product Price Management

```python
products = [
    ("Laptop", 50000),
    ("Mouse", 500),
    ("Keyboard", 1500),
    ("Monitor", 12000),
    ("USB Cable", 200)
]


# Increase prices by 10%
updated_products = map(
    lambda p: (p[0], p[1] * 1.10),
    products
)


# Filter products above 1000
filtered_products = filter(
    lambda p: p[1] > 1000,
    updated_products
)


# Display report
for product, price in filtered_products:

    print(
        f"Product: {product}, Updated Price: ₹{price:.2f}"
    )
```

## Practical 3: Sales Data Analysis

```python
sales = [2000, 4500, 6000, 8000, 3000, 10000, 12000]


# Increase sales by 10%
updated_sales = map(
    lambda x: x * 1.10,
    sales
)


# Filter sales above 5000
filtered_sales = filter(
    lambda x: x > 5000,
    updated_sales
)


# Display report
for index, amount in enumerate(filtered_sales, start=1):

    print(f"Sale {index}: ₹{amount:.2f}")
```

---

# 9. Understanding Python Iterators

## 9.1 What is an Iterator?

An iterator is an object that allows us to access elements one at a time.

The map(), filter(), zip(), and enumerate() functions return iterators.

Example:

```python
numbers = [1, 2, 3, 4, 5]

result = map(lambda x: x * 2, numbers)

print(result)
```

Output:

```text
<map object at 0x...>
```

To display the actual values:

```python
print(list(result))
```

Output:

```text
[2, 4, 6, 8, 10]
```

## 9.2 Iterator Exhaustion

Once an iterator is consumed, it cannot be reused to retrieve the same elements.

```python
numbers = [1, 2, 3, 4]

result = map(lambda x: x * 2, numbers)

print(list(result))

print(list(result))
```

Output:

```text
[2, 4, 6, 8]

[]
```

The second output is empty because the iterator has already been consumed.

---

# 10. map() vs filter() vs List Comprehension

### Using map()

```python
numbers = [1, 2, 3, 4, 5]

result = list(map(lambda x: x * 2, numbers))

print(result)
```

### Using List Comprehension

```python
numbers = [1, 2, 3, 4, 5]

result = [x * 2 for x in numbers]

print(result)
```

Both produce:

```text
[2, 4, 6, 8, 10]
```

### Comparison

| Feature | map() | filter() | List Comprehension |
|---|---|---|---|
| Main purpose | Transform data | Filter data | Transform/filter data |
| Returns | Iterator | Iterator | List |
| Lambda support | Yes | Yes | Optional |
| Condition support | Possible in function | Yes | Yes |
| Best use | Applying a function | Selecting records | Readable transformations |

---

# 11. Common Mistakes

### Mistake 1: Forgetting list()

```python
numbers = [1, 2, 3]

result = map(lambda x: x * 2, numbers)

print(result)
```

This displays a map object, not the actual values.

Correct:

```python
print(list(result))
```

### Mistake 2: Using Assignment Instead of Comparison

Incorrect:

```python
filter(lambda x: x = 10, numbers)
```

Correct:

```python
filter(lambda x: x == 10, numbers)
```

### Mistake 3: Reusing an Exhausted Iterator

Create a new iterator or store the results in a list before reusing the data.

### Mistake 4: Using map() When filter() Is Required

Use map() to transform values and filter() to select values.

### Mistake 5: Different Lengths in zip()

Remember that zip() stops at the shortest iterable unless you use zip_longest().

---

# 12. Practice Exercises

## Exercise 1: Lambda Function

1. Create a lambda function to calculate the square of a number.
2. Create a lambda function to calculate the cube of a number.
3. Create a lambda function to add two numbers.
4. Check whether a number is even or odd.
5. Find the maximum of two numbers.
6. Convert a string into uppercase.
7. Calculate the length of a string.

## Exercise 2: map() Function

Given:

```python
numbers = [10, 20, 30, 40, 50]
```

Perform:

1. Multiply every number by 2.
2. Calculate the square of every number.
3. Convert every number into a string.
4. Add 100 to every number.
5. Calculate 18% GST on each price.
6. Convert Celsius into Fahrenheit.

## Exercise 3: filter() Function

Given:

```python
numbers = [12, 15, 20, 25, 30, 35, 40, 45, 50]
```

Perform:

1. Extract even numbers.
2. Extract odd numbers.
3. Extract numbers greater than 25.
4. Extract numbers divisible by 5.
5. Extract numbers between 20 and 40.

## Exercise 4: zip() Function

Create:

```python
names = ["Amit", "Rahul", "Priya", "Sneha"]

marks = [85, 90, 75, 95]

subjects = ["Python", "Java", "SQL", "MongoDB"]
```

Perform:

1. Combine names and marks.
2. Combine all three lists.
3. Create a dictionary using names and marks.
4. Display each student's name and subject.
5. Handle lists with different lengths.

## Exercise 5: enumerate() Function

Given:

```python
courses = [
    "Python",
    "Java",
    "Machine Learning",
    "Data Science",
    "SQL"
]
```

Perform:

1. Display courses with indexes.
2. Start indexing from 1.
3. Display courses at even indexes.
4. Generate a numbered course list.

## Exercise 6: Combined Data Processing

Create a student management program that:

1. Stores 10 student records.
2. Extracts marks using map().
3. Filters students who scored at least 50.
4. Adds 5 bonus marks using map().
5. Calculates grades.
6. Displays the report using enumerate().
7. Combines student names and grades using zip().

---

# 13. Exercise Solutions

## Solution 1: Lambda

```python
square = lambda x: x ** 2

cube = lambda x: x ** 3

add = lambda a, b: a + b

check = lambda x: "Even" if x % 2 == 0 else "Odd"

maximum = lambda a, b: a if a > b else b

uppercase = lambda name: name.upper()

length = lambda name: len(name)


print(square(5))
print(cube(3))
print(add(10, 20))
print(check(10))
print(maximum(10, 20))
print(uppercase("python"))
print(length("Pankaj"))
```

## Solution 2: map()

```python
numbers = [10, 20, 30, 40, 50]

# Multiply by 2
print(list(map(lambda x: x * 2, numbers)))

# Square
print(list(map(lambda x: x ** 2, numbers)))

# Convert to string
print(list(map(str, numbers)))

# Add 100
print(list(map(lambda x: x + 100, numbers)))

# GST calculation
print(list(map(lambda x: x * 0.18, numbers)))
```

## Solution 3: filter()

```python
numbers = [12, 15, 20, 25, 30, 35, 40, 45, 50]

# Even numbers
print(list(filter(lambda x: x % 2 == 0, numbers)))

# Odd numbers
print(list(filter(lambda x: x % 2 != 0, numbers)))

# Greater than 25
print(list(filter(lambda x: x > 25, numbers)))

# Divisible by 5
print(list(filter(lambda x: x % 5 == 0, numbers)))

# Between 20 and 40
print(list(filter(lambda x: 20 <= x <= 40, numbers)))
```

## Solution 4: zip()

```python
names = ["Amit", "Rahul", "Priya", "Sneha"]

marks = [85, 90, 75, 95]

subjects = ["Python", "Java", "SQL", "MongoDB"]

# Combine names and marks
print(list(zip(names, marks)))

# Combine three lists
print(list(zip(names, marks, subjects)))

# Dictionary
print(dict(zip(names, marks)))

# Display student and subject
for name, subject in zip(names, subjects):
    print(name, subject)
```

## Solution 5: enumerate()

```python
courses = [
    "Python",
    "Java",
    "Machine Learning",
    "Data Science",
    "SQL"
]

# Start from 0
for index, course in enumerate(courses):
    print(index, course)

# Start from 1
for index, course in enumerate(courses, start=1):
    print(index, course)

# Even indexes
for index, course in enumerate(courses):
    if index % 2 == 0:
        print(course)
```

---

# 14. Mini Projects

## Project 1: Student Performance Management System

Requirements:

- Store student names and marks.
- Filter passed students.
- Calculate grades.
- Add bonus marks.
- Generate a final result report.

Concepts:

- Lambda
- map()
- filter()
- enumerate()
- zip()

## Project 2: Employee Salary Management System

Requirements:

- Store employee names and salaries.
- Increase salary by 10%.
- Filter employees earning above ₹40,000.
- Sort employees by salary.
- Generate an employee report.

Concepts:

- Lambda
- map()
- filter()
- zip()
- enumerate()

## Project 3: E-Commerce Product Management

Requirements:

- Store product names and prices.
- Calculate GST.
- Apply discounts.
- Filter products based on price.
- Generate a product report.

Concepts:

- Lambda
- map()
- filter()
- zip()

## Project 4: Sales Analysis System

Requirements:

- Store daily sales.
- Increase sales values by 10%.
- Filter sales above ₹5,000.
- Generate serial numbers.
- Calculate total filtered sales.

Concepts:

- Lambda
- map()
- filter()
- enumerate()

---

# 15. Interview Questions

1. What is a lambda function in Python?
2. What is the difference between lambda and def?
3. What is the purpose of map()?
4. What is the purpose of filter()?
5. What is the difference between map() and filter()?
6. What does zip() do?
7. What is enumerate()?
8. What is the default starting index of enumerate()?
9. Can map() accept multiple iterables?
10. What happens when iterables have different lengths in zip()?
11. What is zip_longest()?
12. What is an iterator?
13. What is lazy evaluation?
14. Can lambda functions contain multiple statements?
15. Can we use lambda with sorted()?
16. What is the difference between map() and list comprehension?
17. Why does map() return an iterator?
18. Can filter() work without a lambda function?
19. What happens when an iterator is exhausted?
20. How can map() and filter() be combined?

---

# 16. Quick Revision

| Topic | Purpose | Example |
|---|---|---|
| Lambda | Anonymous function | `lambda x: x * 2` |
| map() | Transform data | `map(str, numbers)` |
| filter() | Select data | `filter(lambda x: x > 10, numbers)` |
| zip() | Combine iterables | `zip(names, marks)` |
| enumerate() | Generate indexes | `enumerate(names, start=1)` |

## Recommended Learning Order

1. Lambda Function
2. map() Function
3. filter() Function
4. zip() Function
5. enumerate() Function
6. Python Iterators
7. Data Processing Using map() and filter()
8. Real-World Projects

---

# 17. Conclusion

In this tutorial, we learned how to use Python's functional programming features to transform, filter, combine, and process data.

These functions are especially useful in:

- Python Development
- Data Analytics
- Data Science
- Machine Learning
- Automation
- Data Cleaning
- Real-World Business Applications

Practice each example and complete the mini projects to strengthen your Python programming skills.

---

## Author

**Pankaj Chouhan**

Senior IT Trainer | Python Developer | Data Science & Machine Learning Mentor

**Website:** https://www.codeswithpankaj.com

**YouTube:** https://www.youtube.com/@CodesWithPankaj.official

**Instagram:** https://www.instagram.com/codeswithpankaj/

---


**Happy Learning & Keep Coding!**

⭐ Don't forget to Star the Repository!
