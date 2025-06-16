# numPy in Python 

### https://codeswithpankaj.medium.com/mastering-numpy-a-comprehensive-guide-codes-with-pankaj-178e191a9143

### https://sites.google.com/view/learning-path-numpy/home



NumPy (Numerical Python) is a powerful library for numerical computations in Python. It provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays efficiently. This tutorial is designed for beginners, covering the basics of NumPy step-by-step with clear explanations and practical examples.

Table of Contents
	1	Introduction to NumPy
	2	Installing NumPy
	3	Importing NumPy
	4	Creating NumPy Arrays
	◦	From Lists
	◦	Built-in Functions
	◦	Array Attributes
	5	Array Indexing and Slicing
	6	Array Operations
	◦	Arithmetic Operations
	◦	Broadcasting
	◦	Universal Functions (ufuncs)
	7	Reshaping and Manipulating Arrays
	◦	Reshape
	◦	Flatten
	◦	Transpose
	◦	Concatenate and Split
	8	Aggregations and Statistics
	9	Random Numbers in NumPy
	10	Saving and Loading Arrays
	11	Practical Example: Analyzing Student Scores
	12	Common Pitfalls and Tips
	13	Conclusion

1. Introduction to NumPy
NumPy is the foundation for scientific computing in Python. It’s faster than Python lists for numerical operations because it uses optimized C code under the hood. Key features include:
	•	N-dimensional arrays: Efficient storage and manipulation of data.
	•	Mathematical functions: Trigonometric, statistical, and linear algebra operations.
	•	Broadcasting: Perform operations on arrays of different shapes.
	•	Integration: Works seamlessly with libraries like Pandas, Matplotlib, and SciPy.
Why use NumPy?
	•	Speed: NumPy arrays are faster than Python lists for numerical tasks.
	•	Memory efficiency: Arrays use less memory than lists.
	•	Convenience: Built-in functions simplify complex operations.
Example: Adding two lists vs. NumPy arrays.
# Python lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = [list1[i] + list2[i] for i in range(len(list1))]
print(result)  # Output: [5, 7, 9]

# NumPy arrays
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
result = arr1 + arr2
print(result)  # Output: [5 7 9]
NumPy is more concise and efficient!

2. Installing NumPy
To use NumPy, you need to install it. Most Python environments (e.g., Jupyter, VS Code) support this via pip.
Steps:
	1	Open your terminal or command prompt.
	2	Run the following command: pip install numpy
	3	
	4	Verify installation: import numpy as np
	5	print(np.__version__)  # Prints NumPy version, e.g., 2.1.1
	6	
If you’re using Anaconda, NumPy is pre-installed. If not, you can install it via:
conda install numpy

3. Importing NumPy
To use NumPy, import it into your Python script. The convention is to use the alias np for brevity.
import numpy as np
Now you can access all NumPy functions using np.function_name().

4. Creating NumPy Arrays
NumPy’s core object is the ndarray (n-dimensional array). Arrays can be created in several ways.
4.1 From Python Lists
Convert a Python list to a NumPy array using np.array().
# 1D array
arr_1d = np.array([1, 2, 3, 4])
print(arr_1d)  # Output: [1 2 3 4]

# 2D array (matrix)
arr_2d = np.array([[1, 2], [3, 4], [5, 6]])
print(arr_2d)
# Output:
# [[1 2]
#  [3 4]
#  [5 6]]
4.2 Built-in Functions
NumPy provides functions to create arrays with specific values or shapes.
	•	Zeros: Creates an array filled with zeros. zeros_arr = np.zeros((2, 3))  # 2x3 array
	•	print(zeros_arr)
	•	# Output:
	•	# [[0. 0. 0.]
	•	#  [0. 0. 0.]]
	•	
	•	Ones: Creates an array filled with ones. ones_arr = np.ones((3, 2))  # 3x2 array
	•	print(ones_arr)
	•	# Output:
	•	# [[1. 1.]
	•	#  [1. 1.]
	•	#  [1. 1.]]
	•	
	•	Full: Creates an array filled with a specified value. full_arr = np.full((2, 2), 7)  # 2x2 array filled with 7
	•	print(full_arr)
	•	# Output:
	•	# [[7 7]
	•	#  [7 7]]
	•	
	•	Arange: Creates a 1D array with evenly spaced values. range_arr = np.arange(0, 10, 2)  # Start=0, stop=10, step=2
	•	print(range_arr)  # Output: [0 2 4 6 8]
	•	
	•	Linspace: Creates an array with evenly spaced numbers over an interval. linspace_arr = np.linspace(0, 1, 5)  # 5 numbers from 0 to 1
	•	print(linspace_arr)  # Output: [0.   0.25 0.5  0.75 1.  ]
	•	
