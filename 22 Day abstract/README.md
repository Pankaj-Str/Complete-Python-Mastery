# Abstract Classes in Python

**Tutorial Name**: Codes With Pankaj  
**Website**: www.codeswithpankaj.com

### Introduction to Abstract Classes

An **abstract class** in Python is a class that cannot be instantiated. Instead, it serves as a blueprint for other classes. It typically contains one or more abstract methods, which are methods declared in a base class but without any implementation. Subclasses of the abstract class are responsible for providing the implementation for these abstract methods.

Abstract classes are a key concept in object-oriented programming (OOP) and are particularly useful when you want to enforce that certain methods are implemented by any subclass.

### Key Concepts

- Abstract Classes and Methods
- The `abc` Module in Python
- Creating Abstract Classes
- Implementing Abstract Methods
- Concrete Methods in Abstract Classes
- Example: Abstract Class in Action
- Advantages of Using Abstract Classes

### 1. Abstract Classes and Methods

An abstract class is a class that contains at least one abstract method. An abstract method is a method that is declared but contains no implementation. Abstract classes cannot be instantiated, meaning you cannot create objects of abstract classes.

For example, consider a `Vehicle` class that defines the blueprint for all vehicles. You may not want to instantiate a generic vehicle, but rather specific types like `Car` or `Bike`.

### 2. The `abc` Module in Python

Python provides the `abc` (Abstract Base Classes) module to define abstract classes. The `ABC` class from the `abc` module is used as a base class for defining abstract classes. Abstract methods are defined using the `@abstractmethod` decorator.

```python
from abc import ABC, abstractmethod
```

### 3. Creating Abstract Classes

To create an abstract class in Python, inherit from the `ABC` class and define abstract methods using the `abstractmethod` decorator.

Example:

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
```

In this example:
- `Vehicle` is an abstract class because it inherits from `ABC`.
- The `start_engine` method is an abstract method that must be implemented by any subclass of `Vehicle`.

### 4. Implementing Abstract Methods

When you create a subclass of an abstract class, you must implement all the abstract methods defined in the base class. Otherwise, Python will raise an error.

Example:

```python
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started")
```

Here:
- `Car` and `Bike` are concrete classes that implement the `start_engine` method from the `Vehicle` abstract class.
- You can now create objects of `Car` and `Bike`, but not of `Vehicle`.

### 5. Concrete Methods in Abstract Classes

An abstract class can also contain **concrete methods**—methods that have an implementation. These methods can be used by subclasses without redefining them.

Example:

```python
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    
    def stop_engine(self):
        print("Engine stopped")
```

The `stop_engine` method is a concrete method that provides a default implementation. Subclasses can use this method as is, or override it if needed.

### 6. Example: Abstract Class in Action

Let’s put everything together with a simple program that demonstrates how abstract classes work.

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    
    def stop_engine(self):
        print("Engine stopped")

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started")

# Create objects
car = Car()
bike = Bike()

# Use methods
car.start_engine()  # Output: Car engine started
bike.start_engine()  # Output: Bike engine started
car.stop_engine()  # Output: Engine stopped
bike.stop_engine()  # Output: Engine stopped
```

### 7. Advantages of Using Abstract Classes

- **Enforce a Contract**: Abstract classes ensure that certain methods are implemented in subclasses, providing consistency.
- **Code Reusability**: Abstract classes can contain common methods and properties that can be shared among subclasses.
- **Simplify Complex Systems**: Abstract classes help in organizing code, making it easier to maintain and extend.

### Conclusion

Abstract classes in Python provide a powerful mechanism for creating blueprints for other classes. By using abstract classes, you can ensure that certain methods are implemented in any subclass, enforce a common interface, and simplify code management in complex systems.

This tutorial on Abstract Classes in Python is brought to you by **codeswithpankaj.com**, your trusted resource for mastering Python programming and more.
