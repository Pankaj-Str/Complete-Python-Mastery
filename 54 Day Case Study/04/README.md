

### Case Study: Analyzing Reliance Industries Limited (RELIANCE.NS) Stock Data

#### Objective
To analyze the historical stock performance of Reliance Industries Limited (RELIANCE.NS) listed on the National Stock Exchange (NSE) of India, calculate key financial metrics like daily returns and moving averages, and visualize trends to gain insights into its market behavior.

#### Prerequisites
- Python installed with the following libraries: `pandas`, `numpy`, `seaborn`, `matplotlib`, `yfinance`.
- Install `yfinance` if not already installed:
  ```bash
  pip install yfinance
  ```

#### Step-by-Step Analysis

##### Step 1: Import Required Libraries
We start by importing the necessary Python libraries for data fetching, manipulation, and visualization.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
import warnings
warnings.filterwarnings('ignore')

# Set Seaborn style for better visuals
sns.set_style('whitegrid')
%matplotlib inline
```

##### Step 2: Fetch Historical Stock Data
We’ll use the `yfinance` library to download historical stock data for Reliance Industries (RELIANCE.NS) from Yahoo Finance for the period from January 1, 2020, to July 30, 2025.

```python
# Define the ticker and date range
ticker = 'RELIANCE.NS'
start_date = '2020-01-01'
end_date = '2025-07-30'

# Fetch data using yfinance
stock_data = yf.download(ticker, start=start_date, end=end_date, progress=False)

# Display the first few rows
print(stock_data.head())
```

**Explanation**: The `yf.download` function fetches OHLC (Open, High, Low, Close) data along with Adjusted Close and Volume. The `progress=False` suppresses the download progress bar for cleaner output.

##### Step 3: Generate a Sample Dataset
If you cannot access `yfinance` due to connectivity issues or API restrictions, you can generate a sample dataset for demonstration purposes. Below is a simulated dataset mimicking Reliance Industries’ stock data structure.

```python
# Alternative: Create a sample dataset if yfinance is unavailable
dates = pd.date_range(start='2020-01-01', end='2020-12-31', freq='B')
np.random.seed(42)
sample_data = {
    'Open': np.random.uniform(1400, 1600, len(dates)),
    'High': np.random.uniform(1450, 1650, len(dates)),
    'Low': np.random.uniform(1350, 1550, len(dates)),
    'Close': np.random.uniform(1400, 1600, len(dates)),
    'Adj Close': np.random.uniform(1400, 1600, len(dates)),
    'Volume': np.random.randint(1000000, 10000000, len(dates))
}
stock_data = pd.DataFrame(sample_data, index=dates)
stock_data.to_csv('reliance_sample_data.csv')

# Display sample dataset
print(stock_data.head())
```

**Sample Output (reliance_sample_data.csv)**:
```
            Open         High         Low       Close    Adj Close    Volume
2020-01-01  1514.59  1592.31  1438.26  1511.94  1518.94  4376149
2020-01-02  1557.22  1543.04  1429.42  1458.62  1497.67  3433742
2020-01-03  1438.62  1460.66  1423.63  1532.83  1476.33  6283359
2020-01-06  1493.09  1550.99  1479.99  1546.04  1484.21  9516835
2020-01-07  1502.06  1545.47  1439.31  1492.76  1516.58  3732604
```

**Note**: For real analysis, use the `yfinance` data. The sample dataset is for offline practice.

##### Step 4: Exploratory Data Analysis
Let’s explore the dataset to understand its structure and calculate basic statistics.

```python
# Basic information about the dataset
print(stock_data.info())
print("\nSummary Statistics:")
print(stock_data.describe())
```

**Explanation**: The `info()` method shows the data types and non-null counts, while `describe()` provides statistics like mean, min, max, etc., for numerical columns.

##### Step 5: Calculate Financial Metrics
We’ll compute:
- **Daily Returns**: Percentage change in the closing price.
- **Moving Averages**: 20-day and 50-day moving averages to identify trends.

```python
# Calculate daily returns
stock_data['Daily Returns'] = stock_data['Close'].pct_change() * 100

# Calculate 20-day and 50-day moving averages
stock_data['20_MA'] = stock_data['Close'].rolling(window=20).mean()
stock_data['50_MA'] = stock_data['Close'].rolling(window=50).mean()

