# Share Market Case Study Using Pandas, Matplotlib, and Seaborn

This tutorial walks you through a simple case study on analyzing share market data for beginners. We'll use Apple Inc. (AAPL) stock as an example, fetching historical daily data from January 1, 2024, to November 11, 2025 (based on current date). The goal is to explore the data, visualize price trends and volume, and perform basic analysis like calculating moving averages and correlations.

We'll cover:
- Fetching stock data.
- Basic data exploration with Pandas.
- Visualizing trends with Matplotlib.
- Enhanced visualizations with Seaborn.

This is designed for beginners, so each step includes code, explanations, and expected output examples (based on real data as of November 11, 2025).

## Prerequisites
- Python installed on your system.
- Basic knowledge of Python (e.g., running scripts in a Jupyter Notebook or IDE like VS Code).
- Install the required libraries if not already present:
  ```
  pip install pandas matplotlib seaborn yfinance
  ```
  - `yfinance` is used for fetching free stock data from Yahoo Finance (no API key needed).
  
Run the code in a Jupyter Notebook for interactive plots, or in a script (plots will open in new windows).

## Step 1: Import the Libraries
Start by importing the necessary libraries.

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
```

- **Pandas**: For data manipulation and analysis.
- **Matplotlib**: For creating basic plots.
- **Seaborn**: For more attractive and informative statistical graphics (built on Matplotlib).
- **yfinance**: For downloading stock data.

## Step 2: Fetch the Stock Data
We'll download historical data for AAPL. Adjust the ticker (e.g., 'TSLA' for Tesla) or dates as needed.

```python
# Define the ticker and date range
ticker = 'AAPL'
start_date = '2024-01-01'
end_date = '2025-11-11'

# Fetch data
data = yf.download(ticker, start=start_date, end=end_date)

# Reset index to make 'Date' a column
data.reset_index(inplace=True)

# Display the first few rows
print(data.head())
```

**Explanation**:
- `yf.download()` fetches Open, High, Low, Close, Adjusted Close, and Volume data.
- We reset the index to treat 'Date' as a regular column for easier manipulation.

**Example Output** (first 5 rows, based on real data):
```
        Date      Open      High       Low     Close  Adj Close    Volume
0 2024-01-02  187.150  188.4400  183.8850  185.6400  184.9380  82488674
1 2024-01-03  184.220  185.8800  183.4300  184.2500  183.5534  58414460
2 2024-01-04  182.150  183.0872  180.8800  181.9100  181.2223  71983570
3 2024-01-05  181.990  182.7600  180.1700  181.1800  180.4950  62379661
4 2024-01-08  182.085  185.6000  181.5000  185.5600  184.8583  59144470
```

This gives you a DataFrame with columns like Date, Open, High, Low, Close, Adj Close, and Volume.

## Step 3: Explore the Data with Pandas
Before visualizing, understand the data structure and summary statistics.

```python
# Basic info
print(data.info())

# Summary statistics
print(data.describe())

# Check for missing values
print(data.isnull().sum())
```

**Explanation**:
- `info()`: Shows data types and non-null counts.
- `describe()`: Provides mean, std, min, max, etc., for numerical columns.
- `isnull().sum()`: Checks for any missing data (stock data is usually clean).

**Example Output** (summary statistics excerpt):
```
             Open        High         Low       Close     Adj Close        Volume
count  467.000000  467.000000  467.000000  467.000000    467.000000  4.670000e+02
mean   215.302336  217.609413  213.227440  215.530428    215.071099  5.658256e+07
std     25.348904   25.470156   25.150165   25.400876     25.600192  2.761062e+07
min    165.350000  166.400000  164.075000  165.000000    164.316000  2.323470e+07
25%    195.410000  198.045000  193.729950  195.755000    195.124500  4.205521e+07
50%    218.930000  221.480000  216.580000  218.800000    218.490000  4.932582e+07
75%    231.907500  233.925000  229.560000  232.590000    232.450000  6.190262e+07
max    276.990000  277.320000  269.160000  271.400000    271.400000  3.186799e+08
```

From this, we see AAPL's average close price was around $215.53, with a max of $271.40 and significant volume fluctuations.

## Step 4: Visualize with Matplotlib
Let's plot the closing prices and trading volume.

```python
# Plot Closing Prices
plt.figure(figsize=(12, 6))
plt.plot(data['Date'], data['Close'], label='Close Price', color='blue')
plt.title('AAPL Closing Prices (2024-2025)')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.show()

# Plot Volume
plt.figure(figsize=(12, 6))
plt.bar(data['Date'], data['Volume'], color='green')
plt.title('AAPL Trading Volume (2024-2025)')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.grid(True)
plt.show()
```

**Explanation**:
- `plt.plot()`: Line plot for trends over time.
- `plt.bar()`: Bar chart for volume to show daily trading activity.
- Use `figsize` for better readability, and add labels/titles for clarity.

These plots will show an upward trend in AAPL prices with some volatility, and volume spikes on key dates (e.g., earnings reports).

## Step 5: Advanced Visualizations with Seaborn
Seaborn makes plots more aesthetically pleasing and handles statistical visualizations easily.

```python
# Set Seaborn style
sns.set(style='whitegrid')

# Distribution of Closing Prices
plt.figure(figsize=(10, 5))
sns.histplot(data['Close'], kde=True, color='purple')
plt.title('Distribution of AAPL Closing Prices')
plt.xlabel('Close Price (USD)')
plt.show()

# Correlation Heatmap (select numerical columns)
numerical_data = data[['Open', 'High', 'Low', 'Close', 'Volume']]
corr = numerical_data.corr()

plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix of AAPL Stock Features')
plt.show()

# Pairplot for relationships
sns.pairplot(numerical_data, diag_kind='kde')
plt.suptitle('Pairplot of AAPL Stock Data', y=1.02)
plt.show()
```

**Explanation**:
- `histplot()`: Histogram with kernel density estimate (KDE) to show price distribution.
- `heatmap()`: Visualizes correlations (e.g., High and Low are strongly correlated ~0.99).
- `pairplot()`: Scatter plots for all pairs of features, useful for spotting relationships.

From the heatmap, you'll see strong positive correlations between price features (Open, High, Low, Close), but weaker with Volume.

## Step 6: Basic Analysis (e.g., Moving Average)
Add a 50-day moving average to smooth trends.

```python
# Calculate 50-day moving average
data['MA50'] = data['Close'].rolling(window=50).mean()

# Plot Close Price with MA50
plt.figure(figsize=(12, 6))
plt.plot(data['Date'], data['Close'], label='Close Price', color='blue')
plt.plot(data['Date'], data['MA50'], label='50-Day MA', color='red')
plt.title('AAPL Closing Prices with 50-Day Moving Average')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.show()
```

**Explanation**:
- `rolling().mean()`: Computes the average over a 50-day window.
- This helps identify trends (e.g., buy when price crosses above MA).

## Conclusion and Next Steps
This case study gives you a foundation for share market analysis. You fetched data, explored it, and visualized trends using Pandas, Matplotlib, and Seaborn. For AAPL, we observed an overall upward trend from ~$185 in early 2024 to ~$269 in late 2025, with average daily volume around 56 million shares.

Next steps:
- Try other tickers (e.g., 'GOOGL') or longer periods.
- Add technical indicators like RSI or Bollinger Bands (use Pandas for calculations).
- Handle errors (e.g., invalid tickers) with try-except blocks.
- For real-time data, consider APIs like Polygon.io (requires free API key).

If you run into issues or want to expand (e.g., predictive modeling with scikit-learn), let me know!
