# Visualizing PS4 Sales Data with Matplotlib

This tutorial will guide you through creating various data visualizations using Matplotlib, a popular Python library for plotting. We'll focus on analyzing hypothetical PS4 sales data, such as monthly sales figures, sales by region, price vs. sales relationships, and more. The examples assume you have Python installed with Matplotlib (you can install it via `pip install matplotlib` if needed).

We'll use the following sample dataset for PS4 sales (in thousands of units):
- Monthly sales over 12 months: [150, 180, 200, 220, 250, 280, 300, 270, 240, 210, 190, 170]
- Sales by region: North America (500), Europe (400), Asia (300), Other (100)
- Scatter data: Prices ([299, 349, 399, 449, 499]) and corresponding sales ([250, 220, 180, 150, 120])

Start by importing Matplotlib and preparing the data in your Python script or Jupyter notebook:

```python
import matplotlib.pyplot as plt

# Sample data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
monthly_sales = [150, 180, 200, 220, 250, 280, 300, 270, 240, 210, 190, 170]  # in thousands
regions = ['North America', 'Europe', 'Asia', 'Other']
region_sales = [500, 400, 300, 100]  # total sales in thousands
prices = [299, 349, 399, 449, 499]  # in USD
price_sales = [250, 220, 180, 150, 120]  # sales in thousands
```

Now, let's dive into each plot type with step-by-step instructions.

#### 1. Histogram: Distribution of Monthly Sales
A histogram is great for showing the frequency distribution of numerical data, like how PS4 monthly sales are spread out.

**Step 1:** Prepare your data. We'll use the `monthly_sales` list.

**Step 2:** Create the histogram using `plt.hist()`. Specify bins for grouping the data.

**Step 3:** Add labels, title, and display the plot.

**Example Code:**
```python
plt.figure(figsize=(8, 5))  # Set figure size
plt.hist(monthly_sales, bins=5, color='skyblue', edgecolor='black')  # bins=5 for 5 groups
plt.title('Distribution of PS4 Monthly Sales')
plt.xlabel('Sales (in thousands)')
plt.ylabel('Frequency')
plt.grid(True)  # Add grid for readability
plt.show()
```

**What it shows:** This histogram groups sales into bins (e.g., 150-200, 200-250). You'll see most months fall in the 200-300 range, indicating peak sales periods. Adjust `bins` for more/less detail.

#### 2. Scatter Plot: Price vs. Sales Relationship
A scatter plot visualizes the relationship between two variables, like how PS4 price affects sales volume.

**Step 1:** Use your paired data: `prices` and `price_sales`.

**Step 2:** Plot points with `plt.scatter()`.

**Step 3:** Add labels, title, and optionally a trend line (using NumPy for a simple linear fit, if installed via `pip install numpy`).

**Example Code:**
```python
import numpy as np  # For trend line (optional)

plt.figure(figsize=(8, 5))
plt.scatter(prices, price_sales, color='red', marker='o')  # Plot points
# Optional trend line
trend = np.polyfit(prices, price_sales, 1)
plt.plot(prices, np.polyval(trend, prices), color='blue', linestyle='--')
plt.title('PS4 Price vs. Sales')
plt.xlabel('Price (USD)')
plt.ylabel('Sales (in thousands)')
plt.grid(True)
plt.show()
```

**What it shows:** Each dot represents a price point and its sales. The downward trend suggests higher prices correlate with lower sales. The dashed line is a simple linear regression for visualization.

#### 3. Line Plot: Monthly Sales Trend Over Time
A line plot is ideal for showing trends over time, such as PS4 sales across months.

**Step 1:** Use ordered data: `months` for x-axis, `monthly_sales` for y-axis.

**Step 2:** Connect points with `plt.plot()`.

**Step 3:** Customize with markers, labels, and rotation for x-ticks if needed.

**Example Code:**
```python
plt.figure(figsize=(10, 5))  # Wider for months
plt.plot(months, monthly_sales, marker='o', linestyle='-', color='green')  # Line with markers
plt.title('PS4 Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales (in thousands)')
plt.xticks(rotation=45)  # Rotate labels for readability
plt.grid(True)
plt.show()
```

**What it shows:** The line rises to a peak in July (300k) then declines, highlighting seasonal trends like holiday boosts. Markers emphasize individual data points.

#### 4. Bar Plot: Sales by Region
A bar plot compares categorical data, perfect for regional PS4 sales breakdowns.

**Step 1:** Use categories (`regions`) and values (`region_sales`).

**Step 2:** Create bars with `plt.bar()` (vertical) or `plt.barh()` (horizontal).

**Step 3:** Add labels and colors for clarity.

**Example Code:**
```python
plt.figure(figsize=(8, 5))
plt.bar(regions, region_sales, color=['blue', 'orange', 'green', 'red'])  # Different colors per bar
plt.title('PS4 Sales by Region')
plt.xlabel('Region')
plt.ylabel('Total Sales (in thousands)')
plt.grid(axis='y')  # Grid only on y-axis
plt.show()
```

**What it shows:** Bars compare sales, with North America leading at 500k. Use horizontal bars (`plt.barh()`) if labels are long.

#### 5. Pie Chart: Regional Sales Proportion
A pie chart displays parts of a whole, like the percentage of total PS4 sales by region.

**Step 1:** Calculate percentages if needed (Matplotlib handles it automatically with labels).

**Step 2:** Use `plt.pie()` with values and labels.

**Step 3:** Add percentages, explode slices for emphasis, and a title.

**Example Code:**
```python
plt.figure(figsize=(7, 7))  # Square for pie
explode = (0.1, 0, 0, 0)  # Explode the first slice (North America)
plt.pie(region_sales, labels=regions, autopct='%1.1f%%', explode=explode, shadow=True, startangle=90)
plt.title('PS4 Sales Proportion by Region')
plt.axis('equal')  # Equal aspect ratio for circle
plt.show()
```

**What it shows:** The pie divides total sales (1300k) into wedges: North America ~38.5%, Europe ~30.8%, etc. The exploded slice draws attention to the largest share. Use `autopct` for percentage labels.

### Final Tips
- **Customization:** Experiment with colors (`color=`), styles (`linestyle=`), and subplots (`plt.subplot()`) for multiple plots in one figure.
- **Saving Plots:** Add `plt.savefig('filename.png')` before `plt.show()` to export images.
- **Interactivity:** In Jupyter, plots appear inline; in scripts, `plt.show()` opens a window.
- **Advanced:** Combine plots (e.g., bar + line) or use Seaborn for fancier styles (install via `pip install seaborn`).
