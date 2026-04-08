# Seaborn

Seaborn is a powerful Python library for **statistical data visualization**. It is built on top of Matplotlib and works seamlessly with Pandas DataFrames. It makes beautiful, publication-ready plots with very little code, especially for exploratory data analysis (EDA).

### Topics Covered in This Tutorial
Here is the complete list of topics we will cover step by step:

1. Installation and Setup  
2. Importing Seaborn and Required Libraries  
3. Loading Built-in Datasets (tips, iris, titanic, etc.)  
4. Understanding Data with `sns.load_dataset()` and Pandas  
5. Relational Plots (`scatterplot`, `lineplot`, `relplot`)  
6. Distribution Plots (`histplot`, `kdeplot`, `displot`)  
7. Categorical Plots (`barplot`, `countplot`, `boxplot`, `violinplot`, `stripplot`, `swarmplot`, `catplot`)  
8. Regression Plots (`regplot`, `lmplot`)  
9. Matrix Plots (`heatmap`)  
10. Multi-plot Grids (`pairplot`, `jointplot`, `FacetGrid`)  
11. Customization (Themes, Color Palettes, Styles, Figure Size)  
12. Saving and Exporting Plots  
13. Best Practices & Common Pitfalls for Beginners  

---

### Step-by-Step Tutorial

#### Step 1: Installation
Open your terminal / command prompt and run:
```bash
pip install seaborn pandas matplotlib numpy
```
(If you are using Jupyter Notebook or Google Colab, just run the same command inside a cell with `!` prefix.)

#### Step 2: Importing Libraries
```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Optional: Set a beautiful default style (highly recommended)
sns.set_theme(style="whitegrid", palette="pastel")
plt.rcParams['figure.figsize'] = (10, 6)  # Default figure size
```

#### Step 3: Loading Built-in Datasets
Seaborn comes with several ready-to-use datasets. Let's load the most popular one:
```python
tips = sns.load_dataset("tips")
print(tips.head())          # View first 5 rows
print(tips.info())          # Data types and missing values
```
**Explanation**:  
- `total_bill`, `tip`: numeric  
- `sex`, `smoker`, `day`, `time`: categorical  
- `size`: integer (party size)  

Other popular datasets: `iris`, `titanic`, `diamonds`, `penguins`, `flights`.

#### Step 4: Relational Plots (Relationship between two numeric variables)

**Example 1: Simple Scatter Plot**
```python
sns.scatterplot(data=tips, x="total_bill", y="tip")
plt.title("Total Bill vs Tip")
plt.show()
```
**Explanation**: Shows how tip amount changes with total bill. Each dot = one customer.

**Example 2: Scatter with Hue, Style & Size (most powerful)**
```python
sns.scatterplot(
    data=tips,
    x="total_bill",
    y="tip",
    hue="sex",          # Color by gender
    style="smoker",     # Different marker shapes
    size="size",        # Size of dots by party size
    palette="deep"
)
plt.title("Tip vs Bill - Colored by Sex & Smoker")
plt.show()
```

**Example 3: Line Plot**
```python
flights = sns.load_dataset("flights")
sns.lineplot(data=flights, x="year", y="passengers", hue="month")
plt.title("Airline Passengers Over Years")
plt.show()
```

**Figure-level version (recommended for beginners)**:
```python
sns.relplot(data=tips, x="total_bill", y="tip", hue="sex", col="time", row="day")
plt.show()
```

#### Step 5: Distribution Plots

**Example 1: Histogram + KDE**
```python
sns.histplot(data=tips, x="total_bill", kde=True, bins=30)
plt.title("Distribution of Total Bill")
plt.show()
```

**Example 2: Separate distributions by category**
```python
sns.displot(data=tips, x="total_bill", hue="sex", kde=True, bins=25)
plt.title("Total Bill Distribution by Sex")
plt.show()
```

**Example 3: ECDF Plot (Empirical Cumulative Distribution)**
```python
sns.ecdfplot(data=tips, x="tip", hue="time")
plt.title("ECDF of Tips")
plt.show()
```

#### Step 6: Categorical Plots

**Example 1: Bar Plot**
```python
sns.barplot(data=tips, x="day", y="total_bill", hue="sex", estimator=np.mean)
plt.title("Average Total Bill by Day and Sex")
plt.show()
```

**Example 2: Count Plot**
```python
sns.countplot(data=tips, x="day", hue="sex")
plt.title("Number of Customers per Day")
plt.show()
```

**Example 3: Box Plot & Violin Plot**
```python
sns.boxplot(data=tips, x="day", y="total_bill", hue="sex")
plt.title("Box Plot - Total Bill by Day")
plt.show()

sns.violinplot(data=tips, x="day", y="total_bill", hue="sex", split=True)
plt.title("Violin Plot - Total Bill by Day")
plt.show()
```

