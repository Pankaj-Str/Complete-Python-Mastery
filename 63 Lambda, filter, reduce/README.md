# **Lambda, filter, reduce**
---

### **1. Lambda Functions**
- **What**: A `lambda` function is a small, anonymous function defined in a single line using the `lambda` keyword. It’s used for short, simple operations without needing a named function.
- **Syntax**: `lambda arguments: expression`
- **Key Points**:
  - No need for `def` statement.
  - Can take multiple arguments but only one expression.
  - Often used with `map`, `filter`, and `reduce`.

**Example**:
```python
# Lambda to square a number
square = lambda x: x ** 2
print(square(4))  # Output: 16

# Lambda with multiple arguments
add = lambda x, b: a + b
print(add(2, 4))  # Output: 6
```

**Use Case**: Temporary functions, sorting, or inline operations.
```python
# Sorting a list of tuples by second element
pairs = [(1, 'one'), (3, 'three'), (2, 'two')]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)  # Output: [(1, 'one'), (3, 'three'), (2, 'two')]
```

---

### **2. Filter**
- **What**: `filter()` applies a function to each item in an iterable and returns an iterator with only the items for which the function returns `True`.
- **Syntax**: `filter(function, iterable)`
- **Key Points**:
  - The function must return a boolean (`True` or `False`).
  - Returns a filter object (convert to `list` or other iterable if needed).
  - Often paired with `lambda` for concise code.

**Example**:
```python
# Filter even numbers
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Output: [2, 4, 6]

# Filter strings longer than 3 characters
words = ['cat', 'dog', 'elephant', 'rat']
long_words = list(filter(lambda x: len(x) > 3, words))
print(long_words)  # Output: ['elephant']
```

**Use Case**: Selecting elements based on a condition.

---

### **3. Map**
- **What**: `map()` applies a function to each item in an iterable and returns an iterator with the transformed results.
- **Syntax**: `map(function, iterable, ...)`
- **Key Points**:
  - Can process multiple iterables in parallel (function must accept multiple arguments).
  - Returns a map object (convert to `list` or other iterable if needed).
  - Useful for transforming data.

**Example**:
```python
# Square all numbers
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)  # Output: [1, 4, 9, 16]

# Combine two lists element-wise
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
sums = list(map(lambda x, y: x + y, nums1, nums2))
print(sums)  # Output: [5, 7, 9]
```

**Use Case**: Applying a transformation to all elements.

---

### **4. Reduce**
- **What**: `reduce()` applies a function cumulatively to the items of an iterable, reducing it to a single value.
- **Syntax**: `reduce(function, iterable[, initializer])`
- **Key Points**:
  - Requires `from functools import reduce`.
  - The function must take two arguments and return one value.
  - Optional `initializer` provides a starting value.
  - Processes elements pairwise, accumulating the result.

**Example**:
```python
from functools import reduce

# Sum all numbers
numbers = [1, 2, 3, 4]
total = reduce(lambda x, y: x + y, numbers)
print(total)  # Output: 10

# Find maximum value
max_val = reduce(lambda x, y: x if x > y else y, numbers)
print(max_val)  # Output: 4

# With initializer (start with 10)
total_with_init = reduce(lambda x, y: x + y, numbers, 10)
print(total_with_init)  # Output: 20 (10 + 1 + 2 + 3 + 4)
```

**How it works** (for `reduce(lambda x, y: x + y, [1, 2, 3, 4])`):
- Step 1: `x = 1, y = 2` → `1 + 2 = 3`
- Step 2: `x = 3, y = 3` → `3 + 3 = 6`
- Step 3: `x = 6, y = 4` → `6 + 4 = 10`
- Result: `10`

**Use Case**: Aggregating data (e.g., sum, product, max/min).

---

### **Combined Example**
Let’s use `lambda`, `filter`, `map`, and `reduce` together to process a list of numbers:
- Filter even numbers.
- Square them.
- Sum the results.

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]
result = reduce(lambda x, y: x + y, map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
print(result)  # Output: 56 (2² + 4² + 6² = 4 + 16 + 36 = 56)
```

**Step-by-step**:
1. `filter(lambda x: x % 2 == 0, numbers)` → `[2, 4, 6]`
2. `map(lambda x: x ** 2, [2, 4, 6])` → `[4, 16, 36]`
3. `reduce(lambda x, y: x + y, [4, 16, 36])` → `56`

---

### **Key Tips**
- **Readability**: Use `lambda` sparingly; named functions are often clearer for complex logic.
- **Performance**: List comprehensions (e.g., `[x**2 for x in numbers]`) are sometimes faster than `map` or `filter`.
- **Edge Cases**:
  - Empty iterables with `reduce` raise `TypeError` unless an initializer is provided.
  - Ensure the function passed to `map` or `filter` matches the iterable’s data type.
- **Alternatives**:
  - `filter` → List comprehensions: `[x for x in lst if condition]`
  - `map` → List comprehensions: `[f(x) for x in lst]`
  - `reduce` → Built-in functions like `sum()`, `max()`, or loops for clarity.

---

### **Practice Problems**
1. Use `map` to convert a list of strings to uppercase.
2. Use `filter` to get all numbers divisible by 3 from a list.
3. Use `reduce` to compute the product of a list of numbers.
4. Combine all three to filter positive numbers, double them, and find their sum.

**Sample Solution** (Problem 1):
```python
words = ['hello', 'world']
upper = list(map(lambda x: x.upper(), words))
print(upper)  # Output: ['HELLO', 'WORLD']
```

---

### **Summary**
- **`lambda`**: Creates anonymous functions for quick, simple operations.
- **`filter`**: Selects elements based on a condition.
- **`map`**: Transforms elements by applying a function.
- **`reduce`**: Aggregates elements into a single value.
- Combine them for powerful, concise data processing, but balance with readability and performance.

