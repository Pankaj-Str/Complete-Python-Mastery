# Regular Expressions in Python

## Introduction

Welcome! In this tutorial, we will learn **Regular Expressions (RegEx)** in Python. This is a useful tool for searching and working with text.

---

## 1. Understanding Regular Expressions (RegEx)

### What is Regular Expression?

A **Regular Expression (RegEx)** is a pattern used to search for specific words, numbers, or symbols in text. It helps in finding, replacing, and extracting information from large text data easily.

### How to Use RegEx in Python?

Python has a built-in module called `re` that helps us use regular expressions. To use it, we first need to import it:

```python
import re
```

### Basic RegEx Patterns

| Pattern | Meaning                      | Example                                  |
| ------- | ---------------------------- | ---------------------------------------- |
| `\d`    | Matches any digit (0-9)      | "My number is 1234" → `\d+` finds `1234` |
| `\w`    | Matches any letter or number | "Hello_123" → `\w+` finds `Hello_123`   |
| `\s`    | Matches spaces               | "Hello World" → `\s` finds space         |
| `.`     | Matches any character        | "a.b" → `.` finds `a` and `b`            |
| `*`     | Matches 0 or more times      | "go*" → matches "g", "go", "goo"        |
| `+`     | Matches 1 or more times      | "go+" → matches "go", "goo", but not "g" |
| `?`     | Matches 0 or 1 time          | "colou?r" → matches "color" and "colour" |
| `^`     | Matches start of string      | "^Hello" → matches "Hello World" but not "World Hello" |
| `$`     | Matches end of string        | "world$" → matches "Hello world" but not "world Hello" |
| `[]`    | Matches any character inside brackets | `[aeiou]` → matches "a" in "apple" |
| `()`    | Groups patterns              | `(ab)+` → matches "ababab" in "abababxyz" |

### Example: Finding Numbers in a Sentence

```python
import re

text = "The price is 150 dollars."
match = re.search(r'\d+', text)
if match:
    print("Number found:", match.group())  # Output: 150
```

### Example: Finding Emails in a Text

```python
import re

text = "Contact me at test@example.com and info@mail.com"
emails = re.findall(r'[\w.-]+@[\w.-]+', text)
print("Emails found:", emails)
# Output: ['test@example.com', 'info@mail.com']
```

### Example: Replacing Text Using RegEx

```python
import re

text = "Hello 123, this is a test 456."
new_text = re.sub(r'\d+', '###', text)
print(new_text)  # Output: "Hello ###, this is a test ###."
```

### Example: Extracting Words from a Sentence

```python
import re

text = "Python is an amazing programming language!"
words = re.findall(r'\w+', text)
print("Words found:", words)
# Output: ['Python', 'is', 'an', 'amazing', 'programming', 'language']
```

---

## Conclusion

- **Regular Expressions (RegEx)** help search for patterns in text.
- Useful for finding words, numbers, emails, and more.
- We can replace and extract specific parts of text using RegEx.
- Python's `re` module makes working with RegEx easy.

With these basics, you can now start using Regular Expressions in Python to manipulate text data efficiently! 🚀

