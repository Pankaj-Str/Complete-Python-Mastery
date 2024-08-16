# Python Abstract Classes

**Tutorial Name**: Codes With Pankaj  
**Website**: www.codeswithpankaj.com

### Introduction

In Python, abstract classes provide a way to define methods that must be created within any child classes built from the abstract class. It allows you to enforce certain properties on subclasses while leaving room for flexibility. Abstract classes can be used when you have a blueprint for future classes that must adhere to certain standards.

This tutorial explores Python abstract classes step-by-step, making it easy for students to understand. It covers what abstract classes are, why they are useful, and how to implement them using Python’s `abc` module.

### Table of Contents

1. What is an Abstract Class?
2. Why Use Abstract Classes?
3. Python `abc` Module
4. Creating an Abstract Class
5. Implementing Abstract Methods
6. Working with Concrete Methods
7. Example: Abstract Class in Action
8. Key Points to Remember
9. Conclusion

---

### 1. What is an Abstract Class?

An **abstract class** is a class that cannot be instantiated, meaning you cannot create an object from it. Its main purpose is to serve as a blueprint for other classes. An abstract class typically contains one or more abstract methods. These abstract methods do not have any implementation and must be defined in the derived classes (subclasses).

For example, if you have a `Shape` class that defines the basic properties of a shape but doesn't specify how to draw it, you would make `Shape` an abstract class. Then, you would create subclasses like `Circle` and `Square` to implement the drawing method.

### 2. Why Use Abstract Classes?

Abstract classes are useful for several reasons:

- **Enforce a Contract**: They ensure that certain methods are implemented in any subclass. This is particularly useful in large projects where consistency is required.
- **Code Reusability**: Abstract classes can contain common code that can be reused by multiple subclasses.
- **Simplify Complex Systems**: They help in organizing code better, especially in scenarios where multiple classes share similar properties.

### 3. Python `abc` Module

Python provides the `abc` (Abstract Base Classes) module, which allows you to define abstract classes. The `abc` module provides the `ABC` class, which is used as a base for defining abstract classes, and the `abstractmethod` decorator to define abstract methods.

To use abstract classes, you need to import the `ABC` class and the `abstractmethod` decorator from the `abc` module:

```python
from abc import ABC, abstractmethod
```

### 4. Creating an Abstract Class

To create an abstract class in Python, you inherit from the `ABC` class and define abstract methods using the `abstractmethod` decorator.

Here's a simple example:

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
```

In this example:
- `Shape` is an abstract class because it inherits from `ABC`.
- `area` and `perimeter` are abstract methods that must be implemented by any subclass of `Shape`.

### 5. Implementing Abstract Methods

When you create a subclass of an abstract class, you must implement all the abstract methods in the subclass. If you fail to do so, Python will raise an error.

Let’s implement two subclasses, `Circle` and `Rectangle`, that inherit from the `Shape` abstract class:

```python
import math

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius ** 2)
    
    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
```

Here:
- `Circle` and `Rectangle` are concrete classes that implement the `area` and `perimeter` methods from the `Shape` abstract class.
- You can now create objects of `Circle` and `Rectangle`, but not of `Shape`.

### 6. Working with Concrete Methods

An abstract class can also contain **concrete methods**—methods that have an implementation. These methods can be used by subclasses without redefining them.

Here’s an updated version of the `Shape` class with a concrete method:

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
    def describe(self):
        return "This is a shape."
```

The `describe` method provides a default implementation that can be used by any subclass. You can override it in a subclass if needed.

### 7. Example: Abstract Class in Action

Let’s put everything together with a simple program that calculates the area and perimeter of different shapes:

```python
import math
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
    def describe(self):
        return "This is a shape."

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius ** 2)
    
    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

# Create objects
circle = Circle(5)
rectangle = Rectangle(10, 5)

# Use methods
print(circle.describe())
print(f"Circle Area: {circle.area()} | Perimeter: {circle.perimeter()}")
print(rectangle.describe())
print(f"Rectangle Area: {rectangle.area()} | Perimeter: {rectangle.perimeter()}")
```

Output:

```
This is a shape.
Circle Area: 78.53981633974483 | Perimeter: 31.41592653589793
This is a shape.
Rectangle Area: 50 | Perimeter: 30
```

### 8. Key Points to Remember

- **Abstract classes** cannot be instantiated. They are designed to be inherited by subclasses that provide concrete implementations of the abstract methods.
- **Abstract methods** are defined using the `@abstractmethod` decorator and must be overridden in subclasses.
- **Concrete methods** can be defined in abstract classes and used directly by subclasses without modification.
- **The `abc` module** in Python allows for the creation of abstract classes and methods.

### 9. Conclusion

Abstract classes in Python are a powerful tool for creating structured, reusable code. By using abstract classes, you ensure that your subclasses follow a consistent structure and implement the required methods. This helps maintain the integrity of your code, especially in larger projects.

For more Python tutorials, visit **www.codeswithpankaj.com**.
