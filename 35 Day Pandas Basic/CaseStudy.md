# Pandas Case Study: Analyzing Sales Data
# This case study introduces beginners to basic Pandas operations using a sample sales dataset

import pandas as pd
import numpy as np

# Step 1: Create a sample sales dataset
data = {
    'order_id': [1, 2, 3, 4, 5, 6],
    'product': ['Laptop', 'Phone', 'Tablet', 'Laptop', 'Phone', 'Tablet'],
    'category': ['Electronics', 'Electronics', 'Electronics', 'Electronics', 'Electronics', 'Electronics'],
    'quantity': [1, 2, 1, 3, 1, 2],
    'price': [999.99, 499.99, 299.99, 999.99, 499.99, 299.99],
    'date': ['2025-01-01', '2025-01-02', '2025-01-02', '2025-01-03', '2025-01-03', '2025-01-04']
}
df = pd.DataFrame(data)

# Step 2: Display basic information about the dataset
print("Step 2: Basic Dataset Information")
print("\nFirst 5 rows of the dataset:")
print(df.head())
print("\nDataset Info:")
print(df.info())
print("\nBasic Statistics:")
print(df.describe())

# Step 3: Calculate total revenue (quantity * price)
df['total_revenue'] = df['quantity'] * df['price']
print("\nStep 3: Dataset with Total Revenue")
print(df[['order_id', 'product', 'quantity', 'price', 'total_revenue']])

# Step 4: Group by product and calculate total quantity sold and revenue
product_summary = df.groupby('product').agg({
    'quantity': 'sum',
    'total_revenue': 'sum'
}).reset_index()
print("\nStep 4: Product Summary")
print(product_summary)

# Step 5: Find the best-selling product by quantity
best_seller = product_summary.loc[product_summary['quantity'].idxmax()]
print("\nStep 5: Best-Selling Product")
print(f"Best-selling product: {best_seller['product']} with {best_seller['quantity']} units sold")

# Step 6: Filter orders with total revenue > $1000
high_value_orders = df[df['total_revenue'] > 1000]
print("\nStep 6: High-Value Orders (> $1000)")
print(high_value_orders[['order_id', 'product', 'total_revenue']])

# Step 7: Convert date column to datetime and extract month
df['date'] = pd.to_datetime(df['date'])
df['month'] = df['date'].dt.month
daily_sales = df.groupby('date').agg({
    'total_revenue': 'sum'
}).reset_index()
print("\nStep 7: Daily Sales Summary")
print(daily_sales)

# Step 8: Save the processed data to a CSV file
df.to_csv('processed_sales_data.csv', index=False)
print("\nStep 8: Data saved to 'processed_sales_data.csv'")