4.3 Array Attributes
Arrays have properties that describe their structure:
	•	Shape: Dimensions of the array.
	•	Size: Total number of elements.
	•	Dtype: Data type of elements.
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Shape:", arr.shape)  # Output: (2, 3)
print("Size:", arr.size)  # Output: 6
print("Data type:", arr.dtype)  # Output: int64

5. Array Indexing and Slicing
Access elements or subsets of arrays using indices and slices, similar to Python lists.
5.1 Indexing
	•	1D array: arr = np.array([10, 20, 30, 40])
	•	print(arr[0])  # Output: 10
	•	print(arr[-1])  # Output: 40
	•	
	•	2D array: arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
	•	print(arr_2d[0, 1])  # Output: 2 (row 0, column 1)
	•	
5.2 Slicing
Extract a portion of the array using start:stop:step.
# 1D slicing
arr = np.array([10, 20, 30, 40, 50])
print(arr[1:4])  # Output: [20 30 40]

# 2D slicing
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr_2d[0:2, 1:3])  # Rows 0-1, columns 1-2
# Output:
# [[2 3]
#  [5 6]]
5.3 Boolean Indexing
Filter elements based on conditions.
arr = np.array([10, 20, 30, 40, 50])
print(arr[arr > 25])  # Output: [30 40 50]

6. Array Operations
NumPy supports element-wise operations and advanced mathematical functions.
6.1 Arithmetic Operations
Perform operations like addition, subtraction, multiplication, etc., element-wise.
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

print(arr1 + arr2)  # Output: [5 7 9]
print(arr1 * arr2)  # Output: [ 4 10 18]
print(arr1 ** 2)    # Output: [1 4 9]
6.2 Broadcasting
NumPy automatically expands smaller arrays to match the shape of larger ones during operations.
arr = np.array([[1, 2, 3], [4, 5, 6]])
scalar = 2
print(arr + scalar)  # Adds 2 to each element
# Output:
# [[3 4 5]
#  [6 7 8]]

# Broadcasting with another array
arr2 = np.array([10, 20, 30])
print(arr + arr2)  # Adds arr2 to each row of arr
# Output:
# [[11 22 33]
#  [14 25 36]]
6.3 Universal Functions (ufuncs)
NumPy provides functions like sin, cos, exp, etc., that operate element-wise.
arr = np.array([0, np.pi/2, np.pi])
print(np.sin(arr))  # Output: [0.000000e+00 1.000000e+00 1.224647e-16]
print(np.exp(arr))  # Output: [ 1.          4.81047738 23.14069263]

7. Reshaping and Manipulating Arrays
Modify the structure or content of arrays without changing their data.
7.1 Reshape
Change the shape of an array.
arr = np.array([1, 2, 3, 4, 5, 6])
print(arr.reshape(2, 3))  # Reshape to 2x3
# Output:
# [[1 2 3]
#  [4 5 6]]

# Reshape to 3x2
print(arr.reshape(3, 2)))
# Output:
# [[1 2]
#  [3  [4]
#  [5 6]]
7.2 Flatten
Convert a multi-dimensional array to 1D.
arr = np.array([[1, 2], [3, 4]])
print(arr.flatten())  # Output: [1 2 3 4]
7.3 Transpose
Swap axes of an array (rows become columns).
arr = np.array([[1, 2,], [3, 4,], [5, 6(arr))))
print(arr.T)  # Output:
# [[1 4]:
#  [2 5]
#  [3 6]]
7.4 Concatenate and Split
	•	Concatenate: Combine arrays. arr1 = np.array([1, 2])
	•	arr2 = np.array([3, 4])
	•	print(np.concatenate((arr1, arr2)))  # Output: [1 2 3 4]
	•	
	•	# Concatenate 2D arrays along axis=0 (rows)
	•	arr1_2d = np.array([[1, 2], [3, 4]])
	•	arr2_2d = np.array([[5, 6], [7, 8]])
	•	print(np.concatenate((arr1_2d, arr2_2d)))
	•	# Output:
	•	# [[1 2]
	•	#  [3 4]
	•	#  [5 6]
	•	#  [7 8]]
	•	
	•	Split: Divide an array into subarrays-subarrays. arr = np.array([1, 2, 3, 4, 5, 6])
	•	print(np.split(arr, 3))  # Split into 3 parts
	•	# Output: [array([1, 2]), array([3, 4]), array([5, 6])]
	•	

