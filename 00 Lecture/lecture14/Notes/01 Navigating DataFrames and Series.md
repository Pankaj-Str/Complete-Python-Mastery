# Data Manipulation and Analysis with Pandas

This tutorial is designed for beginners to get started with Pandas, a powerful Python library for data manipulation and analysis. We'll cover navigating DataFrames and Series, essential data preparation techniques, and more, using step-by-step examples. Pandas is built on NumPy and is great for handling structured data like spreadsheets or SQL tables.

### Prerequisites
- Basic Python knowledge (e.g., variables, lists).
- Install Pandas if not already: Run `pip install pandas` in your terminal (though in this tutorial, we'll assume it's available).
- We'll use a simple example dataset throughout. For demonstration, I'll create a sample CSV in code, but in real scenarios, you'd load from a file.

All examples are executable in a Python environment like Jupyter Notebook or a script. I'll include code snippets, explanations, and sample outputs.

## 1. Introduction to Pandas: DataFrames and Series
Pandas has two core structures:
- **Series**: A one-dimensional labeled array (like a column in a table).
- **DataFrame**: A two-dimensional labeled data structure (like a table with rows and columns).

### Step-by-Step Example: Creating and Navigating Basics
1. Import Pandas:
   ```python
   import pandas as pd
   ```

2. Create a simple Series:
   ```python
   # A Series from a list
   s = pd.Series([1, 3, 5, None, 7])
   print(s)
   ```
   Output:
   ```
   0    1.0
   1    3.0
   2    5.0
   3    NaN
   4    7.0
   dtype: float64
   ```
   - Navigation: Access by index `s[0]` → 1.0; or slice `s[1:3]` → Series with values 3.0 and 5.0.

3. Create a simple DataFrame:
   ```python
   # A DataFrame from a dictionary
   data = {
       'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
       'Age': [25, 30, 35, None, 28],
       'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
   }
   df = pd.DataFrame(data)
   print(df)
   ```
   Output:
   ```
         Name   Age         City
   0    Alice  25.0     New York
   1      Bob  30.0  Los Angeles
   2  Charlie  35.0      Chicago
   3    David   NaN      Houston
   4      Eve  28.0      Phoenix
   ```

