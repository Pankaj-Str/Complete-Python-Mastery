# Understanding Covariance and Correlation in NumPy

## Introduction

In Data Science, Machine Learning, and Statistics, we often need to understand how two variables are related to each other.

For example:

* Does study time affect exam marks?
* Does temperature affect ice cream sales?
* Does age affect salary?

To answer such questions, we use **Measures of Association** such as:

1. Covariance
2. Correlation

In this tutorial, you will learn:

* What a statistical variable is
* Independent and dependent variables
* Measures of association
* Positive, negative, and zero relationships
* Covariance using NumPy
* Correlation using NumPy
* Interpretation of results

---

# What is a Statistical Variable?

A **statistical variable** is any characteristic or property that can take different values.

### Examples

| Variable    | Possible Values     |
| ----------- | ------------------- |
| Age         | 18, 25, 40          |
| Height      | 150cm, 170cm, 180cm |
| Salary      | ₹20,000, ₹50,000    |
| Temperature | 20°C, 35°C          |

### Python Example

```python
age = [18, 20, 22, 25, 30]
```

Here, **Age** is a statistical variable because it can have different values.

---

# Independent and Dependent Variables

Before studying relationships, we must understand these two terms.

## Independent Variable (X)

The variable that influences another variable.

It is also called:

* Predictor
* Input Variable
* Feature

### Example

Hours Studied

```python
hours = [1, 2, 3, 4, 5]
```

---

## Dependent Variable (Y)

The variable whose value depends on another variable.

It is also called:

* Response Variable
* Output Variable
* Target Variable

### Example

Exam Marks

```python
marks = [40, 50, 60, 70, 80]
```

Marks depend on hours studied.

Therefore:

* Hours Studied → Independent Variable
* Marks → Dependent Variable

---

# What are Measures of Association?

Measures of association help us understand:

### Questions They Answer

* Are two variables related?
* How strong is the relationship?
* Is the relationship positive or negative?

Common measures:

1. Covariance
2. Correlation

---

# Types of Relationships Between Variables

There are three main types of relationships.

---

# 1. Positive Relationship

When one variable increases, the other also increases.

### Example

| Hours Studied | Marks |
| ------------- | ----- |
| 1             | 40    |
| 2             | 50    |
| 3             | 60    |
| 4             | 70    |
| 5             | 80    |

As study hours increase, marks increase.

This is a positive relationship.

### Visualization

```text
Hours ↑  → Marks ↑
```

---

# 2. Negative Relationship

When one variable increases, the other decreases.

### Example

| Speed | Travel Time |
| ----- | ----------- |
| 20    | 10          |
| 40    | 8           |
| 60    | 6           |
| 80    | 4           |

As speed increases, travel time decreases.

### Visualization

```text
Speed ↑ → Time ↓
```

This is a negative relationship.

---

# 3. Zero Relationship

When changing one variable does not affect another.

### Example

| Shoe Size | Exam Marks |
| --------- | ---------- |
| 6         | 80         |
| 7         | 55         |
| 8         | 90         |
| 9         | 60         |

No meaningful relationship exists.

### Visualization

```text
X changes
Y changes randomly
```

This is a zero relationship.

---

# What is Covariance?

Covariance measures the direction of the relationship between two variables.

It tells us whether variables move together.

### Formula

Cov(X,Y)=\frac{\sum (X_i-\bar{X})(Y_i-\bar{Y})}{n-1}

Where:

* X = First Variable
* Y = Second Variable
* X̄ = Mean of X
* Ȳ = Mean of Y

---

# Interpreting Covariance

| Covariance Value | Meaning               |
| ---------------- | --------------------- |
| Positive         | Positive Relationship |
| Negative         | Negative Relationship |
| Zero             | No Relationship       |

Important:

Covariance only shows direction.

It does not tell us the strength clearly.

---

# Calculating Covariance Using NumPy

## Example 1: Positive Relationship

### Step 1: Import NumPy

```python
import numpy as np
```

---

### Step 2: Create Data

```python
hours = np.array([1, 2, 3, 4, 5])
marks = np.array([40, 50, 60, 70, 80])
```

---

### Step 3: Compute Covariance

```python
cov_matrix = np.cov(hours, marks)

print(cov_matrix)
```

### Output

```python
[[  2.5  25. ]
 [ 25.  250. ]]
```

---

### Explanation

The covariance value is:

```python
25
```

Positive value means:

```text
Hours ↑ → Marks ↑
```

Positive relationship exists.

