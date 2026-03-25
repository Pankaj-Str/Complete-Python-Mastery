# **Grouping Data in Pandas**  
*(Using `groupby()` – The Most Powerful Tool in Pandas)*

---

## What is Grouping?

**Grouping** = Split data → Apply a function → Combine results  
(Split-Apply-Combine pattern)

Think of it like **Excel Pivot Tables** or SQL `GROUP BY`.

---

## Simple Example (Step-by-Step)

```python
# 1. Import pandas
import pandas as pd

# 2. Create sample sales data
data = {
    'Store': ['North', 'South', 'North', 'East', 'South', 'East', 'North'],
    'Product': ['Laptop', 'Phone', 'Laptop', 'Tablet', 'Phone', 'Laptop', 'Tablet'],
    'Sales': [1200, 800, 1500, 600, 900, 1100, 700],
    'Quantity': [2, 3, 3, 1, 4, 2, 2]
}

df = pd.DataFrame(data)
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

## `df.groupby()` – The Magic Starts Here

### 1. **Group by One Column** → Total Sales per Store

```python
# Group by 'Store' and sum all numeric columns
store_summary = df.groupby('Store').sum()
print("\nTotal Sales & Quantity by Store:")
print(store_summary)
```

**Output:**
```
       Sales  Quantity
Store                 
East    1700         3
North   3400         7
South   1700         7
```

> **Note:** Non-numeric columns (like `Product`) are **dropped** automatically.

---

### 2. **Group by One Column, Select One Column**

```python
# Total Sales per Store (only Sales column)
sales_by_store = df.groupby('Store')['Sales'].sum()
print("\nSales by Store:")
print(sales_by_store)
```

**Output:**
```
Store
East     1700
North    3400
South    1700
Name: Sales, dtype: int64
```

---

### 3. **Multiple Aggregations** (sum, mean, count)

```python
# Use .agg() to apply multiple functions
summary = df.groupby('Store').agg({
    'Sales': ['sum', 'mean', 'count'],
    'Quantity': 'sum'
})
print("\nAdvanced Summary:")
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

---

### 4. **Group by Multiple Columns**

```python
# Sales by Store AND Product
by_store_product = df.groupby(['Store', 'Product'])['Sales'].sum()
print("\nSales by Store & Product:")
print(by_store_product)
```

**Output:**
```
Store  Product
East   Laptop     1100
       Tablet      600
North  Laptop     2700
       Tablet      700
South  Phone      1700
Name: Sales, dtype: int64
```

> Use `.unstack()` to turn into a table:

```python
print(by_store_product.unstack(fill_value=0))
```

**Output:**
```
Product  Laptop  Phone  Tablet
Store                         
East       1100      0     600
North      2700      0     700
South         0   1700       0
```

---

### 5. **Custom Function with `apply()`**

```python
# Add a column: "High Value" if Sales > 1000
def label_sales(group):
    group['High_Value'] = group['Sales'] > 1000
    return group

result = df.groupby('Store').apply(label_sales)
print("\nWith Custom Label:")
print(result[['Store', 'Product', 'Sales', 'High_Value']])
```

**Output:**
```
   Store Product  Sales  High_Value
0  North  Laptop   1200        True
1  South   Phone    800       False
2  North  Laptop   1500        True
3   East  Tablet    600       False
4  South   Phone    900       False
5   East  Laptop   1100        True
6  North  Tablet    700       False
```

---

## Common Aggregation Functions

| Function | What it does |
|--------|-------------|
| `.sum()` | Total |
| `.mean()` | Average |
| `.median()` | Middle value |
| `.min()`, `.max()` | Smallest / largest |
| `.count()` | Number of rows |
| `.nunique()` | Number of unique values |
| `.first()`, `.last()` | First / last in group |

---

## Quick Cheat Sheet

| Goal | Code |
|------|------|
| Total sales by store | `df.groupby('Store')['Sales'].sum()` |
| Multiple stats | `df.groupby('Store').agg({'Sales': 'sum', 'Quantity': 'mean'})` |
| Group by 2 columns | `df.groupby(['Store', 'Product']).sum()` |
| Count rows per group | `df.groupby('Store').size()` |
| Top item in each group | `df.groupby('Store').apply(lambda x: x.nlargest(1, 'Sales'))` |

---

## Practice: Try This!

```python
# Dataset
practice = pd.DataFrame({
    'Team': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Player': ['X', 'Y', 'Z', 'W', 'X', 'Y'],
    'Points': [10, 15, 8, 20, 12, 18]
})

# Tasks:
# 1. Total points per team
# 2. Average points per player
# 3. Player with max points in each team
```

**Solutions:**

```python
# 1
print(practice.groupby('Team')['Points'].sum())

# 2
print(practice.groupby('Player')['Points'].mean())

# 3
print(practice.groupby('Team').apply(lambda x: x.loc[x['Points'].idxmax()]))
```

---

## Visual Summary

```
Original Data → groupby('Store') → [North Group], [South Group], [East Group]
                         ↓
                   Apply sum(), mean(), etc.
                         ↓
                  Combined Result (Summary Table)
```

---

## You're Now a **Pandas Grouping Pro**!

Use `groupby()` to:
- Summarize sales
- Analyze user behavior
- Build reports
- Prepare data for charts

---

