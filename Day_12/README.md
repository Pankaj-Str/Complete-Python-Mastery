# Python Sets

A set is a collection of unique data. That is, elements of a set cannot be duplicate. For example,

Suppose we want to store information about student IDs. Since student IDs cannot be duplicate, we can use a set.

![python-set-elements](https://github.com/Pankaj-Str/Learn_Python/assets/36913690/f1781769-194d-4485-83ec-470c62f27a34)

Create a Set in Python

In Python, we create sets by placing all the elements inside curly braces {}, separated by comma.

A set can have any number of items and they may be of different types (integer, float, tuple, string etc.). But a set cannot have mutable elements like lists, sets or dictionaries as its elements.

Let's see an example,

```python
# create a set of integer type
student_id = {112, 114, 116, 118, 115}
print('Student ID:', student_id)

# create a set of string type
vowel_letters = {'a', 'e', 'i', 'o', 'u'}
print('Vowel Letters:', vowel_letters)

# create a set of mixed data types
mixed_set = {'Hello', 101, -2, 'Bye'}
print('Set of mixed data types:', mixed_set)
```
Output

```python
Student ID: {112, 114, 115, 116, 118}
Vowel Letters: {'u', 'a', 'e', 'i', 'o'}
Set of mixed data types: {'Hello', 'Bye', 101, -2}
```

In the above example, we have created different types of sets by placing all the elements inside the curly braces {}.
```
Note: When you run this code, you might get output in a different order. This is because the set has no particular order.
Create an Empty Set in Python
```
Creating an empty set is a bit tricky. Empty curly braces {} will make an empty dictionary in Python.

To make a set without any elements, we use the set() function without any argument. For example,
```python
# create an empty set
empty_set = set()

# create an empty dictionary
empty_dictionary = { }

# check data type of empty_set
print('Data type of empty_set:', type(empty_set))

# check data type of dictionary_set
print('Data type of empty_dictionary', type(empty_dictionary))
```
Output
```python
Data type of empty_set: <class 'set'>
Data type of empty_dictionary <class 'dict'>
```
Here,
```
    empty_set - an empty set created using set()
    empty_dictionary - an empty dictionary created using {}
```
Finally we have used the type() function to know which class empty_set and empty_dictionary belong to.
## Duplicate Items in a Set

Let's see what will happen if we try to include duplicate items in a set.
```python
numbers = {2, 4, 6, 6, 2, 8}
print(numbers)   # {8, 2, 4, 6}
```

Here, we can see there are no duplicate items in the set as a set cannot contain duplicates.
Add and Update Set Items in Python

Sets are mutable. However, since they are unordered, indexing has no meaning.

We cannot access or change an element of a set using indexing or slicing. Set data type does not support it.
Add Items to a Set in Python

In Python, we use the add() method to add an item to a set. For example,
```python
numbers = {21, 34, 54, 12}

print('Initial Set:',numbers)

# using add() method
numbers.add(32)

print('Updated Set:', numbers) 
```

Output
```python
Initial Set: {34, 12, 21, 54}
Updated Set: {32, 34, 12, 21, 54}
```
In the above example, we have created a set named numbers. Notice the line,
```python
numbers.add(32)
```
Here, add() adds 32 to our set.
## Update Python Set

The update() method is used to update the set with items other collection types (lists, tuples, sets, etc). For example,
```python
companies = {'Lacoste', 'Ralph Lauren'}
tech_companies = ['apple', 'google', 'apple']

companies.update(tech_companies)

print(companies)

# Output: {'google', 'apple', 'Lacoste', 'Ralph Lauren'}
```

Here, all the unique elements of tech_companies are added to the companies set.
Remove an Element from a Set

We use the discard() method to remove the specified element from a set. For example,
```python
languages = {'Swift', 'Java', 'Python'}

print('Initial Set:',languages)

# remove 'Java' from a set
removedValue = languages.discard('Java')

print('Set after remove():', languages)
```

Output
```python
Initial Set: {'Python', 'Swift', 'Java'}
Set after remove(): {'Python', 'Swift'}
```
Here, we have used the discard() method to remove 'Java' from the languages set.
Built-in Functions with Set

Built-in functions like all(), any(), enumerate(), len(), max(), min(), sorted(), sum() etc. are commonly used with sets to perform different tasks.
|Python set Methods	     |       Description|
|------------------------|-------------------|
|all()  |Returns True if all elements of the set are true (or if the set is empty).	|		
|any() |Returns True if any element of the set is true. If the set is empty, returns False.	|		
|enumerate() |Returns an enumerate object. It contains the index and value for all the items of the set as a pair.		|
|len() |Returns the length (the number of items) in the set.	|		
|max() |Returns the largest item in the set.	|		
|min() |Returns the smallest item in the set.	|		
|sorted() |Returns a new sorted list from elements in the set(does not sort the set itself).|
|sum() |Returns the sum of all elements in the set.|

## Iterate Over a Set in Python
```python
fruits = {"Apple", "Peach", "Mango"}

# for loop to access each fruits
for fruit in fruits: 
    print(fruit)
```
Output
```python
Mango
Peach
Apple
```
## Find Number of Set Elements

We can use the len() method to find the number of elements present in a Set. For example,
```python
even_numbers = {2,4,6,8}
print('Set:',even_numbers)

# find number of elements
print('Total Elements:', len(even_numbers))
```
Output
```python
Set: {8, 2, 4, 6}
Total Elements: 4
```
Here, we have used the len() method to find the number of elements present in a Set.

## Python Set Methods

|Python set Methods	     |       Description|
|------------------------|-------------------|
|add()	                  |      Add elements to the set object.|
|clear()	                  |      Removes all elements from the set.|
|copy()	                  |      Copy the set object to another set object.|
|difference()	         |       Returns the difference between two sets as a new set.|
|difference_update()	      |      Updates the difference on the called set.|
|symmetric_difference()	   |     Returns elements that are not present in each other.|
|symmetric_difference_update()	|Updates the difference on the called set.|
|remove()	   |                 Removes the specified element from the list. Returns error when the element is not present.|
|discard()	 |                   Removes the specified element from the list. Does nothing when the element is not present.|
|pop()	     |                   Returns an arbitrary element from the set.|
|intersection()	|                Returns a new set that contains the elements that are common to both sets.|
|union()	      |                  Returns a new set by combining elements from both sets.|
|update()	 |                   Add a list or set to the set object.|
|isdisjoint()	|                Returns True if the sets are disjoint, and False if they are not|
|issubset()	  |                  Checks if a set is a subset of another set.|
|issuperset()	 |                Checks if s set is a superset of another set.|


## add() – Add an element to set

The set.add() method is used to add an element to the set object. It takes a single argument, which is the element that you want to add to the set. The set.add() method can only be used to add a single element to a set at a time. The syntax of the method is set.add(element).

Here is an example of using the set.add() method to add an element to a set:

```python
# Create set
languages = {'Python', 'C++', 'Java'}

# Add element to set
languages.add('Go')
print(languages)  

# Output: 
# {'Python', 'C++', 'Java', 'Go'}
```
## clear() – Remove elements from a set

Use the set.clear() method to remove all the elements from the Python set. The set.clear() method is permanent and cannot be undone. This method does not take any arguments and does not return any value. When this method is called on a set, it simply removes all the elements from the set.

```python
# Remove all elements from set
languages = {'Python', 'C++', 'Java'}
languages.clear()
print(languages)  

# Output: 
# set()
```

## copy() – Create a copy of a set

To create a copy of a set, you can use the set.copy() method. This Python set method does not take any arguments and returns a new set that is a copy of the original set.

The set.copy() method is useful when you want to create a new set based on an existing set, but do not want to modify the original set.
It is also useful as a way to create a backup of a set before making changes to it, as the copy is independent of the original set.

```python
# Create set
original_set = {'Python', 'C++', 'Java'}

# Create a copy of the set
new_set = original_set.copy()
print(new_set) 
 
# Output: 
# {'Python', 'C++', 'Java'}

# Modify the original set
original_set.add('Go')
print(original_set)  

# Output: 
# {'Python', 'C++', 'Java', 'Go'}

# Print the copy
print(new_set)  

# Output: 
# {'Python', 'C++', 'Java'}
```
# union() – Union of Two Sets

The set.union() method returns a new set that contains all the elements from both sets. It does not modify the original sets. The set.union() method returns a new set and does not modify the original sets.

The set.union() method can take multiple sets as arguments, in which case it returns the union of all the sets. See the following example.
```python

# Find the union of three sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {5, 6, 7}
union = set1.union(set2, set3)
print(union) 
 
# Output: 
# {1, 2, 3, 4, 5, 6, 7}
```
## intersection() – Get Intersection of Two Sets

The set.intersection() method returns a new set that contains the elements that are common to both sets. It does not modify the original sets. The set.intersection() method returns a new set and does not modify the original sets. The syntax of the method is new_set = set.intersection(other_set).
```python
# Find the intersection of two sets
set1 = {'Python', 'Java', 'C++'}
set2 = {'Java', 'C++', 'Go'}
intersection = set1.intersection(set2)
print(intersection)
  
# Output: 
# {'Java', 'C++'}
```
## update() – Add Multiple Elements to Set

The set.update() method adds the elements of an iterable (such as a list or a set) to the set. It can also take multiple sets as arguments, in which case it adds all the elements of the sets to the set. It modifies the set in place and does not return a new set.

```python
# Add multiple elements to a set
s = {1, 2, 3}
s.update([4, 5, 6])
print(s)  

# Output: 
# {1, 2, 3, 4, 5, 6}

# Add multiple sets to a set
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = {5, 6, 7}
s1.update(s2, s3)
print(s1)  

# Output: 
# {1, 2, 3, 4, 5, 6, 7}
```
## Set Differences Methods in Python

There are several methods to find the difference between two sets in Python. These methods allow you to find the difference between two sets in different ways, depending on your specific needs and requirements.

Here are 4 different ways of finding the difference between the two sets.

# difference() method

This method returns the difference between two sets as a new set. This method does not modify the original sets.
```python

# Create two sets
set1 = {1, 2, 3}
set2 = {2, 3, 4}

# difference()
difference = set1.difference(set2)
print(difference)  

# Output: 
# {1}
```
# difference_update() method

This method is used to update a set with the elements that are present in the set but not in the specified iterable. . It modifies the original set in place and does not return any value.

```python
# difference_update()
set1.difference_update(set2)
print(set1)  

# Output: 
# {1}
```
# symmetric_difference() method

This method returns the symmetric difference of two sets as a new set. This method does not modify the original sets. The symmetric difference of two sets is the set of elements that are present in one set but not in the other.

```python
# symmetric_difference()
symmetric_difference = set1.symmetric_difference(set2)
print(symmetric_difference)  

# Output: 
# {1, 4}
```
# symmetric_difference_update() method

This method is used to update a set with the symmetric difference of itself and another set. It modifies the original set in place and does not return any value.

```python
# symmetric_difference_update()
set1.symmetric_difference_update(set2)
print(set1)  

# Output: 
# {1, 4}
```
# Remove Element From a Set

There are 3 different ways to remove elements from a list. Each of these Python set methods uses different approaches to remove the elements.

# remove() method

The remove() method removes the specified element from the Python set. If the element is not present in the set, it raises a KeyError exception.
```python

# Remove an element from a set
s = {'Python', 'C++', 'Java'}
s.remove('C++')
print(s)  

# Output: 
# { 'Python', 'Java'}

# Remove an element that is not present
s.remove('Go')  

# Output: 
# KeyError: 'Go'
```
# discard() method

This discard() method removes the specified element from the set. If the element is not present in the set, it does nothing.

```python
# Remove an element from a set
s = {'Python', 'C++', 'Java'}
s.discard('C++')
print(s)  

# Output: 
# {'Python', 'Java'}

# Remove element that is not present in the set
s.discard('Go')  

# No output or exception
```
# pop() method

The pop() method returns an arbitrary element from the set. If the set is empty, it raises an KeyError exception.

```python
# Remove an element from a set
s = {1, 2, 3}
element = s.pop()
print(element) 
 
# Output: 
# 1

print(s)  
# Output: {2, 3}
```
```python
# Remove an element from an empty set
s = set()
element = s.pop()  

# Output: 
# KeyError: 'pop from an empty set'
```
# isdisjoint() – Check Two Sets are Disjoint

The set.isdisjoint() method returns True if the sets are disjoint, and False if they are not. It does not modify the original sets. A set is disjoint if it has no elements in common with another set. The set.isdisjoint() method returns a Boolean value and does not modify the original sets.

```python
# Check if two sets are disjoint
set1 = {1, 2, 3}
set2 = {4, 5, 6}
result = set1.isdisjoint(set2)
print(result)  # Output: True

set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.isdisjoint(set2)
print(result)  # Output: False
```
# issubset() – Check Set is Subset of Another

The set.issubset() method returns True if the first set is a subset of the second set, and False if it is not. It does not modify the original sets. A set is a subset of another set if all the elements of the first set are also present in the second set.

```python
# Check if one set is a subset of another
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
result = set1.issubset(set2)
print(result)  

# Output: 
# True

# Another example
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.issubset(set2)
print(result)
  
# Output: 
# False
```
# issuperset() – Check Set is Superset of Another

The set.issuperset() method returns True if the first set is a superset of the second set, and False if it is not. It does not modify the original sets. A set is a superset of another set if it contains all the elements of the other set.

```python
# Check if one set is a superset of another
set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3}
result = set1.issuperset(set2)
print(result)  

# Output: 
True

# Another example
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.issuperset(set2)
print(result) 
 
# Output: 
# False
```

