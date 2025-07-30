## Case study for Reliance Industries Limited (RELIANCE.NS) stock analysis
----
### Prerequisites
Ensure you have the required libraries installed:
```bash
pip install pandas numpy seaborn matplotlib yfinance
```

### Case Study: Comprehensive Analysis of Reliance Industries Stock
Below is the updated Python script that answers 15 questions about Reliance Industries' stock performance from January 1, 2023, to July 30, 2025. Each question is addressed step-by-step, with corresponding code and visualizations.

```python
```python
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import yfinance as yf
from datetime import datetime

# Step 1: Fetch Real-Life Data
ticker = "RELIANCE.NS"
df = yf.download(ticker, start="2023-01-01", end="2025-07-31", progress=False)

# Step 2: Data Cleaning
print("Q1: Are there any missing values in the dataset?")
print("Missing Values:\n", df.isnull().sum())
df = df.dropna()
df.index = pd.to_datetime(df.index)
df = df[['Open', 'High', 'Low', 'Close', 'Volume']]

# Step 3: Calculate Key Metrics
df['Daily_Return'] = df['Close'].pct_change() * 100
df['MA20'] = df['Close'].rolling(window=20).mean()
df['MA50'] = df['Close'].rolling(window=50).mean()
df['Volatility'] = df['Daily_Return'].rolling(window=30).std() * np.sqrt(252)
# Relative Strength Index (RSI)
def calculate_rsi(data, periods=14):
    delta = data.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=periods).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=periods).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))
df['RSI'] = calculate_rsi(df['Close'])
# Bollinger Bands
df['BB_Middle'] = df['Close'].rolling(window=20).mean()
df['BB_Std'] = df['Close'].rolling(window=20).std()
df['BB_Upper'] = df['BB_Middle'] + 2 * df['BB_Std']
df['BB_Lower'] = df['BB_Middle'] - 2 * df['BB_Std']

# Set seaborn style
sns.set(style='whitegrid')

# Q2: What is the trend of the stock price over time?
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['Close'], label='Close Price', color='blue')
plt.plot(df.index, df['MA20'], label='20-Day MA', color='orange')
plt.plot(df.index, df['MA50'], label='50-Day MA', color='green')
plt.title('Q2: Reliance Industries - Stock Price and Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price (INR)')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('q2_price_ma.png')
plt.close()

