# Python JSON

## Python JSON

Welcome to [codeswithpankaj.com](https://codeswithpankaj.com)! In this tutorial, we will explore how to work with JSON in Python using the `json` module. We'll cover how to encode and decode JSON, and provide detailed examples to illustrate their application.

### Table of Contents

1. Introduction to JSON
2. Why Use JSON?
3. The `json` Module
4. Encoding JSON
5. Decoding JSON
6. Working with JSON Files
7. Customizing JSON Encoding and Decoding
8. Practical Examples
9. Summary

### 1. Introduction to JSON

#### What is JSON?

JSON (JavaScript Object Notation) is a lightweight data-interchange format that is easy for humans to read and write and easy for machines to parse and generate. JSON is built on two structures:

* A collection of name/value pairs (often referred to as an object, dictionary, hash table, etc.).
* An ordered list of values (often referred to as an array, list, vector, etc.).

#### Key Points

* JSON is language-independent but uses conventions familiar to programmers of the C-family of languages.
* JSON is often used to transmit data between a server and web application as text.

### 2. Why Use JSON?

* **Interoperability:** JSON is a widely accepted format for data exchange between different systems and programming languages.
* **Simplicity:** JSON is easy to read and write for both humans and machines.
* **Flexibility:** JSON supports complex data structures like nested objects and arrays.

### 3. The `json` Module

The `json` module in Python provides functions to encode (serialize) and decode (deserialize) JSON data.

### 4. Encoding JSON

#### Example: Encoding a Python Dictionary to JSON

```python
import json

# Python dictionary
data = {
    "name": "Pankaj",
    "age": 30,
    "city": "New York"
}

# Convert Python dictionary to JSON
json_data = json.dumps(data, indent=4)
print(json_data)
```

#### Example: Encoding a Python List to JSON

```python
import json

# Python list
data = ["apple", "banana", "cherry"]

# Convert Python list to JSON
json_data = json.dumps(data, indent=4)
print(json_data)
```

### 5. Decoding JSON

#### Example: Decoding JSON to a Python Dictionary

```python
import json

# JSON data
json_data = '''
{
    "name": "Pankaj",
    "age": 30,
    "city": "New York"
}
'''

# Convert JSON to Python dictionary
data = json.loads(json_data)
print(data)
```

#### Example: Decoding JSON to a Python List

```python
import json

# JSON data
json_data = '''
[
    "apple",
    "banana",
    "cherry"
]
'''

# Convert JSON to Python list
data = json.loads(json_data)
print(data)
```

### 6. Working with JSON Files

#### Example: Writing JSON to a File

```python
import json

# Python dictionary
data = {
    "name": "Pankaj",
    "age": 30,
    "city": "New York"
}

# Write JSON to a file
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)
```

#### Example: Reading JSON from a File

```python
import json

# Read JSON from a file
with open('data.json', 'r') as file:
    data = json.load(file)

print(data)
```

### 7. Customizing JSON Encoding and Decoding

#### Example: Customizing Encoding with `cls` Parameter

```python
import json

class User:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

def encode_user(obj):
    if isinstance(obj, User):
        return {"name": obj.name, "age": obj.age, "city": obj.city}
    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

user = User("Pankaj", 30, "New York")

# Encode User object to JSON
json_data = json.dumps(user, default=encode_user, indent=4)
print(json_data)
```

#### Example: Customizing Decoding with `object_hook` Parameter

```python
import json

class User:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

def decode_user(dct):
    return User(dct['name'], dct['age'], dct['city'])

json_data = '''
{
    "name": "Pankaj",
    "age": 30,
    "city": "New York"
}
'''

# Decode JSON to User object
user = json.loads(json_data, object_hook=decode_user)
print(user.name, user.age, user.city)
```

### 8. Practical Examples

#### Example 1: Handling Nested JSON

```python
import json

# Nested Python dictionary
data = {
    "name": "Pankaj",
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "state": "NY"
    },
    "phone_numbers": [
        {"type": "home", "number": "212-555-1234"},
        {"type": "work", "number": "646-555-4567"}
    ]
}

# Convert Python dictionary to JSON
json_data = json.dumps(data, indent=4)
print(json_data)
```

#### Example 2: Parsing JSON from a Web API

```python
import json
import requests

# Fetch JSON data from a web API
response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
data = response.json()

# Pretty print the JSON data
print(json.dumps(data, indent=4))
```

#### Example 3: Encoding and Decoding DateTime Objects

```python
import json
from datetime import datetime

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

data = {
    "name": "Pankaj",
    "timestamp": datetime.now()
}

# Encode datetime object to JSON
json_data = json.dumps(data, cls=DateTimeEncoder, indent=4)
print(json_data)

# Decode datetime object from JSON
def decode_datetime(dct):
    for key, value in dct.items():
        try:
            dct[key] = datetime.fromisoformat(value)
        except:
            pass
    return dct

decoded_data = json.loads(json_data, object_hook=decode_datetime)
print(decoded_data)
```

### 9. Summary

In this tutorial, we explored how to work with JSON in Python using the `json` module. We covered encoding and decoding JSON, working with JSON files, customizing JSON encoding and decoding, and provided practical examples to illustrate the application of JSON in Python. The `json` module is a powerful tool for handling JSON data in Python.

For more tutorials and in-depth explanations, visit [codeswithpankaj.com](https://codeswithpankaj.com)!

***

This tutorial provides a comprehensive overview of working with JSON in Python, detailing each topic and subtopic with examples and explanations. For more such tutorials, keep following [codeswithpankaj.com](https://codeswithpankaj.com)!