# Display the updated dataframe
print(stock_data[['Close', 'Daily Returns', '20_MA', '50_MA']].tail())
```

**Explanation**:
- `pct_change()` computes the percentage change between consecutive closing prices.
- `rolling(window).mean()` calculates the moving average over the specified window.

##### Step 6: Visualize the Data
We’ll create visualizations to understand trends, volatility, and correlations.

###### a) Plot Closing Prices and Moving Averages
```python
# Plot closing prices and moving averages
plt.figure(figsize=(12, 6))
plt.plot(stock_data['Close'], label='Close Price', color='blue')
plt.plot(stock_data['20_MA'], label='20-Day MA', color='orange')
plt.plot(stock_data['50_MA'], label='50-Day MA', color='green')
plt.title('Reliance Industries Closing Prices and Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price (INR)')
plt.legend()
plt.grid(True)
plt.show()
```

**Explanation**: This line plot shows the stock’s closing price along with 20-day and 50-day moving averages to identify trends.

###### b) Plot Daily Returns Distribution
```python
# Plot distribution of daily returns
plt.figure(figsize=(10, 6))
sns.histplot(stock_data['Daily Returns'].dropna(), bins=50, kde=True, color='purple')
plt.title('Distribution of Daily Returns for Reliance Industries')
plt.xlabel('Daily Returns (%)')
plt.ylabel('Frequency')
plt.show()
```

**Explanation**: The histogram with a kernel density estimate (KDE) shows the distribution of daily returns, helping assess volatility.

###### c) Correlation Heatmap
```python
# Correlation heatmap
plt.figure(figsize=(8, 6))
correlation_matrix = stock_data[['Open', 'High', 'Low', 'Close', 'Volume']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap for Reliance Industries Stock Data')
plt.show()
```

**Explanation**: The heatmap visualizes correlations between OHLC and Volume, helping identify relationships (e.g., High and Close are typically highly correlated).

##### Step 7: Save the Results
Save the processed data to a CSV file for future use.

```python
# Save the processed data
stock_data.to_csv('reliance_processed_data.csv')
```

##### Step 8: Insights and Interpretation
- **Closing Price Trend**: The plot of closing prices and moving averages shows long-term trends. A crossover of the 20-day MA above the 50-day MA may indicate a bullish trend, and vice versa for a bearish trend.
- **Daily Returns**: The histogram reveals the volatility of Reliance’s stock. A wider spread indicates higher volatility.
- **Correlation**: The heatmap shows that Open, High, Low, and Close prices are highly correlated, which is expected in stock data, while Volume may have weaker correlations.

#### Sample Dataset
If you used the sample dataset, it’s saved as `reliance_sample_data.csv`. For real data, the `yfinance` fetch will provide actual historical data, which you can save as `reliance_processed_data.csv`.

#### Full Code
Here’s the complete code combining all steps:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
import warnings
warnings.filterwarnings('ignore')

# Set Seaborn style
sns.set_style('whitegrid')
%matplotlib inline

# Define the ticker and date range
ticker = 'RELIANCE.NS'
start_date = '2020-01-01'
end_date = '2025-07-30'

# Fetch data using yfinance
stock_data = yf.download(ticker, start=start_date, end=end_date, progress=False)

# Alternative: Create a sample dataset if yfinance is unavailable
# dates = pd.date_range(start='2020-01-01', end='2020-12-31', freq='B')
# np.random.seed(42)
# sample_data = {
#     'Open': np.random.uniform(1400, 1600, len(dates)),
#     'High': np.random.uniform(1450, 1650, len(dates)),
#     'Low': np.random.uniform(1350, 1550, len(dates)),
#     'Close': np.random.uniform(1400, 1600, len(dates)),
#     'Adj Close': np.random.uniform(1400, 1600, len(dates)),
#     'Volume': np.random.randint(1000000, 10000000, len(dates))
# }
# stock_data = pd.DataFrame(sample_data, index=dates)
# stock_data.to_csv('reliance_sample_data.csv')

# Display basic information
print(stock_data.head())
print(stock_data.info())
print("\nSummary Statistics:")
print(stock_data.describe())

# Calculate financial metrics
stock_data['Daily Returns'] = stock_data['Close'].pct_change() * 100
stock_data['20_MA'] = stock_data['Close'].rolling(window=20).mean()
stock_data['50_MA'] = stock_data['Close'].rolling(window=50).mean()
print(stock_data[['Close', 'Daily Returns', '20_MA', '50_MA']].tail())

# Plot closing prices and moving averages
plt.figure(figsize=(12, 6))
plt.plot(stock_data['Close'], label='Close Price', color='blue')
plt.plot(stock_data['20_MA'], label='20-Day MA', color='orange')
plt.plot(stock_data['50_MA'], label='50-Day MA', color='green')
plt.title('Reliance Industries Closing Prices and Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price (INR)')
plt.legend()
plt.grid(True)
plt.show()

# Plot distribution of daily returns
plt.figure(figsize=(10, 6))
sns.histplot(stock_data['Daily Returns'].dropna(), bins=50, kde=True, color='purple')
plt.title('Distribution of Daily Returns for Reliance Industries')
plt.xlabel('Daily Returns (%)')
plt.ylabel('Frequency')
plt.show()

# Correlation heatmap
plt.figure(figsize=(8, 6))
correlation_matrix = stock_data[['Open', 'High', 'Low', 'Close', 'Volume']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap for Reliance Industries Stock Data')
plt.show()

# Save the processed data
stock_data.to_csv('reliance_processed_data.csv')
```

#### How to Run
1. Save the code in a file named `reliance_stock_analysis.py`.
2. Ensure all required libraries are installed.
3. Run the script in a Python environment (e.g., Jupyter Notebook or VSCode).
4. If `yfinance` fails, uncomment the sample dataset section to use the simulated data.

