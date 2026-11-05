**What is an Identifier in Python?**  

An **identifier** is just a **name** that you give to things in your Python program.

Like in real life we give names to everything:  
- Bottle  
- Chair  
- Phone  
- Rohan  

In the same way, in Python you give names to:  
- Variables  
- Functions  
- Classes  
- And other things  

All these names are called **identifiers**.

### definition:
Identifier = **any name** you create in your code

### Easy examples:

```python
name = "Amit"           # 'name' is an identifier (name of a variable)
age = 20                # 'age' is an identifier
total_marks = 85        # 'total_marks' is an identifier
calculate_sum()         # 'calculate_sum' is an identifier (name of a function)
```

All of these — name, age, total_marks, calculate_sum — are identifiers.

### Rules for making good identifiers (very important):

1. You can only use these characters:
   - Small letters (a-z)
   - Capital letters (A-Z)
   - Numbers (0-9)
   - Underscore (_)

   Nothing else! No @ # $ % & * space etc.

2. First character **cannot** be a number
   - Correct: age, _count, student1, total2
   - Wrong: 1student, 2marks

3. No spaces allowed
   - Correct: my_name
   - Wrong: my name

4. You cannot use Python's special words (called keywords)
   - Examples of keywords: if, for, while, class, def, True, False, return, etc.
   - Wrong: if = 10, def = "hello"

5. Python is **case-sensitive** (big and small letters are different)
   - age  
   - Age  
   - AGE  
   → These are **three different** identifiers

### Quick table – Good vs Bad examples

| Good (Valid) Identifiers   | Bad (Invalid) Identifiers   | Why wrong?              |
|----------------------------|-----------------------------|--------------------------|
| name                       | 1name                       | starts with number      |
| student_age                | student age                 | has space               |
| _hidden                    | @price                      | @ is not allowed        |
| total2                     | if                          | 'if' is a keyword       |
| MyScore                    | My-Score                    | - (minus) not allowed   |
| userName                   | user@name                   | @ not allowed           |

### Best tips for beginners:
- Keep names short and clear
- Join words with underscore → student_name, total_price
- Use small letters mostly (this is the most common style)