4. Navigating DataFrames:
   - View first few rows: `df.head(2)` → Shows rows 0 and 1.
   - Access a column as Series: `df['Age']` → Returns the Age column.
   - Access rows by index: `df.iloc[0]` → First row as Series.
   - Access by label (if index is set): `df.loc[0]` (same as iloc for integer index).
   - Slice rows/columns: `df.iloc[0:2, 0:2]` → Subset of first two rows and columns.
   - Filter rows: `df[df['Age'] > 30]` → Rows where Age > 30 (e.g., Charlie's row).

## 2. Data Preparation Essentials: CSV as Your Data Foundation
CSV (Comma-Separated Values) files are a common data source. Pandas makes loading them easy.

### Step-by-Step Example: Loading from CSV
1. For this tutorial, simulate a CSV file using a string (in practice, use a real file path).
   ```python
   import io  # To simulate file from string

   csv_data = """Name,Age,City,Score
   Alice,25,New York,85
   Bob,30,Los Angeles,90
   Charlie,35,Chicago,
   David,,Houston,75
   Eve,28,Phoenix,95
   """
   df = pd.read_csv(io.StringIO(csv_data))
   print(df)
   ```
   Output (note missing values as NaN or empty):
   ```
         Name   Age         City  Score
   0    Alice  25.0     New York   85.0
   1      Bob  30.0  Los Angeles   90.0
   2  Charlie  35.0      Chicago    NaN
   3    David   NaN      Houston   75.0
   4      Eve  28.0      Phoenix   95.0
   ```
   - In real use: `df = pd.read_csv('your_file.csv')`.
   - Handles headers, data types automatically, but you can customize (e.g., `skiprows=1` to skip lines).

We'll use this `df` for the rest of the tutorial.

## 3. Identifying Missing Values
Missing data appears as NaN (Not a Number).

### Step-by-Step:
1. Check for missing values:
   ```python
   print(df.isnull())  # Boolean mask: True where missing
   ```
   Output:
   ```
         Name    Age   City  Score
   0    False  False  False  False
   1    False  False  False  False
   2    False  False  False   True
   3    False   True  False  False
   4    False  False  False  False
   ```

2. Count missing per column:
   ```python
   print(df.isnull().sum())
   ```
   Output:
   ```
   Name     0
   Age      1
   City     0
   Score    1
   dtype: int64
   ```
   - `notnull()` is the opposite for non-missing.

## 4. Removing Rows with Missing Values
Use `dropna()` to remove rows containing NaN.

### Step-by-Step:
1. Remove rows with any missing values:
   ```python
   df_clean_rows = df.dropna(axis=0)  # axis=0 for rows
   print(df_clean_rows)
   ```
   Output (removes rows 2 and 3):
   ```
       Name   Age         City  Score
   0  Alice  25.0     New York   85.0
   1    Bob  30.0  Los Angeles   90.0
   4    Eve  28.0      Phoenix   95.0
   ```
   - Use `how='all'` to drop only if all values in row are missing.
   - `inplace=True` modifies original df.

## 5. Removing Columns with Missing Values
Similar, but for columns.

### Step-by-Step:
1. Remove columns with any missing values:
   ```python
   df_clean_cols = df.dropna(axis=1)  # axis=1 for columns
   print(df_clean_cols)
   ```
   Output (removes Age and Score columns):
   ```
         Name         City
   0    Alice     New York
   1      Bob  Los Angeles
   2  Charlie      Chicago
   3    David      Houston
   4      Eve      Phoenix
   ```

## 6. Filling Missing Values (with Random Values)
Instead of removing, fill NaNs. Here, we'll fill with random values as requested (e.g., random integers).

### Step-by-Step:
1. Import random if needed:
   ```python
   import numpy as np  # For random
   ```

2. Fill specific column with random values:
   ```python
   # Fill 'Age' missing with random int between 20-40
   df['Age'] = df['Age'].fillna(np.random.randint(20, 40))
   # Fill 'Score' with random float between 70-100
   df['Score'] = df['Score'].fillna(np.random.uniform(70, 100))
   print(df)
   ```
   Sample Output (random values vary):
   ```
         Name   Age         City      Score
   0    Alice  25.0     New York   85.00000
   1      Bob  30.0  Los Angeles   90.00000
   2  Charlie  35.0      Chicago   82.34567  # Random example
   3    David  27.0      Houston   75.00000  # Random example
   4      Eve  28.0      Phoenix   95.00000
   ```
   - Alternatives: `fillna(0)` for constant, or `fillna(method='ffill')` to forward-fill.

## 7. Describe Method: Summary Statistics
Get quick stats on numerical columns.

### Step-by-Step:
1. Run describe:
   ```python
   print(df.describe())
   ```
   Sample Output (after filling):
   ```
             Age      Score
   count   5.0000   5.000000
   mean   29.0000  85.469134  # Varies with random
   std     3.8079   8.123456   # Approximate
   min    25.0000  75.000000
   25%    27.0000  82.345670
   50%    28.0000  85.000000
   75%    30.0000  90.000000
   max    35.0000  95.000000
   ```
   - Includes count, mean, std, min, percentiles, max.
   - For all columns: `df.describe(include='all')`.

## 8. Drop Methods: Removing Specific Rows/Columns
Beyond dropna, use `drop()` for targeted removal.

### Step-by-Step:
1. Drop a column:
   ```python
   df_dropped_col = df.drop('City', axis=1)
   print(df_dropped_col)
   ```
   Output:
   ```
         Name   Age      Score
   0    Alice  25.0   85.00000
   1      Bob  30.0   90.00000
   2  Charlie  35.0   82.34567
   3    David  27.0   75.00000
   4      Eve  28.0   95.00000
   ```

2. Drop rows by index:
   ```python
   df_dropped_row = df.drop(2, axis=0)  # Drop row index 2
   print(df_dropped_row)
   ```
   Output:
   ```
       Name   Age         City  Score
   0  Alice  25.0     New York   85.0
   1    Bob  30.0  Los Angeles   90.0
   3  David  27.0      Houston   75.0
   4    Eve  28.0      Phoenix   95.0
   ```

## 9. Splitting Data
Split for training/testing or subsets.

### Step-by-Step:
1. Simple row split (e.g., 80/20):
   ```python
   split_index = int(len(df) * 0.8)
   train_df = df.iloc[:split_index]
   test_df = df.iloc[split_index:]
   print("Train:\n", train_df)
   print("Test:\n", test_df)
   ```
   Output:
   ```
   Train:
         Name   Age         City      Score
   0    Alice  25.0     New York   85.00000
   1      Bob  30.0  Los Angeles   90.00000
   2  Charlie  35.0      Chicago   82.34567
   3    David  27.0      Houston   75.00000
   Test:
     Name   Age      City  Score
   4  Eve  28.0  Phoenix   95.0
   ```
   - For random split, use `sklearn.model_selection.train_test_split(df, test_size=0.2)` (requires scikit-learn).

2. Column split: `names = df['Name'] ; other = df.drop('Name', axis=1)`

## 10. Creating New Columns
Add derived columns easily.

### Step-by-Step:
1. Create from existing:
   ```python
   df['Age_Group'] = df['Age'].apply(lambda x: 'Young' if x < 30 else 'Adult')
   print(df)
   ```
   Output:
   ```
         Name   Age         City      Score Age_Group
   0    Alice  25.0     New York   85.00000     Young
   1      Bob  30.0  Los Angeles   90.00000     Adult
   2  Charlie  35.0      Chicago   82.34567     Adult
   3    David  27.0      Houston   75.00000     Young
   4      Eve  28.0      Phoenix   95.00000     Young
   ```
   - Or arithmetic: `df['Score_Adjusted'] = df['Score'] + 5`

## 11. Exploring Unique Values
Check distinct values in columns.

### Step-by-Step:
1. Unique values:
   ```python
   print(df['City'].unique())
   ```
   Output:
   ```
   ['New York' 'Los Angeles' 'Chicago' 'Houston' 'Phoenix']
   ```

2. Number of unique (nunique):
   ```python
   print(df['City'].nunique())  # 5
   print(df.nunique())  # Per column
   ```
   Output:
   ```
   Name         5
   Age          5
   City         5
   Score        5
   Age_Group    2
   dtype: int64
   ```
   - Useful for categorical data analysis.

## 12. Data Type Conversion (dtype, astype)
Check and change data types for efficiency or operations.

### Step-by-Step:
1. Check types:
   ```python
   print(df.dtypes)
   ```
   Output:
   ```
   Name          object
   Age          float64
   City          object
   Score        float64
   Age_Group     object
   dtype: object
   ```

2. Convert types:
   ```python
   df['Age'] = df['Age'].astype(int)  # Float to int (assuming no NaN now)
   print(df.dtypes)
   ```
   Output:
   ```
   Name          object
   Age            int64
   City          object
   Score        float64
   Age_Group     object
   dtype: object
   ```
   - For strings to datetime: `pd.to_datetime(df['date_col'])`.
   - Handle errors: `astype(int, errors='ignore')`.


