# Pandas

### **1. What is Pandas?**

Pandas is a Python library built on top of NumPy. It is designed for data analysis and manipulation tasks. It provides flexible data structures to work efficiently with structured data, such as CSV files, Excel sheets, SQL tables, and more.

#### **Installing Pandas**

```python
pip install pandas
```

#### **Importing Pandas**

```python
import pandas as pd
```

***

### **2. Series and DataFrames**

#### **Series (1D Data Structure)**

A `Series` is similar to a column in a table. It consists of data and an index.

```python
import pandas as pd

# Creating a Series
s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print(s)
```

**Output:**

```
a    10
b    20
c    30
d    40
dtype: int64
```

#### **DataFrame (2D Data Structure)**

A `DataFrame` is a table-like structure with rows and columns.

```python
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Paris']
}

df = pd.DataFrame(data)
print(df)
```

**Output:**

```
    Name  Age      City
0  Alice   25  New York
1    Bob   30   London
2 Charlie   35    Paris
```

***

### **3. Creating DataFrames**

#### **From Dictionary**

```python
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
print(df)
```

#### **From List of Lists**

```python
df = pd.DataFrame([[1, 2], [3, 4]], columns=['A', 'B'])
print(df)
```

#### **From NumPy Array**

```python
import numpy as np

df = pd.DataFrame(np.array([[1, 2], [3, 4]]), columns=['A', 'B'])
print(df)
```

***

### **4. Reading and Writing Data**

#### **Reading CSV Files**

```python
df = pd.read_csv('data.csv')
```

#### **Writing to CSV**

```python
df.to_csv('output.csv', index=False)
```

#### **Reading Excel Files**

```python
df = pd.read_excel('data.xlsx', sheet_name='Sheet1')
```

#### **Writing to Excel**

```python
df.to_excel('output.xlsx', index=False)
```

***

### **5. Data Types and Missing Values**

#### **Checking Data Types**

```python
print(df.dtypes)
```

#### **Handling Missing Values**

```python
# Fill missing values with a specific value
df.fillna(0, inplace=True)

# Drop rows with missing values
df.dropna(inplace=True)
```

***

### **6. Indexing Methods: loc, iloc**

#### **Using `loc` (Label-based Indexing)**

```python
print(df.loc[0, 'Name'])  # Fetch value from row 0 and 'Name' column
```

#### **Using `iloc` (Integer-based Indexing)**

```python
print(df.iloc[0, 1])  # Fetch value from row 0, column 1
```

***

### **7. Boolean Indexing**

Boolean indexing allows filtering rows based on conditions.

```python
df[df['Age'] > 30]
```

***

### **8. Selection Based on Conditions**

#### **Filtering Data**

```python
filtered_df = df[df['City'] == 'New York']
print(filtered_df)
```

#### **Using Multiple Conditions**

```python
df[(df['Age'] > 25) & (df['City'] == 'New York')]
```

***

### **9. Adding and Deleting Columns**

#### **Adding a New Column**

```python
df['Salary'] = [50000, 60000, 70000]
```

#### **Deleting a Column**

```python
df.drop('Salary', axis=1, inplace=True)
```

***

### **10. Handling Missing Data**

#### **Filling Missing Values**

```python
df.fillna(value=0, inplace=True)
```

#### **Dropping Missing Values**

```python
df.dropna(inplace=True)
```

***

### **11. Grouping and Aggregation**

#### **Grouping Data**

```python
grouped = df.groupby('City').mean()
print(grouped)
```

#### **Aggregation**

```python
df.groupby('City')['Age'].agg(['mean', 'max', 'min'])
```

***

### **12. Merging and Joining DataFrames**

#### **Merging (Similar to SQL JOIN)**

```python
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'ID': [1, 2, 4], 'Score': [90, 80, 85]})

merged_df = pd.merge(df1, df2, on='ID', how='inner')  # Inner Join
print(merged_df)
```

#### **Concatenation**

```python
df3 = pd.concat([df1, df2], axis=0)  # Stacking rows
df4 = pd.concat([df1, df2], axis=1)  # Stacking columns
```

***

### **Conclusion**

This tutorial covers the essential functionalities of Pandas, including creating DataFrames, reading and writing data, indexing, filtering, grouping, and merging data. Pandas is an incredibly powerful tool for data analysis, and mastering these concepts will help you work efficiently with structured data in Python.

