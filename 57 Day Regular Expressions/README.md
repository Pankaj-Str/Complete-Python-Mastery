# Regular Expressions in Python

Regular Expressions (regex) in Python are powerful tools for pattern matching and text manipulation. They allow you to search, match, and manipulate strings based on specific patterns. This tutorial will guide you through the basics of regex in Python using the `re` module, with examples to help you understand each step.

## Step 1: Understanding Regular Expressions
A regular expression is a sequence of characters that defines a search pattern. For example, you can use regex to:
- Find all email addresses in a text.
- Validate phone numbers.
- Extract specific words or patterns from strings.

In Python, the `re` module provides functions to work with regex.

## Step 2: Importing the `re` Module
To use regex in Python, you need to import the `re` module.

```python
import re
```

## Step 3: Basic Regex Patterns
Regex patterns use special characters to define rules. Here are some common ones:
- `.` : Matches any single character (except newline).
- `^` : Matches the start of a string.
- `$` : Matches the end of a string.
- `*` : Matches 0 or more repetitions of the previous character.
- `+` : Matches 1 or more repetitions of the previous character.
- `?` : Matches 0 or 1 repetition of the previous character.
- `\d` : Matches any digit (0–9).
- `\w` : Matches any alphanumeric character (a–z, A–Z, 0–9, _).
- `\s` : Matches any whitespace character (space, tab, newline).
- `[abc]` : Matches any single character in the set (e.g., a, b, or c).
- `[^abc]` : Matches any single character not in the set.

## Step 4: Common `re` Module Functions
The `re` module provides several functions to work with regex:
- `re.search(pattern, string)`: Searches for the first occurrence of the pattern in the string.
- `re.match(pattern, string)`: Checks if the string starts with the pattern.
- `re.findall(pattern, string)`: Returns a list of all non-overlapping matches.
- `re.sub(pattern, replacement, string)`: Replaces matches with a new string.

## Step 5: Writing Your First Regex
Let’s find a word in a string using `re.search()`.

```python
import re

text = "Hello, my name is Alice."
pattern = r"Alice"

match = re.search(pattern, text)
if match:
    print("Found:", match.group())  # Output: Found: Alice
else:
    print("Not found")
```

Explanation:
- `r"Alice"`: The `r` denotes a raw string, which prevents Python from interpreting backslashes.
- `re.search()`: Looks for "Alice" in the text.
- `match.group()`: Returns the matched string.

## Step 6: Matching Digits
Let’s find all numbers in a string using `\d`.

```python
import re

text = "My phone number is 123-456-7890."
pattern = r"\d+"

numbers = re.findall(pattern, text)
print(numbers)  # Output: ['123', '456', '7890']
```

Explanation:
- `\d+`: Matches one or more digits.
- `re.findall()`: Returns a list of all matches.

## Step 7: Validating an Email Address
Let’s create a regex pattern to validate an email address.

```python
import re

email = "example@domain.com"
pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

if re.match(pattern, email):
    print("Valid email")
else:
    print("Invalid email")
```

Explanation:
- `^`: Ensures the string starts with the pattern.
- `[a-zA-Z0-9._%+-]+`: Matches one or more letters, digits, or specific symbols for the username.
- `@`: Matches the @ symbol.
- `[a-zA-Z0-9.-]+`: Matches the domain name.
- `\.`: Matches a literal dot.
- `[a-zA-Z]{2,}`: Matches the top-level domain (e.g., com, org).
- `$`: Ensures the string ends with the pattern.

## Step 8: Replacing Text with `re.sub()`
Let’s replace all digits in a string with a placeholder.

```python
import re

text = "My number is 123-456-7890."
pattern = r"\d+"
result = re.sub(pattern, "XXX", text)
print(result)  # Output: My number is XXX-XXX-XXX.
```

Explanation:
- `re.sub()`: Replaces all matches of `\d+` with "XXX".

## Step 9: Using Groups
Groups allow you to capture parts of a match using parentheses `()`.

```python
import re

text = "Contact: alice@example.com"
pattern = r"(\w+)@([\w.]+)"

match = re.search(pattern, text)
if match:
    username = match.group(1)  # First group
    domain = match.group(2)    # Second group
    print(f"Username: {username}, Domain: {domain}")
    # Output: Username: alice, Domain: example.com
```

Explanation:
- `(\w+)`: Captures one or more alphanumeric characters (username).
- `@`: Matches the @ symbol.
- `([\w.]+)`: Captures the domain name.

## Step 10: Tips for Beginners
- **Test your regex**: Use online tools like regex101.com to experiment with patterns.
- **Start simple**: Break complex patterns into smaller parts.
- **Use raw strings**: Always use `r"pattern"` to avoid issues with backslashes.
- **Practice**: Try matching patterns like phone numbers, URLs, or dates.

## Next Steps
- Explore more advanced regex patterns like lookaheads and lookbehinds.
- Practice with real-world examples, such as parsing logs or cleaning data.
- Check the official Python `re` module documentation for more functions and options.



