# Step-by-step case study example using Pandas to analyze a dataset of sales transactions.

```python
import pandas as pd
import numpy as np

# Step 1: Create sample sales data
data = {
    'order_id': [1, 2, 3, 4, 5, 6, 7, 8],
    'customer': ['John', 'Alice', 'Bob', 'Alice', 'John', 'Bob', 'Charlie', 'Alice'],
    'product': ['Laptop', 'Phone', 'Tablet', 'Laptop', 'Phone', 'Tablet', 'Laptop', 'Monitor'],
    'quantity': [1, 2, 1, 1, 3, 2, 1, 1],
    'price': [1000, 500, 300, 1000, 500, 300, 1000, 200],
    'date': ['2023-01-01', '2023-01-02', '2023-01-02', '2023-01-03', 
             '2023-01-04', '2023-01-04', '2023-01-05', '2023-01-05']
}

# Step 2: Create DataFrame
df = pd.DataFrame(data)

# Step 3: Data Cleaning
# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])

# Check for missing values
print("Missing values:\n", df.isnull().sum())

# Step 4: Basic Data Analysis
# Calculate total revenue per order
df['total_revenue'] = df['quantity'] * df['price']

# Step 5: Grouping and Aggregation
# Total revenue by customer
customer_revenue = df.groupby('customer')['total_revenue'].sum().reset_index()
print("\nTotal Revenue by Customer:\n", customer_revenue)

# Step 6: Product Analysis
# Most popular products by quantity sold
product_sales = df.groupby('product')['quantity'].sum().reset_index()
print("\nProduct Sales by Quantity:\n", product_sales)

# Step 7: Time-based Analysis
# Sales by date
daily_sales = df.groupby('date')['total_revenue'].sum().reset_index()
print("\nDaily Sales:\n", daily_sales)

# Step 8: Customer Behavior Analysis
# Average order value per customer
avg_order_value = df.groupby('customer')['total_revenue'].mean().reset_index()
avg_order_value.columns = ['customer', 'avg_order_value']
print("\nAverage Order Value by Customer:\n", avg_order_value)

# Step 9: Filtering
# High-value orders (total revenue > 1000)
high_value_orders = df[df['total_revenue'] > 1000]
print("\nHigh Value Orders (>1000):\n", high_value_orders)

# Step 10: Data Export
# Export results to CSV
customer_revenue.to_csv('customer_revenue.csv', index=False)
product_sales.to_csv('product_sales.csv', index=False)

print("\nResults exported to 'customer_revenue.csv' and 'product_sales.csv'")
```

This case study demonstrates common Pandas operations:
1. Creating a sample dataset
2. Converting to DataFrame
3. Cleaning data (date conversion, checking for missing values)
4. Calculating derived metrics
5. Grouping and aggregating data
6. Analyzing product sales
7. Time-based analysis
8. Customer behavior analysis
9. Filtering for specific conditions
10. Exporting results to CSV files

---------------------------------


# Pandas Step-by-Step Example Guide
*Updated: June 25, 2025*

## 1. What is Pandas?
Pandas is a powerful Python library for data manipulation and analysis. It provides data structures like Series and DataFrames, which are ideal for handling structured data, such as tabular data, time series, and more.

```python
import pandas as pd
import numpy as np
```

## 2. Series and DataFrames
- **Series**: A one-dimensional array-like object that can hold data of any type (integers, strings, floats, etc.). It has an index for labeling data.
- **DataFrame**: A two-dimensional, tabular data structure with labeled rows and columns, similar to a spreadsheet or SQL table.

```python
# Creating a Series
series = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print("Series:\n", series)

# Creating a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)
print("\nDataFrame:\n", df)
```

## 3. Creating DataFrames
DataFrames can be created from dictionaries, lists, or other data structures.

```python
# From a dictionary
data = {'Product': ['Apple', 'Banana', 'Orange'], 'Price': [1.0, 0.5, 0.75]}
df = pd.DataFrame(data, index=['P1', 'P2', 'P3'])
print("DataFrame from dictionary:\n", df)

# From a list of dictionaries
list_data = [{'Product': 'Apple', 'Price': 1.0}, {'Product': 'Banana', 'Price': 0.5}]
df_list = pd.DataFrame(list_data)
print("\nDataFrame from list:\n", df_list)
```

## 4. Reading and Writing Data
Pandas supports reading from and writing to various file formats like CSV, Excel, and JSON.

```python
# Writing DataFrame to CSV
df.to_csv('products.csv', index=True)

# Reading from CSV
df_read = pd.read_csv('products.csv', index_col=0)
print("Read from CSV:\n", df_read)
```

## 5. Data Types and Missing Values
Pandas automatically infers data types, but you can inspect and handle missing values.

```python
# Checking data types
print("Data types:\n", df.dtypes)

# Introducing missing values
df_with_na = df.copy()
df_with_na.loc['P1', 'Price'] = np.nan
print("\nDataFrame with missing values:\n", df_with_na)

# Checking for missing values
print("\nMissing values:\n", df_with_na.isna())
```

## 6. Indexing Methods: loc and iloc
- `loc`: Access data by label/index.
- `iloc`: Access data by integer position.

```python
# Using loc
print("Using loc (select P1):\n", df.loc['P1'])

# Using iloc
print("\nUsing iloc (select first row):\n", df.iloc[0])
```

## 7. Boolean Indexing
Filter rows based on conditions using boolean masks.

```python
# Select rows where Price > 0.6
print("Boolean indexing (Price > 0.6):\n", df[df['Price'] > 0.6])
```

## 8. Selection Based on Conditions
Combine conditions for more complex filtering.

```python
# Select rows where Product is 'Apple' or Price > 0.6
condition = (df['Product'] == 'Apple') | (df['Price'] > 0.6)
print("Complex condition:\n", df[condition])
```

## 9. Adding and Deleting Columns
Modify DataFrames by adding or removing columns.

```python
# Adding a new column
df['Stock'] = [100, 200, 150]
print("After adding Stock column:\n", df)

# Deleting a column
df = df.drop('Stock', axis=1)
print("\nAfter deleting Stock column:\n", df)
```

## 10. Handling Missing Data
Handle missing values by filling or dropping them.

```python
# Filling missing values
df_with_na['Price'] = df_with_na['Price'].fillna(df_with_na['Price'].mean())
print("After filling missing values:\n", df_with_na)

# Dropping rows with missing values
df_dropped = df_with_na.dropna()
print("\nAfter dropping missing values:\n", df_dropped)
```

## 11. Grouping and Aggregation
Group data by a column and perform aggregations like sum, mean, etc.

```python
# Adding a Category column for grouping
df['Category'] = ['Fruit', 'Fruit', 'Fruit']
grouped = df.groupby('Category').agg({'Price': ['mean', 'sum']})
print("Grouped by Category:\n", grouped)
```

## 12. Merging and Joining DataFrames
Combine DataFrames using merge or join operations.

```python
# Creating another DataFrame
df2 = pd.DataFrame({'Product': ['Apple', 'Banana'], 'Region': ['North', 'South']})

# Merging DataFrames
merged = pd.merge(df, df2, on='Product', how='left')
print("Merged DataFrame:\n", merged)
```

