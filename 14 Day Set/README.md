# Python Sets


### What We Cover in This Tutorial
We will go through **everything** you need to know about Python sets, from zero to hero. Here’s the complete list:

- What is a Set and why it is useful  
- How to create a Set  
- Important properties of Sets  
- Adding elements to a Set  
- Removing elements from a Set  
- Checking if an item exists  
- Looping through a Set  
- All built-in Set methods (with examples)  
- Mathematical Set Operations (Union, Intersection, Difference, etc.)  
- Set Comprehensions (a shortcut way to create sets)  
- Frozen Sets (the “read-only” version of sets)  
- Real-world examples and common mistakes  
- Practice exercises with solutions  

---

### Table of Contents
1. [What is a Python Set?](#1-what-is-a-python-set)  
2. [Creating a Set](#2-creating-a-set)  
3. [Properties of a Set](#3-properties-of-a-set)  
4. [Adding Elements to a Set](#4-adding-elements-to-a-set)  
5. [Removing Elements from a Set](#5-removing-elements-from-a-set)  
6. [Checking Membership (Is an item in the set?)](#6-checking-membership)  
7. [Iterating (Looping) Through a Set](#7-iterating-through-a-set)  
8. [Built-in Set Methods](#8-built-in-set-methods)  
9. [Set Operations (Mathematics)](#9-set-operations-mathematics)  
10. [Set Comprehensions](#10-set-comprehensions)  
11. [Frozen Sets](#11-frozen-sets)  
12. [Real-World Examples](#12-real-world-examples)  
13. [Common Mistakes & Tips](#13-common-mistakes--tips)  
14. [Practice Exercises](#14-practice-exercises)  

---

### 1. What is a Python Set?

A **Set** in Python is a collection of items where:
- Every item is **unique** (no duplicates allowed)
- The order of items **does not matter** (unordered)
- You can add or remove items later (it is mutable)

**Real-life analogy**:  
Think of a set like a **bag of marbles** where:
- You cannot put two identical marbles (duplicates are automatically removed)
- You don’t care which marble comes out first
- You can add or remove marbles anytime

**Why use Sets?**  
- Automatically remove duplicates  
- Very fast to check if something exists (much faster than lists)  
- Perfect for finding common or different items between groups

---

### 2. Creating a Set

There are two easy ways to create a set:

#### Method 1: Using curly braces `{}`
```python
# Creating a set of fruits
fruits = {"apple", "banana", "cherry"}
print(fruits)
```

#### Method 2: Using the `set()` function
```python
numbers = set([1, 2, 3, 4])          # from a list
letters = set("hello")               # from a string
empty_set = set()                    # empty set (IMPORTANT: {} creates a dictionary!)
```

**Output example**:
```
{'apple', 'banana', 'cherry'}
```

**Pro Tip**:  
`{}` creates an **empty dictionary**, not a set. Always use `set()` for an empty set.

---

### 3. Properties of a Set

| Property              | Description                                      | Example |
|-----------------------|--------------------------------------------------|---------|
| Unordered             | No guaranteed order                              | Items can print in any order |
| Unique elements       | Duplicates are automatically removed             | `{"a", "a", "b"}` → `{"a", "b"}` |
| Mutable               | You can add/remove items after creation          | Yes |
| Elements must be immutable | Only numbers, strings, tuples allowed (not lists) | `{"apple", 42, (1,2)}` works |
| Cannot be indexed     | No `set[0]` because order doesn’t exist         | Error if you try |

---

### 4. Adding Elements to a Set

#### `add()` – Add **one** item
```python
colors = {"red", "blue"}
colors.add("green")
print(colors)        # {'red', 'blue', 'green'}
```

#### `update()` – Add **multiple** items (from list, tuple, or another set)
```python
colors.update(["yellow", "purple", "red"])   # "red" already exists → ignored
print(colors)
```

---

### 5. Removing Elements from a Set

| Method      | What it does                              | Error if item not found? |
|-------------|-------------------------------------------|--------------------------|
| `remove()`  | Removes item                              | Yes (raises error)      |
| `discard()` | Removes item (safer)                      | No                      |
| `pop()`     | Removes and returns **one random** item   | No (works on empty too) |
| `clear()`   | Removes **all** items                     | No                      |

**Examples**:
```python
fruits = {"apple", "banana", "cherry"}

fruits.remove("banana")      # works
# fruits.remove("mango")     # ← would give KeyError!

fruits.discard("mango")      # safe, does nothing

item = fruits.pop()          # removes one random item
print("Removed:", item)

fruits.clear()               # now empty
```

---

### 6. Checking Membership (Is an item in the set?)

Use the `in` keyword — super fast!
```python
fruits = {"apple", "banana", "cherry"}

print("apple" in fruits)     # True
print("mango" in fruits)     # False
```

---

### 7. Iterating (Looping) Through a Set

```python
fruits = {"apple", "banana", "cherry"}

for fruit in fruits:
    print(fruit)
```

**Note**: Order may be different every time you run it — that’s normal for sets!

---

### 8. Built-in Set Methods

Here’s a quick reference table of **all** important set methods:

| Method              | Description                              | Example |
|---------------------|------------------------------------------|---------|
| `add()`             | Add one item                             | `s.add(5)` |
| `update()`          | Add multiple items                       | `s.update([6,7])` |
| `remove()`          | Remove item (error if missing)           | `s.remove(5)` |
| `discard()`         | Remove item (no error)                   | `s.discard(99)` |
| `pop()`             | Remove & return random item              | `x = s.pop()` |
| `clear()`           | Remove all items                         | `s.clear()` |
| `copy()`            | Make a copy                              | `new = s.copy()` |
| `len()`             | Count items                              | `len(s)` |

---

### 9. Set Operations (Mathematics)

Sets shine when you combine them! Here are the 4 most useful operations:

| Operation              | Symbol | Method                | Meaning                          | Example Result |
|------------------------|--------|-----------------------|----------------------------------|----------------|
| Union (combine)        | `\|`   | `union()`             | All items from both sets         | A ∪ B |
| Intersection           | `&`    | `intersection()`      | Common items only                | A ∩ B |
| Difference             | `-`    | `difference()`        | Items in A but not in B          | A – B |
| Symmetric Difference   | `^`    | `symmetric_difference()` | Items in either but not both  | A △ B |

**Code Example**:
```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B)      # Union: {1,2,3,4,5,6}
print(A & B)      # Intersection: {3,4}
print(A - B)      # Difference: {1,2}
print(A ^ B)      # Symmetric difference: {1,2,5,6}
```

You can also use the full method names:
```python
print(A.union(B))
print(A.intersection(B))
```
---
### Union 

<img width="2816" height="1536" alt="Gemini_Generated_Image_tdx47ztdx47ztdx4" src="https://github.com/user-attachments/assets/68150e14-bbaf-4234-937e-0237522abdcb" />

---
### Intersection

<img width="2816" height="1536" alt="Gemini_Generated_Image_u4mp1ju4mp1ju4mp" src="https://github.com/user-attachments/assets/e6392df1-9c41-473a-9114-0979c416e9a8" />

---

### Difference

<img width="2816" height="1536" alt="Gemini_Generated_Image_tzgjfftzgjfftzgj" src="https://github.com/user-attachments/assets/63198460-3efd-45a8-9c70-bedf652fa6df" />

---

### Symmetric difference

<img width="2816" height="1536" alt="Gemini_Generated_Image_tzgjfftzgjfftzgj" src="https://github.com/user-attachments/assets/e6a7db4a-ee14-41fb-b7d2-6aa85e260869" />


---

### 10. Set Comprehensions

A short and beautiful way to create sets (just like list comprehensions):

```python
# Create a set of squares
squares = {x**2 for x in range(1, 6)}
print(squares)          # {1, 4, 9, 16, 25}

# Set of even numbers from a list
numbers = [1, 2, 3, 4, 5, 6]
evens = {x for x in numbers if x % 2 == 0}
print(evens)            # {2, 4, 6}
```

---

### 11. Frozen Sets

A **frozen set** is like a set that cannot be changed (immutable).

```python
frozen = frozenset(["apple", "banana"])
# frozen.add("cherry")   ← This will give an error!
```

**When to use?**  
When you want to use a set as a **key** in a dictionary or inside another set.

---

### 12. Real-World Examples

**Example 1: Remove duplicates from a list**
```python
names = ["Alice", "Bob", "Alice", "Charlie"]
unique_names = set(names)
print(unique_names)      # {'Alice', 'Bob', 'Charlie'}
```

**Example 2: Find common friends**
```python
my_friends = {"Alice", "Bob", "David"}
your_friends = {"Bob", "Charlie", "David"}

common = my_friends & your_friends
print("Common friends:", common)
```

---

### 13. Common Mistakes & Tips

- **Mistake**: Trying `set[0]` → Sets have no index!
- **Tip**: Use `set()` for empty set, not `{}`
- **Tip**: Sets are fastest for membership testing (`in`)
- **Tip**: You cannot put a list or another set inside a set (they are mutable)

---

### 14. Practice Exercises

**Exercise 1**: Create a set of your favorite movies. Add 2 more, then remove one.

**Exercise 2**: Given two sets `A = {10, 20, 30, 40}` and `B = {30, 40, 50, 60}`, print:
- Union
- Intersection
- Items only in A

**Exercise 3**: Write a set comprehension to create a set of all odd numbers from 1 to 20.

**Solutions** (try first, then check):

```python
# Exercise 2 solution
A = {10, 20, 30, 40}
B = {30, 40, 50, 60}
print(A | B)
print(A & B)
print(A - B)

# Exercise 3 solution
odds = {x for x in range(1, 21) if x % 2 == 1}
print(odds)
```

---
