# Regular Expressions 

## Introduction

Welcome! In this tutorial, we will learn **Regular Expressions (RegEx)** and **Web Scraping** in Python. These are useful tools for searching text and extracting data from websites.

---

## 1. Understanding Regular Expressions (RegEx)

###

A **Regular Expression (RegEx)** is a pattern used to search for specific words, numbers, or symbols in text.

### How to Use RegEx in Python?

Python has a built-in module called `re` that helps us use regular expressions.

### Basic RegEx Patterns

| Pattern | Meaning                      | Example                                  |
| ------- | ---------------------------- | ---------------------------------------- |
| `\d`    | Matches any digit (0-9)      | "My number is 1234" → `\d+` finds `1234` |
| `\w`    | Matches any letter or number | "Hello\_123" → `\w+` finds `Hello_123`   |
| `\s`    | Matches spaces               | "Hello World" → `\s` finds space         |
| `.`     | Matches any character        | "a.b" → `.` finds `a` and `b`            |
| `*`     | Matches 0 or more times      | "go\*" → matches "g", "go", "goo"        |
| `+`     | Matches 1 or more times      | "go+" → matches "go", "goo", but not "g" |

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

---

## 2. Web Scraping in Python

### What is Web Scraping?

Web scraping is a technique to extract information from websites.

### Libraries for Web Scraping

- **Requests**: Fetches web pages.
- **BeautifulSoup**: Extracts data from HTML.

### Install Required Libraries

Run the following command to install them:

```sh
pip install requests beautifulsoup4
```

### Example: Extracting Headlines from a News Website

```python
import requests
from bs4 import BeautifulSoup

# Get webpage content
url = "https://news.ycombinator.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract headlines
headlines = soup.find_all("a", class_="storylink")

for i, headline in enumerate(headlines[:5]):
    print(f"{i+1}. {headline.text}")
```

### Example: Extracting All Links from a Webpage

```python
import requests
from bs4 import BeautifulSoup

url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all links
links = soup.find_all('a')
for link in links:
    print(link.get('href'))
```

---

## 3. Combining RegEx and Web Scraping

Now, let’s extract **email addresses** from a webpage using both **RegEx and BeautifulSoup**.

```python
import requests
from bs4 import BeautifulSoup
import re

url = "https://example.com/contact"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract text
page_text = soup.get_text()

# Find email addresses using RegEx
emails = re.findall(r'[\w.-]+@[\w.-]+', page_text)
print("Extracted Emails:", emails)
```

---

## Conclusion

- **Regular Expressions (RegEx)** help search for patterns in text.
- **BeautifulSoup** makes it easy to extract data from websites.
- **Requests** fetches web pages for scraping.



