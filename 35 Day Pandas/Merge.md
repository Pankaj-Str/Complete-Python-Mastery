# Merging DataFrames in Pandas

---

## What is Merging?

**Merging** = Combining two DataFrames based on **common columns** (like SQL `JOIN`).

Think of it as **joining two Excel sheets** using a shared ID or name.

---

## Simple Example (Step-by-Step)

We’ll create **two small tables** and merge them.

```python
# 1. Import pandas
import pandas as pd

# 2. Create Table 1: Students
students = pd.DataFrame({
    'StudentID': [101, 102, 103, 104],
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [20, 21, 19, 22]
})
print("Students Table:")
print(students)
```

**Output:**
```
   StudentID     Name  Age
0        101    Alice   20
1        102      Bob   21
2        103  Charlie   19
3        104    Diana   22
```

```python
# 3. Create Table 2: Scores
scores = pd.DataFrame({
    'StudentID': [101, 102, 103, 105],
    'Subject': ['Math', 'Math', 'Science', 'English'],
    'Score': [85, 90, 78, 88]
})
print("\nScores Table:")
print(scores)
```

**Output:**
```
   StudentID  Subject  Score
0        101     Math     85
1        102     Math     90
2        103  Science     78
3        105  English     88
```

---

## `pd.merge()` – The Main Function

```python
# 4. Merge on 'StudentID'
merged = pd.merge(students, scores, on='StudentID')
print("\nMerged Table (Inner Join):")
print(merged)
```

**Output (Inner Join – default):**
```
   StudentID     Name  Age  Subject  Score
0        101    Alice   20     Math     85
1        102      Bob   21     Math     90
2        103  Charlie   19  Science     78
```

> **Note:**  
> - Student **104** (Diana) → no score → **excluded**  
> - Student **105** → no name → **excluded**

---

## Types of Merges (Joins)

| Type        | Keeps                     | Use Case |
|-------------|---------------------------|----------|
| `inner`     | Only matching rows        | Strict match |
| `left`      | All from **left** table   | Keep all students |
| `right`     | All from **right** table  | Keep all scores |
| `outer`     | All from **both**         | Full picture |

---

### 1. **Left Join** – Keep all students

```python
left_merge = pd.merge(students, scores, on='StudentID', how='left')
print("\nLeft Join (keep all students):")
print(left_merge)
```

**Output:**
```
   StudentID     Name   Age  Subject  Score
0        101    Alice  20.0     Math   85.0
1        102      Bob  21.0     Math   90.0
2        103  Charlie  19.0  Science   78.0
3        104    Diana  22.0      NaN    NaN
```

> Diana has `NaN` because no score.

---

### 2. **Right Join** – Keep all scores

```python
right_merge = pd.merge(students, scores, on='StudentID', how='right')
print("\nRight Join (keep all scores):")
print(right_merge)
```

**Output:**
```
   StudentID     Name   Age  Subject  Score
0        101    Alice  20.0     Math     85
1        102      Bob  21.0     Math     90
2        103  Charlie  19.0  Science     78
3        105      NaN   NaN  English     88
```

> Student 105 has no name → `NaN`

---

### 3. **Outer Join** – Keep everything

```python
outer_merge = pd.merge(students, scores, on='StudentID', how='outer')
print("\nOuter Join (keep all):")
print(outer_merge)
```

**Output:**
```
   StudentID     Name   Age  Subject  Score
0        101    Alice  20.0     Math   85.0
1        102      Bob  21.0     Math   90.0
2        103  Charlie  19.0  Science   78.0
3        104    Diana  22.0      NaN    NaN
4        105      NaN   NaN  English   88.0
```

---

## What if Column Names Are Different?

Use `left_on` and `right_on`.

```python
# Example: different column names
students2 = students.rename(columns={'StudentID': 'ID'})
merged_diff = pd.merge(students2, scores, left_on='ID', right_on='StudentID')
print(merged_diff)
```

---

## Quick Cheat Sheet

| Code | Meaning |
|------|--------|
| `pd.merge(df1, df2, on='key')` | Inner join on column `'key'` |
| `how='left'` | Keep all rows from **df1** |
| `how='right'` | Keep all rows from **df2** |
| `how='outer'` | Keep all rows from both |
| `left_on='A', right_on='B'` | Join when column names differ |

---

## Practice: Try This!

```python
# Create your own tables
orders = pd.DataFrame({
    'OrderID': [1, 2, 3],
    'Customer': ['A', 'B', 'A']
})

customers = pd.DataFrame({
    'Customer': ['A', 'C'],
    'City': ['NY', 'LA']
})

# Task: Merge to see which customers placed orders and their cities
# Use left, right, and outer — see the difference!
```

**Solution (Left Join):**
```python
result = pd.merge(orders, customers, on='Customer', how='left')
print(result)
```

---

## Summary

| You Want | Use |
|--------|-----|
| Only matching data | `how='inner'` (default) |
| All from first table | `how='left'` |
| All from second table | `how='right'` |
| All data (with NaN) | `how='outer'` |

---


