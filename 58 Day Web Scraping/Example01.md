#### This example will scrape book titles and prices from the sample website `http://books.toscrape.com/`, use regex to extract prices, and save the data to a CSV file. It’s beginner-friendly and includes clear explanations.

```x-python

```python
import requests
from bs4 import BeautifulSoup
import re
import csv

# Step 1: Fetch the web page
url = "http://books.toscrape.com/"
response = requests.get(url)

# Check if the request was successful
if response.status_code != 200:
    print("Failed to fetch page")
    exit()

# Step 2: Parse the HTML
soup = BeautifulSoup(response.text, "html.parser")

# Step 3: Extract book titles and prices
books = soup.find_all("article", class_="product_pod")
data = []

for book in books:
    # Get book title
    title = book.find("h3").find("a")["title"]
    
    # Get price and use regex to extract the numerical part (e.g., 51.77 from £51.77)
    price_text = book.find("p", class_="price_color").text
    price_match = re.search(r"£(\d+\.\d{2})", price_text)
    price = price_match.group(1) if price_match else "N/A"
    
    data.append([title, price])

# Step 4: Save to CSV
with open("scraped_books.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price (£)"])  # Header
    writer.writerows(data)  # Data

print("Data saved to scraped_books.csv")

# Step 5: Print a few results
print("\nSample Results:")
for title, price in data[:3]:  # Show first 3 books
    print(f"Book: {title}, Price: £{price}")
```

```

### Explanation
1. **Fetching the Page**:
   - Uses `requests.get()` to download the HTML from `http://books.toscrape.com/`.
   - Checks the response status to ensure the page was fetched successfully.

2. **Parsing with BeautifulSoup**:
   - `BeautifulSoup` parses the HTML to make it easy to navigate.
   - Finds all `<article>` tags with class `product_pod`, which contain book information.

3. **Extracting Data**:
   - **Title**: Extracts the book title from the `<a>` tag’s `title` attribute within each `<h3>`.
   - **Price**: Finds the price in the `<p>` tag with class `price_color`. Uses regex pattern `r"£(\d+\.\d{2})"` to extract the numerical part (e.g., `51.77` from `£51.77`).
     - `£`: Matches the pound symbol.
     - `(\d+\.\d{2})`: Captures digits followed by a decimal point and exactly two digits.
     - `group(1)`: Retrieves the captured numerical part.

4. **Saving to CSV**:
   - Writes the titles and prices to a CSV file named `scraped_books.csv` with headers.
   - Uses `utf-8` encoding to handle special characters.

5. **Output**:
   - Prints a confirmation message and displays the first three scraped books for verification.

### Expected Output
The script creates a file `scraped_books.csv` with content like:
```csv
Title,Price (£)
A Light in the Attic,51.77
Tipping the Velvet,53.74
Soumission,50.10
...
```

Console output (sample):
```
Data saved to scraped_books.csv

Sample Results:
Book: A Light in the Attic, Price: £51.77
Book: Tipping the Velvet, Price: £53.74
Book: Soumission, Price: £50.10
```

### Prerequisites
Install the required libraries:
```bash
pip install requests beautifulsoup4
```

### Notes
- **Website**: The example uses `http://books.toscrape.com/`, a site designed for scraping practice.
- **Ethics**: Always check a website’s `robots.txt` and terms of service before scraping.
- **Customization**: You can modify the regex pattern (e.g., `r"\$(\d+\.\d{2})"` for USD) or extract other data like book ratings.
- **Chart Option**: If you’d like a chart (e.g., a histogram of prices), let me know, and I can generate one using the scraped data!

