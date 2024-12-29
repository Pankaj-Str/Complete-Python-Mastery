# Python Inheritance

## Tutorial on Python Inheritance

Welcome to codeswithpankaj.com! In this tutorial, we will dive deep into the concept of inheritance in Python. We'll explore what inheritance is, its types, and how to implement it in Python with detailed explanations and examples.

### Table of Contents

1. Introduction to Inheritance
2. Benefits of Inheritance
3. Types of Inheritance
   * Single Inheritance
   * Multiple Inheritance
   * Multilevel Inheritance
   * Hierarchical Inheritance
   * Hybrid Inheritance
4. Base and Derived Classes
5. Method Overriding
6. The `super()` Function
7. Inheritance and `__init__` Method
8. Practical Examples
9. Summary

### 1. Introduction to Inheritance

#### What is Inheritance?

Inheritance is a fundamental concept in object-oriented programming that allows a class to inherit attributes and methods from another class. The class that inherits is called the **derived class** or **child class**, while the class being inherited from is called the **base class** or **parent class**.

#### Why Use Inheritance?

* **Code Reusability:** Inheritance promotes code reuse by allowing new classes to use the properties and methods of existing classes.
* **Maintainability:** It helps in maintaining the code by minimizing redundancy.
* **Extensibility:** New functionality can be easily added to an existing class without modifying it.

### 2. Benefits of Inheritance

* **Reusability:** You can reuse code from the base class in the derived class.
* **Improved Code Organization:** It helps in organizing code into a hierarchical structure.
* **Polymorphism:** Inheritance allows for polymorphic behavior, where a method can have different implementations in different classes.

### 3. Types of Inheritance

#### Single Inheritance

Single inheritance involves a single base class and a single derived class.

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

dog = Dog()
dog.speak()
dog.bark()
```

#### Multiple Inheritance

Multiple inheritance involves multiple base classes and a single derived class.

```python
class Mammal:
    def has_fur(self):
        print("Has fur")

class Bird:
    def has_feathers(self):
        print("Has feathers")

class Bat(Mammal, Bird):
    def fly(self):
        print("Can fly")

bat = Bat()
bat.has_fur()
bat.has_feathers()
bat.fly()
```

#### Multilevel Inheritance

Multilevel inheritance involves a chain of inheritance.

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Puppy(Dog):
    def weep(self):
        print("Puppy weeps")

puppy = Puppy()
puppy.speak()
puppy.bark()
puppy.weep()
```

#### Hierarchical Inheritance

Hierarchical inheritance involves multiple derived classes inheriting from a single base class.

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")

dog = Dog()
cat = Cat()
dog.speak()
dog.bark()
cat.speak()
cat.meow()
```

#### Hybrid Inheritance

Hybrid inheritance is a combination of two or more types of inheritance.

```python
class Engine:
    def start(self):
        print("Engine starts")

class ElectricEngine(Engine):
    def charge(self):
        print("Charging...")

class Car(Engine):
    def drive(self):
        print("Car drives")

class HybridCar(Car, ElectricEngine):
    def eco_mode(self):
        print("Eco mode enabled")

hybrid_car = HybridCar()
hybrid_car.start()
hybrid_car.charge()
hybrid_car.drive()
hybrid_car.eco_mode()
```

### 4. Base and Derived Classes

#### Base Class

The base class is the class being inherited from.

```python
class Base:
    def base_method(self):
        print("Base method")
```

#### Derived Class

The derived class inherits from the base class.

```python
class Derived(Base):
    def derived_method(self):
        print("Derived method")

obj = Derived()
obj.base_method()
obj.derived_method()
```

### 5. Method Overriding

Method overriding allows a derived class to provide a specific implementation of a method that is already defined in its base class.

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

dog = Dog()
dog.speak()  # Output: Dog barks
```

### 6. The `super()` Function

The `super()` function is used to call a method from the base class.

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Dog barks")

dog = Dog()
dog.speak()
```

### 7. Inheritance and `__init__` Method

When you initialize an instance of a derived class, the `__init__` method of the base class is not called automatically. You must call it explicitly.

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

dog = Dog("Buddy", "Golden Retriever")
print(dog.name)
print(dog.breed)
```

### 8. Practical Examples

#### Example 1: Inheritance in Real Life

```python
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"Vehicle Make: {self.make}, Model: {self.model}")

class Car(Vehicle):
    def __init__(self, make, model, doors):
        super().__init__(make, model)
        self.doors = doors

    def display_info(self):
        super().display_info()
        print(f"Number of doors: {self.doors}")

car = Car("Toyota", "Corolla", 4)
car.display_info()
```

#### Example 2: Polymorphism with Inheritance

```python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

def make_animal_speak(animal):
    animal.speak()

dog = Dog()
cat = Cat()

make_animal_speak(dog)
make_animal_speak(cat)
```

### 9. Summary

In this tutorial, we covered the concept of inheritance in Python, its benefits, and different types. We also explored method overriding, the `super()` function, and practical examples to understand inheritance better. With inheritance, you can create more organized, maintainable, and reusable code.

For more tutorials and in-depth explanations, visit codeswithpankaj.com!

***

This tutorial provides a comprehensive overview of Python inheritance, detailing each topic and subtopic with examples and explanations. For more such tutorials, keep following codeswithpankaj.com!
