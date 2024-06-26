# Polymorphism

Polymorphism is a fundamental concept in object-oriented programming that allows objects of different classes to be treated as objects of a common superclass. It enables you to write more flexible and reusable code by allowing different classes to provide their own implementations of methods with the same name.

Polymorphism can be achieved in various ways, and one of them is through class methods. Class methods are methods that are associated with a class rather than an instance of the class. They can be called on the class itself, and they can also be overridden in subclasses, which makes them a suitable candidate for implementing polymorphism.

Here's an example of how polymorphism can be achieved with class methods in Python:

```python
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
   
    def area(self): # Use self instead of cls
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self,length, width):
        self.length = length
        self.width = width
    
    
    def area(self): # Use self instead of cls
        return self.length * self.width

# Usage
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Polymorphic behavior
shapes = [circle, rectangle]

for shape in shapes:
  print(f"Area: {shape.area()}")
```

In this example, we have a base class `Shape` with a method `area()`, which is overridden in the `Circle` and `Rectangle` subclasses as class methods. The `@classmethod` decorator is used to define these class methods.

When we create instances of `Circle` and `Rectangle` and store them in a list, we can iterate through the list and call the `area()` method on each object. Despite the different implementations in the subclasses, polymorphism allows us to treat all shapes as if they have a common `area()` method.

Polymorphism with class methods makes it possible for different classes to provide their own implementations of the same method, allowing for more flexible and extensible code.

# Type of Polymorphism

Polymorphism is a fundamental concept in object-oriented programming that allows objects of different classes to be treated as objects of a common superclass. In Python, it's important to note that method overriding and runtime polymorphism are more common, while method overloading and compile-time polymorphism are not as prevalent due to Python's dynamic and duck-typed nature.

Let's explore these concepts one by one with examples:

1. **Runtime Polymorphism (Method Overriding):**

   Runtime polymorphism occurs when a subclass provides a specific implementation of a method that is already defined in its superclass. The method in the subclass "overrides" the method in the superclass. This allows objects of the subclass to be treated as objects of the superclass.

   Example:

   ```python
   class Animal:
       def speak(self):
           pass

   class Dog(Animal):
       def speak(self):
           return "Woof!"

   class Cat(Animal):
       def speak(self):
           return "Meow!"

   # Polymorphism in action
   def animal_sound(animal):
       return animal.speak()

   dog = Dog()
   cat = Cat()

   print(animal_sound(dog))  # Output: Woof!
   print(animal_sound(cat))  # Output: Meow!
   ```

2. **Compile Time Polymorphism (Method Overloading):**

   Python doesn't support method overloading in the traditional sense where you can have multiple methods with the same name but different parameter lists. However, you can achieve a similar effect using default arguments or variable-length argument lists.

   Example using default arguments:

   ```python
   class Calculator:
       def add(self, a, b=0):
           return a + b

   calc = Calculator()
   result1 = calc.add(5)
   result2 = calc.add(3, 2)

   print(result1)  # Output: 5
   print(result2)  # Output: 5
   ```

3. **Python Overloading (Operator Overloading):**

   Python allows you to define custom behavior for built-in operators by overloading special methods. This is often used for customizing how objects of your classes behave with operators like `+`, `-`, `*`, and others.

   Example using `+` operator overloading:

   ```python
   class Point:
       def __init__(self, x, y):
           self.x = x
           self.y = y

       def __add__(self, other):
           return Point(self.x + other.x, self.y + other.y)

   p1 = Point(1, 2)
   p2 = Point(3, 4)
   p3 = p1 + p2

   print(f"({p3.x}, {p3.y})")  # Output: (4, 6)
   ```

   In this example, we've overloaded the `+` operator to add two `Point` objects together.
