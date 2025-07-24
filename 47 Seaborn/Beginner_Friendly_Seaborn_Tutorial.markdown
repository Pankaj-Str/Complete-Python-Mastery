# Beginner-Friendly Seaborn Tutorial

**Date:** June 27, 2025  
**Duration:** 1 Hour  
**Objective:** Learn the basics of Seaborn, a Python tool for making beautiful charts, and create different types of plots with simple examples.

---

## What is Seaborn?
Seaborn is a Python library that makes it easy to create colorful and informative charts (like graphs and plots) to understand data. It’s built on top of another library called Matplotlib but is simpler to use and creates prettier visuals. Seaborn is great for:
- Showing patterns in data (e.g., relationships between numbers).
- Making charts like histograms, box plots, and heatmaps.
- Working with data tables (like spreadsheets).

In this tutorial, we’ll use the **Iris dataset** (a table with flower measurements) to practice making different charts.

---

## Step 1: Installing Seaborn
Before we start, we need to install Seaborn. You’ll also need Python installed on your computer.

### How to Install Seaborn
1. Open your computer’s terminal (on Windows, use Command Prompt or PowerShell; on Mac/Linux, use Terminal).
2. Type this command and press Enter:
   ```bash
   pip install seaborn
   ```
3. To check if Seaborn is installed, open Python (e.g., in IDLE, VSCode, or Jupyter Notebook) and run:
   ```python
   import seaborn as sns
   print(sns.__version__)
   ```
   If you see a version number (e.g., 0.13.2), Seaborn is ready!

**Alternative (if you use Anaconda):**
Run this in the Anaconda Prompt:
```bash
conda install seaborn
```

**Note:** Seaborn needs other libraries like NumPy, Pandas, and Matplotlib. If the above commands don’t work, try `pip install numpy pandas matplotlib seaborn`.

---

## Step 2: Setting Up Your Python Environment
We’ll use Python with Seaborn, Matplotlib (for displaying plots), and Pandas (for handling data). Here’s how to start:

```python
import seaborn as sns
import matplotlib.pyplot as plt  # Needed to show plots
import pandas as pd  # For working with data tables
```

We’ll also use Seaborn’s built-in **Iris dataset**, which has measurements of flowers (sepal length, sepal width, petal length, petal width, and species).

```python
# Load the Iris dataset
iris = sns.load_dataset('iris')
print(iris.head())  # Shows the first 5 rows of the data
```

**What this does:** This loads a table with flower data. The `head()` function shows a preview so you can see what the data looks like.

---

## Step 3: Exploring Data with `sns.pairplot`
A **pairplot** shows how different columns in your data relate to each other. It creates a grid of scatter plots and histograms.

### Example: Pairplot
```python
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
iris = sns.load_dataset('iris')

# Create a pairplot
sns.pairplot(iris, hue='species')  # Colors points by flower species
plt.show()  # Displays the plot
```

**What you’ll see:** A grid of charts. Each square shows how two measurements (like sepal length vs. petal length) relate, with points colored by species (setosa, versicolor, virginica). The diagonal shows histograms for each measurement.

**Why it’s useful:** Helps you spot patterns, like how petal length differs between species.

---

## Step 4: Showing Correlations with `sns.heatmap`
A **heatmap** shows how strongly columns in your data are related (using correlation). Numbers closer to 1 or -1 mean a strong relationship; numbers near 0 mean no relationship.

### Example: Heatmap
```python
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
iris = sns.load_dataset('iris')

# Calculate correlations (only for number columns)
corr = iris.drop(columns='species').corr()

# Create heatmap
sns.heatmap(corr, annot=True, cmap='coolwarm')  # annot=True shows numbers
plt.show()
```

**What you’ll see:** A colorful grid where each square shows a correlation number. Red means a strong positive relationship; blue means a strong negative relationship.

**Why it’s useful:** You can quickly see which measurements (e.g., petal length and sepal length) are related.

---

## Step 5: Scatterplot Matrices (Using `sns.pairplot`)
We already saw `pairplot` in Step 3. It’s also called a scatterplot matrix because it shows scatter plots for all pairs of columns. Let’s make a simpler version with just two columns.

### Example: Simplified Pairplot
```python
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
iris = sns.load_dataset('iris')

# Create pairplot for two columns
sns.pairplot(iris, vars=['sepal_length', 'sepal_width'], hue='species')
plt.show()
```

**What you’ll see:** A smaller grid showing scatter plots and histograms for just sepal length and sepal width, colored by species.

**Why it’s useful:** Focuses on specific columns to avoid overwhelming beginners.

---

## Step 6: Kernel Density Estimation (KDE) with `sns.kdeplot`
A **KDE plot** is like a smooth line that shows the shape of your data’s distribution (how values are spread out).

### Example: KDE Plot
```python
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
iris = sns.load_dataset('iris')

# Create KDE plot
sns.kdeplot(data=iris, x='sepal_length', hue='species')  # One line per species
plt.show()
```

