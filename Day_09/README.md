# Python List

Python lists and explore some of their key characteristics and operations.

**1. Creation of Lists:**
Lists in Python are ordered collections of items enclosed in square brackets `[]`. Each item in the list is separated by a comma. Lists can contain elements of any data type, including other lists.

```python
fruits = ["apple", "banana", "orange"]
```

**2. Indexing and Slicing:**
Lists are ordered, meaning each element has an index associated with it. Indexing starts from 0 for the first element, -1 for the last element, -2 for the second-to-last, and so on.

```python
print(fruits[0])  # Output: "apple"
print(fruits[-1])  # Output: "orange"
```

You can also use slicing to extract a portion of the list:

```python
subset = fruits[1:3]  # Extracts elements at index 1 and 2
print(subset)        # Output: ["banana", "orange"]
```

**3. Mutability:**
Lists are mutable, which means you can change their contents after creation. You can modify, add, or remove elements from a list.

```python
fruits[1] = "pear"   # Modifying element at index 1
fruits.append("kiwi")  # Adding "kiwi" to the end
fruits.remove("apple")  # Removing "apple" by value
```

**4. Adding and Removing Elements:**
You can add elements using methods like `append()` (adds to the end), `insert()` (adds at a specific index), and extend a list using `extend()`.

```python
fruits.append("grape")    # Adds "grape" to the end
fruits.insert(1, "peach")  # Adds "peach" at index 1
fruits.extend(["mango", "cherry"])  # Adds multiple elements
```

You can remove elements using methods like `remove()` (removes by value), `pop()` (removes by index and returns the element), and `del` statement.

```python
fruits.remove("banana")  # Removes "banana" by value
removed_fruit = fruits.pop(2)  # Removes element at index 2 and returns it
del fruits[0]            # Removes element at index 0
```

**5. Common Operations:**
- `len(list)`: Returns the number of elements in the list.
- `list.index(item)`: Returns the index of the first occurrence of `item`.
- `item in list`: Checks if `item` exists in the list, returning a boolean.
- `list.sort()`: Sorts the list in ascending order.
- `list.reverse()`: Reverses the order of elements in the list.

**6. Nested Lists:**
Lists can contain other lists as elements, allowing for nested structures.

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][2])  # Output: 6
```


#  list of some common methods that you can use with Python lists:

1. **`append(item)`**: Adds `item` to the end of the list.

```python
fruits = ["apple", "banana"]
fruits.append("orange")
# fruits is now ["apple", "banana", "orange"]
```

2. **`insert(index, item)`**: Inserts `item` at the specified `index` in the list.

```python
fruits = ["apple", "banana"]
fruits.insert(1, "orange")
# fruits is now ["apple", "orange", "banana"]
```

3. **`extend(iterable)`**: Appends each element of the `iterable` (usually another list) to the end of the list.

```python
fruits = ["apple", "banana"]
fruits.extend(["orange", "kiwi"])
# fruits is now ["apple", "banana", "orange", "kiwi"]
```

4. **`remove(item)`**: Removes the first occurrence of `item` from the list.

```python
fruits = ["apple", "banana", "banana", "orange"]
fruits.remove("banana")
# fruits is now ["apple", "banana", "orange"]
```

5. **`pop(index)`**: Removes and returns the element at the specified `index`. If no index is provided, the last element is removed and returned.

```python
fruits = ["apple", "banana", "orange"]
removed_fruit = fruits.pop(1)
# removed_fruit is "banana", fruits is now ["apple", "orange"]
```

6. **`index(item)`**: Returns the index of the first occurrence of `item` in the list.

```python
fruits = ["apple", "banana", "orange"]
index = fruits.index("banana")
# index is 1
```

7. **`count(item)`**: Returns the number of times `item` appears in the list.

```python
fruits = ["apple", "banana", "banana", "orange"]
count = fruits.count("banana")
# count is 2
```

8. **`sort()`**: Sorts the list in ascending order. You can also use the `reverse` parameter to sort in descending order.

```python
numbers = [4, 1, 7, 3]
numbers.sort()
# numbers is now [1, 3, 4, 7]

