# Matplotlib


Matplotlib is the most popular Python library for creating **static, animated, and interactive visualizations**. It is highly customizable and works great with NumPy, pandas, and seaborn.

## 1. Installation & Setup
```bash
pip install matplotlib numpy
```

**Basic import (always start with this):**
```python
import matplotlib.pyplot as plt
import numpy as np
```

**Show a plot in Jupyter/Colab:**
```python
plt.show()
```

**Save a plot as image:**
```python
plt.savefig('my_plot.png', dpi=300, bbox_inches='tight')
```

---

## 2. Your First Plot – Line Plot (with customization)

```python
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x, y1, 'b-', linewidth=2, label='sin(x)')
ax.plot(x, y2, 'r--', linewidth=2, label='cos(x)')
ax.set_title('Line Plot Example: sin(x) and cos(x)')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend()
plt.show()
```

**Result:**



**Key takeaways:**
- `plt.subplots()` → creates figure + axes (recommended way)
- `ax.plot()` → line plot
- `linewidth`, `linestyle` (`-`, `--`, `-.`, `:`), `color` (`'b'`, `'r'`, hex codes)
- `set_title()`, `set_xlabel()`, `set_ylabel()`
- `legend()`, `grid()`

---

## 3. Scatter Plot

```python
np.random.seed(42)
x = np.random.rand(100)
y = 2 * x + np.random.randn(100) * 0.3

plt.figure(figsize=(8, 5))
plt.scatter(x, y, c=np.random.rand(100), s=100*np.random.rand(100),
            alpha=0.6, cmap='viridis')
plt.title('Scatter Plot Example')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.colorbar(label='Color intensity')
plt.grid(True, alpha=0.3)
plt.show()
```

**Result:**



**Pro tips:**
- `c=` for color mapping
- `s=` for marker size
- `cmap=` (viridis, plasma, coolwarm, etc.)
- `alpha=` for transparency

---

## 4. Bar Plot (with value labels)

```python
categories = ['Category A', 'Category B', 'Category C', 'Category D', 'Category E']
values = [23, 45, 12, 67, 34]

plt.figure(figsize=(8, 5))
bars = plt.bar(categories, values, color=['#1f77b4','#ff7f0e','#2ca02c','#d62728','#9467bd'])
plt.title('Bar Plot Example')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Add value labels on top of bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 1,
             f'{height}', ha='center', va='bottom')
plt.show()
```

**Result:**



---

## 5. Histogram

```python
data = np.random.normal(0, 1, 1000)

plt.figure(figsize=(8, 5))
plt.hist(data, bins=30, color='#2ca02c', alpha=0.7, edgecolor='black')
plt.title('Histogram Example')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True, alpha=0.3)
plt.show()
```

**Result:**



**Useful options:**
- `bins=30` or `bins='auto'`
- `density=True` (for probability density)

---

## 6. Pie Chart

```python
labels = ['Python', 'JavaScript', 'Java', 'C++', 'Others']
sizes = [45, 25, 15, 10, 5]
explode = (0.1, 0, 0, 0, 0)   # explode first slice

plt.figure(figsize=(8, 5))
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90,
        colors=['#1f77b4','#ff7f0e','#2ca02c','#d62728','#9467bd'])
plt.title('Pie Chart Example: Programming Language Popularity')
plt.axis('equal')
plt.show()
```

**Result:**



---

## 7. Subplots (Multiple plots in one figure)

```python
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

axs[0,0].plot(x, np.sin(x))
axs[0,0].set_title('Line Plot')

axs[0,1].scatter(x[:50], y[:50])
axs[0,1].set_title('Scatter Plot')

axs[1,0].bar(['A','B','C','D'], [23,45,12,67])
axs[1,0].set_title('Bar Plot')

axs[1,1].hist(np.random.randn(1000), bins=20, color='orange', alpha=0.7)
axs[1,1].set_title('Histogram')

plt.suptitle('Subplots Example: Combining Multiple Plots')
plt.tight_layout()
plt.show()
```

**Result:**



**Pro tip:** Use `fig, axs = plt.subplots(nrows, ncols)` and `plt.tight_layout()` or `plt.suptitle()`.

---

## 8. Quick Customization Cheat Sheet

| Task                        | Code Example                                      |
|-----------------------------|---------------------------------------------------|
| Figure size                 | `plt.figure(figsize=(10,6))`                     |
| Title                       | `plt.title('My Title', fontsize=16)`             |
| Labels                      | `plt.xlabel('X')`, `plt.ylabel('Y')`             |
| Legend                      | `plt.legend(['Line1', 'Line2'])`                  |
| Grid                        | `plt.grid(True, linestyle='--')`                  |
| Colors                      | `'r'`, `'blue'`, `'#FF5733'`, or colormap        |
| Line styles                 | `'-'`, `'--'`, `'-.'`, `':'`                     |
| Marker styles               | `'o'`, `'s'`, `'^'`, `'*'`                        |
| Rotate x-ticks              | `plt.xticks(rotation=45)`                         |
| Global style                | `plt.style.use('seaborn-v0_8-darkgrid')`         |
| Save high-res               | `plt.savefig('plot.png', dpi=300, bbox_inches='tight')` |

**Popular styles:** `default`, `seaborn-v0_8`, `ggplot`, `fivethirtyeight`, `dark_background`

---

## 9. Bonus Tips for Beginners

1. Always use **object-oriented style** (`fig, ax = plt.subplots()`) instead of `plt.plot()` for complex plots.
2. `plt.tight_layout()` or `fig.tight_layout()` fixes overlapping labels.
3. For pandas DataFrame: `df.plot(kind='line')` works directly!
4. Combine with seaborn for beautiful default styles:
   ```python
   import seaborn as sns
   sns.set_style("whitegrid")
   ```
5. Need 3D? `from mpl_toolkits.mplot3d import Axes3D`

---
