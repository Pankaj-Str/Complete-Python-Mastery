# **Aggregation in Pandas**  
**`sum()` • `count()` • `mean()`**  
*(With Step-by-Step Examples)*

---

## What is Aggregation?

**Aggregation** = Taking many values → **reduce** them to **one value**  
(e.g., total, average, count)

Used **after `groupby()`** to summarize data.

---

## Sample Data

```python
import pandas as pd

# Create sample sales data
df = pd.DataFrame({
    'Store': ['North', 'South', 'North', 'East', 'South', 'East', 'North'],
    'Product': ['Laptop', 'Phone', 'Laptop', 'Tablet', 'Phone', 'Laptop', 'Tablet'],
    'Sales': [1200, 800, 1500, 600, 900, 1100, 700],
    'Quantity': [2, 3, 3, 1, 4, 2, 2]
})

print("Original Data:")
print(df)
```

**Output:**
```
    Store Product  Sales  Quantity
0  North  Laptop   1200         2
1  South   Phone    800         3
2  North  Laptop   1500         3
3   East  Tablet    600         1
4  South   Phone    900         4
5   East  Laptop   1100         2
6  North  Tablet    700         2
```

---

## 1. `sum()` – Total

### Total Sales per Store

```python
total_sales = df.groupby('Store')['Sales'].sum()
print("Total Sales by Store:")
print(total_sales)
```

**Output:**
```
Store
East     1700
North    3400
South    1700
Name: Sales, dtype: int64
```

> **Visualize it:**
```python
total_sales.plot(kind='bar', title='Total Sales by Store')
```

---

## 2. `count()` – How Many?

### Number of Sales Records per Store

```python
count_sales = df.groupby('Store')['Sales'].count()
print("Number of Sales by Store:")
print(count_sales)
```

**Output:**
```
Store
East     2
North    3
South    2
Name: Sales, dtype: int64
```

> Use `.size()` for same result (includes all columns):
```python
df.groupby('Store').size()
```

---

## 3. `mean()` – Average

### Average Sales per Store

```python
avg_sales = df.groupby('Store')['Sales'].mean()
print("Average Sales by Store:")
print(avg_sales)
```

**Output:**
```
Store
East      850.0
North    1133.333333
South     850.0
Name: Sales, dtype: float64
```

---

## Combine All Three: `agg()`

### One line → Multiple Stats

```python
summary = df.groupby('Store').agg({
    'Sales': ['sum', 'mean', 'count'],
    'Quantity': 'sum'
})

print("Full Summary:")
print(summary)
```

**Output:**
```
      Sales            Quantity
        sum   mean count     sum
Store                          
East   1700  850.0     2       3
North  3400 1133.3     3       7
South  1700  850.0     2       7
```

> **Flatten column names** (optional):
```python
summary.columns = ['_'.join(col) for col in summary.columns]
print(summary)
```

**Output:**
```
       Sales_sum  Sales_mean  Sales_count  Quantity_sum
Store                                                 
East        1700       850.0            2             3
North       3400      1133.3            3             7
South       1700       850.0            2             7
```

---

## Quick Examples (Copy-Paste)

| Goal | Code |
|------|------|
| Total sales per product | `df.groupby('Product')['Sales'].sum()` |
| Average quantity per store | `df.groupby('Store')['Quantity'].mean()` |
| Count of each product | `df.groupby('Product').size()` |
| Sum + Count in one go | `df.groupby('Store')['Sales'].agg(['sum', 'count'])` |

---

## Practice: Try This!

```python
# Dataset
practice = pd.DataFrame({
    'City': ['NY', 'LA', 'NY', 'LA', 'CHI'],
    'Item': ['Apple', 'Banana', 'Apple', 'Apple', 'Banana'],
    'Price': [1.0, 0.5, 1.2, 0.9, 0.6],
    'Units': [10, 15, 8, 12, 20]
})

# Tasks:
# 1. Total revenue (Price × Units) per city
# 2. Average price per item
# 3. Count how many times each item was sold
```

### Solution

```python
# 1. Add Revenue column
practice['Revenue'] = practice['Price'] * practice['Units']

# Group by City → sum of Revenue
print(practice.groupby('City')['Revenue'].sum())

# 2. Average price per item
print(practice.groupby('Item')['Price'].mean())

# 3. Count of sales per item
print(practice.groupby('Item').size())
```

---

## Cheat Sheet

| Function | Use |
|--------|-----|
| `.sum()` | Total |
| `.mean()` | Average |
| `.count()` | Number of non-null values |
| `.size()` | Total rows (including nulls) |
| `.agg(['sum','mean'])` | Multiple stats |
| `.agg({'Col': 'sum'})` | Custom per column |

---

## You're Done!

You now know how to:
- **Sum** sales
- **Count** transactions
- **Average** values
- **Combine** all with `agg()`

---

