# In-Depth Regular Expression 

Regular expressions (regex) are powerful tools for pattern matching and text manipulation.
---

## Table of Contents
1. **Introduction to Regular Expressions**
2. **The `match` Function**
3. **The `search` Function**
4. **Matching vs. Searching**
5. **Modifiers**
6. **Common Regex Patterns**
7. **Practical Examples**
8. **Tips for Beginners**
9. **Conclusion**

---

## 1. Introduction to Regular Expressions

A regular expression is a sequence of characters that defines a search pattern. It's used to find, match, or manipulate text based on specific rules. Think of regex as a way to describe what you're looking for in a string, like finding all email addresses or validating a phone number.

In Python, the `re` module provides functions like `match` and `search` to work with regex. To use it, import the module:

```python
import re
```

---

## 2. The `match` Function

The `match` function checks if the **beginning** of a string matches a specified pattern. If the pattern is found at the start, it returns a match object; otherwise, it returns `None`.

### Syntax
```python
re.match(pattern, string, flags=0)
```
- `pattern`: The regex pattern to match.
- `string`: The text to search.
- `flags`: Optional modifiers (e.g., `re.IGNORECASE`).

### How It Works
- `match` only looks at the **start** of the string.
- If the pattern doesn't match at the beginning, it fails, even if the pattern exists later in the string.

### Example: Using `match`
Let's check if a string starts with "Hello".

```python
import re

text = "Hello, World!"
pattern = r"Hello"

match = re.match(pattern, text)

if match:
    print("Match found:", match.group())  # Output: Match found: Hello
else:
    print("No match")
```

**Step-by-Step Explanation**:
1. We import the `re` module.
2. The pattern `r"Hello"` is a raw string (using `r` to avoid escaping backslashes).
3. `re.match(pattern, text)` checks if `text` starts with "Hello".
4. The `match.group()` method returns the matched text.
5. Since "Hello" is at the start, it prints "Match found: Hello".

### Example: No Match
```python
text = "Hi, Hello, World!"
pattern = r"Hello"

match = re.match(pattern, text)

if match:
    print("Match found:", match.group())
else:
    print("No match")  # Output: No match
```

**Explanation**: Since "Hello" is not at the start of the string, `match` returns `None`.

---

## 3. The `search` Function

The `search` function scans the **entire** string to find the **first occurrence** of a pattern. Unlike `match`, it doesn't require the pattern to be at the start.

### Syntax
```python
re.search(pattern, string, flags=0)
```
- `pattern`: The regex pattern to find.
- `string`: The text to search.
- `flags`: Optional modifiers.

### How It Works
- `search` looks through the entire string and returns a match object for the first match.
- If no match is found, it returns `None`.

### Example: Using `search`
Let's find "Hello" anywhere in the string.

```python
import re

text = "Hi, Hello, World!"
pattern = r"Hello"

match = re.search(pattern, text)

if match:
    print("Match found:", match.group())  # Output: Match found: Hello
else:
    print("No match")
```

**Step-by-Step Explanation**:
1. The pattern `r"Hello"` looks for "Hello" in the string.
2. `re.search(pattern, text)` scans the entire string and finds "Hello".
3. `match.group()` returns the matched text.

### Example: No Match
```python
text = "Hi, World!"
pattern = r"Hello"

match = re.search(pattern, text)

if match:
    print("Match found:", match.group())
else:
    print("No match")  # Output: No match
```

**Explanation**: Since "Hello" is not in the string, `search` returns `None`.

---

## 4. Matching vs. Searching

Here's a clear comparison between `match` and `search`:

| Feature                | `re.match`                          | `re.search`                         |
|------------------------|-------------------------------------|-------------------------------------|
| **Where it looks**     | Only at the **start** of the string | **Anywhere** in the string          |
| **Returns**            | Match object or `None`             | Match object or `None`             |
| **Use case**           | Validate string starts with pattern | Find first occurrence of pattern    |
| **Performance**        | Stops if start doesn't match        | Scans entire string                 |

### Example: `match` vs. `search`
```python
import re

text = "The quick brown fox"

# Using match
pattern = r"quick"
match_result = re.match(pattern, text)
print("Match result:", match_result)  # Output: None (because "quick" is not at the start)

# Using search
search_result = re.search(pattern, text)
print("Search result:", search_result.group())  # Output: quick
```

**Key Takeaway**: Use `match` when you need to ensure the pattern is at the beginning (e.g., validating formats). Use `search` to find a pattern anywhere in the text.

---

## 5. Modifiers

Modifiers (or flags) change how regex patterns are interpreted. They are optional arguments passed to `match` or `search`. Common modifiers include:

| Modifier            | Description                              | Example Usage                     |
|---------------------|------------------------------------------|-----------------------------------|
| `re.IGNORECASE` (`re.I`) | Ignores case (uppercase/lowercase)       | `r"hello"` matches "HELLO"        |
| `re.MULTILINE` (`re.M`)  | Treats each line as a separate string    | `^` matches start of each line    |
| `re.DOTALL` (`re.S`)     | Makes `.` match newlines as well         | `.*` matches across lines         |

### Example: Using `re.IGNORECASE`
```python
import re

text = "HELLO, World!"
pattern = r"hello"

match = re.search(pattern, text, re.IGNORECASE)

if match:
    print("Match found:", match.group())  # Output: Match found: HELLO
else:
    print("No match")
```

