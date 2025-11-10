# Introduction to Matplotlib for Beginners


Matplotlib is a popular Python library for creating static, animated, and interactive visualizations. It's widely used for data analysis and is great for beginners because it allows you to start with simple plots and gradually add enhancements. In this step-by-step tutorial, we'll use Matplotlib to analyze PlayStation 4 (PS4) sales data. We'll cover the basics, create simple plots for cumulative and annual sales, and then enhance them with labels, colors, and more.

We'll use approximate real-world PS4 sales data (in millions of units) based on publicly available figures from sources like Sony's reports and industry trackers. The PS4 launched in November 2013 and sold over 117 million units by 2022.

**Prerequisites:**
- Python installed on your machine.
- Matplotlib installed (run `pip install matplotlib` in your terminal if needed).
- We'll also use NumPy for simple data handling (install with `pip install numpy`).

All code examples can be run in a Python script or Jupyter Notebook. Let's dive in!

### Step 1: Importing Matplotlib and Preparing Data
Start by importing the necessary libraries. Matplotlib's `pyplot` module provides a simple interface for plotting.

```python
import matplotlib.pyplot as plt
import numpy as np
```

Next, prepare the data. We'll use two datasets:
- Cumulative sales (total units sold up to the end of each year).
- Annual sales (units sold in each year, calculated as the difference from the previous year).

```python
# Years and approximate cumulative sales (in millions)
years = np.array(['2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022'])
cum_sales = np.array([4.2, 18.5, 35.9, 53.4, 73.6, 91.6, 106.0, 110.4, 115.9, 117.2])

# Calculate annual sales as differences (first year is the initial value)
annual_sales = np.diff(cum_sales, prepend=0)  # prepend=0 to handle the first year
```

This gives us:
- `cum_sales`: [4.2, 18.5, 35.9, ...]
- `annual_sales`: [4.2, 14.3, 17.4, 17.5, 20.2, 18.0, 14.4, 4.4, 5.5, 1.3]

### Step 2: Creating a Basic Line Plot (Matplotlib Basics)
A line plot is ideal for showing trends over time, like cumulative sales growth.

```python
# Create a figure and axis
plt.figure(figsize=(10, 5))  # Set figure size (width=10, height=5 inches)

# Plot the data
plt.plot(years, cum_sales)  # x-axis: years, y-axis: cum_sales

# Display the plot
plt.show()
```

This generates a simple line plot. The `plt.plot()` function connects the points with lines. `plt.show()` displays it (in a script) or renders it inline (in Jupyter).

What you'll see: A basic line showing sales increasing over time, but without labels or titles—it's plain!

### Step 3: Adding Basic Enhancements
Let's make it more informative by adding axis labels, a title, and a grid.

```python
plt.figure(figsize=(10, 5))

plt.plot(years, cum_sales, marker='o')  # Add circle markers for data points

# Add labels and title
plt.xlabel('Year')  # x-axis label
plt.ylabel('Cumulative Sales (Millions)')  # y-axis label
plt.title('PS4 Cumulative Sales Over Time')  # Plot title

# Add a grid for readability
plt.grid(True)

plt.show()
```

Improvements:
- `marker='o'`: Adds dots at each data point.
- Labels and title: Explain what the plot shows.
- `plt.grid(True)`: Adds a background grid.

Now the plot is clearer and more professional.

### Step 4: Creating a Bar Chart for Annual Sales
Bar charts are great for comparing values, like yearly sales.

```python
plt.figure(figsize=(10, 5))

# Create bar chart
plt.bar(years, annual_sales)  # x: years, y: annual_sales

plt.xlabel('Year')
plt.ylabel('Annual Sales (Millions)')
plt.title('PS4 Annual Sales')

plt.show()
```

This shows bars for each year's sales. Notice the peak around 2017 (about 20 million units), reflecting the PS4's strongest year.

### Step 5: Enhancing the Bar Chart
Add colors, rotate x-axis labels (for better readability), and include data labels on bars.

```python
plt.figure(figsize=(10, 5))

# Bar chart with custom color
plt.bar(years, annual_sales, color='skyblue')  # Set bar color

# Add data labels on top of bars
for i, value in enumerate(annual_sales):
    plt.text(i, value + 0.2, f'{value:.1f}', ha='center')  # Display value above bar

plt.xlabel('Year')
plt.ylabel('Annual Sales (Millions)')
plt.title('PS4 Annual Sales')
plt.xticks(rotation=45)  # Rotate x-axis labels for better fit
plt.grid(axis='y')  # Grid only on y-axis

plt.show()
```

Enhancements:
- `color='skyblue'`: Changes bar color (you can use hex codes like '#FF5733' too).
- Data labels: Use `plt.text()` in a loop to add numbers above each bar.
- `plt.xticks(rotation=45)`: Tilts year labels.
- `plt.grid(axis='y')`: Horizontal grid lines only.

This makes the chart more engaging and easier to interpret—sales peaked in 2017 and declined as the PS5 launched.

### Step 6: Combining Plots (Subplots for Advanced Analysis)
To compare cumulative and annual sales side-by-side, use subplots.

```python
fig, axs = plt.subplots(1, 2, figsize=(15, 5))  # 1 row, 2 columns

# Left subplot: Cumulative line plot
axs[0].plot(years, cum_sales, marker='o', color='green')
axs[0].set_xlabel('Year')
axs[0].set_ylabel('Cumulative Sales (Millions)')
axs[0].set_title('Cumulative Sales')
axs[0].grid(True)

# Right subplot: Annual bar chart
axs[1].bar(years, annual_sales, color='orange')
for i, value in enumerate(annual_sales):
    axs[1].text(i, value + 0.2, f'{value:.1f}', ha='center')
axs[1].set_xlabel('Year')
axs[1].set_ylabel('Annual Sales (Millions)')
axs[1].set_title('Annual Sales')
axs[1].set_xticklabels(years, rotation=45)
axs[1].grid(axis='y')

plt.suptitle('PS4 Sales Analysis')  # Overall title
plt.tight_layout()  # Adjust spacing
plt.show()
```

This creates a figure with two plots:
- Left: Enhanced line plot in green.
- Right: Enhanced bar chart in orange.
- `plt.suptitle()`: Adds a main title.
- `plt.tight_layout()`: Prevents overlapping.

### Step 7: Saving and Customizing Further
To save your plot as an image (e.g., PNG or PDF):

```python
# After creating a plot, add:
plt.savefig('ps4_sales_analysis.png', dpi=300)  # High resolution
```

More customizations:
- Change line style: `plt.plot(..., linestyle='--')` for dashed lines.
- Add legend: If multiple lines, use `plt.plot(..., label='Cumulative')` then `plt.legend()`.
- Themes: `plt.style.use('ggplot')` for a different look (try 'seaborn', 'bmh', etc.).

### Key Insights from the Data
- The PS4 saw explosive growth from 2013–2017, peaking annual sales at ~20 million in 2017.
- Sales tapered off post-2019 due to the PS5 launch in 2020.
- Total lifetime sales: ~117 million units, making it one of the best-selling consoles ever.

Practice by tweaking the code—change colors, add more data, or plot regional sales if you find more datasets. Matplotlib has extensive documentation at [matplotlib.org](https://matplotlib.org) for advanced features like 3D plots or animations. Happy plotting! If you run into issues, share your code output for troubleshooting.
