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

### Creating a Series
You can create a Pandas Series from a list, NumPy array, or dictionary.

#### From a List
```python
data_list = [1, 2, 3, 4, 5]
series_from_list = pd.Series(data_list)
print(series_from_list)
```

#### From a NumPy Array
```python
import numpy as np

data_array = np.array([1, 2, 3, 4, 5])
series_from_array = pd.Series(data_array)
print(series_from_array)
```

#### From a Dictionary
```python
data_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
series_from_dict = pd.Series(data_dict)
print(series_from_dict)
```

### Accessing Elements
You can access elements using index.

```python
print(series_from_list[0])  # Accessing the first element
print(series_from_dict['b'])  # Accessing the value with key 'b'
```

### Basic Operations
```python
# Adding two series
result_series = series_from_list + series_from_array
print(result_series)
```

### Series Attributes and Methods
```python
print(series_from_list.shape)  # Shape of the series
print(series_from_dict.index)  # Index of the series

# Describe method to get statistics
print(series_from_array.describe())
```

### Handling Missing Data
```python
data_with_nan = pd.Series([1, 2, np.nan, 4, 5])
print(data_with_nan)

# Drop missing values
data_without_nan = data_with_nan.dropna()
print(data_without_nan)

# Fill missing values
data_filled = data_with_nan.fillna(0)
print(data_filled)
```

### Filtering
```python
# Filtering values greater than 3
filtered_series = series_from_array[series_from_array > 3]
print(filtered_series)
```

## A Pandas DataFrame is a two-dimensional, tabular data structure with labeled axes (rows and columns).

### Installing Pandas
If you haven't installed Pandas yet, you can install it using the following command:

```bash
pip install pandas
```

### Importing Pandas
```python
import pandas as pd
```

### Creating a DataFrame

#### From a Dictionary
```python
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'San Francisco', 'Los Angeles']}

df_from_dict = pd.DataFrame(data)
print(df_from_dict)
```

#### From a List of Lists
```python
data_list = [['Alice', 25, 'New York'],
             ['Bob', 30, 'San Francisco'],
             ['Charlie', 35, 'Los Angeles']]

df_from_list = pd.DataFrame(data_list, columns=['Name', 'Age', 'City'])
print(df_from_list)
```

### Basic DataFrame Operations

#### Accessing Columns
```python
print(df_from_dict['Name'])  # Accessing the 'Name' column
```

#### Accessing Rows
```python
print(df_from_dict.iloc[0])  # Accessing the first row using index
```

#### Adding a New Column
```python
df_from_dict['Gender'] = ['Female', 'Male', 'Male']
print(df_from_dict)
```

#### Basic Statistics
```python
print(df_from_dict.describe())  # Summary statistics
```

### Indexing and Slicing

#### Setting a Column as Index
```python
df_with_index = df_from_dict.set_index('Name')
print(df_with_index)
```

#### Slicing Rows and Columns
```python
# Slicing rows
print(df_from_dict[1:3])

# Slicing columns
print(df_from_dict[['Name', 'City']])
```

### Handling Missing Data

#### Checking for Missing Data
```python
print(df_from_dict.isnull())
```

#### Dropping Missing Values
```python
df_no_missing = df_from_dict.dropna()
print(df_no_missing)
```

#### Filling Missing Values
```python
df_filled = df_from_dict.fillna(value={'Age': 0})
print(df_filled)
```

### Reading and Writing Data

#### Reading from CSV
```python
df_csv = pd.read_csv('example.csv')
print(df_csv)
```

#### Writing to CSV
```python
df_from_dict.to_csv('output.csv', index=False)
```

### Advanced DataFrame Operations

#### Grouping Data
```python
grouped_data = df_from_dict.groupby('City').mean()
print(grouped_data)
```

#### Merging DataFrames
```python
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'ID': [2, 3, 4], 'Salary': [50000, 60000, 70000]})

merged_df = pd.merge(df1, df2, on='ID', how='inner')
print(merged_df)
```

#### Pivot Tables
```python
pivot_table = df_from_dict.pivot_table(values='Age', index='City', columns='Gender', aggfunc='mean')
print(pivot_table)
```

### Conclusion
This tutorial covers the basics and some advanced features of working with Pandas DataFrames. As you become more familiar with Pandas, you can explore additional features such as reshaping data, time series analysis, and more complex data manipulations. The official Pandas documentation is a valuable resource for further exploration: [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/index.html).