**Example 4: Strip + Swarm Plot**
```python
sns.stripplot(data=tips, x="day", y="total_bill", hue="sex", jitter=True)
plt.title("Strip Plot")
plt.show()

sns.swarmplot(data=tips, x="day", y="total_bill", hue="sex")
plt.title("Swarm Plot (no overlap)")
plt.show()
```

**Figure-level categorical plot**:
```python
sns.catplot(data=tips, x="day", y="total_bill", hue="sex", kind="box", col="time")
```

#### Step 7: Regression Plots

```python
sns.regplot(data=tips, x="total_bill", y="tip")
plt.title("Linear Regression: Bill vs Tip")
plt.show()

sns.lmplot(data=tips, x="total_bill", y="tip", hue="sex", col="time")
```

#### Step 8: Matrix Plots (Heatmap)

```python
# Correlation heatmap
corr = tips.select_dtypes(include=np.number).corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Heatmap")
plt.show()
```

#### Step 9: Multi-plot Grids (Super Useful!)

**Pairplot (best for quick EDA)**
```python
sns.pairplot(tips, hue="sex", diag_kind="kde")
plt.show()
```

**Joint Plot**
```python
sns.jointplot(data=tips, x="total_bill", y="tip", hue="sex", kind="scatter")
plt.show()
```

**FacetGrid (most flexible)**
```python
g = sns.FacetGrid(tips, col="time", row="sex")
g.map_dataframe(sns.scatterplot, x="total_bill", y="tip")
plt.show()
```

#### Step 10: Customization (Make Your Plots Beautiful)

```python
# Global style
sns.set_theme(style="darkgrid", palette="husl", font_scale=1.2)

# Change palette
custom_palette = ["#FF5733", "#33FF57", "#3357FF"]
sns.set_palette(custom_palette)

# For single plot
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="day", palette="viridis")
plt.title("Customized Scatter Plot", fontsize=16, fontweight='bold')
plt.xlabel("Total Bill ($)", fontsize=14)
plt.ylabel("Tip ($)", fontsize=14)
plt.legend(title="Day of Week")
plt.show()
```

#### Step 11: Saving Plots
```python
plt.savefig("my_beautiful_plot.png", dpi=300, bbox_inches="tight")
# or high-quality PDF
plt.savefig("my_plot.pdf", dpi=300, bbox_inches="tight")
```

---

### Seaborn Cheat Sheet (Methods + Most Used Sub-Methods / Parameters)

| Plot Type          | Function                  | Figure-level | Key Parameters (most used)                                      | When to Use                          |
|--------------------|---------------------------|--------------|-----------------------------------------------------------------|--------------------------------------|
| Relational         | `scatterplot`             | `relplot`    | `x, y, hue, style, size, palette, markers`                     | Numeric vs Numeric                   |
| Relational         | `lineplot`                | `relplot`    | `x, y, hue, style, markers, dashes`                            | Time series / Trends                 |
| Distribution       | `histplot`                | `displot`    | `x, hue, kde=True, bins, multiple="stack"`                     | Distribution shape                   |
| Distribution       | `kdeplot`                 | `displot`    | `x, hue, fill=True, bw_adjust`                                  | Smooth density                       |
| Categorical        | `barplot`                 | `catplot`    | `x, y, hue, estimator=np.mean, ci=95`                          | Average comparison                   |
| Categorical        | `countplot`               | `catplot`    | `x, hue, order`                                                 | Count of categories                  |
| Categorical        | `boxplot` / `violinplot`  | `catplot`    | `x, y, hue, split=True (violin)`                               | Distribution + Outliers              |
| Categorical        | `stripplot` / `swarmplot` | `catplot`    | `x, y, hue, jitter=True, dodge=True`                           | Individual points                    |
| Regression         | `regplot`                 | `lmplot`     | `x, y, hue, order=2 (polynomial)`                              | Linear / Polynomial fit              |
| Matrix             | `heatmap`                 | -            | `annot=True, cmap, linewidths, fmt=".2f"`                      | Correlation / Pivot tables           |
| Pairwise           | `pairplot`                | -            | `hue, diag_kind="kde", corner=True`                            | Quick EDA of all numeric columns     |
| Joint              | `jointplot`               | -            | `kind="scatter", "kde", "reg", "hex"`                          | One relationship + marginals         |

**Common Parameters Across Almost All Functions**:
- `data=` → Pandas DataFrame (always use this!)
- `hue=` → Color by category
- `palette=` → "deep", "pastel", "husl", "viridis", "coolwarm", etc.
- `order=` / `hue_order=` → Control order of categories
- `col=` / `row=` → Faceting (in `relplot`, `catplot`, `displot`, `lmplot`)
- `height=` / `aspect=` → Control size in figure-level functions

**Quick Style Commands**:
```python
sns.set_theme(style="whitegrid")      # whitegrid, darkgrid, white, dark, ticks
sns.set_palette("husl")               # best for categorical
plt.figure(figsize=(12, 8))
```

**Pro Tip**: Always start with `relplot`, `displot`, or `catplot` (figure-level) when you want subplots. They are more flexible for beginners.

