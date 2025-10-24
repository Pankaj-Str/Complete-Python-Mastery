
# NumPy Methods and Functions 

## 1. Array Creation
Functions for creating NumPy arrays.

- `np.array(object, dtype=None, copy=True, order='K', ndmin=0)`: Create an array from any object exposing the array interface.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Creating a 2D array from a list of lists, specifying dtype as float
    # This is useful for converting Python data structures to efficient NumPy arrays for numerical computations.
    data = [[1, 2, 3], [4, 5, 6]]
    arr = np.array(data, dtype=float, ndmin=2)  # Ensures at least 2 dimensions
    print(arr)
    print("Shape:", arr.shape)
    print("Data type:", arr.dtype)

    # Variation: Creating from a tuple with copy=False (if possible, shares memory)
    tup = (7, 8, 9)
    arr2 = np.array(tup, copy=False)
    print(arr2)

    # Edge case: Empty list creates an empty array
    empty_arr = np.array([])
    print("Empty array:", empty_arr)
    ```
    **Explanation**: The function converts iterable objects into ndarrays. Here, we create a 2D array from lists, inspect its properties, and show variations like using tuples or empty inputs.  
    **Output**:
    ```
    [[1. 2. 3.]
     [4. 5. 6.]]
    Shape: (2, 3)
    Data type: float64
    [7 8 9]
    Empty array: []
    ```

- `np.arange(start, stop, step, dtype=None)`: Return evenly spaced values within a given interval.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Generating an array of even numbers from 0 to 10 (exclusive), useful for indexing or loops.
    arr = np.arange(0, 10, 2, dtype=int)
    print(arr)

    # Variation: Floating-point steps for non-integer sequences
    arr_float = np.arange(0.5, 5.5, 1.0)
    print(arr_float)

    # Edge case: Negative step for descending order
    arr_desc = np.arange(10, 0, -2)
    print(arr_desc)
    ```
    **Explanation**: Similar to Python's range but returns an ndarray. Useful for creating sequences in simulations or data generation. Shows integer, float, and descending examples.  
    **Output**:
    ```
    [0 2 4 6 8]
    [0.5 1.5 2.5 3.5 4.5 5.5]
    [10  8  6  4  2]
    ```

- `np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)`: Return evenly spaced numbers over a specified interval.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Creating 5 evenly spaced points from 0 to 10, including endpoint. Useful for plotting functions.
    arr, step = np.linspace(0, 10, 5, endpoint=True, retstep=True)
    print(arr)
    print("Step size:", step)

    # Variation: Excluding endpoint for open intervals
    arr_no_end = np.linspace(0, 10, 5, endpoint=False)
    print(arr_no_end)

    # Edge case: Single point (num=1)
    single = np.linspace(5, 5, 1)
    print(single)
    ```
    **Explanation**: Generates linearly spaced arrays, ideal for sampling in scientific computing. Demonstrates retstep, endpoint exclusion, and minimal cases.  
    **Output**:
    ```
    [ 0.   2.5  5.   7.5 10. ]
    Step size: 2.5
    [0. 2. 4. 6. 8.]
    [5.]
    ```

- `np.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None)`: Return numbers spaced evenly on a log scale.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Generating 4 log-spaced points from 10^1 to 10^3 (base 10). Useful for logarithmic scales in data analysis.
    arr = np.logspace(1, 3, 4, base=10)
    print(arr)

    # Variation: Base 2 for binary exponents
    arr_base2 = np.logspace(0, 3, 4, base=2)
    print(arr_base2)

    # Edge case: Excluding endpoint
    arr_no_end = np.logspace(0, 3, 4, endpoint=False)
    print(arr_no_end)
    ```
    **Explanation**: Creates logarithmically spaced arrays for applications like frequency analysis. Shows different bases and endpoint options.  
    **Output**:
    ```
    [  10.           46.41588834  215.443469    1000.        ]
    [1. 2. 4. 8.]
    [ 1.          2.15443469  4.64158883 10.        ]
    ```

- `np.zeros(shape, dtype=float, order='C')`: Return a new array of given shape filled with zeros.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Creating a 2x3 zero matrix, useful for initializing weights in ML or placeholders.
    arr = np.zeros((2, 3), dtype=int)
    print(arr)

    # Variation: 3D array
    arr_3d = np.zeros((2, 2, 2))
    print(arr_3d)

    # Edge case: Scalar shape (0D)
    scalar_zero = np.zeros(())
    print(scalar_zero)
    ```
    **Explanation**: Initializes arrays with zeros for memory allocation. Demonstrates shapes and dtypes.  
    **Output**:
    ```
    [[0 0 0]
     [0 0 0]]
    [[[0. 0.]
      [0. 0.]]

     [[0. 0.]
      [0. 0.]]]
    0.0
    ```

- `np.ones(shape, dtype=float, order='C')`: Return a new array of given shape filled with ones.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Creating a 3x2 ones array, useful for bias terms or masks.
    arr = np.ones((3, 2), dtype=float)
    print(arr)

    # Variation: Integer dtype for counting
    arr_int = np.ones((2,), dtype=int)
    print(arr_int)

    # Edge case: Empty shape
    try:
        empty = np.ones((0, 3))
        print(empty)
    except ValueError as e:
        print("Error:", e)
    ```
    **Explanation**: Similar to zeros but with ones. Shows usage and empty array handling.  
    **Output**:
    ```
    [[1. 1.]
     [1. 1.]
     [1. 1.]]
    [1 1]
    []
    ```

- `np.empty(shape, dtype=float, order='C')`: Return a new array of given shape without initializing entries.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Creating an uninitialized 2x2 array (values are garbage from memory). Useful for performance when values will be set later.
    arr = np.empty((2, 2))
    print(arr)  # Output varies

    # Variation: Specify dtype
    arr_int = np.empty((3,), dtype=int)
    print(arr_int)  # Output varies

    # Edge case: 1D empty array
    empty_1d = np.empty(5)
    print(empty_1d)  # Output varies
    ```
    **Explanation**: Faster than zeros/ones as it skips initialization. Values are unpredictable.  
    **Output**: (Varies, e.g.)
    ```
    [[6.95230887e-310 6.95230887e-310]
     [6.95230887e-310 6.95230887e-310]]
    [0 0 0]
    [6.95230887e-310 6.95230887e-310 6.95230887e-310 6.95230887e-310 6.95230887e-310]
    ```

- `np.full(shape, fill_value, dtype=None, order='C')`: Return a new array of given shape filled with `fill_value`.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Filling a 2x3 array with pi, useful for constants in simulations.
    arr = np.full((2, 3), np.pi)
    print(arr)

    # Variation: String fill for non-numeric
    arr_str = np.full((2,), 'hello', dtype='U10')
    print(arr_str)

    # Edge case: Complex numbers
    arr_complex = np.full((2,), 1+2j)
    print(arr_complex)
    ```
    **Explanation**: Generalizes ones/zeros for any value. Shows numeric and non-numeric uses.  
    **Output**:
    ```
    [[3.14159265 3.14159265 3.14159265]
     [3.14159265 3.14159265 3.14159265]]
    ['hello' 'hello']
    [1.+2.j 1.+2.j]
    ```

- `np.eye(N, M=None, k=0, dtype=float, order='C')`: Return a 2-D array with ones on the diagonal and zeros elsewhere.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Creating a 3x3 identity matrix, fundamental in linear algebra.
    arr = np.eye(3)
    print(arr)

    # Variation: Offset diagonal (k=1 for superdiagonal)
    arr_offset = np.eye(3, k=1)
    print(arr_offset)

    # Edge case: Non-square (3x4)
    arr_rect = np.eye(3, 4)
    print(arr_rect)
    ```
    **Explanation**: Creates identity-like matrices for transformations. Shows offsets and rectangular shapes.  
    **Output**:
    ```
    [[1. 0. 0.]
     [0. 1. 0.]
     [0. 0. 1.]]
    [[0. 1. 0.]
     [0. 0. 1.]
     [0. 0. 0.]]
    [[1. 0. 0. 0.]
     [0. 1. 0. 0.]
     [0. 0. 1. 0.]]
    ```

- `np.identity(n, dtype=float)`: Return the identity array (square array with ones on the main diagonal).
  - **In-depth Example**:
    ```python
    import numpy as np

    # Creating a 4x4 identity matrix, similar to eye but always square and k=0.
    arr = np.identity(4, dtype=int)
    print(arr)

    # Variation: Use in matrix multiplication to verify
    mat = np.array([[1, 2], [3, 4]])
    identity = np.identity(2)
    result = np.dot(mat, identity)
    print(result)

    # Edge case: Size 1
    single = np.identity(1)
    print(single)
    ```
    **Explanation**: Strict square identity. Demonstrates usage in operations.  
    **Output**:
    ```
    [[1 0 0 0]
     [0 1 0 0]
     [0 0 1 0]
     [0 0 0 1]]
    [[1. 2.]
     [3. 4.]]
    [[1.]]
    ```

- `np.diag(v, k=0)`: Extract a diagonal or construct a diagonal array.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Constructing a diagonal matrix from a vector.
    vec = [1, 2, 3]
    arr = np.diag(vec)
    print(arr)

    # Variation: Extract diagonal from 2D array
    mat = np.array([[4, 5, 6], [7, 8, 9], [10, 11, 12]])
    diag = np.diag(mat, k=1)
    print(diag)

    # Edge case: Offset k negative
    diag_sub = np.diag(mat, k=-1)
    print(diag_sub)
    ```
    **Explanation**: Builds or extracts diagonals for eigenvalue problems. Shows construction and extraction.  
    **Output**:
    ```
    [[1 0 0]
     [0 2 0]
     [0 0 3]]
    [5 9]
    [ 7 10]
    ```

- `np.fromfunction(function, shape, dtype=float)`: Construct an array by executing a function over each coordinate.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Creating a 3x3 array where each element is i*j (row*col indices).
    def func(i, j):
        return i * j
    arr = np.fromfunction(func, (3, 3), dtype=int)
    print(arr)

    # Variation: 1D with lambda
    arr_1d = np.fromfunction(lambda i: i**2, (5,))
    print(arr_1d)

    # Edge case: Higher dimensions
    arr_3d = np.fromfunction(lambda i, j, k: i + j + k, (2, 2, 2))
    print(arr_3d)
    ```
    **Explanation**: Applies a function to grid coordinates for custom arrays. Useful for meshes.  
    **Output**:
    ```
    [[0 0 0]
     [0 1 2]
     [0 2 4]]
    [ 0.  1.  4.  9. 16.]
    [[[0. 1.]
      [1. 2.]]

     [[1. 2.]
      [2. 3.]]]
    ```

- `np.frombuffer(buffer, dtype=float, count=-1, offset=0)`: Interpret a buffer as a 1-D array.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Interpreting bytes as uint8 array, useful for binary data parsing.
    buf = b'\x01\x02\x03\x04'
    arr = np.frombuffer(buf, dtype=np.uint8, count=4)
    print(arr)

    # Variation: Offset and partial count
    arr_offset = np.frombuffer(buf, dtype=np.uint8, count=2, offset=1)
    print(arr_offset)

    # Edge case: Float dtype on byte buffer
    float_buf = b'\x00\x00\x80\x3f'  # Little-endian 1.0 float32
    arr_float = np.frombuffer(float_buf, dtype=np.float32)
    print(arr_float)
    ```
    **Explanation**: Converts binary buffers to arrays for I/O or network data. Shows offsets and dtypes.  
    **Output**:
    ```
    [1 2 3 4]
    [2 3]
    [1.]
    ```