# Q3: How volatile is the stock?
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['Volatility'], color='red')
plt.title('Q3: Reliance Industries - 30-Day Volatility')
plt.xlabel('Date')
plt.ylabel('Annualized Volatility (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('q3_volatility.png')
plt.close()

# Q4: What is the distribution of daily returns?
plt.figure(figsize=(10, 6))
sns.histplot(df['Daily_Return'].dropna(), bins=50, kde=True, color='purple')
plt.title('Q4: Distribution of Daily Returns - Reliance Industries')
plt.xlabel('Daily Return (%)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('q4_returns_dist.png')
plt.close()

# Q5: How does trading volume vary over time?
plt.figure(figsize=(12, 6))
plt.bar(df.index, df['Volume'], color='gray')
plt.title('Q5: Reliance Industries - Trading Volume Over Time')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('q5_volume.png')
plt.close()

# Q6: What is the correlation between variables?
correlation_matrix = df[['Close', 'Volume', 'Daily_Return', 'Volatility', 'RSI']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Q6: Correlation Matrix - Reliance Industries')
plt.tight_layout()
plt.savefig('q6_correlation.png')
plt.close()

# Q7: What are the summary statistics of the stock price?
print("\nQ7: Summary Statistics for Close Price:")
print(df['Close'].describe())

# Q8: What are the summary statistics of daily returns?
print("\nQ8: Summary Statistics for Daily Returns:")
print(df['Daily_Return'].describe())

# Q9: What is the annualized return of the stock?
avg_return = df['Daily_Return'].mean()
annualized_return = ((1 + avg_return/100) ** 252 - 1) * 100
print(f"\nQ9: Annualized Return: {annualized_return:.2f}%")

# Q10: What is the average volatility?
avg_volatility = df['Volatility'].mean()
print(f"\nQ10: Average Annualized Volatility: {avg_volatility:.2f}%")

# Q11: How does RSI indicate overbought or oversold conditions?
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['RSI'], color='purple')
plt.axhline(70, color='red', linestyle='--', label='Overbought (70)')
plt.axhline(30, color='green', linestyle='--', label='Oversold (30)')
plt.title('Q11: Reliance Industries - Relative Strength Index (RSI)')
plt.xlabel('Date')
plt.ylabel('RSI')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('q11_rsi.png')
plt.close()

# Q12: How do Bollinger Bands indicate price boundaries?
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['Close'], label='Close Price', color='blue')
plt.plot(df.index, df['BB_Upper'], label='Upper Bollinger Band', color='red')
plt.plot(df.index, df['BB_Middle'], label='20-Day MA', color='orange')
plt.plot(df.index, df['BB_Lower'], label='Lower Bollinger Band', color='green')
plt.title('Q12: Reliance Industries - Bollinger Bands')
plt.xlabel('Date')
plt.ylabel('Price (INR)')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('q12_bollinger.png')
plt.close()

# Q13: What is the maximum drawdown?
cum_returns = (1 + df['Daily_Return'] / 100).cumprod()
peak = cum_returns.cummax()
drawdown = (cum_returns - peak) / peak * 100
max_drawdown = drawdown.min()
print(f"\nQ13: Maximum Drawdown: {max_drawdown:.2f}%")

# Q14: How does the stock perform in different months?
df['Month'] = df.index.month
monthly_returns = df.groupby('Month')['Daily_Return'].mean()
monthly_returns.index = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
plt.figure(figsize=(10, 6))
monthly_returns.plot(kind='bar', color='teal')
plt.title('Q14: Average Monthly Returns - Reliance Industries')
plt.xlabel('Month')
plt.ylabel('Average Daily Return (%)')
plt.tight_layout()
plt.savefig('q14_monthly_returns.png')
plt.close()

# Q15: What are the key financial highlights from recent data?
print("\nQ15: Key Financial Highlights (as of July 2025):")
print("Market Cap: ₹18,77,765.90 Crore")
print("1-Year Stock Performance: -7.0%")
print("Q1 FY26 Consolidated Net Profit: ₹26,994 Crore (up 39% QoQ)")
print("Revenue for Q1 FY26: ₹2,48,000 Crore")
print("Source: Web data and posts on X")

# Additional Visualization for Q13: Maximum Drawdown
plt.figure(figsize=(12, 6))
plt.plot(df.index, drawdown, color='orange')
plt.title('Q13: Reliance Industries - Drawdown Over Time')
plt.xlabel('Date')
plt.ylabel('Drawdown (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('q13_drawdown.png')
plt.close()
```
```

### Questions Addressed
1. **Are there any missing values in the dataset?**
   - Checks for missing values and removes them to ensure data integrity.
2. **What is the trend of the stock price over time?**
   - Visualizes closing price with 20-day and 50-day moving averages to identify trends.
3. **How volatile is the stock?**
   - Plots 30-day annualized volatility to assess risk fluctuations.
4. **What is the distribution of daily returns?**
   - Shows a histogram with KDE of daily returns to understand return patterns.
5. **How does trading volume vary over time?**
   - Displays trading volume over time to gauge market activity.
6. **What is the correlation between variables?**
   - Creates a heatmap to show correlations between Close, Volume, Daily Returns, Volatility, and RSI.
7. **What are the summary statistics of the stock price?**
   - Provides descriptive statistics for the Close price (mean, std, min, max, etc.).
8. **What are the summary statistics of daily returns?**
   - Summarizes daily returns statistics to understand return variability.
9. **What is the annualized return of the stock?**
   - Calculates the annualized return based on average daily returns.
10. **What is the average volatility?**
    - Computes the average annualized volatility over the period.
11. **How does RSI indicate overbought or oversold conditions?**
    - Plots the Relative Strength Index (RSI) with thresholds at 70 (overbought) and 30 (oversold).
12. **How do Bollinger Bands indicate price boundaries?**
    - Visualizes Bollinger Bands to show price volatility and potential reversal points.
13. **What is the maximum drawdown?**
    - Calculates and plots the maximum drawdown to assess the largest loss from a peak.
14. **How does the stock perform in different months?**
    - Analyzes average daily returns by month to identify seasonal patterns.
15. **What are the key financial highlights from recent data?**
    - Summarizes real-world financial data, including market cap, 1-year performance, and Q1 FY26 financials.

### Visualizations
The script generates nine PNG files:
- `q2_price_ma.png`: Stock price with moving averages.
- `q3_volatility.png`: 30-day volatility over time.
- `q4_returns_dist.png`: Distribution of daily returns.
- `q5_volume.png`: Trading volume over time.
- `q6_correlation.png`: Correlation heatmap.
- `q11_rsi.png`: RSI with overbought/oversold thresholds.
- `q12_bollinger.png`: Bollinger Bands with closing price.
- `q13_drawdown.png`: Drawdown over time.
- `q14_monthly_returns.png`: Average monthly returns bar chart.



### Notes
- **Data Source**: Uses `yfinance` to fetch data from Yahoo Finance. Verify data accuracy with sources like NSE India or Moneycontrol.
- **Real-Life Context**: Incorporates financial highlights from web sources (e.g., market cap ₹18,77,765.90 Crore, Q1 FY26 profit ₹26,994 Crore).
- **Limitations**: `yfinance` may have occasional data gaps or API issues. Adjust the date range or metrics as needed.
- **Customization**: Add more metrics (e.g., MACD, ATR) or extend the date range for deeper analysis.
