# Product Sales Dataset Case Study

### **Step 1: Creating a Product Sales Dataset using Pandas**

We will manually create the dataset using `pandas.DataFrame`.

```python
import pandas as pd

# Creating a dataset
data = {
    "Product_ID": [101, 102, 103, 104, 105, 101, 102, 103, 104, 105],
    "Product_Name": ["Laptop", "Smartphone", "Shoes", "Headphones", "T-Shirt", 
                     "Laptop", "Smartphone", "Shoes", "Headphones", "T-Shirt"],
    "Category": ["Electronics", "Electronics", "Clothing", "Electronics", "Clothing",
                 "Electronics", "Electronics", "Clothing", "Electronics", "Clothing"],
    "Store_ID": [201, 202, 203, 204, 205, 201, 202, 203, 204, 205],
    "Store_Location": ["New York", "Los Angeles", "Chicago", "Houston", "San Francisco",
                        "New York", "Los Angeles", "Chicago", "Houston", "San Francisco"],
    "Date": pd.date_range(start="2024-01-01", periods=10, freq="D"),
    "Quantity_Sold": [5, 3, 8, 6, 7, 4, 5, 7, 3, 6],
    "Unit_Price": [800, 600, 50, 150, 20, 820, 620, 55, 160, 22]
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Adding Total Sales column
df["Total_Sales"] = df["Quantity_Sold"] * df["Unit_Price"]

# Display dataset
print(df)
```

***

### **Step 2: Data Exploration**

#### **Basic Information**

```python
# Check dataset structure
print(df.info())

# Summary statistics
print(df.describe())

# Checking for missing values
print(df.isnull().sum())
```

***

### **Step 3: Data Analysis using Pandas**

#### **1. Total Sales by Category**

```python
sales_by_category = df.groupby("Category")["Total_Sales"].sum()
print(sales_by_category)
```

#### **2. Best-Selling Products (By Quantity Sold)**

```python
best_selling_products = df.groupby("Product_Name")["Quantity_Sold"].sum().sort_values(ascending=False)
print(best_selling_products)
```

#### **3. Top Stores by Sales**

```python
top_stores = df.groupby("Store_Location")["Total_Sales"].sum().sort_values(ascending=False)
print(top_stores)
```

#### **4. Average Sales Price per Category**

```python
avg_price_category = df.groupby("Category")["Unit_Price"].mean()
print(avg_price_category)
```

***

### **Step 4: Saving Processed Data**

```python
df.to_csv("processed_product_sales.csv", index=False)
```

***

### **Conclusion**

* **Created a product sales dataset** using Pandas
* **Performed exploratory data analysis** (total sales, best products, top stores)
* **Used only Pandas** for all operations