- `np.fromiter(iterable, dtype, count=-1)`: Create a new 1-D array from an iterable object.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Creating array from a generator, efficient for large data without lists.
    gen = (x**2 for x in range(5))
    arr = np.fromiter(gen, dtype=int, count=5)
    print(arr)

    # Variation: Infinite generator with count limit
    def infinite():
        i = 0
        while True:
            yield i
            i += 1
    arr_limit = np.fromiter(infinite(), dtype=int, count=3)
    print(arr_limit)

    # Edge case: Empty iterable
    empty_gen = (x for x in [])
    arr_empty = np.fromiter(empty_gen, dtype=float)
    print(arr_empty)
    ```
    **Explanation**: Builds arrays from iterables for memory efficiency. Shows generators and limits.  
    **Output**:
    ```
    [ 0  1  4  9 16]
    [0 1 2]
    []
    ```

- `np.loadtxt(fname, dtype=float, delimiter=None, skiprows=0, usecols=None)`: Load data from a text file.
  - **In-depth Example**:
    ```python
    import numpy as np
    from io import StringIO  # For in-memory file simulation

    # Simulating a CSV file load, useful for data import.
    data = StringIO("1,2,3\n4,5,6")
    arr = np.loadtxt(data, delimiter=',', dtype=int)
    print(arr)

    # Variation: Skip rows and select columns
    data.seek(0)
    arr_select = np.loadtxt(data, delimiter=',', skiprows=1, usecols=(0, 2))
    print(arr_select)

    # Edge case: Handling comments
    data_with_comment = StringIO("# Header\n1 2\n3 4")
    arr_comment = np.loadtxt(data_with_comment, comments='#', delimiter=' ')
    print(arr_comment)
    ```
    **Explanation**: Reads text files into arrays for data analysis. Uses StringIO for demo.  
    **Output**:
    ```
    [[1 2 3]
     [4 5 6]]
    [4 6]
    [[1. 2.]
     [3. 4.]]
    ```

- `np.genfromtxt(fname, dtype=float, delimiter=None, skip_header=0, usecols=None)`: Load data from a text file, handling missing values.
  - **In-depth Example**:
    ```python
    import numpy as np
    from io import StringIO

    # Loading with missing values, sets to NaN.
    data = StringIO("1,2,\n4,5,6")
    arr = np.genfromtxt(data, delimiter=',', missing_values='', filling_values=np.nan)
    print(arr)

    # Variation: Skip header and specify dtype
    data_with_header = StringIO("Header\n1 2 3\n4 5 6")
    arr_header = np.genfromtxt(data_with_header, skip_header=1, delimiter=' ', dtype=int)
    print(arr_header)

    # Edge case: All missing in a row
    data_missing = StringIO(",,\n7,8,9")
    arr_missing = np.genfromtxt(data_missing, delimiter=',', filling_values=0)
    print(arr_missing)
    ```
    **Explanation**: More flexible than loadtxt for irregular data. Handles missing values.  
    **Output**:
    ```
    [[ 1.  2. nan]
     [ 4.  5.  6.]]
    [[1 2 3]
     [4 5 6]]
    [[0. 0. 0.]
     [7. 8. 9.]]
    ```

## 2. Array Manipulation
Functions and methods for reshaping, joining, splitting, and modifying arrays.

### Functions
- `np.reshape(a, newshape, order='C')`: Give a new shape to an array without changing its data.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Reshaping a 1D array to 2D for image-like data.
    arr = np.arange(12)
    reshaped = np.reshape(arr, (3, 4))
    print(reshaped)

    # Variation: Order 'F' for Fortran-style (column-major)
    reshaped_f = np.reshape(arr, (3, 4), order='F')
    print(reshaped_f)

    # Edge case: Use -1 to infer dimension
    inferred = np.reshape(arr, (2, -1))
    print(inferred)
    ```
    **Explanation**: Changes array shape for data restructuring. Shows orders and inference.  
    **Output**:
    ```
    [[ 0  1  2  3]
     [ 4  5  6  7]
     [ 8  9 10 11]]
    [[ 0  3  6  9]
     [ 1  4  7 10]
     [ 2  5  8 11]]
    [[ 0  1  2  3  4  5]
     [ 6  7  8  9 10 11]]
    ```

- `np.ravel(a, order='C')`: Return a contiguous flattened array.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Flattening a 2D array to 1D, useful for vectorization.
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    flat = np.ravel(arr)
    print(flat)

    # Variation: 'F' order
    flat_f = np.ravel(arr, order='F')
    print(flat_f)

    # Edge case: Already 1D
    one_d = np.ravel(np.array([7, 8, 9]))
    print(one_d)
    ```
    **Explanation**: Flattens to 1D, returning a view if possible. Shows orders.  
    **Output**:
    ```
    [1 2 3 4 5 6]
    [1 4 2 5 3 6]
    [7 8 9]
    ```

- `np.transpose(a, axes=None)`: Permute the dimensions of an array.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Transposing a 2D matrix, common in linear algebra.
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    trans = np.transpose(arr)
    print(trans)

    # Variation: Specify axes for higher dims
    arr_3d = np.arange(24).reshape(2, 3, 4)
    trans_3d = np.transpose(arr_3d, axes=(2, 0, 1))
    print(trans_3d.shape)

    # Edge case: 1D array (no change)
    one_d_trans = np.transpose(np.array([1, 2]))
    print(one_d_trans)
    ```
    **Explanation**: Swaps dimensions for data reorientation. Shows 2D, 3D, and 1D.  
    **Output**:
    ```
    [[1 4]
     [2 5]
     [3 6]]
    (4, 2, 3)
    [1 2]
    ```

- `np.swapaxes(a, axis1, axis2)`: Interchange two axes of an array.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Swapping axes in 3D array, useful for tensor operations.
    arr = np.arange(24).reshape(2, 3, 4)
    swapped = np.swapaxes(arr, 0, 2)
    print(swapped.shape)

    # Variation: Swap in 2D (like transpose)
    arr_2d = np.array([[1, 2], [3, 4]])
    swapped_2d = np.swapaxes(arr_2d, 0, 1)
    print(swapped_2d)

    # Edge case: Same axis (no change)
    same = np.swapaxes(arr_2d, 0, 0)
    print(same)
    ```
    **Explanation**: Specific axis swap for multidimensional data.  
    **Output**:
    ```
    (4, 3, 2)
    [[1 3]
     [2 4]]
    [[1 2]
     [3 4]]
    ```

- `np.concatenate((a1, a2, ...), axis=0)`: Join a sequence of arrays along an existing axis.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Concatenating along rows (axis=0), for stacking datasets.
    a1 = np.array([[1, 2], [3, 4]])
    a2 = np.array([[5, 6]])
    concat = np.concatenate((a1, a2), axis=0)
    print(concat)

    # Variation: Along columns (axis=1)
    a3 = np.array([[7], [8]])
    concat_col = np.concatenate((a1, a3), axis=1)
    print(concat_col)

    # Edge case: 1D arrays
    concat_1d = np.concatenate(([1, 2], [3, 4]))
    print(concat_1d)
    ```
    **Explanation**: Joins arrays for data merging. Shows axes and 1D.  
    **Output**:
    ```
    [[1 2]
     [3 4]
     [5 6]]
    [[1 2 7]
     [3 4 8]]
    [1 2 3 4]
    ```

- `np.stack(arrays, axis=0)`: Join a sequence of arrays along a new axis.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Stacking 1D arrays into 2D along new axis, for batching.
    a1 = np.array([1, 2])
    a2 = np.array([3, 4])
    stacked = np.stack((a1, a2), axis=0)
    print(stacked)

    # Variation: Axis=1 for column stack
    stacked_col = np.stack((a1, a2), axis=1)
    print(stacked_col)

    # Edge case: 3 arrays
    a3 = np.array([5, 6])
    stacked_3 = np.stack((a1, a2, a3))
    print(stacked_3.shape)
    ```
    **Explanation**: Adds a new dimension for stacking.  
    **Output**:
    ```
    [[1 2]
     [3 4]]
    [[1 3]
     [2 4]]
    (3, 2)
    ```

- `np.vstack(tup)`: Stack arrays in sequence vertically (row-wise).
  - **In-depth Example**:
    ```python
    import numpy as np

    # Vertical stacking, equivalent to concatenate axis=0 for 2D.
    a1 = np.array([1, 2])
    a2 = np.array([3, 4])
    vstacked = np.vstack((a1, a2))
    print(vstacked)

    # Variation: Mixing 1D and 2D
    a3 = np.array([[5, 6]])
    vstacked_mix = np.vstack((vstacked, a3))
    print(vstacked_mix)

    # Edge case: Scalar inputs (promoted to 2D)
    vstack_scalar = np.vstack((1, 2))
    print(vstack_scalar)
    ```
    **Explanation**: Row-wise stacking for table building.  
    **Output**:
    ```
    [[1 2]
     [3 4]]
    [[1 2]
     [3 4]
     [5 6]]
    [[1]
     [2]]
    ```

- `np.hstack(tup)`: Stack arrays in sequence horizontally (column-wise).
  - **In-depth Example**:
    ```python
    import numpy as np

    # Horizontal stacking, for adding columns.
    a1 = np.array([[1], [2]])
    a2 = np.array([[3], [4]])
    hstacked = np.hstack((a1, a2))
    print(hstacked)

    # Variation: 1D arrays become row
    a3 = np.array([5, 6])
    a4 = np.array([7, 8])
    hstack_1d = np.hstack((a3, a4))
    print(hstack_1d)

    # Edge case: Mismatched shapes raise error
    try:
        np.hstack((np.array([1]), np.array([[2]])))
    except ValueError as e:
        print("Error:", e)
    ```
    **Explanation**: Column-wise for feature addition. Shows errors.  
    **Output**:
    ```
    [[1 3]
     [2 4]]
    [5 6 7 8]
    Error: All the input array dimensions except for the concatenation axis must match exactly
    ```

- `np.dstack(tup)`: Stack arrays in sequence depth-wise (along third axis).
  - **In-depth Example**:
    ```python
    import numpy as np

    # Depth stacking for RGB images (channels).
    r = np.array([[1, 2], [3, 4]])
    g = np.array([[5, 6], [7, 8]])
    dstacked = np.dstack((r, g))
    print(dstacked)

    # Variation: Three layers
    b = np.array([[9, 10], [11, 12]])
    dstacked_3 = np.dstack((r, g, b))
    print(dstacked_3.shape)

    # Edge case: 1D inputs
    dstack_1d = np.dstack(([1, 2], [3, 4]))
    print(dstack_1d)
    ```
    **Explanation**: Adds depth for multi-channel data.  
    **Output**:
    ```
    [[[1 5]
      [2 6]]

     [[3 7]
      [4 8]]]
    (2, 2, 3)
    [[[1 3]
      [2 4]]]
    ```

- `np.split(a, indices_or_sections, axis=0)`: Split an array into multiple sub-arrays.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Splitting into equal parts, for data partitioning.
    arr = np.arange(9)
    splits = np.split(arr, 3)
    print(splits)

    # Variation: Unequal with indices
    splits_uneq = np.split(arr, [3, 6])
    print(splits_uneq)

    # Edge case: Along axis=1 for 2D
    arr_2d = np.arange(12).reshape(3, 4)
    splits_2d = np.split(arr_2d, 2, axis=1)
    print([s.shape for s in splits_2d])
    ```
    **Explanation**: Divides arrays for parallel processing. Shows equal/unequal.  
    **Output**:
    ```
    [array([0, 1, 2]), array([3, 4, 5]), array([6, 7, 8])]
    [array([0, 1, 2]), array([3, 4, 5]), array([6, 7, 8])]
    [(3, 2), (3, 2)]
    ```

- `np.array_split(a, indices_or_sections, axis=0)`: Split an array into multiple sub-arrays with unequal sizes.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Unequal split when not divisible.
    arr = np.arange(10)
    splits = np.array_split(arr, 3)
    print(splits)

    # Variation: Indices for custom points
    splits_ind = np.array_split(arr, [2, 5, 8])
    print(splits_ind)

    # Edge case: More sections than elements
    splits_more = np.array_split(arr, 12)
    print(len(splits_more))
    ```
    **Explanation**: Handles non-even divisions gracefully.  
    **Output**:
    ```
    [array([0, 1, 2, 3]), array([4, 5, 6]), array([7, 8, 9])]
    [array([0, 1]), array([2, 3, 4]), array([5, 6, 7]), array([8, 9])]
    10
    ```

- `np.tile(A, reps)`: Construct an array by repeating A the number of times given by reps.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Tiling a vector for pattern repetition.
    arr = np.array([1, 2])
    tiled = np.tile(arr, 3)
    print(tiled)

    # Variation: Multi-dimensional reps
    tiled_2d = np.tile(arr, (2, 3))
    print(tiled_2d)

    # Edge case: Scalar tile
    tiled_scalar = np.tile(5, (2, 2))
    print(tiled_scalar)
    ```
    **Explanation**: Repeats arrays for broadcasting or patterns.  
    **Output**:
    ```
    [1 2 1 2 1 2]
    [[1 2 1 2 1 2]
     [1 2 1 2 1 2]]
    [[5 5]
     [5 5]]
    ```

- `np.repeat(a, repeats, axis=None)`: Repeat elements of an array.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Repeating elements, for data augmentation.
    arr = np.array([1, 2, 3])
    repeated = np.repeat(arr, 2)
    print(repeated)

    # Variation: Different repeats per element
    repeated_var = np.repeat(arr, [1, 2, 3])
    print(repeated_var)

    # Edge case: Along axis in 2D
    arr_2d = np.array([[1, 2], [3, 4]])
    repeated_axis = np.repeat(arr_2d, 2, axis=0)
    print(repeated_axis)
    ```
    **Explanation**: Element-wise repetition. Shows variable repeats.  
    **Output**:
    ```
    [1 1 2 2 3 3]
    [1 2 2 3 3 3]
    [[1 2]
     [1 2]
     [3 4]
     [3 4]]
    ```

- `np.append(arr, values, axis=None)`: Append values to the end of an array.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Appending to 1D, but note: inefficient for loops (use lists instead).
    arr = np.array([1, 2])
    appended = np.append(arr, [3, 4])
    print(appended)

    # Variation: Along axis in 2D
    arr_2d = np.array([[1, 2], [3, 4]])
    appended_2d = np.append(arr_2d, [[5, 6]], axis=0)
    print(appended_2d)

    # Edge case: Append scalar
    appended_scalar = np.append(arr, 5)
    print(appended_scalar)
    ```
    **Explanation**: Adds elements, but creates new array.  
    **Output**:
    ```
    [1 2 3 4]
    [[1 2]
     [3 4]
     [5 6]]
    [1 2 5]
    ```

