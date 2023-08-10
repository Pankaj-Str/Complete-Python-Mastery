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
```
1. all() Returns True if all elements of the set are true (or if the set is empty).			
2. any() Returns True if any element of the set is true. If the set is empty, returns False.			
3. enumerate() Returns an enumerate object. It contains the index and value for all the items of the set as a pair.		
4. len() Returns the length (the number of items) in the set.			
5. max() Returns the largest item in the set.			
6. min() Returns the smallest item in the set.			
7. sorted() Returns a new sorted list from elements in the set(does not sort the set itself).
8. sum() Returns the sum of all elements in the set.
```
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

# Python Set Operations

Python Set provides different built-in methods to perform mathematical set operations like union, intersection, subtraction, and symmetric difference.
Union of Two Sets

The union of two sets A and B include all the elements of set A and B.

![python-union](https://github.com/Pankaj-Str/Learn_Python/assets/36913690/943b45b3-f478-40d1-9eaa-55be61e3fb1c)

We use the | operator or the union() method to perform the set union operation. For example,
```python
# first set
A = {1, 3, 5}

# second set
B = {0, 2, 4}

# perform union operation using |
print('Union using |:', A | B)

# perform union operation using union()
print('Union using union():', A.union(B)) 

```
Output
```python
Union using |: {0, 1, 2, 3, 4, 5}
Union using union(): {0, 1, 2, 3, 4, 5}
```
