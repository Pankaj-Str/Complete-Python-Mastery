# real-time web scraping project 

## **Project: Live News Scraper & Notifier**  
We will build a Python script that:  
✅ Scrapes **latest news headlines** from a website (e.g., BBC, Times of India, etc.)  
✅ Extracts the **headline, link, and publication time**  
✅ Sends a **desktop notification** or **email alert** for new articles  

### **Tech Stack:**  
- `requests` → Fetch web pages  
- `BeautifulSoup` → Extract news headlines  
- `plyer` → Show desktop notifications  
- `smtplib` → Send email alerts (optional)  
- `schedule` → Run the script every few minutes  

---

## **Step 1: Install Required Libraries**  
```sh
pip install requests beautifulsoup4 plyer schedule
```

---

## **Step 2: Scrape Latest News**  
Let’s extract the latest news headlines from **BBC News**.  

```python
import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Extract top news headlines
articles = soup.find_all("h3", class_="gs-c-promo-heading__title")

news = []
for article in articles[:5]:  # Get top 5 headlines
    title = article.text.strip()
    news.append(title)

print("Latest News Headlines:")
for i, headline in enumerate(news, start=1):
    print(f"{i}. {headline}")
```

---

## **Step 3: Show Desktop Notification**  
Let’s display the top news headline as a **desktop notification**.  

```python
from plyer import notification

notification_title = "Latest News Alert"
notification_message = news[0]  # Show the first news headline

notification.notify(
    title=notification_title,
    message=notification_message,
    timeout=10  # Show for 10 seconds
)
```

---

## **Step 4: Automate News Updates**  
We can run this script **every 10 minutes** using `schedule`.  

```python
import schedule
import time

def get_news():
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.find_all("h3", class_="gs-c-promo-heading__title")

    if articles:
        latest_news = articles[0].text.strip()
        print(f"New Headline: {latest_news}")

        # Show desktop notification
        notification.notify(title="News Alert", message=latest_news, timeout=10)

# Run the script every 10 minutes
schedule.every(10).minutes.do(get_news)

while True:
    schedule.run_pending()
    time.sleep(1)
```

---

## **Step 5: (Optional) Send Email Alerts**  
If you want to receive news updates via **email**, use `smtplib`.  

```python
import smtplib
from email.mime.text import MIMEText

def send_email(news):
    sender_email = "your_email@gmail.com"
    receiver_email = "receiver_email@gmail.com"
    password = "your_app_password"

    msg = MIMEText("\n".join(news))
    msg["Subject"] = "Latest News Update"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

send_email(news)
```

🛑 **Note:** Enable "Less Secure Apps" or use an **App Password** in Gmail.

---

## **Final Steps**  
- Run `news_scraper.py`, and it will notify you of the latest news!  
- Use `Task Scheduler (Windows)` or `Cron Jobs (Linux)` to run it automatically.  
- Modify the script to scrape news from **Times of India, CNN, or other websites**.  

