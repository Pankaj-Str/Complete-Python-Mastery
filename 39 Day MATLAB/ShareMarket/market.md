## Visualizing Data with Matplotlib – Share Bazaar (Stock Market) Analysis

Stock market (share bazaar) data visualization helps you **understand trends, patterns, and decisions quickly**. Using Matplotlib in Python, you can easily analyze stock prices like a pro.

---

# 1. Setup (Install & Import)

```bash
pip install matplotlib pandas yfinance
```

```python
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf
```

---

# 2. Load Share Market Data

We will use **real stock data** (example: Reliance)

```python
stock = yf.download("RELIANCE.NS", start="2023-01-01", end="2024-01-01")
print(stock.head())
```

---

# 3. Line Chart – Stock Closing Price

This is the most basic and important chart in share market analysis.

```python
plt.figure()
plt.plot(stock['Close'])
plt.title("Reliance Stock Closing Price")
plt.xlabel("Date")
plt.ylabel("Price (INR)")
plt.show()
```

### What You Learn:

* Trend (uptrend / downtrend)
* Price movement over time

---

# 4. Moving Average (Trend Analysis)

Moving average helps remove noise and show trend clearly.

```python
stock['MA50'] = stock['Close'].rolling(window=50).mean()

plt.figure()
plt.plot(stock['Close'], label="Close Price")
plt.plot(stock['MA50'], label="50-Day MA")
plt.legend()
plt.title("Moving Average Analysis")
plt.show()
```

### Use:

* Identify **bullish or bearish trend**

---

# 5. Bar Chart – Volume Analysis

```python
plt.figure()
plt.bar(stock.index, stock['Volume']['RELIANCE.NS'])
plt.title("Daily Trading Volume")
plt.xlabel("Date")
plt.ylabel("Volume")
plt.show()
```

### Use:

* High volume = strong movement
* Low volume = weak trend

---

# 6. Candlestick Chart (Advanced)

Matplotlib alone is limited, but with `mplfinance`:

```bash
pip install mplfinance
```

```python
import mplfinance as mpf

# Step 1: Flatten columns
stock.columns = stock.columns.droplevel(1)

# Step 2: Convert to float
stock = stock.astype(float)

# Step 3: Plot
mpf.plot(stock, type='candle', volume=True, title="Reliance Candlestick Chart")
```

### Use:

* Daily trading patterns
* Entry/Exit signals

---

# 7. Multiple Stocks Comparison

```python
stocks = yf.download(["RELIANCE.NS", "TCS.NS"], start="2023-01-01", end="2024-01-01")

plt.figure()
plt.plot(stocks['Close']['RELIANCE.NS'], label="Reliance")
plt.plot(stocks['Close']['TCS.NS'], label="TCS")
plt.legend()
plt.title("Stock Comparison")
plt.show()
```

---

# 8. Daily Returns (Profit/Loss Analysis)

```python
stock['Daily Return'] = stock['Close'].pct_change()

plt.figure()
plt.plot(stock['Daily Return'])
plt.title("Daily Returns")
plt.show()
```

---

# 9. Histogram – Risk Analysis

```python
plt.figure()
plt.hist(stock['Daily Return'].dropna(), bins=50)
plt.title("Return Distribution")
plt.show()
```

### Use:

* Understand **risk & volatility**

---

# 10. Key Insights (Important for Beginners)

| Visualization  | Purpose          |
| -------------- | ---------------- |
| Line Chart     | Trend analysis   |
| Moving Average | Smooth trend     |
| Volume Bar     | Strength of move |
| Candlestick    | Trading patterns |
| Histogram      | Risk analysis    |

---

