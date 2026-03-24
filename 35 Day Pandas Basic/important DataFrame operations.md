# most important DataFrame operations

I have divided them into categories with:
- What it does (use)
- Simple syntax
- Real example with output

### 1. Basic Information Operations

| Method              | Use                                      | Example Code                                      | Output/Example Result |
|---------------------|------------------------------------------|---------------------------------------------------|-----------------------|
| `df.head(n)`        | Show first n rows (default 5)            | `df.head(3)`                                      | First 3 rows |
| `df.tail(n)`        | Show last n rows                         | `df.tail(2)`                                      | Last 2 rows |
| `df.shape`          | Get (rows, columns)                      | `df.shape`                                        | (5, 5) |
| `df.columns`        | Get list of column names                 | `df.columns`                                      | ['Name', 'Age', 'City', 'Salary', 'Join_Date'] |
| `df.dtypes`         | Show data type of each column            | `df.dtypes`                                       | Name: object, Age: int64, etc. |
| `df.info()`         | Full summary (rows, columns, types, memory) | `df.info()`                                    | Detailed info |
| `df.describe()`     | Statistical summary (mean, min, max, etc.) for numeric columns | `df.describe()`                          | Count, mean, std, min, 25%, 50%, 75%, max |

### 2. Selecting Data

| Method                      | Use                                              | Example Code                                               | Result |
|-----------------------------|--------------------------------------------------|------------------------------------------------------------|--------|
| `df['Column']`              | Select one column (returns Series)               | `df['Age']`                                                | Age column |
| `df[['Col1', 'Col2']]`      | Select multiple columns                          | `df[['Name', 'City']]`                                     | Name + City |
| `df.loc[row_label]`         | Select by label (row name/index)                 | `df.loc[0]`                                                | First row |
| `df.iloc[row_position]`     | Select by position (integer location)            | `df.iloc[2]`                                               | Third row (0-based) |
| `df.loc[:, 'Col']`          | Select rows + columns by label                   | `df.loc[1:3, ['Name', 'Salary']]`                          | Rows 1-3, Name & Salary |
| `df.iloc[:, 0:3]`           | Select by position                               | `df.iloc[:, 0:3]`                                          | First 3 columns |

### 3. Filtering Rows (Conditional Selection)

| Operation                   | Use                                              | Example Code |
|-----------------------------|--------------------------------------------------|--------------|
| Simple condition            | Filter based on one condition                    | `df[df['Age'] > 28]` |
| Multiple conditions (AND)   | Use `&`                                          | `df[(df['Age'] > 25) & (df['City'] == 'Mumbai')]` |
| Multiple conditions (OR)    | Use `|`                                          | `df[(df['City'] == 'Mumbai') \| (df['City'] == 'Delhi')]` |
| `isin()`                    | Check if value is in a list                      | `df[df['City'].isin(['Mumbai', 'Delhi'])]` |
| `query()`                   | Filter using string expression (very readable)   | `df.query('Age > 25 and Salary > 80000')` |

### 4. Adding / Removing Columns

| Method                        | Use                                           | Example |
|-------------------------------|-----------------------------------------------|---------|
| Add new column                | Create new column                             | `df['Bonus'] = df['Salary'] * 0.1` |
| Add column with condition     | Using `np.where`                              | `df['Senior'] = np.where(df['Age'] >= 30, 'Yes', 'No')` |
| Drop column                   | Remove column                                 | `df.drop('Bonus', axis=1, inplace=True)` |
| Rename column                 | Change column name                            | `df.rename(columns={'Salary': 'Monthly_Salary'}, inplace=True)` |

### 5. Sorting

| Method          | Use                            | Example |
|-----------------|--------------------------------|---------|
| `sort_values()` | Sort by one or more columns    | `df.sort_values(by='Salary', ascending=False)` |
|                 | Sort by multiple columns       | `df.sort_values(by=['City', 'Salary'], ascending=[True, False])` |

### 6. Handling Missing Values

| Method               | Use                                      | Example |
|----------------------|------------------------------------------|---------|
| `df.isnull()`        | Check for missing values                 | `df.isnull().sum()` |
| `df.dropna()`        | Remove rows with missing values          | `df.dropna()` |
| `df.fillna(value)`   | Fill missing values                      | `df['Age'].fillna(df['Age'].mean())` |

### 7. GroupBy Operations (Very Important)

| Operation                  | Use                                              | Example |
|----------------------------|--------------------------------------------------|---------|
| `groupby()` + `mean()`     | Group and calculate average                      | `df.groupby('City')['Salary'].mean()` |
| `groupby()` + `sum()`      | Group and sum                                    | `df.groupby('City')['Salary'].sum()` |
| `groupby()` + `agg()`      | Multiple aggregations at once                    | `df.groupby('City').agg({'Salary': ['mean', 'max'], 'Age': 'mean'})` |
| `groupby()` + `count()`    | Count rows per group                             | `df.groupby('City').size()` |

### 8. Other Useful Operations

| Method                    | Use                                              | Example |
|---------------------------|--------------------------------------------------|---------|
| `df.value_counts()`       | Count unique values in a column                  | `df['City'].value_counts()` |
| `df.unique()` / `nunique()` | Get unique values or count of unique values     | `df['City'].unique()` |
| `df.apply()`              | Apply a function to each row or column           | `df['Age'].apply(lambda x: x + 5)` |
| `df.astype()`             | Change data type of column                       | `df['Age'] = df['Age'].astype(float)` |
| `pd.concat()`             | Combine two DataFrames vertically or horizontally| `pd.concat([df1, df2])` |
| `df.merge()`              | Join two DataFrames like SQL JOIN                | `df1.merge(df2, on='ID')` |