- `np.resize(a, new_shape)`: Return a new array with the specified shape.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Resizing with repetition if larger.
    arr = np.array([1, 2, 3])
    resized = np.resize(arr, (2, 3))
    print(resized)

    # Variation: Shrink (truncates)
    resized_small = np.resize(arr, (2,))
    print(resized_small)

    # Edge case: Pad with repetition for odd sizes
    resized_odd = np.resize(arr, 5)
    print(resized_odd)
    ```
    **Explanation**: Reshapes with repeat or truncate. Different from reshape.  
    **Output**:
    ```
    [[1 2 3]
     [1 2 3]]
    [1 2]
    [1 2 3 1 2]
    ```

- `np.expand_dims(a, axis)`: Expand the shape of an array by adding a new axis.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Adding dimension for broadcasting.
    arr = np.array([1, 2, 3])
    expanded = np.expand_dims(arr, axis=0)
    print(expanded.shape)

    # Variation: Add at end
    expanded_end = np.expand_dims(arr, axis=1)
    print(expanded_end)

    # Edge case: Multiple expands
    expanded_2 = np.expand_dims(expanded, axis=2)
    print(expanded_2.shape)
    ```
    **Explanation**: Inserts singleton dimensions for ops.  
    **Output**:
    ```
    (1, 3)
    [[1]
     [2]
     [3]]
    (1, 3, 1)
    ```

- `np.squeeze(a, axis=None)`: Remove single-dimensional entries from the shape of an array.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Squeezing singleton dimensions.
    arr = np.array([[[1, 2, 3]]])
    squeezed = np.squeeze(arr)
    print(squeezed.shape)

    # Variation: Specify axis
    squeezed_axis = np.squeeze(arr, axis=0)
    print(squeezed_axis.shape)

    # Edge case: No squeeze if not singleton
    try:
        np.squeeze(np.array([[1, 2]]), axis=1)
    except ValueError as e:
        print("Error:", e)
    ```
    **Explanation**: Removes unnecessary dims. Shows errors.  
    **Output**:
    ```
    (3,)
    (1, 3)
    Error: cannot select an axis to squeeze out which has size not equal to one
    ```

- `np.flip(a, axis=None)`: Reverse the order of elements in an array along the specified axis.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Flipping 1D array.
    arr = np.array([1, 2, 3, 4])
    flipped = np.flip(arr)
    print(flipped)

    # Variation: Flip along axis in 2D
    arr_2d = np.array([[1, 2], [3, 4]])
    flipped_row = np.flip(arr_2d, axis=0)
    print(flipped_row)

    # Edge case: Multi-axis flip
    flipped_both = np.flip(arr_2d, axis=(0, 1))
    print(flipped_both)
    ```
    **Explanation**: Reverses for symmetry or time reversal.  
    **Output**:
    ```
    [4 3 2 1]
    [[3 4]
     [1 2]]
    [[4 3]
     [2 1]]
    ```

- `np.roll(a, shift, axis=None)`: Roll array elements along a given axis.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Rolling 1D array, for circular shifts.
    arr = np.array([1, 2, 3, 4])
    rolled = np.roll(arr, 2)
    print(rolled)

    # Variation: Negative shift
    rolled_neg = np.roll(arr, -1)
    print(rolled_neg)

    # Edge case: Roll in 2D along axis
    arr_2d = np.array([[1, 2], [3, 4]])
    rolled_2d = np.roll(arr_2d, 1, axis=1)
    print(rolled_2d)
    ```
    **Explanation**: Cyclic shift for signal processing.  
    **Output**:
    ```
    [3 4 1 2]
    [4 1 2 3]
    [[2 1]
     [4 3]]
    ```

### Methods
- `ndarray.reshape(newshape, order='C')`: Reshape the array in-place (if possible).
  - **In-depth Example**:
    ```python
    import numpy as np

    # Method version of reshape, returns view if contiguous.
    arr = np.arange(6)
    reshaped = arr.reshape((2, 3))
    print(reshaped)

    # Variation: Check if view (modifies original)
    reshaped[0, 0] = 99
    print(arr)  # Original changed if view

    # Edge case: Non-contiguous (copy)
    arr_t = arr.T if arr.ndim > 1 else arr
    try:
        arr_t.reshape((3, 2))
    except AttributeError:
        print("1D has no T")
    ```
    **Explanation**: Array method for reshape. Shows view vs copy.  
    **Output**:
    ```
    [[0 1 2]
     [3 4 5]]
    [99  1  2  3  4  5]
    1D has no T
    ```

- `ndarray.ravel(order='C')`: Return a flattened array (view if possible).
  - **In-depth Example**:
    ```python
    import numpy as np

    # Method for flattening.
    arr = np.array([[1, 2], [3, 4]])
    raveled = arr.ravel()
    print(raveled)

    # Variation: Modify view
    raveled[0] = 99
    print(arr)

    # Edge case: 'F' order
    raveled_f = arr.ravel(order='F')
    print(raveled_f)
    ```
    **Explanation**: Flattens as view. Shows modification.  
    **Output**:
    ```
    [99  2  3  4]
    [[99  2]
     [ 3  4]]
    [99  3  2  4]
    ```

- `ndarray.flatten(order='C')`: Return a flattened copy of the array.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Always returns copy, unlike ravel.
    arr = np.array([[1, 2], [3, 4]])
    flattened = arr.flatten()
    print(flattened)

    # Variation: Modify doesn't affect original
    flattened[0] = 99
    print(arr)

    # Edge case: 'F' order
    flattened_f = arr.flatten(order='F')
    print(flattened_f)
    ```
    **Explanation**: Safe flatten with copy.  
    **Output**:
    ```
    [1 2 3 4]
    [[1 2]
     [3 4]]
    [1 3 2 4]
    ```

- `ndarray.transpose(*axes)`: Permute the dimensions of the array.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Method for transpose.
    arr = np.array([[1, 2], [3, 4]])
    trans = arr.transpose()
    print(trans)

    # Variation: With axes
    arr_3d = np.arange(8).reshape(2, 2, 2)
    trans_axes = arr_3d.transpose(2, 0, 1)
    print(trans_axes.shape)

    # Edge case: Shorthand arr.T
    print(arr.T)
    ```
    **Explanation**: Array method for transpose.  
    **Output**:
    ```
    [[1 3]
     [2 4]]
    (2, 2, 2)
    [[1 3]
     [2 4]]
    ```

- `ndarray.swapaxes(axis1, axis2)`: Interchange two axes of the array.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Method version.
    arr = np.arange(8).reshape(2, 2, 2)
    swapped = arr.swapaxes(0, 2)
    print(swapped.shape)

    # Variation: Chain swaps
    swapped_chain = swapped.swapaxes(0, 1)
    print(swapped_chain.shape)

    # Edge case: Same axes
    same = arr.swapaxes(0, 0)
    print(same.shape)
    ```
    **Explanation**: In-place axis swap.  
    **Output**:
    ```
    (2, 2, 2)
    (2, 2, 2)
    (2, 2, 2)
    ```

- `ndarray.squeeze(axis=None)`: Remove single-dimensional entries from the array's shape.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Method for squeeze.
    arr = np.array([[[1]], [[2]]])
    squeezed = arr.squeeze()
    print(squeezed.shape)

    # Variation: Specific axis
    squeezed_axis = arr.squeeze(axis=2)
    print(squeezed_axis.shape)

    # Edge case: Error on non-singleton
    try:
        arr.squeeze(axis=0)
    except ValueError as e:
        print("Error:", e)
    ```
    **Explanation**: Cleans shape.  
    **Output**:
    ```
    (2,)
    (2, 1)
    Error: cannot select an axis to squeeze out which has size not equal to one
    ```

- `ndarray.astype(dtype, order='K', casting='unsafe', copy=True)`: Copy of the array, cast to a specified type.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Casting float to int, truncates.
    arr = np.array([1.5, 2.7])
    casted = arr.astype(int)
    print(casted)

    # Variation: To complex
    casted_complex = arr.astype(complex)
    print(casted_complex)

    # Edge case: Unsafe casting (may lose data)
    arr_big = np.array([1000], dtype=np.int8)
    casted_unsafe = arr_big.astype(np.uint8, casting='unsafe')
    print(casted_unsafe)
    ```
    **Explanation**: Type conversion. Shows lossy casts.  
    **Output**:
    ```
    [1 2]
    [1.5+0.j 2.7+0.j]
    [232]
    ```

- `ndarray.copy(order='C')`: Return a copy of the array.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Deep copy.
    arr = np.array([1, 2])
    copied = arr.copy()
    copied[0] = 99
    print(arr)

    # Variation: 'F' order copy
    arr_2d = np.array([[1, 2], [3, 4]])
    copied_f = arr_2d.copy(order='F')
    print(copied_f.flags['F_CONTIGUOUS'])

    # Edge case: View vs copy
    view = arr[:]
    view[0] = 88
    print(arr)
    ```
    **Explanation**: Ensures independent array. Shows orders and views.  
    **Output**:
    ```
    [88  2]
    True
    [88  2]
    ```

- `ndarray.repeat(repeats, axis=None)`: Repeat elements of the array.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Method for repeat.
    arr = np.array([1, 2])
    repeated = arr.repeat(3)
    print(repeated)

    # Variation: Per-element repeats
    repeated_var = arr.repeat([2, 4])
    print(repeated_var)

    # Edge case: Axis in 2D
    arr_2d = np.array([[1], [2]])
    repeated_axis = arr_2d.repeat(2, axis=1)
    print(repeated_axis)
    ```
    **Explanation**: Array method for repeat.  
    **Output**:
    ```
    [1 1 1 2 2 2]
    [1 1 2 2 2 2]
    [[1 1]
     [2 2]]
    ```

## 3. Mathematical Operations
Functions and methods for element-wise mathematical operations.

### Functions
- `np.add(x1, x2)`: Element-wise addition.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Adding arrays, with broadcasting.
    a = np.array([1, 2, 3])
    b = np.array([4])
    added = np.add(a, b)
    print(added)

    # Variation: 2D + 1D
    a2d = np.array([[1, 2], [3, 4]])
    added_2d = np.add(a2d, np.array([10, 20]))
    print(added_2d)

    # Edge case: Scalar + array
    added_scalar = np.add(a, 5)
    print(added_scalar)
    ```
    **Explanation**: Ufunc for addition, supports broadcasting.  
    **Output**:
    ```
    [5 6 7]
    [[11 22]
     [13 24]]
    [6 7 8]
    ```

- `np.subtract(x1, x2)`: Element-wise subtraction.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Subtracting, with broadcasting.
    a = np.array([10, 20, 30])
    b = 5
    sub = np.subtract(a, b)
    print(sub)

    # Variation: 2D - 1D
    a2d = np.array([[10, 20], [30, 40]])
    sub_2d = np.subtract(a2d, np.array([1, 2]))
    print(sub_2d)

    # Edge case: Negative results
    sub_neg = np.subtract([1, 2], [3, 4])
    print(sub_neg)
    ```
    **Explanation**: Ufunc for subtraction.  
    **Output**:
    ```
    [ 5 15 25]
    [[ 9 18]
     [29 38]]
    [-2 -2]
    ```

- `np.multiply(x1, x2)`: Element-wise multiplication.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Element-wise mul, not matrix mul.
    a = np.array([2, 3])
    b = np.array([4, 5])
    mul = np.multiply(a, b)
    print(mul)

    # Variation: Broadcasting scalar
    mul_scalar = np.multiply(a, 10)
    print(mul_scalar)

    # Edge case: With zeros
    mul_zero = np.multiply([1, 0], [2, 3])
    print(mul_zero)
    ```
    **Explanation**: Hadamard product.  
    **Output**:
    ```
    [ 8 15]
    [20 30]
    [2 0]
    ```

- `np.divide(x1, x2)`: Element-wise division.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Division, handles floats.
    a = np.array([10, 20])
    b = np.array([2, 4])
    div = np.divide(a, b)
    print(div)

    # Variation: Divide by scalar
    div_scalar = np.divide(a, 5)
    print(div_scalar)

    # Edge case: Division by zero (inf or nan)
    div_zero = np.divide(1, 0)
    print(div_zero)
    ```
    **Explanation**: True division. Shows inf handling.  
    **Output**:
    ```
    [5. 5.]
    [2. 4.]
    inf
    ```

- `np.power(x1, x2)`: Element-wise power.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Raising to power.
    a = np.array([2, 3])
    powed = np.power(a, 3)
    print(powed)

    # Variation: Array exponents
    exponents = np.array([2, 1])
    powed_arr = np.power(a, exponents)
    print(powed_arr)

    # Edge case: Negative base with fractional power
    pow_neg = np.power(-2, 0.5)
    print(powed_neg)
    ```
    **Explanation**: Exponentiation, handles complexes.  
    **Output**:
    ```
    [ 8 27]
    [4 3]
    nan + 1.4142135623730951j
    ```

- `np.mod(x1, x2)`: Element-wise modulus.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Modulus for integers.
    a = np.array([10, 20])
    modded = np.mod(a, 3)
    print(modded)

    # Variation: Float modulus
    mod_float = np.mod([5.5, 6.5], 2.0)
    print(mod_float)

    # Edge case: Mod by zero (nan)
    mod_zero = np.mod(5, 0)
    print(mod_zero)
    ```
    **Explanation**: Remainder operation.  
    **Output**:
    ```
    [1 2]
    [1.5 0.5]
    nan
    ```

