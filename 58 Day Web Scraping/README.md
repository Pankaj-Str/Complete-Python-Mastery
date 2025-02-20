# Web Scraping in Python

## Introduction
Web scraping is the process of extracting data from websites. Python is widely used for web scraping due to its powerful libraries like `BeautifulSoup` and `requests`. This tutorial will walk you through the basics of web scraping in an easy-to-understand manner.

---

## Prerequisites
Before you start, ensure you have Python installed on your computer. You will also need to install the following libraries:

```sh
pip install requests beautifulsoup4
```

### Import Required Libraries
```python
import requests
from bs4 import BeautifulSoup
```

---

## Step 1: Sending a Request to a Website
To scrape data, you first need to send a request to a website and get the HTML content.

```python
url = "https://example.com"  # Replace with the website URL
target_page = requests.get(url)
print(target_page.text)  # Prints the HTML content
```

### Explanation:
- `requests.get(url)`: Sends a request to the website and gets the response.
- `.text`: Extracts the HTML content of the page.

---

## Step 2: Parsing the HTML
To extract useful information from the HTML content, we use `BeautifulSoup`.

```python
soup = BeautifulSoup(target_page.text, "html.parser")
print(soup.prettify())  # Prints formatted HTML
```

### Explanation:
- `BeautifulSoup(target_page.text, "html.parser")`: Parses the HTML content.
- `.prettify()`: Formats the HTML to make it readable.

---

## Step 3: Extracting Specific Data
Web pages consist of various HTML elements like `<h1>`, `<p>`, `<a>`, etc. You can extract them as follows:

### Extracting Title
```python
title = soup.title.text
print("Page Title:", title)
```

### Extracting All Links
```python
for link in soup.find_all('a'):
    print(link.get('href'))  # Prints all hyperlinks
```

### Extracting Specific Class
If you want to extract elements with a specific class, use:

```python
data = soup.find_all("div", class_="example-class")
for item in data:
    print(item.text)
```

---

## Step 4: Handling Dynamic Websites
Some websites load content dynamically using JavaScript. For such cases, you may need `Selenium`.

### Installing Selenium
```sh
pip install selenium
```

### Example: Using Selenium
```python
from selenium import webdriver

driver = webdriver.Chrome()  # Ensure you have Chrome WebDriver installed
driver.get("https://example.com")
print(driver.page_source)  # Fetches dynamic content
```

---

## Step 5: Avoiding Blocks and Ethical Considerations
- **Respect `robots.txt`**: Check if scraping is allowed by reviewing `https://example.com/robots.txt`.
- **Use Headers**: Mimic a real browser to avoid getting blocked.

```python
headers = {"User-Agent": "Mozilla/5.0"}
target_page = requests.get(url, headers=headers)
```

- **Delay Requests**: Add small delays to avoid overwhelming the server.
```python
import time

time.sleep(2)  # Waits for 2 seconds between requests
```

---

## Conclusion
Congratulations! You have learned the basics of web scraping with Python. With practice, you can scrape and automate data collection from websites efficiently. Always follow ethical guidelines and respect website policies while scraping.

Happy coding! 🚀

