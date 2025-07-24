# Introduction to Matplotlib Tutorial for Beginners

This tutorial introduces Matplotlib, a powerful Python library for data visualization, and guides you through creating and customizing various plots. Designed for beginners, it includes step-by-step instructions and examples to help you get started with Matplotlib.

---

## Session 1: Introduction to Matplotlib
**Date:** June 26, 2025  
**Duration:** 1 Hour  
**Objective:** Understand what Matplotlib is, its importance in data visualization, and learn to create basic plots.

### Step 1: Understanding Matplotlib
Matplotlib is a Python library for creating static, animated, and interactive visualizations. It is widely used in data science, machine learning, and scientific research to visualize data in a clear and informative way. Its `matplotlib.pyplot` module provides a simple interface for plotting.

**Why is Matplotlib important?**
- Visualizes complex data for better understanding.
- Supports a wide range of plots (line, scatter, bar, histograms, etc.).
- Highly customizable for professional-quality graphics.

### Step 2: Installing Matplotlib
Before using Matplotlib, ensure it is installed. If not, you can install it using `pip` or `conda`.

#### Using pip:
1. Open your terminal or command prompt.
2. Run the following command:
   ```bash
   pip install matplotlib
   ```
3. Verify installation by importing Matplotlib in Python:
   ```python
   import matplotlib
   print(matplotlib.__version__)
   ```

#### Using conda:
1. Open your terminal or Anaconda Prompt.
2. Run:
   ```bash
   conda install matplotlib
   ```
3. Verify as above.

**Note:** If you're using Jupyter Notebook or an IDE like VSCode, ensure you have Python and Matplotlib installed in your environment.

### Step 3: Basic Plotting with `matplotlib.pyplot`
Let’s create simple plots using the `matplotlib.pyplot` module. Below are examples of common plot types.

#### Example 1: Line Plot
A line plot connects data points with lines, ideal for showing trends over time.

```python
import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

# Create a line plot
plt.plot(x, y)
plt.show()
```

**Explanation:**
- `plt.plot(x, y)` creates the line plot.
- `plt.show()` displays the plot.

#### Example 2: Scatter Plot
A scatter plot displays individual data points, useful for showing relationships between variables.

```python
import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

# Create a scatter plot
plt.scatter(x, y)
plt.show()
```

#### Example 3: Bar Plot
A bar plot represents categorical data with rectangular bars.

```python
import matplotlib.pyplot as plt

# Data
categories = ['A', 'B', 'C', 'D']
values = [4, 3, 2, 5]

# Create a bar plot
plt.bar(categories, values)
plt.show()
```

#### Example 4: Histogram
A histogram shows the distribution of numerical data.

```python
import matplotlib.pyplot as plt
import numpy as np

# Data
data = np.random.randn(1000)  # Random data

# Create a histogram
plt.hist(data, bins=30)
plt.show()
```

**Explanation:**
- `bins=30` specifies the number of bins (intervals) for the histogram.

#### Example 5: Box Plot
A box plot visualizes data distribution through quartiles, highlighting outliers.

```python
import matplotlib.pyplot as plt
import numpy as np

# Data
data = [np.random.randn(100), np.random.randn(100) + 2, np.random.randn(100) - 2]

# Create a box plot
plt.boxplot(data)
plt.show()
```

**Explanation:**
- `plt.boxplot(data)` creates a box plot for each dataset in the list.

### Assignment for Session 1
1. Install Matplotlib and verify the installation by printing its version.
2. Create a line plot with x-values `[1, 2, 3, 4]` and y-values `[10, 20, 25, 30]`.
3. Create a scatter plot with x-values `[0, 1, 2, 3, 4]` and y-values `[5, 7, 2, 8, 6]`.
4. Create a bar plot with categories `['X', 'Y', 'Z']` and values `[10, 15, 7]`.
5. Generate a histogram with 100 random numbers using `np.random.randn(100)`.
6. Create a box plot with two datasets: `np.random.randn(50)` and `np.random.randn(50) + 1`.

