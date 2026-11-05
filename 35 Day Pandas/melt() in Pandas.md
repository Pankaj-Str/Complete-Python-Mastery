# **`melt()` in Pandas**  
**From Wide to Long Format (Tidy Data!)**

---

## What is `melt()`?

**`pd.melt()`** = **Unpivot** a DataFrame  
→ Turns **wide data** (many columns) into **long data** (fewer columns, more rows)

Think of it like **Excel’s “Unpivot Columns”** or **SQL’s UNPIVOT**.

---

## Why Use `melt()`?

| Wide (Hard to analyze) | Long (Easy to analyze) |
|------------------------|------------------------|
| One row per person, many columns for years | One row per person-year |
| Hard to plot trends | Perfect for `groupby`, `seaborn`, `plotly` |

---

## Simple Example (Step-by-Step)

```python
import pandas as pd

# 1. Create WIDE data: Sales by year
wide_df = pd.DataFrame({
    'Store': ['North', 'South', 'East'],
    '2021': [1200, 800, 600],
    '2022': [1500, 900, 1100],
    '2023': [1400, 850, 1000]
})

print("Wide Format:")
print(wide_df)
```

**Output:**
```
   Store  2021  2022  2023
0  North  1200  1500  1400
1  South   800   900   850
2   East   600  1100  1000
```

---

## `pd.melt()` – Unpivot!

```python
# 2. Melt: Keep 'Store' fixed, turn years into rows
long_df = pd.melt(
    wide_df,
    id_vars=['Store'],          # Columns to KEEP
    value_vars=['2021', '2022', '2023'],  # Columns to MELT
    var_name='Year',            # Name of new column (was column names)
    value_name='Sales'          # Name of new value column
)

print("\nLong Format:")
print(long_df)
```

**Output:**
```
    Store  Year  Sales
0   North  2021   1200
1   South  2021    800
2    East  2021    600
3   North  2022   1500
4   South  2022    900
5    East  2022   1100
6   North  2023   1400
7   South  2023    850
8    East  2023   1000
```

**Perfect for analysis!**

---

## Common `melt()` Patterns

### 1. **Melt ALL value columns (default)**

```python
# Don't specify value_vars → melts all except id_vars
long_all = pd.melt(wide_df, id_vars=['Store'], var_name='Year', value_name='Sales')
print(long_all)
```
→ Same result!

---

### 2. **Multiple ID columns**

```python
# Add 'Manager' column
wide_df['Manager'] = ['Alice', 'Bob', 'Charlie']

long_multi = pd.melt(
    wide_df,
    id_vars=['Store', 'Manager'],
    value_vars=['2021', '2022', '2023'],
    var_name='Year',
    value_name='Sales'
)
print(long_multi.head(6))
```

**Output:**
```
   Store Manager  Year  Sales
0  North   Alice  2021   1200
1  South     Bob  2021    800
2   East Charlie  2021    600
3  North   Alice  2022   1500
4  South     Bob  2022    900
5   East Charlie  2022   1100
```

---

### 3. **Real-World: Student Scores**

```python
scores_wide = pd.DataFrame({
    'Student': ['Ali', 'Beth', 'Cathy'],
    'Math': [85, 90, 78],
    'Science': [88, 92, 80],
    'English': [90, 85, 88]
})

print("Wide Scores:")
print(scores_wide)
```

**Output:**
```
  Student  Math  Science  English
0     Ali    85       88       90
1    Beth    90       92       85
2   Cathy    78       80       88
```

```python
# Melt to long format
scores_long = pd.melt(
    scores_wide,
    id_vars='Student',
    value_vars=['Math', 'Science', 'English'],
    var_name='Subject',
    value_name='Score'
)

print("\nLong Scores:")
print(scores_long)
```

**Output:**
```
  Student  Subject  Score
0     Ali     Math     85
1    Beth     Math     90
2   Cathy     Math     78
3     Ali  Science     88
4    Beth  Science     92
5   Cathy  Science     80
6     Ali  English     90
7    Beth  English     85
8   Cathy  English     88
```

Now you can:
```python
# Average score per subject
print(scores_long.groupby('Subject')['Score'].mean())

# Top student per subject
print(scores_long.loc[scores_long.groupby('Subject')['Score'].idxmax()])
```

---

## `melt()` Cheat Sheet

| Parameter | Meaning |
|---------|--------|
| `id_vars` | Columns to **keep fixed** (not melted) |
| `value_vars` | Columns to **melt** (default: all except `id_vars`) |
| `var_name` | Name of new column for **old column names** |
| `value_name` | Name of new column for **values** |

```python
pd.melt(df, id_vars='A', value_vars=['B','C'], var_name='X', value_name='Y')
```

---

## Practice: Try This!

```python
# Wide data
survey = pd.DataFrame({
    'Person': ['P1', 'P2', 'P3'],
    'Q1': [5, 4, 3],
    'Q2': [2, 5, 4],
    'Q3': [4, 3, 5]
})

# Task: Convert to long format
# → Columns: Person, Question, Rating
```

**Solution:**
```python
long_survey = pd.melt(survey, id_vars='Person', var_name='Question', value_name='Rating')
print(long_survey)
```

---

## Bonus: Plot Long Data (Easy!)

```python
import matplotlib.pyplot as plt

# Plot sales over time
long_df['Year'] = long_df['Year'].astype(int)
long_df.plot(x='Year', y='Sales', kind='line', marker='o', title='Sales Trend')
plt.show()
```

---

## Summary

| Before (`melt`) | After (`melt`) |
|-----------------|----------------|
| Wide, many columns | Long, tidy rows |
| Hard to analyze | Perfect for `groupby`, plots, ML |

---

**You're now a `melt()` master!**  
Use it to:
- Prepare data for **charts**
- Clean **survey/exam** data
- Feed into **machine learning**

---