- `np.abs(x)`: Element-wise absolute value.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Absolute for negatives.
    a = np.array([-1, -2, 3])
    absed = np.abs(a)
    print(absed)

    # Variation: Complex abs (magnitude)
    complex_a = np.array([1+1j, 2+2j])
    abs_complex = np.abs(complex_a)
    print(abs_complex)

    # Edge case: Zero
    abs_zero = np.abs(0)
    print(abs_zero)
    ```
    **Explanation**: Magnitude for complexes too.  
    **Output**:
    ```
    [1 2 3]
    [1.41421356 2.82842712]
    0
    ```

- `np.sqrt(x)`: Element-wise square root.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Square root.
    a = np.array([4, 9, 16])
    sqrted = np.sqrt(a)
    print(sqrted)

    # Variation: Complex sqrt
    sqrt_complex = np.sqrt(-4)
    print(sqrt_complex)

    # Edge case: Negative real (nan)
    sqrt_neg = np.sqrt(-1)
    print(sqrt_neg)
    ```
    **Explanation**: Handles negatives as complex.  
    **Output**:
    ```
    [2. 3. 4.]
    2j
    nan
    ```

- `np.exp(x)`: Element-wise exponential.
  - **In-depth Example**:
    ```python
    import numpy as np

    # e^x.
    a = np.array([0, 1, 2])
    exped = np.exp(a)
    print(exped)

    # Variation: Large values (overflow to inf)
    exp_large = np.exp(1000)
    print(exp_large)

    # Edge case: Negative
    exp_neg = np.exp(-1)
    print(exp_neg)
    ```
    **Explanation**: Base-e exp. Handles overflow.  
    **Output**:
    ```
    [1.         2.71828183 7.3890561 ]
    inf
    0.3678794411714423
    ```

- `np.log(x)`: Element-wise natural logarithm.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Natural log.
    a = np.array([1, np.e, np.e**2])
    logged = np.log(a)
    print(logged)

    # Variation: Complex log
    log_complex = np.log(-1)
    print(log_complex)

    # Edge case: Log zero ( -inf )
    log_zero = np.log(0)
    print(log_zero)
    ```
    **Explanation**: Log base e. Branch for complexes.  
    **Output**:
    ```
    [0. 1. 2.]
    3.141592653589793j
    -inf
    ```

- `np.log10(x)`: Element-wise base-10 logarithm.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Log10.
    a = np.array([1, 10, 100])
    log10ed = np.log10(a)
    print(log10ed)

    # Variation: Small values
    log_small = np.log10(0.01)
    print(log_small)

    # Edge case: Negative (nan + j)
    log_neg = np.log10(-1)
    print(log_neg)
    ```
    **Explanation**: Common log.  
    **Output**:
    ```
    [0. 1. 2.]
    -2.0
    nan + 1.3643763538418412j
    ```

- `np.sin(x)`: Element-wise sine.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Sine in radians.
    a = np.array([0, np.pi/2, np.pi])
    sined = np.sin(a)
    print(sined)

    # Variation: Degrees with conversion
    deg = np.array([0, 90, 180])
    sin_deg = np.sin(np.deg2rad(deg))
    print(sin_deg)

    # Edge case: Large values (periodic)
    sin_large = np.sin(1000 * np.pi)
    print(sin_large)
    ```
    **Explanation**: Trig function.  
    **Output**:
    ```
    [0. 1. 0.]
    [0. 1. 0.]
    -1.9643867237284717e-13
    ```

- `np.cos(x)`: Element-wise cosine.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Cosine.
    a = np.array([0, np.pi/2, np.pi])
    cosed = np.cos(a)
    print(cosed)

    # Variation: With complex
    cos_complex = np.cos(1j)
    print(cos_complex)

    # Edge case: Inf input
    cos_inf = np.cos(np.inf)
    print(cos_inf)
    ```
    **Explanation**: Trig. Handles complex.  
    **Output**:
    ```
    [ 1.  0. -1.]
    1.5430806348152437
    nan
    ```

- `np.tan(x)`: Element-wise tangent.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Tangent.
    a = np.array([0, np.pi/4])
    taned = np.tan(a)
    print(taned)

    # Variation: Near pole (large)
    tan_pole = np.tan(np.pi/2 - 1e-10)
    print(tan_pole)

    # Edge case: At pole (nan)
    tan_nan = np.tan(np.pi/2)
    print(tan_nan)
    ```
    **Explanation**: Tan, singularities at odd pi/2.  
    **Output**:
    ```
    [0. 1.]
    10000000000.0
    nan
    ```

- `np.arcsin(x)`: Element-wise inverse sine.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Arcsin, range [-1,1].
    a = np.array([0, 1, -1])
    arcsin_ed = np.arcsin(a)
    print(arcsin_ed)

    # Variation: Out of range (nan)
    arcsin_out = np.arcsin(2)
    print(arcsin_out)

    # Edge case: Complex
    arcsin_complex = np.arcsin(2j)
    print(arcsin_complex)
    ```
    **Explanation**: Inverse trig. Complex for out-of-range.  
    **Output**:
    ```
    [ 0.          1.57079633 -1.57079633]
    nan
    -1.5707963267948966 + 1.3169578969248166j
    ```

- `np.arccos(x)`: Element-wise inverse cosine.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Arccos.
    a = np.array([1, 0, -1])
    arccos_ed = np.arccos(a)
    print(arccos_ed)

    # Variation: Float values
    arccos_float = np.arccos(0.5)
    print(arccos_float)

    # Edge case: Out of range
    arccos_out = np.arccos(1.1)
    print(arccos_out)
    ```
    **Explanation**: Inverse cos.  
    **Output**:
    ```
    [0.         1.57079633 3.14159265]
    1.0471975511965976
    nan
    ```

- `np.arctan(x)`: Element-wise inverse tangent.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Arctan.
    a = np.array([0, 1, np.inf])
    arctan_ed = np.arctan(a)
    print(arctan_ed)

    # Variation: Negative
    arctan_neg = np.arctan(-1)
    print(arctan_neg)

    # Edge case: Complex
    arctan_complex = np.arctan(1j)
    print(arctan_complex)
    ```
    **Explanation**: Inverse tan, approaches pi/2.  
    **Output**:
    ```
    [0.         0.78539816 1.57079633]
    -0.7853981633974483
    1.5707963267948966j
    ```

- `np.round(a, decimals=0)`: Round elements to the specified number of decimals.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Rounding floats.
    a = np.array([1.234, 5.678])
    rounded = np.round(a, decimals=2)
    print(rounded)

    # Variation: To nearest int
    rounded_int = np.round(a)
    print(rounded_int)

    # Edge case: Banker's rounding (even)
    round_bank = np.round(2.5)
    print(round_bank)
    ```
    **Explanation**: Rounds, uses banker's for .5.  
    **Output**:
    ```
    [1.23 5.68]
    [1. 6.]
    2.0
    ```

- `np.floor(x)`: Return the floor of the input, element-wise.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Floor.
    a = np.array([1.9, -1.1, 3.5])
    floored = np.floor(a)
    print(floored)

    # Variation: Complex (real/imag separate)
    floor_complex = np.floor(1.5 + 2.7j)
    print(floor_complex)

    # Edge case: Inf
    floor_inf = np.floor(np.inf)
    print(floor_inf)
    ```
    **Explanation**: Greatest integer less than or equal.  
    **Output**:
    ```
    [ 1. -2.  3.]
    (1+2j)
    inf
    ```

- `np.ceil(x)`: Return the ceiling of the input, element-wise.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Ceil.
    a = np.array([1.1, -1.9, 3.5])
    ceiled = np.ceil(a)
    print(ceiled)

    # Variation: Integers unchanged
    ceil_int = np.ceil(4)
    print(ceil_int)

    # Edge case: -inf
    ceil_neginf = np.ceil(-np.inf)
    print(ceil_neginf)
    ```
    **Explanation**: Smallest integer greater than or equal.  
    **Output**:
    ```
    [ 2. -1.  4.]
    4.0
    -inf
    ```

- `np.trunc(x)`: Return the truncated value of the input, element-wise.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Trunc towards zero.
    a = np.array([1.9, -1.9])
    trunced = np.trunc(a)
    print(trunced)

    # Variation: Same as floor for positive
    trunc_pos = np.trunc(3.7)
    print(trunc_pos)

    # Edge case: Nan
    trunc_nan = np.trunc(np.nan)
    print(trunc_nan)
    ```
    **Explanation**: Truncates decimal part.  
    **Output**:
    ```
    [ 1. -1.]
    3.0
    nan
    ```

### Methods
- `ndarray.round(decimals=0)`: Return array with elements rounded to the specified number of decimals.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Method round.
    arr = np.array([1.234, 5.678])
    rounded = arr.round(1)
    print(rounded)

    # Variation: Out param for in-place like
    out = np.zeros_like(arr)
    arr.round(1, out=out)
    print(out)

    # Edge case: Integer array
    int_arr = np.array([1, 2])
    int_round = int_arr.round()
    print(int_round)
    ```
    **Explanation**: Array method for round.  
    **Output**:
    ```
    [1.2 5.7]
    [1.2 5.7]
    [1 2]
    ```

- `ndarray.clip(a_min, a_max)`: Clip (limit) the values in the array.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Clipping to range.
    arr = np.array([1, 5, 10, -1])
    clipped = arr.clip(0, 8)
    print(clipped)

    # Variation: Only min or max
    clipped_min = arr.clip(2, None)
    print(clipped_min)

    # Edge case: All clipped
    clipped_all = arr.clip(3, 3)
    print(clipped_all)
    ```
    **Explanation**: Bounds values for normalization.  
    **Output**:
    ```
    [0 5 8 0]
    [ 2  5 10  2]
    [3 3 3 3]
    ```

## 4. Statistical Functions
Functions and methods for statistical computations.

### Functions
- `np.mean(a, axis=None, dtype=None)`: Compute the arithmetic mean along the specified axis.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Mean of array.
    arr = np.array([[1, 2], [3, 4]])
    mean_all = np.mean(arr)
    print(mean_all)

    # Variation: Along axis
    mean_axis = np.mean(arr, axis=0)
    print(mean_axis)

    # Edge case: With nan (use nanmean)
    arr_nan = np.array([1, np.nan, 3])
    mean_nan = np.mean(arr_nan)
    print(mean_nan)
    ```
    **Explanation**: Average. Handles axes.  
    **Output**:
    ```
    2.5
    [2. 3.]
    nan
    ```

- `np.median(a, axis=None)`: Compute the median along the specified axis.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Median.
    arr = np.array([1, 3, 2, 4])
    med = np.median(arr)
    print(med)

    # Variation: 2D axis
    arr_2d = np.array([[1, 2], [3, 4]])
    med_axis = np.median(arr_2d, axis=1)
    print(med_axis)

    # Edge case: Odd/even length
    med_even = np.median([1, 2])
    print(med_even)
    ```
    **Explanation**: Middle value.  
    **Output**:
    ```
    2.5
    [1.5 3.5]
    1.5
    ```

- `np.std(a, axis=None, dtype=None)`: Compute the standard deviation along the specified axis.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Std dev (population).
    arr = np.array([1, 2, 3, 4])
    std = np.std(arr)
    print(std)

    # Variation: ddof=1 for sample std
    std_sample = np.std(arr, ddof=1)
    print(std_sample)

    # Edge case: Single element (0)
    std_single = np.std([5])
    print(std_single)
    ```
    **Explanation**: Spread measure. ddof for sample.  
    **Output**:
    ```
    1.118033988749895
    1.2909944487358056
    0.0
    ```

- `np.var(a, axis=None, dtype=None)`: Compute the variance along the specified axis.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Variance.
    arr = np.array([1, 2, 3, 4])
    var = np.var(arr)
    print(var)

    # Variation: Sample var
    var_sample = np.var(arr, ddof=1)
    print(var_sample)

    # Edge case: Axis in 2D
    arr_2d = np.array([[1, 2], [3, 4]])
    var_axis = np.var(arr_2d, axis=0)
    print(var_axis)
    ```
    **Explanation**: Square of std.  
    **Output**:
    ```
    1.25
    1.6666666666666667
    [1. 1.]
    ```

