# numPy in Python 

### https://codeswithpankaj.medium.com/mastering-numpy-a-comprehensive-guide-codes-with-pankaj-178e191a9143

### https://sites.google.com/view/learning-path-numpy/home


# Codes with Pankaj: In-Depth NumPy Tutorial for Beginners

## What is NumPy?
NumPy (Numerical Python) is a powerful Python library used for numerical computing. It provides support for large, multi-dimensional arrays and matrices, along with a vast collection of mathematical functions to operate on these arrays efficiently. 

## Why Use NumPy?
- **Performance:** NumPy is significantly faster than Python lists because it is implemented in C and optimized for speed.
- **Memory Efficient:** NumPy arrays consume less memory than standard Python lists.
- **Mathematical Operations:** Provides built-in functions for arithmetic, linear algebra, and statistical calculations.
- **Multi-Dimensional Support:** Easily handles multi-dimensional arrays and matrices.
- **Ease of Use:** Operations can be performed efficiently using broadcasting and vectorization.

---

## Installing and Importing NumPy
Before using NumPy, you need to install it. If you haven’t installed it yet, use:
```bash
pip install numpy
```

Now, import NumPy in your Python script:
```python
import numpy as np
```

## Creating NumPy Arrays
A NumPy array is a data structure that stores elements of the same data type. You can create arrays in several ways:

### Creating a 1D Array
```python
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)
```
### Creating a 2D Array
```python
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)
```
### Creating an Array of Zeros or Ones
```python
zeros_arr = np.zeros((3, 3))  # 3x3 array of zeros
ones_arr = np.ones((2, 4))    # 2x4 array of ones
print(zeros_arr)
print(ones_arr)
```
### Creating an Array with a Range of Numbers
```python
range_arr = np.arange(1, 10, 2)  # Start from 1, go up to 10 with a step of 2
print(range_arr)
```
### Creating a Random Array
```python
random_arr = np.random.rand(3, 3)  # 3x3 matrix with random values
print(random_arr)
```

## Array Attributes
Once an array is created, we can check its properties:
```python
print(arr2.shape)  # Returns the shape (rows, columns)
print(arr2.size)   # Total number of elements
print(arr2.dtype)  # Data type of array elements
```

## Array Indexing and Slicing
Just like lists, you can access elements in NumPy arrays using indexing:
```python
print(arr1[0])      # First element
print(arr2[1, 2])   # Element at row index 1, column index 2
```
You can also extract portions of the array using slicing:
```python
print(arr1[1:4])    # Extract elements from index 1 to 3
print(arr2[:, 1])   # Extract all rows but only column 1
```

## Array Operations
### Arithmetic Operations
NumPy allows element-wise arithmetic operations:
```python
arr = np.array([1, 2, 3, 4])
print(arr + 2)  # Add 2 to each element
print(arr * 3)  # Multiply each element by 3
print(arr ** 2) # Square each element
```

### Aggregation Functions
NumPy provides built-in functions for aggregation:
```python
print(arr.sum())  # Sum of all elements
print(arr.mean())  # Mean (average) of elements
print(arr.max())  # Maximum value in the array
print(arr.min())  # Minimum value in the array
```

### Broadcasting (Different Sized Arrays)
NumPy can perform operations between arrays of different sizes:
```python
arr3 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr3 + np.array([1, 2, 3]))  # Adds [1,2,3] to each row
```

## Mathematical Functions
NumPy provides mathematical functions for array computations:
```python
print(np.sin(arr))  # Sine function
print(np.log(arr))  # Natural logarithm
print(np.exp(arr))  # Exponential function
```

## Statistical Functions
You can compute statistical values using NumPy:
```python
print(np.median(arr))  # Median value
print(np.std(arr))  # Standard deviation
print(np.var(arr))  # Variance
```

## Linear Algebra Functions
NumPy provides functions for matrix operations:
```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(np.dot(A, B))  # Matrix multiplication
print(np.linalg.inv(A))  # Inverse of matrix A
```

## Multi-Dimensional Arrays
You can create and work with higher-dimensional arrays:
```python
arr4 = np.zeros((3, 3, 3))  # 3D array filled with zeros
print(arr4)
```

## Reshaping Arrays
Reshaping allows you to change the shape of an array without modifying its data:
```python
arr6 = np.array([1, 2, 3, 4, 5, 6])
reshaped_arr = arr6.reshape(2, 3)  # Convert to 2x3 matrix
print(reshaped_arr)
```

## Concatenation and Splitting
### Concatenation (Joining Arrays)
```python
arr7 = np.array([1, 2, 3])
arr8 = np.array([4, 5, 6])
concatenated_arr = np.concatenate((arr7, arr8))
print(concatenated_arr)
```

### Splitting Arrays
```python
split_arr = np.split(arr6, 2)  # Split into two equal parts
print(split_arr)
```

## Conclusion
This tutorial introduced NumPy from scratch, covering array creation, indexing, operations, and essential functions. Mastering NumPy is fundamental for data science, machine learning, and scientific computing. Keep practicing, and experiment with different operations to get comfortable with NumPy!

