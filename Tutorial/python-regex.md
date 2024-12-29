# Python RegEx

## Python RegEx

Welcome to [codeswithpankaj.com](https://codeswithpankaj.com)! In this tutorial, we will explore how to work with regular expressions (RegEx) in Python using the `re` module. We'll cover the basics of RegEx, how to use them in Python, and provide detailed examples to illustrate their application.

### Table of Contents

1. Introduction to Regular Expressions
2. Why Use Regular Expressions?
3. The `re` Module
4. Basic Patterns and Special Characters
5. Functions in the `re` Module
6. Compiling Regular Expressions
7. Practical Examples
8. Summary

### 1. Introduction to Regular Expressions

#### What are Regular Expressions?

Regular expressions (RegEx) are sequences of characters that form search patterns. They are used to match strings of text, such as particular characters, words, or patterns of characters.

#### Key Points

* Regular expressions are powerful tools for searching and manipulating strings.
* They are widely used in text processing, data validation, and data extraction.

### 2. Why Use Regular Expressions?

* **Pattern Matching:** RegEx can match complex string patterns with ease.
* **Text Manipulation:** They can be used to find, replace, and split strings.
* **Data Validation:** RegEx can validate input data such as email addresses, phone numbers, and more.

### 3. The `re` Module

The `re` module in Python provides functions to work with regular expressions.

### 4. Basic Patterns and Special Characters

#### Special Characters

* `.`: Matches any character except a newline.
* `^`: Matches the start of the string.
* `$`: Matches the end of the string.
* `*`: Matches 0 or more repetitions of the preceding pattern.
* `+`: Matches 1 or more repetitions of the preceding pattern.
* `?`: Matches 0 or 1 repetition of the preceding pattern.
* `[]`: Matches any single character in brackets.
* `\`: Escapes special characters or signals a special sequence.

#### Example: Basic Pattern Matching

```python
import re

# Find all occurrences of 'cat' in the string
pattern = r'cat'
text = 'The cat sat on the cat mat.'
matches = re.findall(pattern, text)
print(matches)
```

### 5. Functions in the `re` Module

#### `re.findall()`

Finds all matches of a pattern in a string.

```python
import re

pattern = r'\d+'  # Matches one or more digits
text = 'There are 123 cats and 456 dogs.'
matches = re.findall(pattern, text)
print(matches)  # Output: ['123', '456']
```

#### `re.search()`

Searches for the first match of a pattern in a string.

```python
import re

pattern = r'\d+'  # Matches one or more digits
text = 'There are 123 cats and 456 dogs.'
match = re.search(pattern, text)
if match:
    print(match.group())  # Output: 123
```

#### `re.match()`

Checks for a match only at the beginning of the string.

```python
import re

pattern = r'\d+'  # Matches one or more digits
text = '123 cats and 456 dogs.'
match = re.match(pattern, text)
if match:
    print(match.group())  # Output: 123
```

#### `re.sub()`

Replaces matches of a pattern with a string.

```python
import re

pattern = r'cat'
text = 'The cat sat on the cat mat.'
new_text = re.sub(pattern, 'dog', text)
print(new_text)  # Output: The dog sat on the dog mat.
```

#### `re.split()`

Splits a string by the occurrences of a pattern.

```python
import re

pattern = r'\d+'
text = 'one1two2three3four4'
split_text = re.split(pattern, text)
print(split_text)  # Output: ['one', 'two', 'three', 'four', '']
```

### 6. Compiling Regular Expressions

Regular expressions can be compiled into pattern objects, which can be used to perform matches more efficiently.

#### Example: Compiling a Regular Expression

```python
import re

pattern = re.compile(r'\d+')
text = 'There are 123 cats and 456 dogs.'

matches = pattern.findall(text)
print(matches)  # Output: ['123', '456']

match = pattern.search(text)
if match:
    print(match.group())  # Output: 123
```

### 7. Practical Examples

#### Example 1: Validating an Email Address

```python
import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

email = 'test@example.com'
print(validate_email(email))  # Output: True
```

#### Example 2: Extracting Phone Numbers

```python
import re

text = 'Contact us at 123-456-7890 or 987-654-3210.'
pattern = r'\d{3}-\d{3}-\d{4}'
phone_numbers = re.findall(pattern, text)
print(phone_numbers)  # Output: ['123-456-7890', '987-654-3210']
```

#### Example 3: Replacing Dates in a String

```python
import re

text = 'The event is on 2024-08-05. Another event is on 2024-09-15.'
pattern = r'\d{4}-\d{2}-\d{2}'
new_text = re.sub(pattern, 'YYYY-MM-DD', text)
print(new_text)  # Output: The event is on YYYY-MM-DD. Another event is on YYYY-MM-DD.
```

#### Example 4: Splitting a String by Multiple Delimiters

```python
import re

text = 'apple;banana,orange|grape'
pattern = r'[;,|]'
split_text = re.split(pattern, text)
print(split_text)  # Output: ['apple', 'banana', 'orange', 'grape']
```

### 8. Summary

In this tutorial, we explored how to work with regular expressions in Python using the `re` module. We covered the basics of RegEx, how to use various functions in the `re` module, compiling regular expressions, and provided practical examples to illustrate their application. Regular expressions are powerful tools for searching, manipulating, and validating strings in Python.

For more tutorials and in-depth explanations, visit [codeswithpankaj.com](https://codeswithpankaj.com)!

***

This tutorial provides a comprehensive overview of working with regular expressions in Python, detailing each topic and subtopic with examples and explanations. For more such tutorials, keep following [codeswithpankaj.com](https://codeswithpankaj.com)!