- `np.min(a, axis=None)`: Return the minimum along a given axis.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Min.
    arr = np.array([[4, 1], [3, 2]])
    min_all = np.min(arr)
    print(min_all)

    # Variation: Axis
    min_axis = np.min(arr, axis=1)
    print(min_axis)

    # Edge case: With nan
    arr_nan = np.array([1, np.nan])
    min_nan = np.min(arr_nan)
    print(min_nan)
    ```
    **Explanation**: Smallest value. nan propagates.  
    **Output**:
    ```
    1
    [1 2]
    nan
    ```

- `np.max(a, axis=None)`: Return the maximum along a given axis.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Max.
    arr = np.array([[1, 4], [2, 3]])
    max_all = np.max(arr)
    print(max_all)

    # Variation: Axis
    max_axis = np.max(arr, axis=0)
    print(max_axis)

    # Edge case: Empty array
    try:
        np.max(np.array([]))
    except ValueError as e:
        print("Error:", e)
    ```
    **Explanation**: Largest.  
    **Output**:
    ```
    4
    [2 4]
    Error: zero-size array to reduction operation maximum which has no identity
    ```

- `np.sum(a, axis=None, dtype=None)`: Sum of array elements over a given axis.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Sum.
    arr = np.array([1, 2, 3])
    summed = np.sum(arr)
    print(summed)

    # Variation: 2D axis
    arr_2d = np.array([[1, 2], [3, 4]])
    sum_axis = np.sum(arr_2d, axis=1)
    print(sum_axis)

    # Edge case: Dtype for large sums
    large = np.array([2**60], dtype=np.int64)
    sum_large = np.sum(large)
    print(sum_large)
    ```
    **Explanation**: Total. Handles overflow with dtype.  
    **Output**:
    ```
    6
    [3 7]
    1152921504606846976
    ```

- `np.prod(a, axis=None, dtype=None)`: Product of array elements over a given axis.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Product.
    arr = np.array([2, 3, 4])
    proded = np.prod(arr)
    print(proded)

    # Variation: Axis
    arr_2d = np.array([[1, 2], [3, 4]])
    prod_axis = np.prod(arr_2d, axis=0)
    print(prod_axis)

    # Edge case: With zero
    prod_zero = np.prod([1, 0, 2])
    print(prod_zero)
    ```
    **Explanation**: Multiplication total.  
    **Output**:
    ```
    24
    [3 8]
    0
    ```

- `np.cumsum(a, axis=None, dtype=None)`: Return the cumulative sum of the elements along a given axis.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Cumsum.
    arr = np.array([1, 2, 3])
    cum = np.cumsum(arr)
    print(cum)

    # Variation: 2D
    arr_2d = np.array([[1, 2], [3, 4]])
    cum_axis = np.cumsum(arr_2d, axis=1)
    print(cum_axis)

    # Edge case: Empty
    cum_empty = np.cumsum([])
    print(cum_empty)
    ```
    **Explanation**: Running sum.  
    **Output**:
    ```
    [1 3 6]
    [[1 3]
     [3 7]]
    []
    ```

- `np.cumprod(a, axis=None, dtype=None)`: Return the cumulative product of the elements along a given axis.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Cumprod.
    arr = np.array([2, 3, 4])
    cumprod = np.cumprod(arr)
    print(cumprod)

    # Variation: Axis
    arr_2d = np.array([[1, 2], [3, 4]])
    cumprod_axis = np.cumprod(arr_2d, axis=0)
    print(cumprod_axis)

    # Edge case: With 1
    cumprod_one = np.cumprod([1, 1, 1])
    print(cumprod_one)
    ```
    **Explanation**: Running product.  
    **Output**:
    ```
    [ 2  6 24]
    [[ 1  2]
     [ 3  8]]
    [1 1 1]
    ```

- `np.percentile(a, q, axis=None)`: Compute the q-th percentile of the data along the specified axis.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Percentile.
    arr = np.array([1, 2, 3, 4, 5])
    perc = np.percentile(arr, 50)
    print(perc)

    # Variation: Multiple q
    perc_multi = np.percentile(arr, [25, 75])
    print(perc_multi)

    # Edge case: Axis in 2D
    arr_2d = np.array([[1, 2], [3, 4]])
    perc_axis = np.percentile(arr_2d, 50, axis=1)
    print(perc_axis)
    ```
    **Explanation**: Quantile calculation.  
    **Output**:
    ```
    3.0
    [2. 4.]
    [1.5 3.5]
    ```

- `np.nanmean(a, axis=None)`: Mean, ignoring NaNs.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Nanmean.
    arr = np.array([1, np.nan, 3])
    nanmean = np.nanmean(arr)
    print(nanmean)

    # Variation: 2D
    arr_2d = np.array([[1, np.nan], [3, 4]])
    nanmean_axis = np.nanmean(arr_2d, axis=0)
    print(nanmean_axis)

    # Edge case: All nan
    all_nan = np.nanmean([np.nan, np.nan])
    print(all_nan)
    ```
    **Explanation**: Handles missing data.  
    **Output**:
    ```
    2.0
    [2. 4.]
    nan
    ```

- `np.nanstd(a, axis=None)`: Standard deviation, ignoring NaNs.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Nanstd.
    arr = np.array([1, np.nan, 3])
    nanstd = np.nanstd(arr)
    print(nanstd)

    # Variation: ddof
    nanstd_sample = np.nanstd(arr, ddof=1)
    print(nanstd_sample)

    # Edge case: Single non-nan
    single = np.nanstd([np.nan, 2, np.nan])
    print(single)
    ```
    **Explanation**: Std with nans skipped.  
    **Output**:
    ```
    1.0
    1.4142135623730951
    0.0
    ```

- `np.nanvar(a, axis=None)`: Variance, ignoring NaNs.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Nanvar.
    arr = np.array([1, np.nan, 3])
    nanvar = np.nanvar(arr)
    print(nanvar)

    # Variation: Axis
    arr_2d = np.array([[1, np.nan], [3, 4]])
    nanvar_axis = np.nanvar(arr_2d, axis=1)
    print(nanvar_axis)

    # Edge case: No valid
    no_valid = np.nanvar([np.nan])
    print(no_valid)
    ```
    **Explanation**: Var with nans.  
    **Output**:
    ```
    1.0
    [0. 0.25]
    nan
    ```

- `np.nanmin(a, axis=None)`: Minimum, ignoring NaNs.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Nanmin.
    arr = np.array([1, np.nan, -3])
    nanmin = np.nanmin(arr)
    print(nanmin)

    # Variation: 2D
    arr_2d = np.array([[np.nan, 2], [3, np.nan]])
    nanmin_axis = np.nanmin(arr_2d, axis=0)
    print(nanmin_axis)

    # Edge case: All nan
    all_nan = np.nanmin([np.nan, np.nan])
    print(all_nan)
    ```
    **Explanation**: Min skipping nans.  
    **Output**:
    ```
    -3.0
    [3. 2.]
    nan
    ```

- `np.nanmax(a, axis=None)`: Maximum, ignoring NaNs.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Nanmax.
    arr = np.array([1, np.nan, 3])
    nanmax = np.nanmax(arr)
    print(nanmax)

    # Variation: Axis
    arr_2d = np.array([[1, np.nan], [3, 4]])
    nanmax_axis = np.nanmax(arr_2d, axis=1)
    print(nanmax_axis)

    # Edge case: Inf and nan
    inf_nan = np.nanmax([np.inf, np.nan])
    print(inf_nan)
    ```
    **Explanation**: Max skipping nans.  
    **Output**:
    ```
    3.0
    [1. 4.]
    inf
    ```

- `np.nansum(a, axis=None)`: Sum, ignoring NaNs.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Nansum.
    arr = np.array([1, np.nan, 3])
    nansum = np.nansum(arr)
    print(nansum)

    # Variation: Axis
    arr_2d = np.array([[1, np.nan], [3, 4]])
    nansum_axis = np.nansum(arr_2d, axis=0)
    print(nansum_axis)

    # Edge case: All nan = 0
    all_nan = np.nansum([np.nan, np.nan])
    print(all_nan)
    ```
    **Explanation**: Sum treating nan as 0.  
    **Output**:
    ```
    4.0
    [4. 4.]
    0.0
    ```

### Methods
- `ndarray.mean(axis=None, dtype=None)`: Compute the arithmetic mean.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Method mean.
    arr = np.array([1, 2, 3])
    mean = arr.mean()
    print(mean)

    # Variation: Axis
    arr_2d = np.array([[1, 2], [3, 4]])
    mean_axis = arr_2d.mean(axis=0)
    print(mean_axis)

    # Edge case: Dtype
    mean_dtype = arr.mean(dtype=float)
    print(mean_dtype)
    ```
    **Explanation**: Array mean.  
    **Output**:
    ```
    2.0
    [2. 3.]
    2.0
    ```

- `ndarray.std(axis=None, dtype=None)`: Compute the standard deviation.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Method std.
    arr = np.array([1, 2, 3])
    std = arr.std()
    print(std)

    # Variation: ddof
    std_sample = arr.std(ddof=1)
    print(std_sample)

    # Edge case: 2D
    arr_2d = np.array([[1, 2], [3, 4]])
    std_axis = arr_2d.std(axis=1)
    print(std_axis)
    ```
    **Explanation**: Array std.  
    **Output**:
    ```
    0.816496580927726
    1.0
    [0.5 0.5]
    ```

- `ndarray.var(axis=None, dtype=None)`: Compute the variance.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Method var.
    arr = np.array([1, 2, 3])
    var = arr.var()
    print(var)

    # Variation: ddof
    var_sample = arr.var(ddof=1)
    print(var_sample)

    # Edge case: Zero var
    zero_var = np.array([5, 5]).var()
    print(zero_var)
    ```
    **Explanation**: Array var.  
    **Output**:
    ```
    0.6666666666666666
    1.0
    0.0
    ```

- `ndarray.min(axis=None)`: Return the minimum.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Method min.
    arr = np.array([3, 1, 2])
    min_val = arr.min()
    print(min_val)

    # Variation: Axis
    arr_2d = np.array([[3, 1], [4, 2]])
    min_axis = arr_2d.min(axis=0)
    print(min_axis)

    # Edge case: Nan
    arr_nan = np.array([1, np.nan])
    min_nan = arr_nan.min()
    print(min_nan)
    ```
    **Explanation**: Array min.  
    **Output**:
    ```
    1
    [3 1]
    nan
    ```

- `ndarray.max(axis=None)`: Return the maximum.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Method max.
    arr = np.array([1, 3, 2])
    max_val = arr.max()
    print(max_val)

    # Variation: Axis
    arr_2d = np.array([[1, 3], [2, 4]])
    max_axis = arr_2d.max(axis=1)
    print(max_axis)

    # Edge case: Inf
    arr_inf = np.array([1, np.inf])
    max_inf = arr_inf.max()
    print(max_inf)
    ```
    **Explanation**: Array max.  
    **Output**:
    ```
    3
    [3 4]
    inf
    ```

- `ndarray.sum(axis=None, dtype=None)`: Sum of array elements.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Method sum.
    arr = np.array([1, 2, 3])
    summed = arr.sum()
    print(summed)

    # Variation: Dtype
    summed_dtype = arr.sum(dtype=float)
    print(summed_dtype)

    # Edge case: Overflow
    large = np.array([2**7 -1], dtype=np.int8)
    sum_large = large.sum()
    print(sum_large)
    ```
    **Explanation**: Array sum.  
    **Output**:
    ```
    6
    6.0
    127
    ```

- `ndarray.prod(axis=None, dtype=None)`: Product of array elements.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Method prod.
    arr = np.array([2, 3])
    proded = arr.prod()
    print(proded)

    # Variation: Axis
    arr_2d = np.array([[2, 3], [4, 5]])
    prod_axis = arr_2d.prod(axis=0)
    print(prod_axis)

    # Edge case: Empty prod = 1
    empty_prod = np.array([]).prod()
    print(empty_prod)
    ```
    **Explanation**: Array product. Empty is 1.  
    **Output**:
    ```
    6
    [ 8 15]
    1.0
    ```

- `ndarray.cumsum(axis=None, dtype=None)`: Cumulative sum.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Method cumsum.
    arr = np.array([1, 2, 3])
    cum = arr.cumsum()
    print(cum)

    # Variation: Dtype
    cum_dtype = arr.cumsum(dtype=float)
    print(cum_dtype)

    # Edge case: 2D axis
    arr_2d = np.array([[1, 2], [3, 4]])
    cum_axis = arr_2d.cumsum(axis=0)
    print(cum_axis)
    ```
    **Explanation**: Array cumsum.  
    **Output**:
    ```
    [1 3 6]
    [1. 3. 6.]
    [[1 2]
     [4 6]]
    ```

- `ndarray.cumprod(axis=None, dtype=None)`: Cumulative product.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Method cumprod.
    arr = np.array([1, 2, 3])
    cumprod = arr.cumprod()
    print(cumprod)

    # Variation: Axis
    arr_2d = np.array([[1, 2], [3, 4]])
    cumprod_axis = arr_2d.cumprod(axis=1)
    print(cumprod_axis)

    # Edge case: With zero
    cum_zero = np.array([1, 0, 2]).cumprod()
    print(cum_zero)
    ```
    **Explanation**: Array cumprod.  
    **Output**:
    ```
    [1 2 6]
    [[ 1  2]
     [ 3 12]]
    [1 0 0]
    ```

## 5. Linear Algebra
Functions for linear algebra operations.