**Explanation**: The `re.IGNORECASE` flag allows `r"hello"` to match "HELLO" regardless of case.

### Example: Using `re.MULTILINE`
```python
import re

text = "start here\nstart there"
pattern = r"^start"

matches = re.findall(pattern, text, re.MULTILINE)

print(matches)  # Output: ['start', 'start']
```

**Explanation**: `re.MULTILINE` makes `^` match the start of each line, so both "start"s are found.

---

## 6. Common Regex Patterns

Regex patterns are built using special characters and constructs. Here are some common ones:

| Pattern         | Description                              | Example                     |
|-----------------|------------------------------------------|-----------------------------|
| `.`             | Matches any character (except newline)   | `h.t` matches "hat", "hot"  |
| `^`             | Matches start of string (or line with `re.M`) | `^Hello` matches "Hello" at start |
| `$`             | Matches end of string (or line with `re.M`) | `World$` matches "World" at end |
| `*`             | Matches 0 or more occurrences            | `a*` matches "", "a", "aa"  |
| `+`             | Matches 1 or more occurrences            | `a+` matches "a", "aa"      |
| `?`             | Matches 0 or 1 occurrence                | `colou?r` matches "color", "colour" |
| `{n}`           | Matches exactly `n` occurrences          | `a{3}` matches "aaa"        |
| `[abc]`         | Matches any single character in set      | `[aeiou]` matches a vowel   |
| `[^abc]`        | Matches any character not in set         | `[^0-9]` matches non-digits |
| `\d`            | Matches any digit (0-9)                  | `\d+` matches "123"         |
| `\w`            | Matches any word character (a-z, A-Z, 0-9, _) | `\w+` matches "hello"  |
| `\s`            | Matches any whitespace character         | `\s+` matches "  "          |
| `|`             | Matches either pattern                   | `cat|dog` matches "cat" or "dog" |

### Example: Matching an Email Address
A simple email pattern might look like: `r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"`

```python
import re

text = "Contact us at example@email.com or support@company.org"
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

emails = re.findall(pattern, text)
print(emails)  # Output: ['example@email.com', 'support@company.org']
```

**Pattern Breakdown**:
- `[a-zA-Z0-9._%+-]+`: One or more letters, digits, or allowed symbols before `@`.
- `@`: Literal `@` symbol.
- `[a-zA-Z0-9.-]+`: One or more letters, digits, dots, or hyphens for the domain.
- `\.`: Literal dot (escaped with `\`).
- `[a-zA-Z]{2,}`: Two or more letters for the top-level domain (e.g., "com", "org").

---

## 7. Practical Examples

### Example 1: Validating a Phone Number
Let's match a phone number in the format `(123) 456-7890`.

```python
import re

text = "Call me at (123) 456-7890"
pattern = r"\(\d{3}\) \d{3}-\d{4}"

match = re.search(pattern, text)

if match:
    print("Phone number found:", match.group())  # Output: Phone number found: (123) 456-7890
else:
    print("No phone number found")
```

**Pattern Breakdown**:
- `\(`: Literal opening parenthesis.
- `\d{3}`: Exactly three digits.
- `\)`: Literal closing parenthesis.
- ` `: Literal space.
- `\d{3}-\d{4}`: Three digits, a hyphen, then four digits.

### Example 2: Replacing Text
Use `re.sub` to replace all digits with `#`.

```python
import re

text = "My number is 12345"
pattern = r"\d"

result = re.sub(pattern, "#", text)
print(result)  # Output: My number is #####
```

**Explanation**: `re.sub(pattern, replacement, string)` replaces all matches of the pattern with the specified replacement.

### Example 3: Splitting a String
Split a string by multiple delimiters (e.g., comma or semicolon).

```python
import re

text = "apple,banana;orange,grape"
pattern = r"[,;]"

fruits = re.split(pattern, text)
print(fruits)  # Output: ['apple', 'banana', 'orange', 'grape']
```

**Explanation**: The pattern `[,;]` matches either a comma or semicolon, and `re.split` splits the string at those points.

---

## 8. Tips for Beginners

1. **Start Simple**: Begin with basic patterns like literal strings or simple character classes (e.g., `[a-z]`).
2. **Test Incrementally**: Use tools like regex101.com to test your patterns interactively.
3. **Escape Special Characters**: Use `\` to escape characters like `.`, `*`, or `(`.
4. **Use Raw Strings**: Prefix patterns with `r` (e.g., `r"\d+"`) to avoid issues with backslashes.
5. **Debug with `findall`**: Use `re.findall(pattern, text)` to see all matches in a string.
6. **Practice Common Patterns**: Memorize patterns like `\d`, `\w`, and `\s` for quick use.
7. **Be Specific**: Overly broad patterns (e.g., `.*`) can match unintended text. Narrow them down when possible.

---

## 9. Conclusion

Regular expressions are a versatile tool for text processing. The `match` function is ideal for validating the start of a string, while `search` is great for finding patterns anywhere. Modifiers like `re.IGNORECASE` enhance flexibility, and common patterns like `\d` or `[a-z]` simplify complex matching tasks. By practicing with real-world examples, you'll gain confidence in using regex effectively.

For further learning, explore:
- Python's `re` module documentation: https://docs.python.org/3/library/re.html
- Interactive regex testers like regex101.com
- Common regex patterns for emails, URLs, or dates
