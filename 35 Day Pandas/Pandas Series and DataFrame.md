# Pandas Series and DataFrame
Pandas is the most popular Python library for data analysis and manipulation.  
- **Series** = 1-dimensional labeled array (like a single column in Excel).  
- **DataFrame** = 2-dimensional labeled table (like a full spreadsheet).

### 1. Setup

```python
import pandas as pd
import numpy as np   # often used together

print(pd.__version__)   # Current version in this environment: 3.0.1
```

### 2. Pandas Series

#### 2.1 Creating a Series

**From a Python list**

```python
s_list = pd.Series([10, 20, 30, 40, 50])
print(s_list)
```

**Output:**
```
0    10
1    20
2    30
3    40
4    50
dtype: int64
```

**With custom index labels**

```python
s_index = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
print(s_index)
```

**Output:**
```
a    10
b    20
c    30
d    40
e    50
dtype: int64
```

**From a dictionary**

```python
s_dict = pd.Series({'a': 10, 'b': 20, 'c': 30})
print(s_dict)
```

**From a NumPy array**

```python
arr = np.array([1, 3, 5, 7, 9])
s_np = pd.Series(arr)
print(s_np)
```

#### 2.2 Accessing Elements

```python
print("By position (0-based) using .iloc:", s_index.iloc[0])
print("By label:", s_index['b'])

print("\nSlicing by position (.iloc):")
print(s_index.iloc[1:4])

print("\nSlicing by label:")
print(s_index['b':'d'])   # inclusive on both ends!
```

**Output:**
```
By position (0-based) using .iloc: 10
By label: 20

Slicing by position (.iloc):
b    20
c    30
d    40
dtype: int64

Slicing by label:
b    20
c    30
d    40
dtype: int64
```

#### 2.3 Vectorized Operations (very fast!)

```python
print(s_list * 2)
print(s_list + s_list)
```

**Output:**
```
0     20
1     40
2     60
3     80
4    100
dtype: int64
```

#### 2.4 Boolean Indexing (filtering)

```python
print("Elements > 25:")
print(s_list[s_list > 25])
```

**Output:**
```
2    30
3    40
4    50
dtype: int64
```

### 3. Pandas DataFrame

#### 3.1 Creating a DataFrame

**From dictionary of lists (most common)**

```python
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'London', 'Paris', 'Tokyo']
}
df = pd.DataFrame(data)
print(df)
```

**Output:**
```
      Name  Age      City
0    Alice   25  New York
1      Bob   30    London
2  Charlie   35     Paris
3    David   40     Tokyo
```

**From list of dictionaries**

```python
data_list = [
    {'Name': 'Alice', 'Age': 25, 'City': 'New York'},
    {'Name': 'Bob', 'Age': 30, 'City': 'London'}
]
df2 = pd.DataFrame(data_list)
print(df2)
```

**From 2D list**

```python
df3 = pd.DataFrame([[1, 2, 3], [4, 5, 6]], columns=['A', 'B', 'C'])
print(df3)
```

#### 3.2 Quick Inspection

```python
print(df.head(2))      # first 2 rows
print(df.tail(2))      # last 2 rows
df.info()              # data types, missing values, memory
print(df.describe())   # numeric summary
```

**Key info output:**
```
<class 'pandas.DataFrame'>
RangeIndex: 4 entries, 0 to 3
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   Name    4 non-null      object
 1   Age     4 non-null      int64 
 2   City    4 non-null      object
dtypes: int64(1), object(2)
```

#### 3.3 Selecting Data

**Columns**

```python
print(df['Name'])                    # single column → Series
print(df[['Name', 'Age']])           # multiple columns → DataFrame
```

**Rows**

```python
print(df.iloc[1])          # by position
print(df.loc[1])           # by label (same as position when default index)
print(df.iloc[1:3])        # slice of rows
```

#### 3.4 Filtering & Adding Columns

```python
# Filtering
print("People older than 30:")
print(df[df['Age'] > 30])

# Adding a new column
df['Salary'] = [50000, 60000, 70000, 80000]
print(df)
```

**Output after adding column:**
```
      Name  Age      City  Salary
0    Alice   25  New York   50000
1      Bob   30    London   60000
2  Charlie   35     Paris   70000
3    David   40     Tokyo   80000
```

#### 3.5 Basic Statistics

```python
print("Average age:", df['Age'].mean())
print("Max salary:", df['Salary'].max())
```

**Output:**
```
Average age: 32.5
Max salary: 80000
```

### 4. Next Steps (Quick Tips)

```python
# Save to CSV
df.to_csv('people.csv', index=False)

# Read from CSV
df_new = pd.read_csv('people.csv')

# Sort
df.sort_values(by='Age', ascending=False)

# Group by
df.groupby('City')['Age'].mean()
```

**You now know the core of pandas!**

**Practice Exercise (try it yourself):**
1. Create a Series of your 5 favorite numbers with index as days of the week.
2. Create a DataFrame of 5 students with columns: `Name`, `Math_Score`, `Science_Score`.
3. Add a column `Total` = Math + Science.
4. Show only students with Total > 150.