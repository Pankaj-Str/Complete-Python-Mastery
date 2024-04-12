# Simple Patterns

Regular expressions in Python provide a powerful way to search, match, and manipulate text based on patterns. Let's start with some simple patterns and gradually delve into more advanced concepts.

## Matching Characters

In regular expressions, you can specify literal characters to match within a string. For example, the pattern `cat` will match the sequence of characters "cat" in a string.

```python
import re

pattern = r'cat'
text = "The cat sat on the mat."

# Search for the pattern in the text
match = re.search(pattern, text)
if match:
    print("Pattern found at index:", match.start())
else:
    print("Pattern not found.")
```

## Repeating Things

You can use quantifiers to specify how many times a character or group should repeat in a pattern. For example, `+` matches one or more occurrences, `*` matches zero or more occurrences, and `{n}` matches exactly `n` occurrences.

```python
import re

pattern = r'ab+'
text = "ab abb abbb"

# Search for the pattern in the text
matches = re.findall(pattern, text)
print("Matches found:", matches)
```

## Using Regular Expressions

Regular expressions are typically created using raw strings (`r'...'`) to avoid escaping special characters. You can use various metacharacters like `.` (matches any character) and `\d` (matches any digit).

```python
import re

pattern = r'\d+'
text = "There are 123 apples and 456 oranges."

# Search for the pattern in the text
matches = re.findall(pattern, text)
print("Digits found:", matches)
```

## Compiling Regular Expressions

To improve performance when using a regular expression multiple times, you can compile it into a regular expression object using `re.compile()`.

```python
import re

pattern = re.compile(r'\d+')
text = "There are 123 apples and 456 oranges."

# Search for the compiled pattern in the text
matches = pattern.findall(text)
print("Digits found:", matches)
```

## The Backslash Plague

Since backslashes are used to escape special characters in regular expressions and Python strings, you often need to double escape them. Alternatively, use raw strings (`r'...'`) to avoid this.

```python
import re

pattern = r'\d+\\'
text = "There are 123\\ apples and 456\\ oranges."

# Search for the pattern in the text
matches = re.findall(pattern, text)
print("Digits found:", matches)
```

## Performing Matches

Regular expressions in Python provide various functions like `search()`, `match()`, and `findall()` to perform pattern matching operations on strings.

```python
import re

pattern = r'cat'
text = "The cat sat on the mat."

# Search for the pattern in the text
match = re.search(pattern, text)
if match:
    print("Pattern found at index:", match.start())
else:
    print("Pattern not found.")
```

## Module-Level Functions

The `re` module in Python provides module-level functions like `search()`, `match()`, `findall()`, `sub()`, and `split()` for performing pattern matching operations.

```python
import re

pattern = r'cat'
text = "The cat sat on the mat."

# Search for the pattern in the text
match = re.search(pattern, text)
if match:
    print("Pattern found at index:", match.start())
else:
    print("Pattern not found.")
```

## Compilation Flags

Regular expressions in Python support compilation flags like `re.IGNORECASE`, `re.MULTILINE`, and `re.DOTALL` to modify the behavior of pattern matching.

```python
import re

pattern = re.compile(r'cat', re.IGNORECASE)
text = "The Cat sat on the mat."

# Search for the compiled pattern in the text
matches = pattern.findall(text)
print("Matches found:", matches)
```

## More Pattern Power

Regular expressions support more powerful patterns using metacharacters like `^` (start of string), `$` (end of string), and `[...]` (character class).

```python
import re

pattern = r'^[A-Z][a-z]*$'
text = "Hello"

# Match the pattern against the text
if re.match(pattern, text):
    print("Pattern matched.")
else:
    print("Pattern not matched.")
```

## More Metacharacters

Metacharacters like `\w` (word character), `\s` (whitespace character), and `\d` (digit character) provide shortcuts for common character classes.

```python
import re

pattern = r'\d{3}-\d{2}-\d{4}'
text = "My SSN is 123-45-6789."

# Search for the pattern in the text
matches = re.findall(pattern, text)
print("SSN found:", matches)
```

## Grouping

You can use parentheses to group parts of a regular expression together. This allows you to apply quantifiers to the entire group.

```python
import re

pattern = r'(ab)+'
text = "ab abab ababab"

# Search for the pattern in the text
matches = re.findall(pattern, text)
print("Matches found:", matches)
```

