# **Seaborn Visualization**  
**5 Essential Plots with Simple Examples**

Seaborn is a **beautiful** and **easy** Python library for statistical plots.  
It works on top of **Matplotlib** and integrates perfectly with **Pandas**.

---

## Setup (Run Once)

```python
# Install if needed (uncomment)
# !pip install seaborn matplotlib pandas

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Optional: Nice style
sns.set_style("whitegrid")
```

---

## Sample Data (We’ll Use This for All Plots)

```python
# Create a simple dataset
data = {
    'Student': ['Ali', 'Beth', 'Cathy', 'David', 'Emma', 'Frank', 'Grace', 'Hank'],
    'Math': [85, 90, 78, 92, 88, 70, 95, 80],
    'Science': [88, 92, 80, 85, 90, 75, 93, 78],
    'Gender': ['M', 'F', 'F', 'M', 'F', 'M', 'F', 'M'],
    'Study_Hours': [5, 6, 4, 7, 6, 3, 8, 5]
}

df = pd.DataFrame(data)
print(df)
```

**Output:**
```
  Student  Math  Science Gender  Study_Hours
0     Ali    85       88      M            5
1    Beth    90       92      F            6
2   Cathy    78       80      F            4
3   David    92       85      M            7
4    Emma    88       90      F            6
5   Frank    70       75      M            3
6   Grace    95       93      F            8
7    Hank    80       78      M            5
```

---

Let’s make **5 plots**!

---

## 1. **Box Plot** – Show Distribution & Outliers

> **Use**: Compare spread, median, outliers across groups.

```python
plt.figure(figsize=(6,4))
sns.boxplot(x='Gender', y='Math', data=df)
plt.title('Math Scores by Gender')
plt.show()
```

**What you see**:
- Median line
- Box = 25th to 75th percentile
- Whiskers = range
- Dots = outliers

---

## 2. **Line Plot** – Show Trends Over Time/Order

> **Use**: Show change over time or sequence.

```python
# Sort by Study Hours for smooth line
df_sorted = df.sort_values('Study_Hours')

plt.figure(figsize=(6,4))
sns.lineplot(x='Study_Hours', y='Math', data=df_sorted, marker='o')
plt.title('Math Score vs Study Hours')
plt.show()
```

**Tip**: Add `hue='Gender'` to compare groups:
```python
sns.lineplot(x='Study_Hours', y='Math', hue='Gender', marker='o', data=df_sorted)
```

---

## 3. **Histogram** – Show Frequency Distribution

> **Use**: See how data is distributed (e.g., most common scores).

```python
plt.figure(figsize=(6,4))
sns.histplot(df['Science'], bins=5, kde=True, color='skyblue')
plt.title('Distribution of Science Scores')
plt.xlabel('Science Score')
plt.show()
```

- `bins=5`: number of bars
- `kde=True`: adds smooth curve

---

## 4. **Scatter Plot** – Show Relationship Between 2 Variables

> **Use**: See if two things are related (correlation).

```python
plt.figure(figsize=(6,4))
sns.scatterplot(x='Study_Hours', y='Math', hue='Gender', size='Science',
                data=df, palette='deep')
plt.title('Study Hours vs Math Score')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()
```

- `hue`: color by group
- `size`: bubble size by another variable

---

## 5. **Bar Plot** – Compare Averages Across Groups

> **Use**: Show average value per category.

```python
plt.figure(figsize=(6,4))
sns.barplot(x='Gender', y='Science', data=df, ci=None, palette='muted')
plt.title('Average Science Score by Gender')
plt.show()
```

- `ci=None`: removes error bars (for simplicity)
- Bars show **mean**

---

## All 5 Plots in One Figure (Optional)

```python
fig, axes = plt.subplots(2, 3, figsize=(15, 8))
fig.suptitle('Seaborn 5 Essential Plots', fontsize=16)

# 1. Boxplot
sns.boxplot(x='Gender', y='Math', data=df, ax=axes[0,0])
axes[0,0].set_title('Box Plot')

# 2. Line plot
sns.lineplot(x='Study_Hours', y='Math', data=df.sort_values('Study_Hours'), 
             marker='o', ax=axes[0,1])
axes[0,1].set_title('Line Plot')

# 3. Histogram
sns.histplot(df['Science'], bins=5, kde=True, ax=axes[0,2])
axes[0,2].set_title('Histogram')

# 4. Scatter plot
sns.scatterplot(x='Study_Hours', y='Math', hue='Gender', data=df, ax=axes[1,0])
axes[1,0].set_title('Scatter Plot')
axes[1,0].legend().remove()

# 5. Bar plot
sns.barplot(x='Gender', y='Science', data=df, ax=axes[1,1])
axes[1,1].set_title('Bar Plot')

# Hide empty subplot
axes[1,2].axis('off')

plt.tight_layout()
plt.show()
```

---

## Quick Cheat Sheet

| Plot | Code |
|------|------|
| **Box** | `sns.boxplot(x='cat', y='num', data=df)` |
| **Line** | `sns.lineplot(x='num1', y='num2', data=df)` |
| **Histogram** | `sns.histplot(df['col'], bins=10)` |
| **Scatter** | `sns.scatterplot(x='x', y='y', hue='cat', data=df)` |
| **Bar** | `sns.barplot(x='cat', y='num', data=df)` |

---

## Practice: Try This!

```python
# Your turn!
# 1. Make a boxplot of Science scores by Gender
# 2. Make a scatterplot of Math vs Science
# 3. Make a bar plot of average Study_Hours by Gender
```

**Solutions:**
```python
sns.boxplot(x='Gender', y='Science', data=df); plt.show()
sns.scatterplot(x='Math', y='Science', data=df); plt.show()
sns.barplot(x='Gender', y='Study_Hours', data=df); plt.show()
```

---

## Summary

| Plot | Best For |
|------|----------|
| **Box Plot** | Distribution, outliers |
| **Line Plot** | Trends over time |
| **Histogram** | Frequency distribution |
| **Scatter Plot** | Relationship between 2 numbers |
| **Bar Plot** | Compare averages |

---

