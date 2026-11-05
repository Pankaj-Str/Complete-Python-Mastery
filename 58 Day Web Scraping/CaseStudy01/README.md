## real example website: **Quotes to Scrape** (`http://quotes.toscrape.com/`).  

### **Web Scraping Example - Extract Quotes and Authors**  

#### **Step 1: Install Required Libraries**  
Run this in your terminal if you haven’t installed them yet:  
```bash
pip install requests beautifulsoup4 pandas
```

---

#### **Step 2: Fetch the Webpage**
We will use `requests` to get the webpage content.  
```python
import requests

url = "http://quotes.toscrape.com/"
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:
    print("Page fetched successfully!")
else:
    print("Failed to fetch page.")
```

---

#### **Step 3: Parse HTML with BeautifulSoup**  
Now, let's use `BeautifulSoup` to parse the HTML and extract data:  
```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(response.text, "html.parser")

# Print formatted HTML (optional)
print(soup.prettify()[:500])  # Show first 500 characters
```

---

#### **Step 4: Extract Quotes and Authors**  
We find all quote and author elements using CSS classes:  
```python
quotes = soup.find_all("span", class_="text")  # Extract quotes
authors = soup.find_all("small", class_="author")  # Extract authors

# Print extracted data
for i in range(len(quotes)):
    print(f"Quote: {quotes[i].text}")
    print(f"Author: {authors[i].text}")
    print("-" * 50)
```

---

#### **Step 5: Save Data to CSV**  
We store the extracted quotes and authors in a CSV file using `pandas`:  
```python
import pandas as pd

data = {"Quote": [q.text for q in quotes], "Author": [a.text for a in authors]}
df = pd.DataFrame(data)

df.to_csv("quotes.csv", index=False)
print("Data saved to quotes.csv!")
```

---

#### **Step 6: Scrape Multiple Pages**  
Let's scrape all pages by handling pagination:  
```python
page = 1
all_quotes = []
all_authors = []

while True:
    url = f"http://quotes.toscrape.com/page/{page}/"
    response = requests.get(url)
    
    if "No quotes found!" in response.text:  # Stop if no more pages
        break

    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all("span", class_="text")
    authors = soup.find_all("small", class_="author")

    all_quotes.extend([q.text for q in quotes])
    all_authors.extend([a.text for a in authors])

    print(f"Scraped Page {page}")
    page += 1

# Save to CSV
df = pd.DataFrame({"Quote": all_quotes, "Author": all_authors})
df.to_csv("all_quotes.csv", index=False)
print("All pages scraped and saved to all_quotes.csv!")
```

---

#### **Step 7: Avoiding Blocks with Headers**  
Some websites block scrapers. To avoid this, use headers with a User-Agent:  
```python
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

response = requests.get(url, headers=headers)
```

---

### **Final Output**
After running these scripts:  
✅ Quotes and authors will be extracted  
✅ Data will be saved in a `quotes.csv` file  
✅ All pages will be scraped automatically  

---

