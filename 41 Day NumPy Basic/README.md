# numPy in Python 

### https://codeswithpankaj.medium.com/mastering-numpy-a-comprehensive-guide-codes-with-pankaj-178e191a9143

### https://sites.google.com/view/learning-path-numpy/home



# NumPy Tutorial for Beginners

NumPy (Numerical Python) is a Python library that makes it easy to work with arrays and perform mathematical operations. It’s fast, efficient, and widely used in data science, machine learning, and scientific computing. This tutorial is designed for beginners, explaining each concept with simple examples.

## Prerequisites
- Basic understanding of Python (lists, loops, functions).
- Python and NumPy installed. To install NumPy, run:
  ```bash
  pip install numpy
  ```

## Step 1: Importing NumPy
To use NumPy, you need to import it. The common convention is to import it as `np` for brevity.

**Example**:
```python
import numpy as np
```

**Explanation**: 
- The `import numpy as np` statement loads the NumPy library and gives it the alias `np`, so you can write `np` instead of `numpy` in your code.

## Step 2: Creating NumPy Arrays
NumPy’s core feature is the `ndarray` (n-dimensional array), which is like a Python list but optimized for numerical operations.

### 2.1 Creating an Array from a List
You can convert a Python list to a NumPy array using `np.array()`.

**Example**:
```python
# Create a 1D array
my_list = [1, 2, 3, 4, 5]
array_1d = np.array(my_list)
print("1D Array:", array_1d)
```

**Output**:
```
1D Array: [1 2 3 4 5]
```

**Explanation**:
- `np.array(my_list)` converts the list `[1, 2, 3, 4, 5]` into a NumPy array.
- The output looks similar to a list but is a NumPy array, which supports advanced operations.

### 2.2 Creating a 2D Array (Matrix)
A 2D array is like a table with rows and columns.

**Example**:
```python
# Create a 2D array
my_2d_list = [[1, 2, 3], [4, 5, 6]]
array_2d = np.array(my_2d_list)
print("2D Array:\n", array_2d)
```

**Output**:
```
2D Array:
 [[1 2 3]
  [4 5 6]]
```

**Explanation**:
- The 2D array is created from a nested list (a list of lists).
- The `\n` in the print statement adds a newline for better formatting.

### 2.3 Creating Arrays with NumPy Functions
NumPy provides functions to create arrays without manually specifying values.

**Example**:
```python
# Array of zeros
zeros = np.zeros((2, 3))  # 2 rows, 3 columns
print("Zeros Array:\n", zeros)

# Array of ones
ones = np.ones((3, 2))  # 3 rows, 2 columns
print("Ones Array:\n", ones)

# Array with a range of numbers
range_array = np.arange(0, 10, 2)  # Start at 0, end before 10, step by 2
print("Range Array:", range_array)

# Array with evenly spaced numbers
linspace_array = np.linspace(0, 1, 5)  # 5 numbers from 0 to 1
print("Linspace Array:", linspace_array)
```

**Output**:
```
Zeros Array:
 [[0. 0. 0.]
  [0. 0. 0.]]
Ones Array:
 [[1. 1.]
  [1. 1.]
  [1. 1.]]
Range Array: [0 2 4 6 8]
Linspace Array: [0.   0.25 0.5  0.75 1.  ]
```

**Explanation**:
- `np.zeros((rows, cols))`: Creates an array filled with zeros.
- `np.ones((rows, cols))`: Creates an array filled with ones.
- `np.arange(start, stop, step)`: Creates a 1D array with numbers from `start` to `stop-1`, incrementing by `step`.
- `np.linspace(start, stop, num)`: Creates an array with `num` evenly spaced numbers from `start` to `stop`.

## Step 3: Array Attributes
NumPy arrays have attributes that provide information about their structure.

**Example**:
```python
array = np.array([[1, 2, 3], [4, 5, 6]])
print("Array:\n", array)
print("Shape:", array.shape)  # Number of rows and columns
print("Size:", array.size)    # Total number of elements
print("Data type:", array.dtype)  # Type of elements
print("Dimension:", array.ndim)   # Number of dimensions
```

**Output**:
```
Array:
 [[1 2 3]
  [4 5 6]]
Shape: (2, 3)
Size: 6
Data type: int64
Dimension: 2
```

**Explanation**:
- `shape`: Returns a tuple `(rows, columns)` for a 2D array.
- `size`: Total number of elements (rows × columns).
- `dtype`: Data type of elements (e.g., `int64` for integers, `float64` for floats).
- `ndim`: Number of dimensions (1 for 1D, 2 for 2D, etc.).

## Step 4: Array Indexing and Slicing
You can access and modify array elements using indexing and slicing, similar to Python lists.

### 4.1 Indexing
**Example**:
```python
array = np.array([10, 20, 30, 40])
print("First element:", array[0])  # Access first element
print("Last element:", array[-1])  # Access last element

# 2D array indexing
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("Element at row 1, column 2:", array_2d[1, 2])  # 6
```

**Output**:
```
First element: 10
Last element: 40
Element at row 1, column 2: 6
```

**Explanation**:
- For 1D arrays, use `array[index]`.
- For 2D arrays, use `array[row, column]`.

