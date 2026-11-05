### **Recursive Functions in Python**

#### **Step 1: Understand What Recursion Is**
- **Definition**: Recursion is a process where a function calls itself to solve a smaller version of the original problem.
- **Key Components**:
  - **Base Case**: A condition that stops the recursion to prevent infinite calls.
  - **Recursive Case**: The part where the function calls itself with a modified input, moving toward the base case.
- **Analogy**: Think of recursion like opening a set of nested boxes. You keep opening smaller boxes until you find the smallest one (base case), then work your way back.

#### **Step 2: Structure of a Recursive Function**
A recursive function in Python typically looks like this:

```python
def recursive_function(input):
    # Base case: stops the recursion
    if base_condition:
        return base_value
    
    # Recursive case: function calls itself
    return recursive_function(modified_input)
```

- **Base case**: Prevents infinite recursion by returning a value when the input reaches a certain condition.
- **Recursive case**: Reduces the problem size and calls the function again.

#### **Step 3: Example 1 - Calculating Factorial**
Let’s write a recursive function to calculate the factorial of a number `n` (denoted `n!`), where `n! = n × (n-1) × (n-2) × ... × 1`.

- **Problem**: Compute `factorial(n)`.
- **Base Case**: If `n == 0` or `n == 1`, return `1` (since `0! = 1` and `1! = 1`).
- **Recursive Case**: For `n > 1`, `factorial(n) = n × factorial(n-1)`.

```python
def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recursive case
    return n * factorial(n - 1)

# Test the function
print(factorial(5))  # Output: 120 (5 × 4 × 3 × 2 × 1)
```

**How it works**:
- `factorial(5)`:
  - `5 * factorial(4)`
  - `5 * (4 * factorial(3))`
  - `5 * (4 * (3 * factorial(2)))`
  - `5 * (4 * (3 * (2 * factorial(1))))`
  - `5 * (4 * (3 * (2 * 1)))`
  - `5 * (4 * (3 * 2))`
  - `5 * (4 * 6)`
  - `5 * 24`
  - `120`

#### **Step 4: Example 2 - Fibonacci Sequence**
The Fibonacci sequence is where each number is the sum of the two preceding ones: `0, 1, 1, 2, 3, 5, 8, ...`.

- **Problem**: Compute the `n`-th Fibonacci number.
- **Base Case**: If `n == 0`, return `0`; if `n == 1`, return `1`.
- **Recursive Case**: For `n > 1`, `fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)`.

```python
def fibonacci(n):
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    # Recursive case
    return fibonacci(n - 1) + fibonacci(n - 2)

# Test the function
print(fibonacci(6))  # Output: 8 (0, 1, 1, 2, 3, 5, 8)
```

**How it works**:
- `fibonacci(6)`:
  - `fibonacci(5) + fibonacci(4)`
  - `[fibonacci(4) + fibonacci(3)] + [fibonacci(3) + fibonacci(2)]`
  - Continues breaking down until base cases (`n == 0` or `n == 1`) are reached.
  - Combines results: `5 + 3 = 8`.

**Note**: This recursive Fibonacci is inefficient for large `n` due to repeated calculations. We’ll address optimization later.

#### **Step 5: Example 3 - Sum of a List**
Let’s write a recursive function to sum all elements in a list.

- **Problem**: Compute the sum of a list `[a1, a2, ..., an]`.
- **Base Case**: If the list is empty, return `0`.
- **Recursive Case**: Sum the first element and the sum of the rest of the list.

```python
def sum_list(lst):
    # Base case
    if not lst:  # If list is empty
        return 0
    # Recursive case
    return lst[0] + sum_list(lst[1:])

# Test the function
print(sum_list([1, 2, 3, 4]))  # Output: 10 (1 + 2 + 3 + 4)
```

**How it works**:
- `sum_list([1, 2, 3, 4])`:
  - `1 + sum_list([2, 3, 4])`
  - `1 + (2 + sum_list([3, 4]))`
  - `1 + (2 + (3 + sum_list([4])))`
  - `1 + (2 + (3 + (4 + sum_list([]))))`
  - `1 + (2 + (3 + (4 + 0)))`
  - `1 + (2 + (3 + 4))`
  - `1 + (2 + 7)`
  - `1 + 9`
  - `10`

#### **Step 6: Handling Edge Cases**
Recursive functions must handle edge cases to avoid errors:
- **Negative inputs**: For `factorial`, negative numbers are invalid.
- **Invalid inputs**: For `sum_list`, ensure the input is a list.
- **Large inputs**: Recursion can hit Python’s default recursion depth limit (usually 1000).

Example with input validation:

```python
def factorial(n):
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be non-negative")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

try:
    print(factorial(-1))  # Raises ValueError
except ValueError as e:
    print(e)  # Output: Input must be non-negative
```

#### **Step 7: Optimizing Recursion**
Recursion can be inefficient due to repeated calculations or stack overflow. Here are optimization techniques:

1. **Memoization** (Caching Results):
   Use a dictionary to store previously computed results.

   Optimized Fibonacci with memoization:

   ```python
   def fibonacci_memo(n, memo={}):
       if n == 0:
           return 0
       if n == 1:
           return 1
       if n not in memo:
           memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
       return memo[n]

   print(fibonacci_memo(50))  # Much faster than naive recursion
   ```

2. **Tail Recursion**:
   Python doesn’t optimize tail recursion, but you can rewrite some recursive functions iteratively for efficiency.

3. **Iterative Alternative**:
   For simple problems like factorial, iteration is often more efficient:

   ```python
   def factorial_iterative(n):
       result = 1
       for i in range(1, n + 1):
           result *= i
       return result
   ```

#### **Step 8: Common Pitfalls**
- **Missing Base Case**: Leads to infinite recursion and a `RecursionError`.
  ```python
  def bad_recursive(n):
      return bad_recursive(n - 1)  # No base case, crashes
  ```
- **Incorrect Recursive Call**: Ensure the input moves toward the base case.
- **Deep Recursion**: Python’s recursion limit can be adjusted, but it’s better to optimize or use iteration.

   Adjust recursion limit (use cautiously):
   ```python
   import sys
   sys.setrecursionlimit(2000)
   ```

#### **Step 9: When to Use Recursion**
- **Good for**:
  - Problems with a natural recursive structure (e.g., tree traversal, divide-and-conquer algorithms like merge sort).
  - Problems where code clarity outweighs performance (e.g., small inputs).
- **Avoid when**:
  - Performance is critical, and iteration is simpler (e.g., factorial).
  - Inputs are very large, risking stack overflow.

#### **Step 10: Practice Problems**
Try writing recursive functions for these:
1. Compute the power of a number (`power(base, exp)`).
2. Reverse a string recursively.
3. Count the number of digits in a number.

Example solution for reversing a string:

```python
def reverse_string(s):
    if len(s) <= 1:  # Base case
        return s
    return reverse_string(s[1:]) + s[0]  # Recursive case

print(reverse_string("hello"))  # Output: "olleh"
```

---

### **Summary**
- Recursive functions break problems into smaller instances.
- Always define a **base case** to stop recursion.
- Use **memoization** or iteration to optimize when needed.
- Test edge cases and validate inputs.
- Recursion is powerful for problems like tree traversal or divide-and-conquer but may not always be the most efficient choice.