**What you’ll see:** Smooth curves showing how sepal length is distributed for each flower species.

**Why it’s useful:** It’s a prettier way to see data distribution compared to a histogram.

---

## Step 7: Visualizing Distributions with `sns.histplot`
A **histogram** shows how often different values appear in your data. Seaborn’s `histplot` can also add a KDE curve.

**Note:** Older tutorials might mention `sns.distplot`, but it’s outdated. Use `sns.histplot` instead.

### Example: Histogram with KDE
```python
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
iris = sns.load_dataset('iris')

# Create histogram with KDE
sns.histplot(data=iris, x='sepal_length', kde=True)  # kde=True adds a smooth line
plt.show()
```

**What you’ll see:** Bars showing how many flowers have different sepal lengths, with a smooth KDE line on top.

**Why it’s useful:** Helps you understand the spread of a single measurement.

---

## Step 8: Scatter Plots with `sns.scatterplot`
A **scatter plot** shows individual data points to reveal relationships between two measurements.

### Example: Scatter Plot
```python
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
iris = sns.load_dataset('iris')

# Create scatter plot
sns.scatterplot(data=iris, x='sepal_length', y='sepal_width', hue='species')
plt.show()
```

**What you’ll see:** Dots showing sepal length vs. sepal width, with different colors for each species.

**Why it’s useful:** Shows how two measurements relate and how species differ.

---

## Step 9: Line Plots with `sns.lineplot`
A **line plot** connects points with a line, great for showing trends (e.g., over time).

### Example: Line Plot
```python
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Create sample data
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

# Create line plot
sns.lineplot(x=x, y=y)
plt.show()
```

**What you’ll see:** A line connecting the points, showing a trend.

**Why it’s useful:** Good for simple trends or patterns.

---

## Step 10: Histograms (Again, for Practice)
Let’s make a histogram with colors for each species.

### Example: Stacked Histogram
```python
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
iris = sns.load_dataset('iris')

# Create histogram
sns.histplot(data=iris, x='petal_length', hue='species', multiple='stack')
plt.show()
```

**What you’ll see:** Stacked bars showing petal length distributions for each species.

**Why it’s useful:** Compares distributions across groups.

---

## Step 11: Box Plots with `sns.boxplot`
A **box plot** shows the spread and outliers of your data.

### Example: Box Plot
```python
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
iris = sns.load_dataset('iris')

# Create box plot
sns.boxplot(data=iris, x='species', y='petal_length')
plt.show()
```

**What you’ll see:** Boxes showing the range of petal lengths for each species, with lines for medians and dots for outliers.

**Why it’s useful:** Summarizes data spread and highlights unusual values.

---

## Step 12: Violin Plots with `sns.violinplot`
A **violin plot** is like a box plot but also shows the shape of the data’s distribution.

### Example: Violin Plot
```python
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
iris = sns.load_dataset('iris')

# Create violin plot
sns.violinplot(data=iris, x='species', y='petal_length')
plt.show()
```

**What you’ll see:** Violin-shaped plots showing the distribution of petal lengths for each species.

**Why it’s useful:** Combines box plot and KDE for a detailed view.

---

## Assignment for Practice
Try these tasks to practice what you’ve learned. Use the Iris dataset unless specified.

1. **Install Seaborn**: Install Seaborn and check its version by printing it.
2. **Pairplot**: Create a pairplot for the Iris dataset with `hue='species'`.
3. **Heatmap**: Make a heatmap of the correlations in the Iris dataset (exclude the species column).
4. **KDE Plot**: Create a KDE plot for `petal_length`, with different lines for each species.
5. **Scatter Plot**: Make a scatter plot of `petal_length` vs. `petal_width`, colored by species.
6. **Line Plot**: Create a line plot for `y = [1, 3, 2, 4]` and `x = [1, 2, 3, 4]`.
7. **Histogram**: Create a histogram of `sepal_width` with `kde=True`.
8. **Box Plot**: Make a box plot of `sepal_length` grouped by species.
9. **Violin Plot**: Create a violin plot of `sepal_width` grouped by species.

---

## Tips for Beginners
- **Use Jupyter Notebook**: It’s great for running code and seeing plots instantly. Install it with `pip install jupyter` and run `jupyter notebook` in your terminal.
- **Try Different Datasets**: Seaborn has other datasets like `tips` or `titanic`. Load them with `sns.load_dataset('tips')`.
- **Experiment**: Change `hue`, colors, or columns to see how plots change.
- **Save Your Plot**: Add `plt.savefig('my_plot.png')` before `plt.show()` to save your chart as an image.
- **Learn More**: Check the [Seaborn website](https://seaborn.pydata.org/) for more examples.

---

This tutorial keeps things simple and uses the Iris dataset to make learning easy. Run each example in Python to see the results, and try the assignments to build your skills!