numbers.sort(reverse=True)
# numbers is now [7, 4, 3, 1]
```

9. **`reverse()`**: Reverses the order of elements in the list.

```python
fruits = ["apple", "banana", "orange"]
fruits.reverse()
# fruits is now ["orange", "banana", "apple"]
```

10. **`copy()`**: Creates a shallow copy of the list.

```python
fruits = ["apple", "banana", "orange"]
fruits_copy = fruits.copy()
```

11. **`clear()`**: Removes all elements from the list, making it empty.

```python
fruits = ["apple", "banana", "orange"]
fruits.clear()
# fruits is now []
```

# Iterating through a list

Iterating through a list in Python means going through each element of the list one by one and performing some action on each element. This can be done using loops or other iteration constructs. Here are a few common methods for iterating through a list:

1. **Using a `for` loop:**
The most common way to iterate through a list is by using a `for` loop. Here's how you can do it:

```python
fruits = ["apple", "banana", "orange", "kiwi"]

for fruit in fruits:
    print(fruit)
```

2. **Using `range` and index:**
You can use the `range` function along with the length of the list to iterate through indices and access elements.

```python
fruits = ["apple", "banana", "orange", "kiwi"]

for i in range(len(fruits)):
    print(fruits[i])
```

3. **Using `enumerate`:**
The `enumerate` function is useful when you want both the index and the value of each element.

```python
fruits = ["apple", "banana", "orange", "kiwi"]

for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")
```

4. **Using a `while` loop:**
You can also use a `while` loop with an index to iterate through the list.

```python
fruits = ["apple", "banana", "orange", "kiwi"]
index = 0

while index < len(fruits):
    print(fruits[index])
    index += 1
```

5. **Using List Comprehension:**
List comprehension provides a concise way to iterate through a list and create a new list based on some condition.

```python
fruits = ["apple", "banana", "orange", "kiwi"]
upper_fruits = [fruit.upper() for fruit in fruits]
print(upper_fruits)
```

Iterating through a list allows you to perform various operations on each element, such as printing, modifying, or filtering, based on your specific requirements. Choose the iteration method that best suits the task you're trying to accomplish.

# Check if an Element Exists in a List 

To check if an element exists in a list in Python, you can use the `in` operator or the `not in` operator. Both of these operators return a boolean value (`True` or `False`). Here's how you can use them:

```python
fruits = ["apple", "banana", "orange", "kiwi"]

# Using the "in" operator
if "banana" in fruits:
    print("Banana is in the list")

# Using the "not in" operator
if "grape" not in fruits:
    print("Grape is not in the list")
```

In the example above, the `in` operator checks if the element `"banana"` is present in the `fruits` list, and the `not in` operator checks if the element `"grape"` is not present in the list. Both conditions are evaluated as `True`, so the corresponding print statements will be executed.

These operators are useful for quickly checking the existence of an element in a list without having to manually iterate through the list.

# Question 
----------
1. Billing System (Basic)

```python
-- User input section
Enter Product List Size : 4
Enter Product 1 -
Samosa
Enter Product 2 -
Kachori
Enter Product 3 -
Fafda
Enter Product 4 -
Jalebi

Enter Samosa Price :
300/-
Enter Kachori Price :
100/-
Enter Fafda Price :
100/-
Enter Jalebi Price :
200/-

Do You Want to add GST [Y/N]
[note : if user select `N` Print bill without GST]
[Note User select yes `Y`]
Enter GST % = 18
-------Out put -------

1. Samosa = 300/-
2. Kachori = 100/-
3. Fafda = 100/-
4. Jalebi = 200/-
-------------------
Total = 700
GST = 18%
-------------------
Final Total = 826/-
-------------------
```