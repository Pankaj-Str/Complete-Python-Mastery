# Python Dictionary

Python dictionary is a built-in data type that allows you to store and organize data in key-value pairs. Each key in a dictionary must be unique, and it is used to retrieve the associated value. Dictionaries are highly efficient for quickly looking up values based on their keys.

Here's the basic syntax of a dictionary in Python:

```python
my_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}
```

In this example, `"key1"`, `"key2"`, and `"key3"` are keys, and `"value1"`, `"value2"`, and `"value3"` are their corresponding values.



**1. Creating a Dictionary:**
You can create a dictionary by enclosing comma-separated key-value pairs within curly braces `{}`. The keys and values are separated by a colon `:`.

```python
student = {
    "name": "John",
    "age": 20,
    "grade": "A"
}
```

**2. Accessing Values:**
You can access the values of a dictionary using its keys.

```python
print(student["name"])  # Output: John
print(student["age"])   # Output: 20
```

**3. Modifying and Adding Items:**
Dictionaries are mutable, meaning you can modify, add, or remove items.

```python
student["age"] = 21  # Updating the age
student["city"] = "New York"  # Adding a new key-value pair
```

**4. Checking Key Existence:**
You can use the `in` keyword to check if a key exists in a dictionary.

```python
if "grade" in student:
    print("Grade exists:", student["grade"])
```

**5. Dictionary Methods:**

Python provides several useful methods for working with dictionaries:

- `keys()`: Returns a list of all keys in the dictionary.
- `values()`: Returns a list of all values in the dictionary.
- `items()`: Returns a list of key-value pairs as tuples.
- `get(key, default)`: Returns the value for a key if it exists, else returns a default value.
- `pop(key, default)`: Removes and returns the value associated with the key.

```python
print(student.keys())
print(student.values())
print(student.items())
```
### Example : 

```python
data = {'name': 'joy', 'age': 6, 'height': 3.4}

# keys(): Returns a list of all keys in the dictionary.
print(data.keys())    # dict_keys(['name', 'age', 'height'])

# values(): Returns a list of all values in the dictionary.
print(data.values()) # dict_values(['joy', 6, 3.4])

# items(): Returns a list of key-value pairs as tuples.
print(data.items()) # dict_items([('name', 'joy'), ('age', 6), ('height', 3.4)])

# get(key, default): Returns the value for a key if it exists, else returns a default value.
print(data.get('age')) # 6

# pop(key, default): Removes and returns the value associated with the key.
print('before pop() ',data) # before pop()  {'name': 'joy', 'age': 6, 'height': 3.4}
print(data.pop('age')) # 6
print('After pop() ',data) # After pop()  {'name': 'joy', 'height': 3.4}

```

**6. Dictionary Comprehension:**
Similar to list comprehensions, you can use dictionary comprehensions to create dictionaries in a concise manner.

```python
squared_numbers = {x: x ** 2 for x in range(1, 6)}
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

**7. Nested Dictionaries:**
You can have dictionaries within dictionaries to represent more complex data structures.

```python
employees = {
    "employee1": {
        "name": "Alice",
        "age": 30
    },
    "employee2": {
        "name": "Bob",
        "age": 25
    }
}

print(employees['employee2']['name']) # output Bob

```

**8. Dictionary Ordering (Python 3.7+):**
Starting from Python 3.7, dictionaries are guaranteed to maintain the insertion order. This means the order in which items are added is preserved.

**9. Hashable Keys:**
Dictionary keys must be hashable, which essentially means they should be immutable (like strings, numbers, and tuples). Lists and dictionaries cannot be used as dictionary keys because they are mutable.

Dictionaries are incredibly useful for a variety of tasks, such as counting occurrences, creating mappings, storing configurations, and handling complex data structures. They provide fast lookups and are a fundamental part of Python's data structures.

## Methods of dictionaries in Python, along with examples to demonstrate their usage:


**1. `keys()` method:**

This method returns a view of all the keys in the dictionary.

```python
student = {
    "name": "John",
    "age": 20,
    "grade": "A"
}

key_list = student.keys()
print(key_list)  # Output: dict_keys(['name', 'age', 'grade'])
```

**2. `values()` method:**

This method returns a view of all the values in the dictionary.

```python
value_list = student.values()
print(value_list)  # Output: dict_values(['John', 20, 'A'])
```

**3. `items()` method:**

This method returns a view of all the key-value pairs in the dictionary as tuples.

```python
item_list = student.items()
print(item_list)  # Output: dict_items([('name', 'John'), ('age', 20), ('grade', 'A')])
```

**4. `get(key, default)` method:**

This method returns the value for a given key. If the key does not exist, it returns a default value.

```python
age = student.get("age", 0)  # Returns 20
city = student.get("city", "Unknown")  # Returns "Unknown"
```

**5. `pop(key, default)` method:**

This method removes and returns the value associated with the given key. If the key does not exist, it returns a default value.

```python
removed_grade = student.pop("grade", "N/A")  # Removes "grade" and returns "A"
removed_city = student.pop("city", "N/A")    # Returns "N/A" since "city" doesn't exist
```

**6. Dictionary Comprehension:**

You can use dictionary comprehension to create dictionaries in a concise way.

```python
squared_numbers = {x: x ** 2 for x in range(1, 6)}
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

**7. Iterating Through Keys and Values:**

You can use a `for` loop to iterate through the keys and values of a dictionary using the `items()` method.

```python
for key, value in student.items():
    print(f"{key}: {value}")
# Output:
# name: John
# age: 20
# grade: A
```

### Example :

```python
Data = {
        "Name": "Hanuman Road",
        "Description": "null",
        "BranchType": "Sub Post Office",
        "DeliveryStatus": "Non-Delivery",
        "Circle": "Maharashtra",
        "District": "Mumbai",
        "Division": "Mumbai  North",
        "Region": "Mumbai",
        "Block": "Mumbai",
        "State": "Maharashtra",
        "Country": "India",
        "Pincode": "400057"
      }

for i in Data:
    print(i , '= ', Data[i])

```