---

# Example 2: Negative Relationship

```python
speed = np.array([20, 40, 60, 80])
time = np.array([10, 8, 6, 4])

cov_matrix = np.cov(speed, time)

print(cov_matrix)
```

### Output

```python
Negative covariance
```

Meaning:

```text
Speed ↑ → Time ↓
```

Negative relationship exists.

---

# Example 3: No Relationship

```python
x = np.array([1, 2, 3, 4, 5])
y = np.array([7, 2, 9, 1, 5])

cov_matrix = np.cov(x, y)

print(cov_matrix)
```

Covariance will be close to zero.

Meaning:

```text
No meaningful relationship
```

---

# What is Correlation?

Correlation measures:

1. Direction of relationship
2. Strength of relationship

Unlike covariance, correlation is standardized.

### Formula

r=\frac{Cov(X,Y)}{\sigma_X\sigma_Y}

Where:

* Cov(X,Y) = Covariance
* σX = Standard Deviation of X
* σY = Standard Deviation of Y

---

# Correlation Range

Correlation always lies between:

-1 \le r \le 1

---

# Correlation Interpretation

| Correlation Value | Meaning           |
| ----------------- | ----------------- |
| +1                | Perfect Positive  |
| +0.8              | Strong Positive   |
| +0.5              | Moderate Positive |
| 0                 | No Relationship   |
| -0.5              | Moderate Negative |
| -0.8              | Strong Negative   |
| -1                | Perfect Negative  |

---

# Calculating Correlation Using NumPy

NumPy provides:

```python
np.corrcoef()
```

---

# Example 1: Positive Correlation

```python
import numpy as np

hours = np.array([1, 2, 3, 4, 5])
marks = np.array([40, 50, 60, 70, 80])

corr_matrix = np.corrcoef(hours, marks)

print(corr_matrix)
```

### Output

```python
[[1. 1.]
 [1. 1.]]
```

Correlation:

```python
1.0
```

Meaning:

Perfect positive relationship.

---

# Example 2: Negative Correlation

```python
speed = np.array([20, 40, 60, 80])
time = np.array([10, 8, 6, 4])

corr_matrix = np.corrcoef(speed, time)

print(corr_matrix)
```

### Output

```python
[[ 1. -1.]
 [-1.  1.]]
```

Meaning:

Perfect negative relationship.

---

# Example 3: Weak Relationship

```python
x = np.array([1, 2, 3, 4, 5])
y = np.array([7, 2, 9, 1, 5])

corr_matrix = np.corrcoef(x, y)

print(corr_matrix)
```

### Output

```python
Correlation near 0
```

Meaning:

Very weak or no relationship.

---

# Complete Example Program

```python
import numpy as np

hours = np.array([1, 2, 3, 4, 5])
marks = np.array([40, 50, 60, 70, 80])

covariance = np.cov(hours, marks)[0, 1]

correlation = np.corrcoef(hours, marks)[0, 1]

print("Covariance:", covariance)
print("Correlation:", correlation)
```

### Output

```python
Covariance: 25.0
Correlation: 1.0
```

---

# Covariance vs Correlation

| Feature           | Covariance | Correlation |
| ----------------- | ---------- | ----------- |
| Shows Direction   | Yes        | Yes         |
| Shows Strength    | No         | Yes         |
| Range Fixed       | No         | Yes         |
| Range             | Any Value  | -1 to +1    |
| Easy to Interpret | No         | Yes         |
| Most Used in ML   | Less       | More        |

---

# Real-World Applications

### Finance

Relationship between:

* Stock A price
* Stock B price

### Education

Relationship between:

* Study Hours
* Exam Scores

### Marketing

Relationship between:

* Advertisement Spending
* Sales Revenue

### Healthcare

Relationship between:

* Exercise Hours
* Weight Loss

---

# Summary

In this tutorial, you learned:

* A statistical variable is a characteristic that can take different values.
* Independent variables influence dependent variables.
* Measures of association help identify relationships between variables.
* Positive relationship: both variables move in the same direction.
* Negative relationship: variables move in opposite directions.
* Zero relationship: no meaningful association exists.
* Covariance shows the direction of a relationship.
* Correlation shows both direction and strength.
* NumPy provides:

  * `np.cov()` for covariance
  * `np.corrcoef()` for correlation
* Correlation values range from -1 to +1 and are easier to interpret than covariance.

This knowledge forms an important foundation for Machine Learning, Data Analysis, Feature Selection, and Statistical Modeling.