### Functions
- `np.dot(a, b)`: Dot product of two arrays.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Vector dot.
    a = np.array([1, 2])
    b = np.array([3, 4])
    dotted = np.dot(a, b)
    print(dotted)

    # Variation: Matrix mul
    mat1 = np.array([[1, 2], [3, 4]])
    mat2 = np.array([[5, 6], [7, 8]])
    dot_mat = np.dot(mat1, mat2)
    print(dot_mat)

    # Edge case: Scalar * array
    dot_scalar = np.dot(2, a)
    print(dot_scalar)
    ```
    **Explanation**: General dot, matrix mul for 2D.  
    **Output**:
    ```
    11
    [[19 22]
     [43 50]]
    [2 4]
    ```

- `np.vdot(a, b)`: Dot product of two vectors (complex conjugate for complex numbers).
  - **In-depth Example**:
    ```python
    import numpy as np

    # Vdot for reals.
    a = np.array([1, 2])
    b = np.array([3, 4])
    vdotted = np.vdot(a, b)
    print(vdotted)

    # Variation: Complex with conjugate
    a_complex = np.array([1+1j, 2+2j])
    b_complex = np.array([3+3j, 4+4j])
    vdot_complex = np.vdot(a_complex, b_complex)
    print(vdot_complex)

    # Edge case: 1D only
    try:
        np.vdot(np.array([[1]]), np.array([[2]]))
    except ValueError as e:
        print("Error:", e)
    ```
    **Explanation**: Vector dot with conjugate.  
    **Output**:
    ```
    11
    (30-0j)
    Error: vdot only works for 1-D arrays
    ```

- `np.cross(a, b, axisa=-1, axisb=-1, axisc=-1, axis=None)`: Cross product of two vectors.
  - **In-depth Example**:
    ```python
    import numpy as np

    # 3D cross.
    a = np.array([1, 0, 0])
    b = np.array([0, 1, 0])
    crossed = np.cross(a, b)
    print(crossed)

    # Variation: 2D (returns scalar)
    a2d = np.array([1, 2])
    b2d = np.array([3, 4])
    cross_2d = np.cross(a2d, b2d)
    print(cross_2d)

    # Edge case: Parallel vectors (zero)
    cross_parallel = np.cross([1, 0], [2, 0])
    print(cross_parallel)
    ```
    **Explanation**: Vector cross. Scalar for 2D.  
    **Output**:
    ```
    [0 0 1]
    -2
    0
    ```

- `np.matmul(a, b)`: Matrix product of two arrays.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Matrix mul.
    mat1 = np.array([[1, 2], [3, 4]])
    mat2 = np.array([[5, 6], [7, 8]])
    matmulled = np.matmul(mat1, mat2)
    print(matmulled)

    # Variation: Vector mat
    vec = np.array([1, 2])
    matmul_vec = np.matmul(mat1, vec)
    print(matmul_vec)

    # Edge case: Broadcasting in higher dims
    mat3d = np.array([[[1, 2]]])
    matmul_3d = np.matmul(mat3d, mat2.T)
    print(matmul_3d.shape)
    ```
    **Explanation**: Preferred for matrix mul, supports stacking.  
    **Output**:
    ```
    [[19 22]
     [43 50]]
    [ 5 11]
    (1, 1, 2)
    ```

- `np.linalg.inv(a)`: Compute the inverse of a square matrix.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Inverse.
    mat = np.array([[1, 2], [3, 4]])
    inv = np.linalg.inv(mat)
    print(inv)

    # Variation: Check identity
    identity_check = np.dot(mat, inv)
    print(np.round(identity_check, decimals=10))

    # Edge case: Singular matrix error
    singular = np.array([[1, 2], [2, 4]])
    try:
        np.linalg.inv(singular)
    except np.linalg.LinAlgError as e:
        print("Error:", e)
    ```
    **Explanation**: Matrix inverse. Checks singularity.  
    **Output**:
    ```
    [[-2.   1. ]
     [ 1.5 -0.5]]
    [[1. 0.]
     [0. 1.]]
    Error: Singular matrix
    ```

- `np.linalg.det(a)`: Compute the determinant of an array.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Determinant.
    mat = np.array([[1, 2], [3, 4]])
    det = np.linalg.det(mat)
    print(det)

    # Variation: 3x3
    mat3 = np.array([[1, 2, 3], [0, 1, 4], [5, 6, 0]])
    det3 = np.linalg.det(mat3)
    print(det3)

    # Edge case: Singular (0)
    singular = np.array([[1, 2], [2, 4]])
    det_sing = np.linalg.det(singular)
    print(det_sing)
    ```
    **Explanation**: Det for invertibility.  
    **Output**:
    ```
    -2.0000000000000004
    1.0
    0.0
    ```

- `np.linalg.eig(a)`: Compute the eigenvalues and eigenvectors of a square array.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Eig.
    mat = np.array([[1, 2], [3, 4]])
    eigenvalues, eigenvectors = np.linalg.eig(mat)
    print("Eigenvalues:", eigenvalues)
    print("Eigenvectors:", eigenvectors)

    # Variation: Verify A v = lambda v
    for i in range(len(eigenvalues)):
        lhs = np.dot(mat, eigenvectors[:, i])
        rhs = eigenvalues[i] * eigenvectors[:, i]
        print(np.allclose(lhs, rhs))

    # Edge case: Complex eig
    mat_complex = np.array([[0, -1], [1, 0]])
    eig_complex = np.linalg.eig(mat_complex)
    print(eig_complex[0])
    ```
    **Explanation**: Decomposition for dynamics.  
    **Output**:
    ```
    Eigenvalues: [-0.37228132  5.37228132]
    Eigenvectors: [[-0.82456484 -0.41597356]
     [ 0.56576746 -0.90937671]]
    True
    True
    [0.+1.j 0.-1.j]
    ```

- `np.linalg.svd(a, full_matrices=True)`: Singular Value Decomposition.
  - **In-depth Example**:
    ```python
    import numpy as np

    # SVD.
    mat = np.array([[1, 2], [3, 4], [5, 6]])
    U, S, Vh = np.linalg.svd(mat, full_matrices=False)
    print("U:", U)
    print("S:", S)
    print("Vh:", Vh)

    # Variation: Reconstruct
    reconstructed = np.dot(U, np.dot(np.diag(S), Vh))
    print(np.allclose(mat, reconstructed))

    # Edge case: Square matrix
    square = np.array([[1, 2], [3, 4]])
    svd_square = np.linalg.svd(square)
    print(svd_square[1])
    ```
    **Explanation**: Factorization for PCA etc.  
    **Output**: (Approximate)
    ```
    U: [[-0.229... -0.883...]
     [-0.525... -0.240...]
     [-0.820...  0.401...]]
    S: [9.525... 0.514...]
    Vh: [[-0.619... -0.784...]
     [ 0.784... -0.619...]]
    True
    [5.4649857  0.36596619]
    ```

- `np.linalg.solve(a, b)`: Solve a linear matrix equation (Ax = b).
  - **In-depth Example**:
    ```python
    import numpy as np

    # Solve system.
    A = np.array([[1, 2], [3, 4]])
    b = np.array([5, 6])
    x = np.linalg.solve(A, b)
    print(x)

    # Variation: Check
    check = np.dot(A, x)
    print(np.allclose(check, b))

    # Edge case: Underdetermined error
    under = np.array([[1, 1]])
    try:
        np.linalg.solve(under, [1])
    except np.linalg.LinAlgError as e:
        print("Error:", e)
    ```
    **Explanation**: Solves linear systems.  
    **Output**:
    ```
    [-4.   4.5]
    True
    Error: Arrays must be square.
    ```

- `np.linalg.lstsq(a, b, rcond=None)`: Return the least-squares solution to a linear matrix equation.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Least squares.
    A = np.array([[1, 1], [1, 2], [1, 3]])
    b = np.array([1, 2, 2])
    x, residuals, rank, s = np.linalg.lstsq(A, b, rcond=None)
    print("x:", x)
    print("Residuals:", residuals)

    # Variation: Overdetermined
    print("Rank:", rank)

    # Edge case: Underdetermined
    under = np.array([[1, 2]])
    under_sol = np.linalg.lstsq(under, [3], rcond=None)
    print(under_sol[0])
    ```
    **Explanation**: For non-square systems.  
    **Output**:
    ```
    x: [0.66666667 0.5       ]
    Residuals: [0.16666667]
    Rank: 2
    [1.5 0. ]
    ```

- `np.trace(a, offset=0, axis1=0, axis2=1)`: Return the sum along diagonals of the array.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Trace.
    mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    trace = np.trace(mat)
    print(trace)

    # Variation: Offset
    trace_offset = np.trace(mat, offset=1)
    print(trace_offset)

    # Edge case: Non-square
    non_square = np.array([[1, 2], [3, 4], [5, 6]])
    trace_non = np.trace(non_square)
    print(trace_non)
    ```
    **Explanation**: Diagonal sum.  
    **Output**:
    ```
    15
    11
    5
    ```

## 6. Indexing and Slicing
Functions and methods for indexing, slicing, and boolean operations.

### Functions
- `np.where(condition, x, y)`: Return elements chosen from `x` or `y` depending on `condition`.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Where for conditional.
    a = np.array([1, 2, 3, 4])
    cond = a > 2
    whered = np.where(cond, a, 0)
    print(whered)

    # Variation: Only indices
    indices = np.where(cond)
    print(indices)

    # Edge case: All false
    all_false = np.where(a > 10, 1, 2)
    print(all_false)
    ```
    **Explanation**: Ternary-like for arrays.  
    **Output**:
    ```
    [0 0 3 4]
    (array([2, 3]),)
    [2 2 2 2]
    ```

- `np.nonzero(a)`: Return the indices of the non-zero elements.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Nonzero indices.
    arr = np.array([0, 1, 0, 2])
    nz = np.nonzero(arr)
    print(nz)

    # Variation: 2D
    arr_2d = np.array([[0, 1], [2, 0]])
    nz_2d = np.nonzero(arr_2d)
    print(nz_2d)

    # Edge case: All zero
    all_zero = np.nonzero([0, 0])
    print(all_zero)
    ```
    **Explanation**: Finds non-zeros. Tuple of arrays.  
    **Output**:
    ```
    (array([1, 3]),)
    (array([0, 1]), array([1, 0]))
    (array([], dtype=int64),)
    ```

- `np.argwhere(a)`: Find the indices of array elements that are non-zero, grouped by element.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Argwhere.
    arr = np.array([0, 1, 0, 2])
    aw = np.argwhere(arr)
    print(aw)

    # Variation: Condition
    aw_cond = np.argwhere(arr > 1)
    print(aw_cond)

    # Edge case: 2D
    arr_2d = np.array([[0, 1], [2, 0]])
    aw_2d = np.argwhere(arr_2d)
    print(aw_2d)
    ```
    **Explanation**: Indices as array rows.  
    **Output**:
    ```
    [[1]
     [3]]
    [[3]]
    [[0 1]
     [1 0]]
    ```

- `np.take(a, indices, axis=None)`: Take elements from an array along an axis.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Take by indices.
    arr = np.array([10, 20, 30, 40])
    taken = np.take(arr, [0, 2])
    print(taken)

    # Variation: Axis in 2D
    arr_2d = np.array([[1, 2], [3, 4]])
    take_axis = np.take(arr_2d, [0], axis=1)
    print(take_axis)

    # Edge case: Out of bounds mode
    take_out = np.take(arr, 5, mode='clip')
    print(take_out)
    ```
    **Explanation**: Fancy indexing alternative.  
    **Output**:
    ```
    [10 30]
    [[1]
     [3]]
    40
    ```

- `np.choose(a, choices, mode='raise')`: Construct an array from an index array and a list of arrays.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Choose from choices.
    indices = np.array([0, 1, 2, 1])
    choices = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
    chosen = np.choose(indices, choices)
    print(chosen)

    # Variation: Mode 'clip'
    indices_clip = np.array([ -1, 3])
    chosen_clip = np.choose(indices_clip, [1, 2, 3], mode='clip')
    print(chosen_clip)

    # Edge case: Mode 'wrap'
    chosen_wrap = np.choose(indices_clip, [1, 2, 3], mode='wrap')
    print(chosen_wrap)
    ```
    **Explanation**: Selects from list by index array.  
    **Output**:
    ```
    [10 50 90 50]
    [1 3]
    [3 1]
    ```

- `np.select(condlist, choicelist, default=0)`: Return an array drawn from elements in choicelist based on conditions.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Select multi-cond.
    a = np.array([1, 2, 3, 4])
    conds = [a < 2, a > 3]
    choices = [10, 20]
    selected = np.select(conds, choices, default=0)
    print(selected)

    # Variation: Overlapping conds (first wins)
    conds_over = [a > 1, a > 2]
    selected_over = np.select(conds_over, [5, 6])
    print(selected_over)

    # Edge case: No match
    no_match = np.select([a > 10], [99], default=-1)
    print(no_match)
    ```
    **Explanation**: Multi-conditional assignment.  
    **Output**:
    ```
    [10  0  0 20]
    [0 5 5 5]
    [-1 -1 -1 -1]
    ```

### Methods
- `ndarray.take(indices, axis=None)`: Take elements from the array along an axis.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Method take.
    arr = np.array([10, 20, 30])
    taken = arr.take([0, 2])
    print(taken)

    # Variation: Axis
    arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
    take_axis = arr_2d.take([0, 2], axis=1)
    print(take_axis)

    # Edge case: Mode 'raise' error
    try:
        arr.take(3)
    except IndexError as e:
        print("Error:", e)
    ```
    **Explanation**: Array method for take.  
    **Output**:
    ```
    [10 30]
    [[1 3]
     [4 6]]
    Error: index 3 is out of bounds for axis 0 with size 3
    ```