### 4.2 Slicing
**Example**:
```python
array = np.array([10, 20, 30, 40, 50])
print("Slice [1:4]:", array[1:4])  # Elements from index 1 to 3

# 2D array slicing
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("First two rows, first two columns:\n", array_2d[0:2, 0:2])
```

**Output**:
```
Slice [1:4]: [20 30 40]
First two rows, first two columns:
 [[1 2]
  [4 5]]
```

**Explanation**:
- Slicing syntax is `[start:end:step]`. The `end` index is excluded.
- For 2D arrays, slice rows and columns separately: `array[row_start:row_end, col_start:col_end]`.

## Step 5: Array Operations
NumPy arrays support element-wise operations, making calculations simple and fast.

### 5.1 Basic Arithmetic
**Example**:
```python
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

# Addition
print("Addition:", array1 + array2)

# Multiplication
print("Multiplication:", array1 * array2)

# Scalar operations
print("Multiply by 2:", array1 * 2)
```

**Output**:
```
Addition: [5 7 9]
Multiplication: [ 4 10 18]
Multiply by 2: [2 4 6]
```

**Explanation**:
- Operations like `+`, `-`, `*`, `/` are applied element-wise.
- Scalar operations (e.g., multiply by 2) apply to every element.

### 5.2 Mathematical Functions
NumPy provides functions like `sin`, `cos`, `sqrt`, etc.

**Example**:
```python
array = np.array([1, 4, 9])
print("Square root:", np.sqrt(array))
print("Sine:", np.sin(array))
```

**Output**:
```
Square root: [1. 2. 3.]
Sine: [0.84147098 -0.7568025   0.41211849]
```

**Explanation**:
 facie: `np.sqrt()` and `np.sin()` apply mathematical operations to each element.

## Step 6: Reshaping Arrays
You can change the shape of an array without changing its data using `reshape()`.

**Example**:
```python
array = np.array([1, 2, 3, 4, 5, 6])
reshaped = array.reshape(2, 3)  # Reshape to 2 rows, 3 columns
print("Reshaped Array:\n", reshaped)
```

**Output**:
```
Reshaped Array:
 [[1 2 3]
  [4 5 6]]
```

**Explanation**:
- `reshape(rows, cols)` changes the array’s shape, but the total number of elements must remain the same (e.g., 6 elements can become 2×3).
- The original array remains unchanged unless reassigned.

## Step 7: Array Aggregation
NumPy provides functions to compute statistics like sum, mean, max, etc.

**Example**:
```python
array = np.array([[1, 2, 3], [4, 5, 6]])
print("Sum:", np.sum(array))
print("Mean:", np.mean(array))
print("Max:", np.max(array))
```

**Output**:
```
Sum: 21
Mean: 3.5
Max: 6
```

**Explanation**:
- `np.sum()`: Adds all elements.
- `np.mean()`: Computes the average.
- `np.max()`: Finds the largest value.

## Step 8: Broadcasting
Broadcasting allows NumPy to perform operations on arrays of different shapes by automatically expanding smaller arrays.

**Example**:
```python
array = np.array([[1, 2, 3], [4, 5, 6]])
scalar = 2
result = array + scalar
print("Broadcasted Addition:\n", result)
```

**Output**:
```
Broadcasted Addition:
 [[3 4 5]
  [6 7 8]]
```

**Explanation**:
- The scalar `2` is “broadcasted” to match the array’s shape, adding 2 to each element.
- Broadcasting saves memory and simplifies code.

## Step 9: Random Number Generation
NumPy’s `random` module generates random numbers for simulations, testing, etc.

**Example**:
```python
# Random integers between 1 and 10
random_array = np.random.randint(1, 11, size=(2, 3))
print("Random Array:\n", random_array)

# Random floats between 0 and 1
random_floats = np.random.random((2, 2))
print("Random Floats:\n", random_floats)
```

**Output** (will vary):
```
Random Array:
 [[7 3 9]
  [2 6 4]]
Random Floats:
 [[0.12345678 0.98765432]
  [0.45678901 0.67890123]]
```

**Explanation**:
- `np.random.randint(low, high, size)`: Generates random integers.
- `np.random.random(size)`: Generates random floats between 0 and 1.
- The `size` parameter specifies the array shape.

## Step 10: Saving and Loading Arrays
You can save NumPy arrays to files and load them later.

**Example**:
```python
array = np.array([[1, 2, 3], [4, 5, 6]])
np.save('my_array.npy', array)  # Save array to file
loaded_array = np.load('my_array.npy')  # Load array from file
print("Loaded Array:\n", loaded_array)
```

**Output**:
```
Loaded Array:
 [[1 2 3]
  [4 5 6]]
```

**Explanation**:
- `np.save(file_name, array)`: Saves the array to a `.npy` file.
- `np.load(file_name)`: Loads the array from the file.
- Useful for storing large datasets.

## Conclusion
This tutorial covered the basics of NumPy: creating arrays, indexing, slicing, operations, reshaping, aggregation, broadcasting, random numbers, and file handling. Practice these examples and experiment with your own arrays to get comfortable with NumPy. It’s a powerful tool for numerical computing, and mastering it will open doors to data science and machine learning.



