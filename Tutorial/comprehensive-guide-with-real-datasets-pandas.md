---
description: 'Pandas Tutorial: Comprehensive Guide with Real Datasets'
---

# Comprehensive Guide with Real Datasets Pandas

### Dataset Creation

Before we dive into the Pandas tutorial, let's create a sample dataset of employees working in different departments with salary details.

```python
import pandas as pd

data = {
    'Employee_ID': [101, 102, 103, 104, 105],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 28, 40],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'HR'],
    'Salary': [50000, 60000, 70000, 80000, 55000]
}
df = pd.DataFrame(data)
print(df)
```

***

### What is Pandas?

Pandas is an open-source Python library used for data manipulation and analysis. It provides powerful data structures: **Series** (1D) and **DataFrame** (2D), which make handling structured data easy and efficient.

#### Key Features of Pandas:

* Fast and efficient DataFrame object
* Tools for reading and writing data from multiple formats (CSV, Excel, SQL, JSON, etc.)
* Data alignment and handling of missing data
* Powerful indexing and slicing capabilities
* Data aggregation, merging, and grouping

***

### 1. Series and DataFrames

#### Series (1D Data Structure)

A **Series** is a one-dimensional labeled array capable of holding data of any type.

```python
series = pd.Series(df['Salary'])
print(series)
```

#### DataFrame (2D Data Structure)

A **DataFrame** is a two-dimensional, size-mutable, and heterogeneous data structure.

```python
print(df)
```

***

### 2. Creating DataFrames

#### From a Dictionary

```python
data = {
    'Employee_ID': [106, 107],
    'Name': ['Frank', 'Grace'],
    'Age': [33, 29],
    'Department': ['Finance', 'IT'],
    'Salary': [72000, 65000]
}
df_new = pd.DataFrame(data)
print(df_new)
```

#### From a CSV File

```python
df = pd.read_csv('sample_data.csv')
print(df.head())
```

***

### 3. Reading and Writing Data

#### Reading CSV

```python
df = pd.read_csv('employee_data.csv')
```

#### Writing CSV

```python
df.to_csv('output.csv', index=False)
```

#### Reading Excel

```python
df = pd.read_excel('employee_data.xlsx')
```

#### Writing Excel

```python
df.to_excel('output.xlsx', index=False)
```

***

### 4. Data Types and Missing Values

#### Checking Data Types

```python
print(df.dtypes)
```

#### Handling Missing Data

```python
df.fillna(0, inplace=True)  # Replace NaN with 0
df.dropna(inplace=True)  # Remove rows with NaN values
```

***

### 5. Indexing Methods: `loc`, `iloc`

#### Using `loc`

```python
print(df.loc[0, 'Name'])  # Get specific value
```

#### Using `iloc`

```python
print(df.iloc[0, 1])  # Get specific value using index positions
```

***

### 6. Boolean Indexing

```python
high_salary = df[df['Salary'] > 60000]
print(high_salary)
```

***

### 7. Selection Based on Conditions

```python
filtered_df = df[(df['Age'] > 30) & (df['Department'] == 'Finance')]
print(filtered_df)
```

***

### 8. Adding and Deleting Columns

#### Adding a Column

```python
df['Bonus'] = df['Salary'] * 0.10
```

#### Deleting a Column

```python
df.drop(columns=['Bonus'], inplace=True)
```

***

### 9. Handling Missing Data

```python
df.fillna(df.mean(), inplace=True)  # Fill missing values with column mean
```

***

### 10. Grouping and Aggregation

#### Grouping Data

```python
grouped = df.groupby('Department').mean()
print(grouped)
```

#### Aggregation

```python
agg = df.groupby('Department').agg({'Salary': 'sum'})
print(agg)
```

***

### 11. Merging and Joining DataFrames

#### Merging DataFrames

```python
df1 = pd.DataFrame({'Employee_ID': [101, 102, 103], 'Name': ['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'Employee_ID': [101, 102, 103], 'Salary': [50000, 60000, 70000]})
merged_df = pd.merge(df1, df2, on='Employee_ID')
print(merged_df)
```

#### Joining DataFrames

```python
df1.set_index('Employee_ID', inplace=True)
df2.set_index('Employee_ID', inplace=True)
joined_df = df1.join(df2)
print(joined_df)
```

***

This tutorial provides an in-depth understanding of Pandas with real-world examples. Stay tuned for more advanced topics !
