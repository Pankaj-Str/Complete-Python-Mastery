
### What is Web Scraping?

Imagine you want to copy 100 names of famous people from a website for your school project.

Normally you would:
- Open the website
- Read one name
- Copy it
- Paste in your notebook
- Repeat 100 times → boring & slow!

**Web scraping** = teaching your computer to do this copying job automatically in 2 seconds.

It's like giving your computer super-fast copy-paste hands.

### We will use Python because:
- It reads almost like English
- Only 10–15 lines needed for simple things
- Free forever

### Super Simple Plan (5 baby steps)

1. Tell computer: "Go to this website and bring me the page"
2. Computer brings the page (looks like messy secret code — that's okay)
3. We teach computer: "Find only the parts I want (like names or prices)"
4. Computer shows or saves them
5. Done! 🎉

### Easiest Example Ever (Copy-Paste & Run)

We will copy famous quotes from this friendly practice website:  
https://quotes.toscrape.com  
(They made this site specially for students to practice — it's safe & allowed)

**Step 0: Get Python (one-time setup)**  
- Go to https://www.python.org/downloads/
- Click big yellow button "Download Python 3.xx"
- Install it → click "Next" many times (add to PATH if it asks)
- Open Command Prompt (Windows) or Terminal (Mac) and type:  
  `python --version`  
  → If you see version number → good!

**Step 1: Install two magic helpers**  
Open Command Prompt / Terminal and copy-paste these two lines one by one:

```bash
pip install requests
pip install beautifulsoup4
```

(Wait 1–2 minutes — computer is downloading helpers)

**Step 2: Make your first tiny program**

1. Open Notepad (or any text editor)
2. Copy ALL this code below
3. Paste into Notepad
4. Save file as → `my_first_scraper.py`  
   (important: must end with `.py`)

```python
# This is our super simple web scraper for school students!

import requests                  # helper to go to website
from bs4 import BeautifulSoup    # helper to read the page like a book

# Step 1: Go to the website
website = "https://quotes.toscrape.com"
page = requests.get(website)

# Step 2: Read the page
soup = BeautifulSoup(page.text, "html.parser")

# Step 3: Find all quotes (they hide inside special boxes)
all_quotes = soup.find_all("span", class_="text")

# Step 4: Show first 5 quotes only
print("Here are some cool quotes I found:\n")

for i in range(5):           # show only first 5
    quote = all_quotes[i].text
    print(f"{i+1}. {quote}\n")
```

**Step 3: Run it!**

- Save the file
- Go to the folder where you saved `my_first_scraper.py`
- Hold SHIFT + right-click inside the folder → "Open command window here" (or terminal)
- Type this and press Enter:

```bash
python my_first_scraper.py
```

You should see something like:

```
Here are some cool quotes I found:

1. “The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”

2. “It is our choices, Harry, that show what we truly are, far more than our abilities.”

3. “There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”

...
```

Yay! 🎉 Your computer just scraped the website!

### What we actually did (in 5-year-old words)

- Computer knocked on website door → "Hello, can I see your page?"
- Website gave big messy page
- We told computer: "Look for words inside `<span class="text">` boxes — those are quotes!"
- Computer found them and showed us

### Want to make it even more fun?

Change these lines and try again:

- Change number 5 → 10 to see more quotes
- Change website address to any simple site (but first ask permission or use practice sites)

Example change — only show first 3 quotes:

```python
for i in range(3):
    quote = all_quotes[i].text
    print(f"{i+1}. {quote}\n")
```