---

## Session 2: Customizing Plots
**Date:** June 26, 2025  
**Duration:** 1 Hour  
**Objective:** Learn how to customize plots by adding titles, labels, legends, and adjusting styles, axes, and annotations.

### Step 1: Adding Titles, Labels, and Legends
Titles and labels make plots more informative, while legends identify multiple datasets.

#### Example: Customized Line Plot
```python
import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.array([1, 2, 3, 4, 5])
y1 = np.array([2, 4, 6, 8, 10])
y2 = np.array([1, 3, 5, 7, 9])

# Create line plots
plt.plot(x, y1, label='Dataset 1')
plt.plot(x, y2, label='Dataset 2')

# Add title and labels
plt.title('Customized Line Plot')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

# Add legend
plt.legend()

plt.show()
```

**Explanation:**
- `plt.title()` sets the plot title.
- `plt.xlabel()` and `plt.ylabel()` label the axes.
- `plt.legend()` displays the legend based on the `label` parameter in `plt.plot()`.

### Step 2: Changing Colors, Line Styles, and Marker Styles
You can customize the appearance of plots using colors, line styles, and markers.

#### Example: Customized Scatter Plot
```python
import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

# Create scatter plot with customization
plt.scatter(x, y, color='red', marker='^', s=100)

# Add title and labels
plt.title('Customized Scatter Plot')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

plt.show()
```

**Explanation:**
- `color='red'` sets the marker color.
- `marker='^'` uses triangle markers.
- `s=100` sets the marker size.

### Step 3: Adjusting Axis Limits and Ticks
You can control the range and tick marks on axes for better readability.

#### Example: Line Plot with Custom Axes
```python
import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

# Create line plot
plt.plot(x, y)

# Set axis limits
plt.xlim(0, 6)
plt.ylim(0, 12)

# Customize ticks
plt.xticks(np.arange(0, 7, 1))
plt.yticks(np.arange(0, 13, 2))

# Add title and labels
plt.title('Line Plot with Custom Axes')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

plt.show()
```

**Explanation:**
- `plt.xlim(0, 6)` and `plt.ylim(0, 12)` set the axis ranges.
- `plt.xticks()` and `plt.yticks()` customize tick marks.

### Step 4: Adding Annotations
Annotations highlight specific points or add text to plots.

#### Example: Scatter Plot with Annotations
```python
import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

# Create scatter plot
plt.scatter(x, y)

# Add annotation
plt.annotate('Highest Point', xy=(5, 10), xytext=(4, 8),
             arrowprops=dict(facecolor='black', arrowstyle='->'))

# Add title and labels
plt.title('Scatter Plot with Annotation')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

plt.show()
```

**Explanation:**
- `plt.annotate()` adds text and an arrow pointing to a specific point.

### Assignment for Session 2
1. Create a line plot with two datasets: `y1 = [1, 4, 9, 16]` and `y2 = [2, 5, 8, 11]` for `x = [1, 2, 3, 4]`. Add a title, axis labels, and a legend.
2. Create a scatter plot with `x = [1, 2, 3, 4]` and `y = [10, 20, 25, 30]`. Use blue circles as markers and set the marker size to 150.
3. Create a bar plot with categories `['A', 'B', 'C']` and values `[5, 10, 15]`. Set custom axis limits and ticks.
4. Create a line plot with `x = [0, 1, 2, 3]` and `y = [0, 1, 4, 9]`. Add an annotation at the point `(3, 9)` with the text “Peak Value”.

---

### Tips for Success
- Use Jupyter Notebook or an IDE for interactive plotting.
- Experiment with different colors, markers, and styles to understand their effects.
- Refer to the [Matplotlib documentation](https://matplotlib.org/stable/contents.html) for more customization options.
- Save your plots using `plt.savefig('plot.png')` if needed.