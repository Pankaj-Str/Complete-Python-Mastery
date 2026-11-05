# Python Pandas 


### https://codeswithpankaj.medium.com/python-pandas-series-f2df7ddf4720

### Installing Pandas
If you haven't installed Pandas yet, you can install it using the following command:

```bash
pip install pandas
```

### Importing Pandas
```python
import pandas as pd
```
Here's an expanded version of your blog with examples and explanations for each topic and subtopic, designed to be simple and easy to understand.

---

### Pandas Data Structures:
Pandas is a powerful Python library for data manipulation and analysis. Understanding its core data structure—the DataFrame—is essential. This blog will guide you through various operations on Pandas DataFrames, from basic tasks to more advanced techniques.

---

#### 1. Creating a DataFrame from a List

**Task:** Convert a list of data into a DataFrame.

**Example:**

```python
import pandas as pd

data = [1, 2, 3, 4, 5]
df = pd.DataFrame(data, columns=['Numbers'])
print(df)
```

**Explanation:**  
In this example, we have a list of numbers `[1, 2, 3, 4, 5]`. Using `pd.DataFrame()`, we convert this list into a DataFrame, where each number becomes a row in a column named 'Numbers'.

**Output:**

```
   Numbers
0        1
1        2
2        3
3        4
4        5
```

---

#### 2. Data Inspection

**Get the Size of a DataFrame**

**Task:** Find out how many rows and columns are in the DataFrame.

**Example:**

```python
df.shape
```

**Explanation:**  
The `.shape` attribute returns a tuple `(rows, columns)` that tells us the size of the DataFrame. For our example, it would return `(5, 1)` because there are 5 rows and 1 column.

**Output:**

```
(5, 1)
```

**Display the First Three Rows**

**Task:** Display the first few rows of the DataFrame to get a quick look at the data.

**Example:**

```python
df.head(3)
```

**Explanation:**  
The `.head()` function shows the first few rows of the DataFrame. If you pass `3` as an argument, it will display the first three rows.

**Output:**

```
   Numbers
0        1
1        2
2        3
```

---

#### 3. Data Selection

**Select Data**

**Task:** Select specific rows and columns from the DataFrame.

**Example:**

```python
df.loc[0:2, ['Numbers']]
```

**Explanation:**  
The `.loc[]` function is used for label-based selection. Here, `0:2` specifies rows 0 to 2, and `['Numbers']` specifies the 'Numbers' column. This will return the first three rows of the 'Numbers' column.

**Output:**

```
   Numbers
0        1
1        2
2        3
```

**Create a New Column**

**Task:** Add a new column to the DataFrame.

**Example:**

```python
df['Squared Numbers'] = df['Numbers'] ** 2
print(df)
```

**Explanation:**  
We are creating a new column called 'Squared Numbers' that contains the square of the values in the 'Numbers' column.

**Output:**

```
   Numbers  Squared Numbers
0        1                1
1        2                4
2        3                9
3        4               16
4        5               25
```

---

#### 4. Data Cleaning

**Drop Duplicate Rows**

**Task:** Remove duplicate rows from the DataFrame.

**Example:**

```python
df.drop_duplicates(inplace=True)
```

**Explanation:**  
The `.drop_duplicates()` function removes duplicate rows. The `inplace=True` argument means the changes will be applied directly to the DataFrame without needing to reassign it.

**Drop Missing Data**

**Task:** Remove rows with missing values (NaN) from the DataFrame.

**Example:**

```python
df.dropna(inplace=True)
```

**Explanation:**  
The `.dropna()` function removes rows with any missing values (NaN). Like before, `inplace=True` means the DataFrame will be updated directly.

**Modify Columns**

**Rename Columns**

**Task:** Rename a column in the DataFrame.

**Example:**

```python
df.rename(columns={'Numbers': 'Nums'}, inplace=True)
print(df)
```

**Explanation:**  
Here, we’re renaming the 'Numbers' column to 'Nums' using the `.rename()` function.

**Output:**

```
   Nums  Squared Numbers
0     1                1
1     2                4
2     3                9
3     4               16
4     5               25
```

**Change Data Type**

**Task:** Convert the data type of a column.

**Example:**

```python
df['Nums'] = df['Nums'].astype(float)
print(df)
```

**Explanation:**  
The `.astype()` function changes the data type of the 'Nums' column from integer to float.

**Output:**

```
   Nums  Squared Numbers
0   1.0                1
1   2.0                4
2   3.0                9
3   4.0               16
4   5.0               25
```

**Fill Missing Data**

**Task:** Replace missing values (NaN) with a specific value.

**Example:**

```python
df.fillna(0, inplace=True)
```

**Explanation:**  
The `.fillna()` function fills any missing values (NaN) with the specified value, in this case, `0`.

---

#### 5. Table Reshaping

**Reshape Data: Concatenate**

**Task:** Combine multiple DataFrames into one.

**Example:**

```python
df2 = pd.DataFrame({'Nums': [6, 7, 8]})
df_concat = pd.concat([df, df2])
print(df_concat)
```

**Explanation:**  
The `pd.concat()` function concatenates `df` and `df2` along the rows, creating a new DataFrame that combines both.

**Output:**

```
   Nums  Squared Numbers
0   1.0              1.0
1   2.0              4.0
2   3.0              9.0
3   4.0             16.0
4   5.0             25.0
0   6.0              NaN
1   7.0              NaN
2   8.0              NaN
```

**Reshape Data: Pivot**

**Task:** Reshape data by turning a column's values into new columns.

**Example:**

```python
df_pivot = df.pivot(index='Nums', columns='Squared Numbers', values='Nums')
print(df_pivot)
```

**Explanation:**  
The `.pivot()` function reshapes the DataFrame by turning unique values from one column into columns themselves.

**Reshape Data: Melt**

**Task:** Convert a wide DataFrame into a long format.

**Example:**

```python
df_melted = pd.melt(df, id_vars=['Nums'], value_vars=['Squared Numbers'])
print(df_melted)
```

**Explanation:**  
The `.melt()` function unpivots the DataFrame, turning columns into rows, which is useful for analysis.

**Output:**

```
   Nums        variable  value
0   1.0  Squared Numbers    1.0
1   2.0  Squared Numbers    4.0
2   3.0  Squared Numbers    9.0
3   4.0  Squared Numbers   16.0
4   5.0  Squared Numbers   25.0
```

---

#### 6. Advanced Techniques

**Method Chaining**

**Task:** Perform multiple operations in a single line of code.

**Example:**

```python
df = (df.drop_duplicates()
        .fillna(0)
        .rename(columns={'Nums': 'Numbers'}))
print(df)
```

**Explanation:**  
Method chaining allows you to perform several operations in one line of code, making your code cleaner and easier to read. Here, we drop duplicates, fill missing values with `0`, and rename the column 'Nums' to 'Numbers' all in one step.
