# list with elements of different data types
list1 = [1, "Hello", 3.4]
print(list1)

# list with duplicate elements
list1 = [1, "Hello", 3.4, "Hello", 1]
print(list1)
# empty list
list3 = []
print(list3)

# Access List Elements
languages = ["Python", "Swift", "C++"]
# access item at index 0
print(languages[0])   # Pythonz
# access item at index 2
print(languages[2])   # C++

# Negative Indexing in Python
languages = ["Python", "Swift", "C++"]
# access item at index 0
print(languages[-1])   # C++
# access item at index 2
print(languages[-3])   # Python

# Slicing of a List
# List slicing in Python

my_list = ['p','4','n','.','i','n']

# items from index 2 to index 4
print(my_list[2:5])

# items from index 5 to end
print(my_list[5:])

# items beginning to end
print(my_list[:])

# Add Elements to a List
numbers = [21, 34, 54, 12]
print("Before Append:", numbers)
# using append method
numbers.append(32)
print("After Append:", numbers)

# Using extend()
numbers = [1, 3, 5]

even_numbers = [4, 6, 8]
# add elements of even_numbers to the numbers list
numbers.extend(even_numbers)
print("List after append:", numbers) 

# Change List Items
languages = ['Python', 'Swift', 'C++']

# changing the third item to 'C'
languages[2] = 'C'
print(languages)  # ['Python', 'Swift', 'C']