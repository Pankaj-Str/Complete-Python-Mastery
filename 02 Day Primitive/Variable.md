**What are Python Variables?**  

A **variable** is like a **labeled box** or **container** that holds a value (a piece of information) so you can use it later in your program.

You put something in the box → give the box a name → and whenever you need that thing again, you just use the box's name.

### Real-life analogy:
Imagine you have a small box:
- You write "age" on the box (this is the variable name)
- You put the number 20 inside the box (this is the value)

Now whenever you want to know the age, you just look at the box named "age" — no need to remember 20 every time.

In Python, it's exactly the same!

### How to create a variable (very easy):

You just write:
```python
name = "Amit"      # box named "name" now holds "Amit"
age = 20           # box named "age" holds 20
marks = 85.5       # box named "marks" holds 85.5
is_student = True  # box named "is_student" holds True (yes/no value)
```

The moment you write `name = "Amit"`, Python creates the variable automatically — no special "declare" word needed!

### Important points about variables:

1. **Variable name = identifier**  
   (We already learned identifiers — same rules apply:  
   - letters, numbers, underscore  
   - cannot start with number  
   - no spaces  
   - no keywords like if, for, True, etc.)

2. **= sign means "put this value into the box"**  
   Not equal like in math — it's assignment.

3. **You can change what's inside the box anytime**  
   (That's why it's called "variable" — it can vary/change)

```python
age = 20
print(age)     # prints 20

age = 21       # now change the value inside the same box
print(age)     # prints 21
```

4. **Variables can hold different kinds of values** (called data types — we'll learn more later):

| Type of value     | Example                     | What it stores          |
|-------------------|-----------------------------|--------------------------|
| Text (string)     | name = "Priya"             | Words, names, sentences |
| Whole number      | age = 18                   | Counting numbers        |
| Decimal number    | price = 99.99              | Money, measurements     |
| True/False        | is_adult = True            | Yes/No answers          |
| List of things    | fruits = ["apple", "banana"] | Multiple items         |

5. **Variables make your code easy to read and reuse**

Bad (hard to understand):
```python
print("Hello my name is Amit and I am 20 years old")
```

Good (using variables):
```python
name = "Amit"
age = 20
print("Hello my name is", name, "and I am", age, "years old")
```

Now if you want to change the name or age later — you change it only in one place!

### Quick summary in one line:
Variable = a named box/container in Python that stores a value (number, text, True/False, etc.) so you can use and change it easily in your program.

### Common beginner mistakes to avoid:
- Forgetting quotes for text:  
  Wrong: city = Mumbai  
  Correct: city = "Mumbai"

- Using space in name:  
  Wrong: student name = "Riya"  
  Correct: student_name = "Riya"

- Starting with number:  
  Wrong: 1st_place = "Gold"  
  Correct: first_place = "Gold"

Got it?  
Variables are one of the very first things you use in every Python program — they are super important!