- `ndarray.nonzero()`: Return the indices of the non-zero elements.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Method nonzero.
    arr = np.array([0, 1, 0, 2])
    nz = arr.nonzero()
    print(nz)

    # Variation: Use to index
    values = arr[nz]
    print(values)

    # Edge case: Empty
    empty_nz = np.array([0, 0]).nonzero()
    print(empty_nz)
    ```
    **Explanation**: Array method.  
    **Output**:
    ```
    (array([1, 3]),)
    [1 2]
    (array([], dtype=int64),)
    ```

## 7. Random Number Generation
Functions from the `np.random` module for generating random numbers.

- `np.random.rand(d0, d1, ..., dn)`: Random values in a given shape (uniform [0, 1)).
  - **In-depth Example**:
    ```python
    import numpy as np

    # Uniform random.
    rand_arr = np.random.rand(2, 3)
    print(rand_arr)  # Random output

    # Variation: Seed for reproducibility
    np.random.seed(42)
    rand_seeded = np.random.rand(2)
    print(rand_seeded)

    # Edge case: Scalar (0D)
    rand_scalar = np.random.rand()
    print(rand_scalar)
    ```
    **Explanation**: Uniform random. Shows seeding.  
    **Output**: (Example)
    ```
    [[0.37454012 0.95071431 0.73199394]
     [0.59865848 0.15601864 0.15599452]]
    [0.37454012 0.95071431]
    0.05808361216819946
    ```

- `np.random.randn(d0, d1, ..., dn)`: Random values from a standard normal distribution.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Normal random.
    np.random.seed(42)
    randn_arr = np.random.randn(3)
    print(randn_arr)

    # Variation: 2D
    randn_2d = np.random.randn(2, 2)
    print(randn_2d)

    # Edge case: Mean and std check
    large = np.random.randn(10000)
    print(np.mean(large), np.std(large))  # Approx 0, 1
    ```
    **Explanation**: Gaussian.  
    **Output**: (Seeded)
    ```
    [ 0.49671415 -0.1382643   0.64768854]
    [[ 1.52302986 -0.23415337]
     [-0.23413696  1.57921282]]
    0.00... 1.00...
    ```

- `np.random.randint(low, high=None, size=None, dtype=int)`: Random integers from low (inclusive) to high (exclusive).
  - **In-depth Example**:
    ```python
    import numpy as np

    # Int random.
    np.random.seed(42)
    randint_arr = np.random.randint(1, 10, size=5)
    print(randint_arr)

    # Variation: No high (from 0)
    randint_low = np.random.randint(5, size=3)
    print(randint_low)

    # Edge case: Single value
    randint_single = np.random.randint(1, 2)
    print(randint_single)
    ```
    **Explanation**: Discrete uniform.  
    **Output**:
    ```
    [7 4 6 4 4]
    [3 1 4]
    1
    ```

- `np.random.choice(a, size=None, replace=True, p=None)`: Generates a random sample from a given 1-D array.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Choice from array.
    items = np.array(['a', 'b', 'c'])
    chosen = np.random.choice(items, size=3)
    print(chosen)  # Random

    # Variation: No replace
    chosen_norep = np.random.choice(items, size=3, replace=False)
    print(chosen_norep)

    # Edge case: With probabilities
    p = [0.1, 0.3, 0.6]
    chosen_p = np.random.choice(items, p=p)
    print(chosen_p)
    ```
    **Explanation**: Sampling.  
    **Output**: (Example)
    ```
    ['c' 'a' 'b']
    ['b' 'c' 'a']
    'c'
    ```

- `np.random.shuffle(x)`: Modify a sequence in-place by shuffling its contents.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Shuffle in-place.
    arr = np.array([1, 2, 3, 4])
    np.random.seed(42)
    np.random.shuffle(arr)
    print(arr)

    # Variation: 2D (shuffles rows)
    arr_2d = np.array([[1, 2], [3, 4], [5, 6]])
    np.random.shuffle(arr_2d)
    print(arr_2d)

    # Edge case: 1 element no change
    single = np.array([10])
    np.random.shuffle(single)
    print(single)
    ```
    **Explanation**: Random permutation in-place.  
    **Output**:
    ```
    [2 4 3 1]
    [[5 6]
     [1 2]
     [3 4]]
    [10]
    ```

- `np.random.permutation(x)`: Return a permuted sequence or array.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Permutation copy.
    arr = np.array([1, 2, 3])
    np.random.seed(42)
    perm = np.random.permutation(arr)
    print(perm)

    # Variation: Integer (range)
    perm_int = np.random.permutation(5)
    print(perm_int)

    # Edge case: Scalar error
    try:
        np.random.permutation(1.5)
    except ValueError as e:
        print("Error:", e)
    ```
    **Explanation**: Shuffled copy.  
    **Output**:
    ```
    [2 3 1]
    [4 1 3 2 0]
    Error: non-integer arg 1 for randrange()
    ```

- `np.random.normal(loc=0.0, scale=1.0, size=None)`: Draw samples from a normal (Gaussian) distribution.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Normal with mean/std.
    np.random.seed(42)
    norm = np.random.normal(5, 2, size=3)
    print(norm)

    # Variation: Scalar
    norm_scalar = np.random.normal()
    print(norm_scalar)

    # Edge case: Negative scale error
    try:
        np.random.normal(scale=-1)
    except ValueError as e:
        print("Error:", e)
    ```
    **Explanation**: General Gaussian.  
    **Output**:
    ```
    [5.99342831 4.7234714  6.29537708]
    0.4967141530112327
    Error: scale < 0
    ```

- `np.random.uniform(low=0.0, high=1.0, size=None)`: Draw samples from a uniform distribution.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Uniform range.
    np.random.seed(42)
    uni = np.random.uniform(10, 20, size=3)
    print(uni)

    # Variation: Size tuple
    uni_2d = np.random.uniform(size=(2, 2))
    print(uni_2d)

    # Edge case: Low > high error
    try:
        np.random.uniform(2, 1)
    except ValueError as e:
        print("Error:", e)
    ```
    **Explanation**: General uniform.  
    **Output**:
    ```
    [13.74540119 19.50714306 17.31993942]
    [[0.59865848 0.15601864]
     [0.15599452 0.05808361]]
    Error: low >= high
    ```

- `np.random.seed(seed=None)`: Seed the random number generator.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Seed for repro.
    np.random.seed(42)
    r1 = np.random.rand(2)
    np.random.seed(42)
    r2 = np.random.rand(2)
    print(r1, r2)  # Same

    # Variation: None for random seed
    np.random.seed(None)
    r_none = np.random.rand()

    # Edge case: Large seed
    np.random.seed(2**32 - 1)
    r_large = np.random.rand()
    print(r_large)
    ```
    **Explanation**: For deterministic random.  
    **Output**:
    ```
    [0.37454012 0.95071431] [0.37454012 0.95071431]
    0.7319939418114051
    ```

## 8. Sorting and Searching
Functions and methods for sorting and searching arrays.

### Functions
- `np.sort(a, axis=-1, kind='quicksort', order=None)`: Return a sorted copy of an array.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Sort copy.
    arr = np.array([3, 1, 2])
    sorted_arr = np.sort(arr)
    print(sorted_arr)

    # Variation: Kind 'mergesort'
    sorted_merge = np.sort(arr, kind='mergesort')
    print(sorted_merge)

    # Edge case: 2D axis=None (flatten)
    arr_2d = np.array([[3, 1], [4, 2]])
    sorted_flat = np.sort(arr_2d, axis=None)
    print(sorted_flat)
    ```
    **Explanation**: Sorted copy. Different algorithms.  
    **Output**:
    ```
    [1 2 3]
    [1 2 3]
    [1 2 3 4]
    ```

- `np.argsort(a, axis=-1, kind='quicksort', order=None)`: Return the indices that would sort an array.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Argsort.
    arr = np.array([3, 1, 2])
    indices = np.argsort(arr)
    print(indices)

    # Variation: Use to sort
    sorted_via_arg = arr[indices]
    print(sorted_via_arg)

    # Edge case: Stable sort with mergesort
    arr_dup = np.array([3, 1, 3])
    args_merge = np.argsort(arr_dup, kind='mergesort')
    print(args_merge)
    ```
    **Explanation**: Indices for indirect sort.  
    **Output**:
    ```
    [1 2 0]
    [1 2 3]
    [1 0 2]
    ```

- `np.argmax(a, axis=None)`: Return the indices of the maximum values along an axis.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Argmax.
    arr = np.array([1, 3, 2])
    argmax = np.argmax(arr)
    print(argmax)

    # Variation: Axis
    arr_2d = np.array([[1, 4], [2, 3]])
    argmax_axis = np.argmax(arr_2d, axis=0)
    print(argmax_axis)

    # Edge case: All equal (first)
    all_eq = np.argmax([5, 5, 5])
    print(all_eq)
    ```
    **Explanation**: Index of max.  
    **Output**:
    ```
    1
    [1 0]
    0
    ```

- `np.argmin(a, axis=None)`: Return the indices of the minimum values along an axis.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Argmin.
    arr = np.array([3, 1, 2])
    argmin = np.argmin(arr)
    print(argmin)

    # Variation: Axis
    arr_2d = np.array([[4, 1], [3, 2]])
    argmin_axis = np.argmin(arr_2d, axis=1)
    print(argmin_axis)

    # Edge case: Nan (nan argmin nan)
    arr_nan = np.array([1, np.nan, 0])
    argmin_nan = np.argmin(arr_nan)
    print(argmin_nan)
    ```
    **Explanation**: Index of min.  
    **Output**:
    ```
    1
    [1 1]
    2
    ```

- `np.searchsorted(a, v, side='left', sorter=None)`: Find indices where elements should be inserted to maintain order.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Searchsorted.
    arr = np.array([1, 3, 5, 7])
    idx = np.searchsorted(arr, 4)
    print(idx)

    # Variation: Multiple v
    idx_multi = np.searchsorted(arr, [0, 4, 8])
    print(idx_multi)

    # Edge case: Side 'right'
    idx_right = np.searchsorted(arr, 3, side='right')
    print(idx_right)
    ```
    **Explanation**: For sorted arrays, insertion point.  
    **Output**:
    ```
    2
    [0 2 4]
    2
    ```

### Methods
- `ndarray.sort(axis=-1, kind='quicksort', order=None)`: Sort the array in-place.
  - **In-depth Example**:
    ```python
    import numpy as np

    # In-place sort.
    arr = np.array([3, 1, 2])
    arr.sort()
    print(arr)

    # Variation: Axis
    arr_2d = np.array([[3, 1], [4, 2]])
    arr_2d.sort(axis=0)
    print(arr_2d)

    # Edge case: Already sorted
    sorted_arr = np.array([1, 2, 3])
    sorted_arr.sort()
    print(sorted_arr)
    ```
    **Explanation**: Modifies array.  
    **Output**:
    ```
    [1 2 3]
    [[3 1]
     [4 2]]
    [1 2 3]
    ```

- `ndarray.argsort(axis=-1, kind='quicksort', order=None)`: Return the indices that would sort the array.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Method argsort.
    arr = np.array([3, 1, 2])
    indices = arr.argsort()
    print(indices)

    # Variation: Stable
    arr_dup = np.array([3, 1, 3])
    indices_stable = arr_dup.argsort(kind='stable')
    print(indices_stable)

    # Edge case: Axis None flatten
    arr_2d = np.array([[3, 1]])
    indices_flat = arr_2d.argsort(axis=None)
    print(indices_flat)
    ```
    **Explanation**: Array method.  
    **Output**:
    ```
    [1 2 0]
    [1 0 2]
    [1 0]
    ```

- `ndarray.argmax(axis=None)`: Return the indices of the maximum values.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Method argmax.
    arr = np.array([1, 3, 2])
    amax = arr.argmax()
    print(amax)

    # Variation: Axis
    arr_2d = np.array([[1, 3], [2, 4]])
    amax_axis = arr_2d.argmax(axis=1)
    print(amax_axis)

    # Edge case: Flat argmax
    arr_flat = arr.argmax(axis=None)
    print(arr_flat)
    ```
    **Explanation**: Array method.  
    **Output**:
    ```
    1
    [1 1]
    1
    ```

- `ndarray.argmin(axis=None)`: Return the indices of the minimum values.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Method argmin.
    arr = np.array([3, 1, 2])
    amin = arr.argmin()
    print(amin)

    # Variation: Axis
    arr_2d = np.array([[3, 1], [4, 2]])
    amin_axis = arr_2d.argmin(axis=0)
    print(amin_axis)

    # Edge case: With ties (first)
    ties = np.array([1, 1, 2])
    amin_ties = ties.argmin()
    print(amin_ties)
    ```
    **Explanation**: Array method.  
    **Output**:
    ```
    1
    [0 0]
    0
    ```

