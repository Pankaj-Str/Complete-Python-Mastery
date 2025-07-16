

### **Operators in Python**

#### **Step 1: What Are Operators?**
Think of operators as buttons on a calculator or words that tell Python what to do with numbers, words, or other data. For example, the `+` sign adds two numbers, and `==` checks if two things are the same. Python has different kinds of operators, and we’ll go through the most important ones step by step.

---

#### **Step 2: Arithmetic Operators (Math Tools)**
These operators are like the math you already know: adding, subtracting, multiplying, and more.

| Operator | What It Does | Example |
|----------|--------------|---------|
| `+`      | Adds numbers | `2 + 3 = 5` |
| `-`      | Subtracts numbers | `5 - 2 = 3` |
| `*`      | Multiplies numbers | `4 * 3 = 12` |
| `/`      | Divides numbers (gives a decimal) | `10 / 2 = 5.0` |
| `//`     | Divides and gives a whole number | `10 // 3 = 3` |
| `%`      | Gives the remainder after division | `10 % 3 = 1` |
| `**`     | Raises a number to a power | `2 ** 3 = 8` (2 × 2 × 2) |

**Example Code:**
```python
a = 10
b = 3
print(a + b)  # Output: 13
print(a - b)  # Output: 7
print(a * b)  # Output: 30
print(a / b)  # Output: 3.333...
print(a % b)  # Output: 1 (remainder when 10 is divided by 3)
print(a ** b) # Output: 1000 (10 × 10 × 10)
```

**Try it yourself:** Open a Python editor (like IDLE or an online tool like Replit) and try adding or multiplying two numbers. For example, change `a` and `b` to different numbers and see what happens.

---

#### **Step 3: Comparison Operators (Checking Things)**
These operators help you compare two values to see if they’re equal, bigger, or smaller. They give you a `True` or `False` answer.

| Operator | What It Does | Example |
|----------|--------------|---------|
| `==`     | Checks if two things are equal | `5 == 5` → `True` |
| `!=`     | Checks if two things are not equal | `5 != 3` → `True` |
| `>`      | Checks if one is bigger | `5 > 3` → `True` |
| `<`      | Checks if one is smaller | `5 < 3` → `False` |
| `>=`     | Checks if one is bigger or equal | `5 >= 5` → `True` |
| `<=`     | Checks if one is smaller or equal | `3 <= 5` → `True` |

**Example Code:**
```python
x = 10
y = 20
print(x == y)  # Output: False (10 is not equal to 20)
print(x < y)   # Output: True (10 is less than 20)
print(x >= y)  # Output: False (10 is not greater than or equal to 20)
```

**Try it yourself:** Try comparing two numbers, like `7 > 4` or `10 == 10`. You can also compare words, like `"cat" == "cat"`.

---

#### **Step 4: Logical Operators (Combining Checks)**
Logical operators let you combine conditions to make decisions. They’re like saying “this AND that” or “this OR that.”

| Operator | What It Does | Example |
|----------|--------------|---------|
| `and`    | True if both things are True | `True and False` → `False` |
| `or`     | True if at least one thing is True | `True or False` → `True` |
| `not`    | Flips True to False (or vice versa) | `not True` → `False` |

**Example Code:**
```python
age = 15
print(age > 10 and age < 20)  # Output: True (both conditions are true)
print(age > 10 or age < 5)    # Output: True (at least one condition is true)
print(not (age > 10))         # Output: False (flips True to False)
```

**Try it yourself:** Think of a number (like your age) and check if it’s between two values using `and`. For example, `age > 5 and age < 18`.

---

#### **Step 5: Assignment Operators (Saving Values)**
These operators help you store or update values in variables. The most common one is `=`, which saves a value.

| Operator | What It Does | Example |
|----------|--------------|---------|
| `=`      | Saves a value | `x = 5` (x becomes 5) |
| `+=`     | Adds and saves | `x += 3` (x becomes x + 3) |
| `-=`     | Subtracts and saves | `x -= 2` (x becomes x - 2) |
| `*=`     | Multiplies and saves | `x *= 2` (x becomes x * 2) |

**Example Code:**
```python
score = 100
score += 10  # Add 10 to score
print(score)  # Output: 110
score -= 5   # Subtract 5 from score
print(score)  # Output: 105
score *= 2   # Double the score
print(score)  # Output: 210
```

**Try it yourself:** Create a variable like `money = 50` and use `+=` to add 20, then `-=` to subtract 10.

---

#### **Step 6: Membership Operators (Checking Lists or Words)**
These operators check if something is inside a list, word, or other collection.

| Operator | What It Does | Example |
|----------|--------------|---------|
| `in`     | Checks if something is inside | `"a" in "cat"` → `True` |
| `not in` | Checks if something is not inside | `"z" not in "cat"` → `True` |

**Example Code:**
```python
fruits = ["apple", "banana", "orange"]
print("apple" in fruits)      # Output: True
print("grape" not in fruits)  # Output: True
word = "hello"
print("h" in word)            # Output: True
```

**Try it yourself:** Make a list of your favorite foods and check if one food is in the list using `in`.

---

#### **Step 7: A Simple Program Using Operators**
Let’s put it all together with a fun example. Imagine you’re buying items at a store, and you get a discount if you spend more than $50.

```python
# Calculate total cost of items
items = [20, 15, 25]  # Prices of items
total = 0
for price in items:
    total += price  # Add each price to total

# Check if total is more than 50 to give a 10% discount
if total > 50:  # Comparison operator
    total *= 0.9  # Multiply by 0.9 to reduce by 10%
    print("You got a discount!")
else:
    print("No discount this time.")

print("Your total is $", total)
```

**Output:**
```
You got a discount!
Your total is $ 54.0
```

**Try it yourself:** Change the item prices or the discount rule (e.g., discount if total > 100) and see how the output changes.

---

#### **Step 8: Tips for Beginners**
- **Start small:** Try one operator at a time, like `+` or `==`, before combining them.
- **Experiment:** Use a Python editor to test code. If you make a mistake, Python will tell you what went wrong.
- **Watch out for types:** You can’t add a number and a word (e.g., `5 + "hello"` will give an error). Make sure both sides of an operator match (like both numbers or both words).
- **Order matters:** Python does multiplication (`*`) before addition (`+`). Use parentheses `()` to control the order. For example, `2 + 3 * 4` is 14, but `(2 + 3) * 4` is 20.

**Example (Order matters):**
```python
print(2 + 3 * 4)    # Output: 14 (3 * 4 = 12, then + 2)
print((2 + 3) * 4)  # Output: 20 (2 + 3 = 5, then * 4)
```

---

#### **Step 9: Practice Ideas**
1. Write a program to check if a number is even (hint: use `% 2 == 0`).
2. Make a list of names and check if your name is in it using `in`.
3. Create a variable for your age and check if you’re old enough to vote (e.g., `age >= 18`).
4. Add two numbers, then double the result using `*=` in one line.

**Example (Check if even):**
```python
number = 6
if number % 2 == 0:
    print("This number is even!")
else:
    print("This number is odd!")
```

---

