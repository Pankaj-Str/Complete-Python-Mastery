---

#  Renaming Column Names – Step-by-Step Example

```python
# -------------------------------------------------
# 1. Import pandas
# -------------------------------------------------
import pandas as pd

# -------------------------------------------------
# 2. Create a tiny sample DataFrame
# -------------------------------------------------
data = {
    "old_name":   ["Alice", "Bob", "Charlie"],
    "old_age":    [25, 30, 35],
    "old_city":   ["NY", "LA", "CHI"]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
```

**Output**

```
Original DataFrame:
   old_name  old_age old_city
0    Alice       25       NY
1      Bob       30       LA
2  Charlie       35      CHI
```

---

### Method 1 – `df.rename(columns={...})`  *(recommended – keeps original df)*

```python
# -------------------------------------------------
# 3. Rename ONE column
# -------------------------------------------------
df_one = df.rename(columns={"old_name": "Name"})
print("\nAfter renaming ONE column:")
print(df_one)
```

**Output**

```
After renaming ONE column:
      Name  old_age old_city
0    Alice       25       NY
1      Bob       30       LA
2  Charlie       35      CHI
```

```python
# -------------------------------------------------
# 4. Rename MULTIPLE columns at once
# -------------------------------------------------
df_multi = df.rename(columns={
    "old_name": "Full Name",
    "old_age":  "Age",
    "old_city": "City"
})
print("\nAfter renaming MULTIPLE columns:")
print(df_multi)
```

**Output**

```
After renaming MULTIPLE columns:
  Full Name  Age City
0     Alice   25   NY
1       Bob   30   LA
2   Charlie   35  CHI
```

> **Tip:** `rename` returns a **new** DataFrame by default.  
> Use `inplace=True` if you want to modify the original:

```python
df.rename(columns={"old_name": "Name"}, inplace=True)
print(df)   # now the original df is changed
```

---

### Method 2 – Assign a **list** to `df.columns` *(quick, but overwrites all names)*

```python
# -------------------------------------------------
# 5. Replace ALL column names with a list
# -------------------------------------------------
df_list = df.copy()                     # work on a copy
df_list.columns = ["Person", "Years", "Location"]

print("\nUsing df.columns = [...] :")
print(df_list)
```

**Output**

```
Using df.columns = [...] :
   Person  Years Location
0   Alice     25       NY
1     Bob     30       LA
2 Charlie     35      CHI
```

> **Caution:** The list length **must** match the number of columns, otherwise you’ll get an error.

---

## Quick Cheat-Sheet

| Goal                              | Code (one-liner)                                   |
|-----------------------------------|----------------------------------------------------|
| Rename one column                 | `df.rename(columns={"old": "new"}, inplace=True)` |
| Rename several columns            | `df.rename(columns={"a":"A","b":"B"}, inplace=True)` |
| Replace **all** column names      | `df.columns = ["Col1","Col2","Col3"]`             |
| Keep original df (no `inplace`)   | `new_df = df.rename(columns={...})`               |

---

### Practice on Your Own

```python
# Try it yourself!
practice_df = pd.DataFrame({
    "ID":   [101, 102, 103],
    "Score": [88, 92, 77],
    "Grade": ["B", "A", "C"]
})

# 1. Rename "ID" → "StudentID"
# 2. Rename "Score" → "Marks"
# 3. Print the result
```

**Solution**

```python
practice_df = practice_df.rename(columns={"ID": "StudentID", "Score": "Marks"})
print(practice_df)
```

---
