# Case study using the provided sales_data_sample.csv dataset. 
- This case study will focus on analyzing sales performance, identifying top-selling products, and exploring customer purchase patterns using Python with pandas and visualization libraries.

```x-python

```python
# Sales Data Analysis Case Study
# Dataset: sales_data_sample.csv from https://github.com/Pankaj-Str/Complete-Python-Mastery
# Objective: Analyze sales performance, product popularity, and customer patterns

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set plot style
plt.style.use('seaborn')
%matplotlib inline

# 1. Load and Inspect the Data
# Reading the CSV file
df = pd.read_csv('sales_data_sample.csv', encoding='latin1')

# Display basic information
print("Dataset Info:")
print(df.info())
print("\nFirst 5 rows:")
print(df.head())

# 2. Data Cleaning
# Convert ORDERDATE to datetime
df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'])

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing ADDRESSLINE2 with 'Unknown'
df['ADDRESSLINE2'] = df['ADDRESSLINE2'].fillna('Unknown')

# Drop rows with missing critical columns (if any)
df = df.dropna(subset=['CUSTOMERNAME', 'SALES'])

# 3. Exploratory Data Analysis
# 3.1 Total Sales by Year
yearly_sales = df.groupby('YEAR_ID')['SALES'].sum().reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(x='YEAR_ID', y='SALES', data=yearly_sales)
plt.title('Total Sales by Year')
plt.ylabel('Total Sales ($)')
plt.xlabel('Year')
plt.savefig('yearly_sales.png')
plt.show()

# 3.2 Top 5 Product Lines by Sales
product_sales = df.groupby('PRODUCTLINE')['SALES'].sum().sort_values(ascending=False).head(5)
plt.figure(figsize=(10, 6))
product_sales.plot(kind='bar')
plt.title('Top 5 Product Lines by Total Sales')
plt.ylabel('Total Sales ($)')
plt.xlabel('Product Line')
plt.xticks(rotation=45)
plt.savefig('top_product_lines.png')
plt.show()

# 3.3 Sales by Territory
territory_sales = df.groupby('TERRITORY')['SALES'].sum().reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(x='TERRITORY', y='SALES', data=territory_sales)
plt.title('Sales by Territory')
plt.ylabel('Total Sales ($)')
plt.xlabel('Territory')
plt.savefig('territory_sales.png')
plt.show()

# 3.4 Monthly Sales Trend
df['MONTH'] = df['ORDERDATE'].dt.month
monthly_sales = df.groupby(['YEAR_ID', 'MONTH'])['SALES'].sum().reset_index()
plt.figure(figsize=(12, 6))
sns.lineplot(x='MONTH', y='SALES', hue='YEAR_ID', data=monthly_sales)
plt.title('Monthly Sales Trend by Year')
plt.ylabel('Total Sales ($)')
plt.xlabel('Month')
plt.savefig('monthly_sales_trend.png')
plt.show()

# 4. Customer Analysis
# 4.1 Top 5 Customers by Sales
top_customers = df.groupby('CUSTOMERNAME')['SALES'].sum().sort_values(ascending=False).head(5)
plt.figure(figsize=(10, 6))
top_customers.plot(kind='bar')
plt.title('Top 5 Customers by Total Sales')
plt.ylabel('Total Sales ($)')
plt.xlabel('Customer Name')
plt.xticks(rotation=45)
plt.savefig('top_customers.png')
plt.show()

# 4.2 Deal Size Distribution
deal_size_counts = df['DEALSIZE'].value_counts()
plt.figure(figsize=(8, 6))
deal_size_counts.plot(kind='pie', autopct='%1.1f%%')
plt.title('Distribution of Deal Sizes')
plt.ylabel('')
plt.savefig('deal_size_distribution.png')
plt.show()

# 5. Product Performance
# 5.1 Top 5 Products by Quantity Ordered
top_products = df.groupby('PRODUCTCODE')['QUANTITYORDERED'].sum().sort_values(ascending=False).head(5)
plt.figure(figsize=(10, 6))
top_products.plot(kind='bar')
plt.title('Top 5 Products by Quantity Ordered')
plt.ylabel('Total Quantity Ordered')
plt.xlabel('Product Code')
plt.savefig('top_products.png')
plt.show()

# 6. Summary Statistics
print("\nSummary Statistics:")
print(df['SALES'].describe())
print("\nTop 5 Countries by Sales:")
print(df.groupby('COUNTRY')['SALES'].sum().sort_values(ascending=False).head(5))

# 7. Save cleaned dataset
df.to_csv('cleaned_sales_data.csv', index=False)
print("\nCleaned dataset saved as 'cleaned_sales_data.csv'")
```

```

This case study performs the following analyses:
1. Loads and inspects the dataset
2. Cleans the data by handling missing values and converting date formats
3. Analyzes sales trends by year, product line, territory, and month
4. Examines customer purchasing patterns and deal size distribution
5. Identifies top-performing products by quantity ordered
6. Generates visualizations for each analysis
7. Saves the cleaned dataset for future use

The code uses pandas for data manipulation, matplotlib and seaborn for visualization, and produces multiple plots saved as PNG files. Each section includes clear visualizations to support business insights, such as identifying high-performing products and key markets.[](https://github.com/Pankaj-Str/Complete-Python-Mastery)