## Non-capturing and Named Groups

Non-capturing groups `(?:...)` are useful when you want to group parts of a pattern without capturing the matched text. Named groups `(?P<name>...)` allow you to refer to captured groups by name.

```python
import re

pattern = r'(?:ab)+'
text = "ab abab ababab"

# Search for the pattern in the text
matches = re.findall(pattern, text)
print("Matches found:", matches)
```

## Lookahead Assertions

Lookahead assertions allow you to assert that a pattern matches or doesn't match ahead of the current position without consuming the characters.

```python
import re

pattern = r'\b\w+(?=\sis\b)'
text = "He is going to the park."

# Search for the pattern in the text
matches = re.findall(pattern, text)
print("Words before 'is':", matches)
```

## Modifying Strings

Regular expressions in Python can be used to modify strings using the `sub()` function, which replaces occurrences of a pattern with a specified replacement string.

```python
import re

pattern = r'\bcat\b'
text = "The cat sat on the mat."

# Replace 'cat' with 'dog'
new_text = re.sub(pattern, 'dog', text)
print("Modified text:", new_text)
```

## Splitting Strings

You can split strings using regular expressions with the `split()` function, which splits a string based on matches of the specified pattern.

```python
import re

pattern = r'\s+'
text = "The quick brown fox"

# Split the text using whitespace as delimiter
words = re.split(pattern, text)
print("Words:", words)
```

## Search and Replace

Regular expressions can be used for search and replace operations using the `sub()` function, which replaces occurrences of a pattern with a specified replacement string.

```python
import re

pattern = r'\bcat\b'
text = "The cat sat on the mat."

# Replace 'cat' with

 'dog'
new_text = re.sub(pattern, 'dog', text)
print("Modified text:", new_text)
```

## Common Problems

Common problems when working with regular expressions include incorrect patterns, inefficient patterns, and unexpected behavior due to special characters.

```python
import re

pattern = r'([a-z]+)\s+\1'
text = "hello hello world world"

# Search for repeated words
matches = re.findall(pattern, text)
print("Repeated words:", matches)
```

## Use String Methods

While regular expressions are powerful, simple string methods like `find()`, `startswith()`, and `endswith()` may suffice for basic pattern matching tasks.

```python
text = "The cat sat on the mat."

# Check if 'cat' is in the text
if 'cat' in text:
    print("Pattern found.")
else:
    print("Pattern not found.")
```

## `match()` versus `search()`

The `match()` function searches for a pattern only at the beginning of the string, while the `search()` function searches for a pattern anywhere in the string.

```python
import re

pattern = r'cat'
text = "The cat sat on the mat."

# Use match() to find 'cat' at the beginning
match = re.match(pattern, text)
if match:
    print("Pattern found at the beginning.")
else:
    print("Pattern not found at the beginning.")

# Use search() to find 'cat' anywhere
match = re.search(pattern, text)
if match:
    print("Pattern found anywhere.")
else:
    print("Pattern not found anywhere.")
```

## Greedy versus Non-Greedy

By default, quantifiers like `*` and `+` are greedy, meaning they match as much text as possible. You can make them non-greedy by adding a `?` after the quantifier.

```python
import re

pattern = r'<.*>'
text = "<html> <head> <title>Page Title</title> </head> <body>Body content</body> </html>"

# Greedy match
match = re.search(pattern, text)
print("Greedy match:", match.group())

# Non-greedy match
pattern = r'<.*?>'
match = re.search(pattern, text)
print("Non-greedy match:", match.group())
```

## Using `re.VERBOSE`

The `re.VERBOSE` flag allows you to write regular expressions more clearly by ignoring whitespace and comments. This can make complex patterns easier to understand.

```python
import re

pattern = re.compile(r'''
    \b          # Word boundary
    \d{3}       # Three digits
    -           # Hyphen
    \d{2}       # Two digits
    -           # Hyphen
    \d{4}       # Four digits
    \b          # Word boundary
    ''', re.VERBOSE)

text = "My SSN is 123-45-6789."

# Search for the pattern in the text
matches = pattern.findall(text)
print("SSN found:", matches)
```

Regular expressions are a versatile tool for text processing and manipulation in Python. By understanding the basics of pattern matching, metacharacters, and quantifiers, you can efficiently work with text data in various applications. Experiment with different patterns and explore the rich capabilities of regular expressions to enhance your Python programming skills.