## 9. Input/Output
Functions for reading and writing arrays to/from files.

- `np.save(file, arr)`: Save an array to a binary file in NumPy `.npy` format.
  - **In-depth Example**:
    ```python
    import numpy as np
    import os

    # Save to file.
    arr = np.array([1, 2, 3])
    np.save('test.npy', arr)

    # Variation: Load back
    loaded = np.load('test.npy')
    print(loaded)

    # Edge case: Allow pickle for objects
    obj_arr = np.array([object()], dtype=object)
    np.save('obj.npy', obj_arr, allow_pickle=True)
    loaded_obj = np.load('obj.npy', allow_pickle=True)
    print(type(loaded_obj[0]))

    # Clean up
    os.remove('test.npy')
    os.remove('obj.npy')
    ```
    **Explanation**: Binary save/load. Shows pickle for objects.  
    **Output**:
    ```
    [1 2 3]
    <class 'object'>
    ```

- `np.savez(file, *args, **kwds)`: Save several arrays into a single file in `.npz` format.
  - **In-depth Example**:
    ```python
    import numpy as np
    import os

    # Save multiple.
    a1 = np.array([1, 2])
    a2 = np.array([3, 4])
    np.savez('multi.npz', a=a1, b=a2)

    # Variation: Load as dict
    data = np.load('multi.npz')
    print(data['a'])
    print(data['b'])

    # Edge case: Compressed
    np.savez_compressed('multi_comp.npz', a=a1)
    data_comp = np.load('multi_comp.npz')
    print(data_comp['a'])

    # Clean up
    os.remove('multi.npz')
    os.remove('multi_comp.npz')
    ```
    **Explanation**: Archive multiple arrays.  
    **Output**:
    ```
    [1 2]
    [3 4]
    [1 2]
    ```

- `np.load(file, mmap_mode=None)`: Load arrays or pickled objects from `.npy` or `.npz` files.
  - **In-depth Example**:
    ```python
    import numpy as np
    import os

    # Save and load.
    arr = np.array([1, 2])
    np.save('load_test.npy', arr)
    loaded = np.load('load_test.npy')
    print(loaded)

    # Variation: Mmap for large files
    large = np.arange(1000000)
    np.save('large.npy', large)
    mmapped = np.load('large.npy', mmap_mode='r')
    print(mmapped[0])

    # Edge case: From npz
    np.savez('test.npz', arr=arr)
    data = np.load('test.npz')
    print(data['arr'])

    # Clean up
    os.remove('load_test.npy')
    os.remove('large.npy')
    os.remove('test.npz')
    ```
    **Explanation**: Load, with mmap for memory efficiency.  
    **Output**:
    ```
    [1 2]
    0
    [1 2]
    ```

- `np.savetxt(fname, X, fmt='%.18e', delimiter=' ')`: Save an array to a text file.
  - **In-depth Example**:
    ```python
    import numpy as np
    import os

    # Save text.
    arr = np.array([[1, 2], [3, 4]])
    np.savetxt('text.txt', arr, fmt='%d', delimiter=',')

    # Variation: Load back
    loaded = np.loadtxt('text.txt', delimiter=',')
    print(loaded)

    # Edge case: Header
    np.savetxt('header.txt', arr, header='Col1 Col2')
    with open('header.txt') as f:
        print(f.readline().strip())

    # Clean up
    os.remove('text.txt')
    os.remove('header.txt')
    ```
    **Explanation**: Text save.  
    **Output**:
    ```
    [[1. 2.]
     [3. 4.]]
    # Col1 Col2
    ```

## 10. Miscellaneous
Other useful functions and methods.

### Functions
- `np.all(a, axis=None)`: Test whether all array elements evaluate to True.
  - **In-depth Example**:
    ```python
    import numpy as np

    # All true.
    arr = np.array([True, True])
    all_true = np.all(arr)
    print(all_true)

    # Variation: Axis
    arr_2d = np.array([[True, False], [True, True]])
    all_axis = np.all(arr_2d, axis=1)
    print(all_axis)

    # Edge case: Empty all true
    empty_all = np.all([])
    print(empty_all)
    ```
    **Explanation**: Logical and reduction. Empty is True.  
    **Output**:
    ```
    True
    [False  True]
    True
    ```

- `np.any(a, axis=None)`: Test whether any array elements evaluate to True.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Any true.
    arr = np.array([False, True])
    any_true = np.any(arr)
    print(any_true)

    # Variation: Axis
    arr_2d = np.array([[False, False], [False, True]])
    any_axis = np.any(arr_2d, axis=0)
    print(any_axis)

    # Edge case: Empty any false
    empty_any = np.any([])
    print(empty_any)
    ```
    **Explanation**: Logical or reduction. Empty is False.  
    **Output**:
    ```
    True
    [False  True]
    False
    ```

- `np.isfinite(a)`: Test element-wise for finiteness.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Isfinite.
    arr = np.array([1, np.inf, np.nan, -np.inf])
    finite = np.isfinite(arr)
    print(finite)

    # Variation: All
    all_finite = np.all(np.isfinite(arr))
    print(all_finite)

    # Edge case: Complex
    complex_f = np.isfinite(1 + np.inf*1j)
    print(complex_f)
    ```
    **Explanation**: Checks not inf/nan.  
    **Output**:
    ```
    [ True False False False]
    False
    False
    ```

- `np.isnan(a)`: Test element-wise for NaN.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Isnan.
    arr = np.array([1, np.nan, np.inf])
    isn = np.isnan(arr)
    print(isn)

    # Variation: Count nans
    count_nan = np.sum(np.isnan(arr))
    print(count_nan)

    # Edge case: Not nan for inf
    isn_inf = np.isnan(np.inf)
    print(isn_inf)
    ```
    **Explanation**: Detects nans.  
    **Output**:
    ```
    [False  True False]
    1
    False
    ```

- `np.isinf(a)`: Test element-wise for positive or negative infinity.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Isinf.
    arr = np.array([1, np.inf, -np.inf, np.nan])
    isi = np.isinf(arr)
    print(isi)

    # Variation: Positive only
    pos_inf = np.isinf(arr) & (arr > 0)
    print(pos_inf)

    # Edge case: Complex inf
    isi_complex = np.isinf(1j * np.inf)
    print(isi_complex)
    ```
    **Explanation**: Detects infs.  
    **Output**:
    ```
    [False  True  True False]
    [False  True False False]
    True
    ```

- `np.unique(ar, return_index=False, return_inverse=False, axis=None)`: Find the unique elements of an array.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Unique.
    arr = np.array([1, 2, 2, 3])
    uniq = np.unique(arr)
    print(uniq)

    # Variation: With index and inverse
    uniq, idx, inv = np.unique(arr, return_index=True, return_inverse=True)
    print(idx, inv)

    # Edge case: Axis in 2D (unique rows)
    arr_2d = np.array([[1, 2], [1, 2], [3, 4]])
    uniq_2d = np.unique(arr_2d, axis=0)
    print(uniq_2d)
    ```
    **Explanation**: Deduplicates.  
    **Output**:
    ```
    [1 2 3]
    [0 1 3] [0 1 1 2]
    [[1 2]
     [3 4]]
    ```

- `np.copy(a, order='K')`: Return a copy of the array.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Copy function.
    arr = np.array([1, 2])
    copied = np.copy(arr)
    copied[0] = 99
    print(arr)

    # Variation: Order 'A' any
    copied_a = np.copy(arr, order='A')
    print(copied_a.flags)

    # Edge case: Subok for subclasses
    # Assume basic
    ```
    **Explanation**: Function version of copy.  
    **Output**:
    ```
    [1 2]
    C_CONTIGUOUS : True
    F_CONTIGUOUS : True
    OWNDATA : True
    WRITEABLE : True
    ALIGNED : True
    WRITEBACKIFCOPY : False
    ```

- `np.atleast_1d(*arys)`: Convert inputs to arrays with at least one dimension.
  - **In-depth Example**:
    ```python
    import numpy as np

    # At least 1D.
    scalar = 5
    at1d = np.atleast_1d(scalar)
    print(at1d)

    # Variation: Multiple
    list_in = [1, 2]
    at1d_multi = np.atleast_1d(scalar, list_in)
    print(at1d_multi)

    # Edge case: Already higher
    arr_2d = np.array([[1]])
    at1d_2d = np.atleast_1d(arr_2d)
    print(at1d_2d.shape)
    ```
    **Explanation**: Ensures min dims.  
    **Output**:
    ```
    [5]
    [array([5]), array([1, 2])]
    (1, 1)
    ```

- `np.atleast_2d(*arys)`: Convert inputs to arrays with at least two dimensions.
  - **In-depth Example**:
    ```python
    import numpy as np

    # At least 2D.
    vec = np.array([1, 2])
    at2d = np.atleast_2d(vec)
    print(at2d)

    # Variation: Scalar to 2D
    scalar = 5
    at2d_scalar = np.atleast_2d(scalar)
    print(at2d_scalar)

    # Edge case: 3D remains
    arr_3d = np.ones((1,1,1))
    at2d_3d = np.atleast_2d(arr_3d)
    print(at2d_3d.shape)
    ```
    **Explanation**: For matrix ops.  
    **Output**:
    ```
    [[1 2]]
    [[5]]
    (1, 1, 1)
    ```

- `np.atleast_3d(*arys)`: Convert inputs to arrays with at least three dimensions.
  - **In-depth Example**:
    ```python
    import numpy as np

    # At least 3D.
    mat = np.array([[1, 2]])
    at3d = np.atleast_3d(mat)
    print(at3d.shape)

    # Variation: 1D to 3D
    vec = np.array([1])
    at3d_vec = np.atleast_3d(vec)
    print(at3d_vec)

    # Edge case: Already 3D
    arr_3d = np.ones((2,2,2))
    at3d_3d = np.atleast_3d(arr_3d)
    print(at3d_3d.shape)
    ```
    **Explanation**: For tensor ops.  
    **Output**:
    ```
    (1, 2, 1)
    [[[1]]]
    (2, 2, 2)
    ```

### Methods
- `ndarray.all(axis=None)`: Test whether all elements evaluate to True.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Method all.
    arr = np.array([True, True])
    all_t = arr.all()
    print(all_t)

    # Variation: Axis
    arr_2d = np.array([[True, False], [True, True]])
    all_axis = arr_2d.all(axis=0)
    print(all_axis)

    # Edge case: Empty
    empty_all = np.array([]).all()
    print(empty_all)
    ```
    **Explanation**: Array all.  
    **Output**:
    ```
    True
    [ True False]
    True
    ```

- `ndarray.any(axis=None)`: Test whether any elements evaluate to True.
  - **In-depth Example**:
    ```python
    import numpy as np

    # Method any.
    arr = np.array([False, True])
    any_t = arr.any()
    print(any_t)

    # Variation: Axis
    arr_2d = np.array([[False, True], [False, False]])
    any_axis = arr_2d.any(axis=1)
    print(any_axis)

    # Edge case: Empty
    empty_any = np.array([]).any()
    print(empty_any)
    ```
    **Explanation**: Array any.  
    **Output**:
    ```
    True
    [ True False]
    False
    ```

- `ndarray.tofile(fid, sep='', format='%s')`: Write array to a file as text or binary.
  - **In-depth Example**:
    ```python
    import numpy as np
    import os

    # To binary file.
    arr = np.array([1, 2, 3])
    arr.tofile('bin.dat')

    # Variation: Text with sep
    arr.tofile('text.dat', sep=',', format='%d')

    # Read back text
    with open('text.dat') as f:
        print(f.read())

    # Edge case: Binary read
    loaded_bin = np.fromfile('bin.dat', dtype=int)
    print(loaded_bin)

    # Clean up
    os.remove('bin.dat')
    os.remove('text.dat')
    ```
    **Explanation**: Low-level I/O.  
    **Output**:
    ```
    1,2,3
    [1 2 3]
    ```

- `ndarray.tolist()`: Return the array as a (possibly nested) list.
  - **In-depth Example**:
    ```python
    import numpy as np

    # To list.
    arr = np.array([[1, 2], [3, 4]])
    lst = arr.tolist()
    print(lst)

    # Variation: 1D
    arr_1d = np.array([5, 6])
    lst_1d = arr_1d.tolist()
    print(lst_1d)

    # Edge case: Scalar
    scalar_arr = np.array(7)
    lst_scalar = scalar_arr.tolist()
    print(lst_scalar)
    ```
    **Explanation**: Converts to Python list.  
    **Output**:
    ```
    [[1, 2], [3, 4]]
    [5, 6]
    7
    ```

## Notes
- Examples assume `import numpy as np` and use seeding for reproducibility where random.
- Outputs are exact or approximate; run code for precise.
- For file I/O, files are created and removed in examples.
- Refer to https://numpy.org/doc/stable/ for updates as of October 2025.

