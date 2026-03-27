# Matplotlib Tutorial for Beginners



---

### Step 1: Installation (Do this once)

Open your terminal (or Anaconda Prompt) and type:

```bash
pip install matplotlib
```

(If you’re using Jupyter Notebook or Google Colab, it’s usually already installed.)

---

### Step 2: Import the Library

Every Matplotlib program starts with this:

```python
import matplotlib.pyplot as plt
import numpy as np          # We use this to create sample data
```

`plt` is the shortcut we’ll use for everything.

---

### Step 3: Your First Plot – Simple Line Plot

```python
import matplotlib.pyplot as plt
import numpy as np

# Create some data
x = np.linspace(0, 10, 100)   # 100 numbers from 0 to 10
y = np.sin(x)                 # sin wave

plt.plot(x, y)                # Draw the line
plt.show()                    # Show the plot (in Jupyter it appears automatically)
```

**What just happened?**  
`plt.plot(x, y)` connects the points with a line.

Here’s what it looks like (with nice labels added):



---

### Step 4: Make It Look Professional (Titles, Labels, Grid)

Add these lines **before** `plt.show()`:

```python
plt.title('Simple Line Plot')      # Big title at the top
plt.xlabel('X Axis')               # Label for bottom
plt.ylabel('Y Axis (sin(x))')      # Label for left side
plt.legend(['sin(x)'])             # Shows what the line is
plt.grid(True)                     # Nice grid lines
```

**Pro tip:** Always add titles and labels — your future self will thank you!

---

### Step 5: Scatter Plot (Dots instead of lines)

```python
x = np.random.rand(50)   # 50 random numbers between 0 and 1
y = np.random.rand(50)

plt.scatter(x, y, color='red', s=50, alpha=0.7)  # s = size, alpha = transparency
plt.title('Scatter Plot')
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.grid(True)
plt.show()
```

**Result:**



---

### Step 6: Bar Chart

```python
categories = ['Apples', 'Bananas', 'Oranges', 'Grapes']
values = [25, 40, 30, 20]

plt.bar(categories, values, color=['blue', 'orange', 'green', 'red'])
plt.title('Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.grid(axis='y')      # Grid only on Y axis
plt.show()
```

**Result:**



---

### Step 7: Histogram (Shows distribution)

```python
data = np.random.randn(1000)   # 1000 random numbers (normal distribution)

plt.hist(data, bins=30, color='green', edgecolor='black', alpha=0.7)
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
```

**Result:**



---

### Step 8: Pie Chart

```python
sizes = [35, 25, 20, 20]
labels = ['Python', 'Java', 'C++', 'JavaScript']

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('Pie Chart')
plt.axis('equal')      # Makes it a perfect circle
plt.show()
```

**Result:**



---

### Step 9: Subplots (Multiple Charts in One Figure)

This is super useful!

```python
fig, axs = plt.subplots(2, 2, figsize=(12, 10))  # 2 rows × 2 columns

# Top-left
axs[0, 0].plot(np.linspace(0,10,100), np.sin(np.linspace(0,10,100)))
axs[0, 0].set_title('Line Plot')

# Top-right
axs[0, 1].scatter(np.random.rand(50), np.random.rand(50), color='red')
axs[0, 1].set_title('Scatter Plot')

# Bottom-left
axs[1, 0].bar(['A', 'B', 'C'], [10, 20, 15])
axs[1, 0].set_title('Bar Plot')

# Bottom-right
axs[1, 1].hist(np.random.randn(500), bins=20, color='purple', alpha=0.7)
axs[1, 1].set_title('Histogram')

plt.suptitle('Subplots Example (2×2)')
plt.tight_layout()   # Prevents overlapping
plt.show()
```

**Result:**



---

### Step 10: How to Save Your Plots

Just add this line **before** `plt.show()`:

```python
plt.savefig('my_awesome_plot.png', dpi=300)   # dpi = high quality
```

You can also save as PDF, JPG, SVG, etc.

---

### Bonus Tips for Beginners

1. **Colors & Styles**  
   Try `color='blue'`, `'red'`, `'#FF5733'` (hex code), or use `plt.style.use('seaborn-v0_8')` for instant beauty.

2. **Jupyter Notebook Magic**  
   Add `%matplotlib inline` at the top so plots appear inside the notebook.

3. **Common Mistakes**  
   - Forgetting `plt.show()` in normal Python scripts  
   - Forgetting to import `numpy` when creating data

4. **Next Level (after this tutorial)**  
   - `plt.subplots()` with more control  
   - Using Matplotlib with Pandas (`df.plot()`)  
   - 3D plots (`from mpl_toolkits.mplot3d import Axes3D`)

---
