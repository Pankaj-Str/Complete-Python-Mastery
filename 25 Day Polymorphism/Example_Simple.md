Polymorphism in a simple way using some easy-to-understand examples.

Polymorphism means "many forms" - it's when we can use the same method name for different classes, and each class can implement that method in its own way. Think of it like different animals making sounds - they all "speak" but each does it differently!

Here are two main types of polymorphism with examples:

1. Method Overriding (Runtime Polymorphism):
```python
class Animal:
    def speak(self):
        return "Animal makes a sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Duck(Animal):
    def speak(self):
        return "Quack!"

# Using polymorphism
dog = Dog()
cat = Cat()
duck = Duck()

# Same method name, different behaviors
print(dog.speak())   # Output: Woof!
print(cat.speak())   # Output: Meow!
print(duck.speak())  # Output: Quack!

# We can also use polymorphism with a list
animals = [Dog(), Cat(), Duck()]
for animal in animals:
    print(animal.speak())  # Each animal makes its own sound
```

2. Method Overloading (using default parameters in Python):
```python
class Calculator:
    def add(self, x, y=0, z=0):
        return x + y + z

# Using the same method in different ways
calc = Calculator()
print(calc.add(5))        # Output: 5  (only x is provided)
print(calc.add(5, 3))     # Output: 8  (x and y are provided)
print(calc.add(5, 3, 2))  # Output: 10 (all parameters provided)
```

A Real-World Example - Shape Calculator:
```python
class Shape:
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def calculate_area(self):
        return self.side * self.side

# Using polymorphism
rectangle = Rectangle(5, 4)
circle = Circle(3)
square = Square(4)

# Same method name, different calculations
print(rectangle.calculate_area())  # Output: 20
print(circle.calculate_area())     # Output: 28.26
print(square.calculate_area())     # Output: 16

# We can also use a list
shapes = [Rectangle(5, 4), Circle(3), Square(4)]
for shape in shapes:
    print(f"Area: {shape.calculate_area()}")
```

Key Points About Polymorphism:
1. Same interface (method name) for different classes
2. Each class can implement the method differently
3. Makes code more flexible and reusable
4. Helps write cleaner, more organized code
5. Follows the principle "one interface, multiple implementations"

Benefits of Polymorphism:
- Code reusability
- Flexibility in adding new classes
- Cleaner and more organized code
- Better method organization
- Easier maintenance

