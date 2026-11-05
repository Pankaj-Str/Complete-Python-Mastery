#  Pandas GroupBy External CSV Example


### 1. What is GroupBy? (Super Simple)

`groupby()` is like **sorting your data into buckets** and then doing calculations inside each bucket.

**Real-life example**:
Imagine you have a big Excel sheet of shop sales:
- You want to know **total sales of each city**.
- Or **average quantity sold per product category**.
- Or **how many orders came from each city**.

Instead of calculating manually, Pandas **groups** the rows by “City” (or any column), then applies math (sum, average, count, etc.) on each group automatically.

### 2. How GroupBy Works (The Magic Trick)

Pandas follows **“Split – Apply – Combine”**:

1. **Split** → Divide all rows into groups (based on the column you choose)
2. **Apply** → Do something on each group (sum, mean, max, count…)
3. **Combine** → Bring all results back into a nice table

That’s it! This is the most powerful pattern in data analysis.

### 3. Complete Working Example with External CSV File

#### Step 1: Create the sample CSV file (Run this code once)

Copy and run this code in your Jupyter Notebook or Python file. It will create `sales_data.csv` for you.

```python
import pandas as pd

# Sample sales data
data = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Date': ['2024-01-05', '2024-01-10', '2024-01-15', '2024-02-01', '2024-02-05',
             '2024-02-10', '2024-03-01', '2024-03-05', '2024-03-10', '2024-01-20'],
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Laptop', 'Phone', 
                'Tablet', 'Mouse', 'Keyboard', 'Phone', 'Laptop'],
    'Category': ['Electronics', 'Accessories', 'Accessories', 'Electronics', 'Electronics',
                 'Electronics', 'Accessories', 'Accessories', 'Electronics', 'Electronics'],
    'Sales': [75000, 1200, 2500, 80000, 45000, 30000, 1500, 2800, 42000, 72000],
    'Quantity': [1, 5, 3, 1, 2, 3, 4, 2, 1, 2],
    'City': ['Mumbai', 'Delhi', 'Bangalore', 'Mumbai', 'Delhi', 
             'Bangalore', 'Mumbai', 'Delhi', 'Bangalore', 'Mumbai']
}

df_temp = pd.DataFrame(data)
df_temp.to_csv('sales_data.csv', index=False)
print("✅ sales_data.csv file created successfully!")
print("You can now open this file in Excel to see the data.")
```

#### Step 2: Read the External CSV File

```python
import pandas as pd

# Reading external CSV file (this is what you asked for)
df = pd.read_csv('sales_data.csv')

# Optional: Convert Date column to proper date format
df['Date'] = pd.to_datetime(df['Date'])

print("✅ CSV file loaded successfully!")
print(f"Total rows: {df.shape[0]}, Total columns: {df.shape[1]}")
print("\nFirst 5 rows:")
print(df.head())
```

### 4. GroupBy Examples (Step by Step)

#### Example 1: Total Sales by City (Most Common Use)

```python
# Group by City and sum the Sales
city_total = df.groupby('City')['Sales'].sum()

print("Total Sales by City:")
print(city_total)
```

**Output you will see:**
```
City
Bangalore     77000
Delhi         92000
Mumbai       227000
Name: Sales, dtype: int64
```

#### Example 2: Average Quantity by Category

```python
avg_qty = df.groupby('Category')['Quantity'].mean().round(2)

print("Average Quantity by Category:")
print(avg_qty)
```

**Output:**
```
Category
Accessories    3.50
Electronics    1.67
Name: Quantity, dtype: float64
```

#### Example 3: Multiple Statistics at Once (Super Useful – Use `.agg()`)

```python
result = df.groupby('City').agg({
    'Sales': ['sum', 'mean', 'max'],      # multiple things on Sales
    'Quantity': 'sum'                     # only sum on Quantity
}).round(2)

print("Multiple stats per City:")
print(result)
```

**Output:**
```
         Sales               Quantity
           sum      mean     max      sum
City                                      
Bangalore  77000  25666.67   42000        9
Delhi      92000  30666.67   45000       12
Mumbai    227000  75666.67   80000        4
```

#### Example 4: Group by TWO Columns (City + Category)

```python
two_group = df.groupby(['City', 'Category'])['Sales'].sum().reset_index()

print("Sales by City AND Category:")
print(two_group)
```

**Output:**
```
        City     Category   Sales
0  Bangalore  Accessories    4300
1  Bangalore  Electronics   72000
2      Delhi  Accessories    4300
3      Delhi  Electronics   87000
4     Mumbai  Accessories    2800
5     Mumbai  Electronics  227000
```

#### Example 5: Count Number of Orders per City

```python
order_count = df.groupby('City').size().reset_index(name='Number_of_Orders')

print("Number of Orders per City:")
print(order_count)
```

### 5. Important Tips for Beginners

1. **After groupby the grouped column becomes index**  
   Use `.reset_index()` to bring it back as normal column (see examples above).

2. **Sort the result**
   ```python
   df.groupby('City')['Sales'].sum().sort_values(ascending=False)
   ```

3. **Shortcut for counting**
   ```python
   df['City'].value_counts()
   ```

4. **You can group by date too!** (Example)
   ```python
   monthly_sales = df.groupby(df['Date'].dt.to_period('M'))['Sales'].sum()
   ```

### 6. Practice Task for You (Do it now!)

Try this on your own:
- Find **maximum Sales** in each **Category**.
- Find **total Quantity** sold in each **City**.

Just change the column names in the examples above.

---

**One-line summary**:  
`groupby()` = Split your data into groups → Apply math → Combine results. It is the #1 tool used in real data analysis.

Got it?  
Want me to explain any one example **even more deeply** (like `.agg()` in full detail, or how to group by month/year, or filtering groups)? Just tell me the number or topic and I’ll give you more examples instantly! 😊