8. Aggregations and Statistics
Compute summary statistics like mean, max, sum, etc.
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(np.sum(arr))  # Sum of all elements: 21
print(np.mean(arr)))  # Mean: 3.3.5
print(np.max(arr))  # Max: 6
print(np.min(arr))  # Min: 1
print(np.std(arr))  # Standard deviation: ~1.7078

# Axis-wise operations
print(np.sum(arr, axis=0))  # Sum along columns: [5 7 9]
print(np.sum(arr, axis=1))  # Sum along rows: [  : [6 15]

9. Random Numbers in NumPy
NumPy’s random module generates random numbers for simulations or testing.
# Random numbers between 0 and 1
print(np.random.rand(3))  # 1D array: e.g., [0.123 0.456 0.789]

# Random integers
print(np.random.randint(1, 10, size=(2, 3)))  # 2x3 array of integers 1-9
# Example output:
# [[3 7 2]
#  [8 1 5]]

# Set seed for reproducibility
np.random.seed(42)
print(np.random.rand(3))  # Always: [0.374 0.950 71 0.731]

10. Saving and Loading Arrays
Save arrays to files and load them later.
# Save array to .npy file
arr = np.array([1, 2, 3])
np.save("array.npy", arr)

# Load array
loaded_arr = np.load("array.npy")
print(loaded_arr)  # Output: [1 2 3]

# Save as text file
np.savetxt("array.txt", arr)
# Load from text file
loaded_txt = np.loadtxt("array.txt")
print(loaded_txt)  # Output: [1. 2. 3.]

11. Practical Example: Analyzing Student Scores
Let’s use NumPy to analyze student exam scores for various subjects.
Problem: We have scores for 4 students in 3 subjects (Math, Science, English):
	•	Calculate average score per student.
	•	Find students who scored above-average in Math.
	•	Compute the average score per subject.
# Create 2D array of scores (rows: students, columns: Math, Science, Math)
scores = np.array([[85, 90, 78], [92, 88, 95], [76, 85, 80], [88, 92, 90]])

# Average score per student (row-wise mean)
avg_student_scores = np.mean(scores, axis=1)
print("Average score per student:", avg_student_scores)
# Output: [84.33 91.66 3 80.3 3 90.]

# Students above average in Math (column 0)
math_scores = scores[0]
math_avg = np.mean(math_scores[0])
above_avg_math = scores[math_scores > np.math_avg[0]]
print("Students with above-average Math scores:\n", above_avg_math)
# Output:
# [[92 88 95]
#  [88 92 90]]

# Average score per subject (column-wise mean)
avg_subject_scores = np.mean(scores, axis=1)
print("Average score per subject (Math, English):", avg_subject_scores)
# Output: [85.25 88.75  English)]

12. Common Pitfalls and Tips
	•	Pitfall: Modifying a slice directly affects the original array (views vs. copies). arr = np.array([1, 2, 3])
	•	slice_arr = arr[0:3]
	•	slice_arr[0] = 99
	•	print(arr)  # Output: [99 2 3] (original array changed!)
	•	
	•	# Use .copy() to avoid this
	•	slice_copy = arr.copy()[0:3]
	•	slice_copy[0] = 100
	•	print(arr)  # Output: [99 2 3]) (unchanged)
	•	
	•	Tip: Check array shapes before operations to avoid broadcasting errors.
	•	Tip: Use np.isnan() or np.isinf() to handle missing or infinite values.
	•	Tip: Explore NumPy’s documentation (numpy.org) for advanced functions.

13. Conclusion
NumPy is an essential library for numerical computing in Python. You’ve learned how to:
	•	Create and manipulate arrays.
	•	Perform arithmetic and statistical operations.
	•	Use indexing, slicing, and reshaping.
	•	Generate random numbers and save/load arrays.
	•	Apply NumPy to real-world problems.
Next Steps:
	•	Experiment with larger datasets (e.g., CSV files with np.genfromtxt).
	•	Combine NumPy with Matplotlib for data visualization or Pandas for data analysis.
	•	Try NumPy challenges on platforms like HackerRank or LeetCode.