**Next Step?** Try:
```python
df.groupby('Store')['Sales'].describe()
```
→ Gives count, mean, std, min, max, quartiles in **one command**!
# Beginner Tutorial: **Aggregation in Pandas**  
**`sum()` • `count()` • `mean()`**  
*(With Step-by-Step Examples)*

---

## What is Aggregation?

**Aggregation** = Taking many values → **reduce** them to **one value**  
(e.g., total, average, count)

Used **after `groupby()`** to summarize data.

---

## Sample Data

```python
import pandas as pd

# Create sample sales data
df = pd.DataFrame({
    'Store': ['North', 'South', 'North', 'East', 'South', 'East', 'North'],
    'Product': ['Laptop', 'Phone', 'Laptop', 'Tablet', 'Phone', 'Laptop', 'Tablet'],
    'Sales': [1200, 800, 1500, 600, 900, 1100, 700],
    'Quantity': [2, 3, 3, 1, 4, 2, 2]
})

print("Original Data:")
print(df)
```

**Output:**
```
    Store Product  Sales  Quantity
0  North  Laptop   1200         2
1  South   Phone    800         3
2  North  Laptop   1500         3
3   East  Tablet    600         1
4  South   Phone    900         4
5   East  Laptop   1100         2
6  North  Tablet    700         2
```

---

## 1. `sum()` – Total

### Total Sales per Store

```python
total_sales = df.groupby('Store')['Sales'].sum()
print("Total Sales by Store:")
print(total_sales)
```

**Output:**
```
Store
East     1700
North    3400
South    1700
Name: Sales, dtype: int64
```

> **Visualize it:**
```python
total_sales.plot(kind='bar', title='Total Sales by Store')
```

---

## 2. `count()` – How Many?

### Number of Sales Records per Store

```python
count_sales = df.groupby('Store')['Sales'].count()
print("Number of Sales by Store:")
print(count_sales)
```

**Output:**
```
Store
East     2
North    3
South    2
Name: Sales, dtype: int64
```

> Use `.size()` for same result (includes all columns):
```python
df.groupby('Store').size()
```

---

## 3. `mean()` – Average

### Average Sales per Store

```python
avg_sales = df.groupby('Store')['Sales'].mean()
print("Average Sales by Store:")
print(avg_sales)
```

**Output:**
```
Store
East      850.0
North    1133.333333
South     850.0
Name: Sales, dtype: float64
```

---

## Combine All Three: `agg()`

### One line → Multiple Stats

```python
summary = df.groupby('Store').agg({
    'Sales': ['sum', 'mean', 'count'],
    'Quantity': 'sum'
})

print("Full Summary:")
print(summary)
```

**Output:**
```
      Sales            Quantity
        sum   mean count     sum
Store                          
East   1700  850.0     2       3
North  3400 1133.3     3       7
South  1700  850.0     2       7
```

> **Flatten column names** (optional):
```python
summary.columns = ['_'.join(col) for col in summary.columns]
print(summary)
```

**Output:**
```
       Sales_sum  Sales_mean  Sales_count  Quantity_sum
Store                                                 
East        1700       850.0            2             3
North       3400      1133.3            3             7
South       1700       850.0            2             7
```

---

## Quick Examples (Copy-Paste)

| Goal | Code |
|------|------|
| Total sales per product | `df.groupby('Product')['Sales'].sum()` |
| Average quantity per store | `df.groupby('Store')['Quantity'].mean()` |
| Count of each product | `df.groupby('Product').size()` |
| Sum + Count in one go | `df.groupby('Store')['Sales'].agg(['sum', 'count'])` |

---

## Practice: Try This!

```python
# Dataset
practice = pd.DataFrame({
    'City': ['NY', 'LA', 'NY', 'LA', 'CHI'],
    'Item': ['Apple', 'Banana', 'Apple', 'Apple', 'Banana'],
    'Price': [1.0, 0.5, 1.2, 0.9, 0.6],
    'Units': [10, 15, 8, 12, 20]
})

# Tasks:
# 1. Total revenue (Price × Units) per city
# 2. Average price per item
# 3. Count how many times each item was sold
```

### Solution

```python
# 1. Add Revenue column
practice['Revenue'] = practice['Price'] * practice['Units']

# Group by City → sum of Revenue
print(practice.groupby('City')['Revenue'].sum())

# 2. Average price per item
print(practice.groupby('Item')['Price'].mean())

# 3. Count of sales per item
print(practice.groupby('Item').size())
```

---

## Cheat Sheet

| Function | Use |
|--------|-----|
| `.sum()` | Total |
| `.mean()` | Average |
| `.count()` | Number of non-null values |
| `.size()` | Total rows (including nulls) |
| `.agg(['sum','mean'])` | Multiple stats |
| `.agg({'Col': 'sum'})` | Custom per column |

---

## You're Done!

You now know how to:
- **Sum** sales
- **Count** transactions
- **Average** values
- **Combine** all with `agg()`

---

**Next Step?** Try:
```python
df.groupby('Store')['Sales'].describe()
```
→ Gives count, mean, std, min, max, quartiles in **one command**!

