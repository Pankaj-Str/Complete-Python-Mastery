# Python Pickle Tutorial
# ====================
import pickle
import json  # for comparison
from dataclasses import dataclass
from typing import List

# Part 1: Basic Pickling and Unpickling
# -----------------------------------
print("Part 1: Basic Pickling and Unpickling")

# Simple data types
data = {
    'name': 'Alice',
    'age': 30,
    'scores': [85, 92, 78],
    'active': True
}

# Pickling (serialization)
with open('data.pkl', 'wb') as file:  # Note: 'wb' for write binary
    pickle.dump(data, file)

# Unpickling (deserialization)
with open('data.pkl', 'rb') as file:  # Note: 'rb' for read binary
    loaded_data = pickle.load(file)

print(f"Original data: {data}")
print(f"Loaded data: {loaded_data}")
print(f"Are they equal? {data == loaded_data}")

# Part 2: Working with Custom Objects
# --------------------------------
print("\nPart 2: Custom Objects")

@dataclass
class Student:
    name: str
    grades: List[int]
    
    def average_grade(self):
        return sum(self.grades) / len(self.grades)

# Create a student object
student = Student("Bob", [88, 92, 85])

# Pickle the custom object
with open('student.pkl', 'wb') as file:
    pickle.dump(student, file)

# Unpickle the custom object
with open('student.pkl', 'rb') as file:
    loaded_student = pickle.load(file)

print(f"Original student: {student}")
print(f"Loaded student: {loaded_student}")
print(f"Average grade (original): {student.average_grade()}")
print(f"Average grade (loaded): {loaded_student.average_grade()}")

# Part 3: Pickling Multiple Objects
# ------------------------------
print("\nPart 3: Multiple Objects")

# Multiple objects
data1 = [1, 2, 3]
data2 = {"a": 1, "b": 2}
data3 = "Hello, Pickle!"

# Pickle multiple objects
with open('multiple.pkl', 'wb') as file:
    pickle.dump(data1, file)
    pickle.dump(data2, file)
    pickle.dump(data3, file)

# Unpickle multiple objects
with open('multiple.pkl', 'rb') as file:
    loaded_data1 = pickle.load(file)
    loaded_data2 = pickle.load(file)
    loaded_data3 = pickle.load(file)

print(f"Loaded multiple objects: {loaded_data1}, {loaded_data2}, {loaded_data3}")

# Part 4: Alternative Methods and Comparison
# --------------------------------------
print("\nPart 4: Alternative Methods")

# Using dumps() and loads() for string serialization
data = {'name': 'Charlie', 'numbers': [1, 2, 3]}

# Pickle to string
pickled_string = pickle.dumps(data)
print(f"Pickled string (first 30 bytes): {pickled_string[:30]}")

# Unpickle from string
unpickled_data = pickle.loads(pickled_string)
print(f"Unpickled data: {unpickled_data}")

# Compare with JSON
print("\nComparison with JSON:")
json_string = json.dumps(data)
print(f"JSON string: {json_string}")
print(f"JSON size: {len(json_string)} bytes")
print(f"Pickle size: {len(pickled_string)} bytes")

# Part 5: Safety and Best Practices
# ------------------------------
print("\nPart 5: Safety and Error Handling")

def safe_pickle_load(filename):
    try:
        with open(filename, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        print(f"Error: File {filename} not found")
        return None
    except pickle.UnpicklingError:
        print("Error: Corrupt or invalid pickle file")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

# Test error handling
print(safe_pickle_load('nonexistent.pkl'))

# Clean up created files
import os
for file in ['data.pkl', 'student.pkl', 'multiple.pkl']:
    if os.path.exists(file):
        os.remove(file)