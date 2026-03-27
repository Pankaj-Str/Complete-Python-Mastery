# 1. What is Matplotlib?

**Matplotlib** is a Python library used for **data visualization**.
It helps you create:

* Line charts
* Bar charts
* Pie charts
* Scatter plots
* Histograms

It is widely used in **data science, machine learning, and analytics**.

---

# 2. Install Matplotlib

First, install the library:

```bash
pip install matplotlib
```

---

# 3. Import Matplotlib

```python
import matplotlib.pyplot as plt
```

`pyplot` is the main module used for plotting.

---

# 4. Your First Line Plot

### Example:

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y)
plt.show()
```

### Explanation:

* `x` → X-axis values
* `y` → Y-axis values
* `plt.plot()` → creates line graph
* `plt.show()` → displays graph

---

# 5. Adding Labels and Title

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y)

plt.title("Simple Line Graph")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.show()
```

---

# 6. Styling the Line

```python
plt.plot(x, y, color='red', linestyle='--', marker='o')
```

### Options:

* `color` → line color
* `linestyle` → solid, dashed, dotted
* `marker` → point markers

---

# 7. Bar Chart

```python
import matplotlib.pyplot as plt

categories = ["A", "B", "C"]
values = [5, 7, 3]

plt.bar(categories, values)

plt.title("Bar Chart Example")
plt.xlabel("Categories")
plt.ylabel("Values")

plt.show()
```

---

# 8. Pie Chart

```python
import matplotlib.pyplot as plt

labels = ["Python", "Java", "C++"]
sizes = [40, 35, 25]

plt.pie(sizes, labels=labels, autopct='%1.1f%%')

plt.title("Language Usage")
plt.show()
```

---

# 9. Scatter Plot

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [5, 7, 8, 5, 6]

plt.scatter(x, y)

plt.title("Scatter Plot")
plt.xlabel("X")
plt.ylabel("Y")

plt.show()
```

---

# 10. Histogram

```python
import matplotlib.pyplot as plt

data = [1, 2, 2, 3, 3, 3, 4, 5]

plt.hist(data, bins=5)

plt.title("Histogram")
plt.show()
```

---

# 11. Multiple Lines in One Graph

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]

y1 = [10, 20, 30, 40]
y2 = [40, 30, 20, 10]

plt.plot(x, y1, label="Line 1")
plt.plot(x, y2, label="Line 2")

plt.legend()
plt.show()
```

---

# 12. Grid and Figure Size

```python
plt.figure(figsize=(8,5))
plt.plot(x, y)

plt.grid(True)
plt.show()
```

---

# 13. Saving the Graph

```python
plt.plot(x, y)
plt.savefig("graph.png")
```

---

# 14. Real Example (Student Marks)

```python
import matplotlib.pyplot as plt

students = ["A", "B", "C", "D"]
marks = [75, 85, 60, 90]

plt.bar(students, marks)

plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()
```

---

# 15. Common Mistakes Beginners Make

1. Forgetting `plt.show()`
2. Mixing x and y sizes
3. Not importing pyplot
4. Wrong data types

---

# 16. Practice Ideas

* Plot your daily expenses
* Create a marks dashboard
* Visualize temperature data
* Compare two products

---

# 17. Summary

Matplotlib basics include:

* `plot()` → line graph
* `bar()` → bar chart
* `pie()` → pie chart
* `scatter()` → scatter plot
* `hist()` → histogram

---


