# Python Object & Class 

objects are instances of classes. A class is a blueprint or template that defines the structure and behavior of an object. It encapsulates data (attributes) and functions (methods) that operate on that data. Let's dive into the concept of objects and classes with an example:

**Creating a Class:**

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} is barking!")

    def describe(self):
        print(f"{self.name} is {self.age} years old.")

# Creating instances of the Dog class
dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)

# Accessing attributes and calling methods
dog1.describe()  # Output: Buddy is 3 years old.
dog2.bark()      # Output: Charlie is barking!
```

In this example, we defined a class called `Dog`. It has an `__init__` method (constructor) that initializes the attributes `name` and `age`. The class also has two methods, `bark()` and `describe()`, which can be called on instances of the class.

**Creating Objects (Instances):**

Creating objects (instances) in Python involves using a class as a blueprint to generate instances with specific attribute values. Here's how you create objects using the example of the `Dog` class from earlier:

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} is barking!")

    def describe(self):
        print(f"{self.name} is {self.age} years old.")

# Creating instances of the Dog class
dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)

# Accessing attributes and calling methods of instances
dog1.describe()  # Output: Buddy is 3 years old.
dog2.bark()      # Output: Charlie is barking!
```

In this example:

1. We defined the `Dog` class with an `__init__` constructor method that initializes the attributes `name` and `age`.
2. We created two instances (objects) of the `Dog` class using the constructor. These instances are `dog1` and `dog2`.
3. We accessed attributes (`name` and `age`) and called methods (`describe()` and `bark()`) on the instances using the dot notation.

When you create instances of a class, each instance is a separate object with its own set of attribute values. You can create multiple instances from the same class, each representing a distinct entity with its own characteristics and behavior.

```python
dog3 = Dog("Max", 2)
dog4 = Dog("Lucy", 4)

dog3.describe()  # Output: Max is 2 years old.
dog4.bark()      # Output: Lucy is barking!
```

Creating objects allows you to model and work with real-world entities in your code, and each object can have its own specific attributes and behavior based on the class blueprint.



**Accessing Attributes and Methods:**

You can access attributes and methods of objects using the dot notation (`object_name.attribute` or `object_name.method()`).


Accessing attributes and methods of objects involves using the dot notation (`object_name.attribute` or `object_name.method()`) to interact with the attributes and methods defined within a class. Let's continue with the `Dog` class example to demonstrate how to access attributes and methods of objects:

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} is barking!")

    def describe(self):
        print(f"{self.name} is {self.age} years old.")

# Creating instances of the Dog class
dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)

# Accessing attributes and calling methods of instances
print(dog1.name)    # Output: Buddy
print(dog2.age)     # Output: 5

dog1.describe()      # Output: Buddy is 3 years old.
dog2.bark()          # Output: Charlie is barking!
```

In this example:

- We access the `name` attribute of `dog1` using `dog1.name` and the `age` attribute of `dog2` using `dog2.age`.
- We call the `describe()` method of `dog1` using `dog1.describe()` to display its attributes, and the `bark()` method of `dog2` using `dog2.bark()` to show its behavior.

Using the dot notation, you can read and modify the attributes of an object and invoke its methods. This is how you interact with the data and behavior encapsulated within the class.


**Constructors (`__init__`):**

The `__init__` method is a special method that gets called when an object is created. It's used to initialize attributes for the object.

Constructors in Python are special methods used to initialize the attributes of an object when it's created. The most common constructor in Python is the `__init__()` method. Let's explore constructors using the example of the `Dog` class:

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} is barking!")

    def describe(self):
        print(f"{self.name} is {self.age} years old.")

# Creating instances of the Dog class
dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)

dog1.describe()  # Output: Buddy is 3 years old.
dog2.bark()      # Output: Charlie is barking!
```

In this example:

- The `__init__()` method is a constructor that gets called automatically when you create a new instance of the `Dog` class.
- The `self` parameter refers to the instance being created. It's a convention to use `self` as the first parameter name in instance methods.
- The `name` and `age` parameters are passed when creating instances. These parameters are used to initialize the attributes `name` and `age`.

When you create an instance like `dog1 = Dog("Buddy", 3)`, the `__init__()` method is called with `self` referring to `dog1`, and the attributes `name` and `age` are set to `"Buddy"` and `3`, respectively.

Constructors are essential for setting up the initial state of objects and providing a way to pass initial data when creating instances of a class. They ensure that objects are created with the required attributes in a consistent manner.

**Instance Methods:**

Instance methods are functions defined within a class that can be called on objects of that class. They often operate on the attributes of the object.

Instance methods in Python are functions defined within a class that can be called on objects (instances) of that class. These methods typically operate on the attributes of the object and can perform various actions related to the object's behavior. Let's continue using the `Dog` class to illustrate instance methods:

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} is barking!")

    def describe(self):
        print(f"{self.name} is {self.age} years old.")

# Creating instances of the Dog class
dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)

# Calling instance methods on the instances
dog1.describe()  # Output: Buddy is 3 years old.
dog2.bark()      # Output: Charlie is barking!
```

In this example:

- `bark()` and `describe()` are instance methods defined within the `Dog` class.
- When you call `dog1.describe()`, the `describe()` method is called on the `dog1` instance. Inside the method, `self` refers to the instance `dog1`, allowing you to access its attributes like `self.name` and `self.age`.
- Similarly, when you call `dog2.bark()`, the `bark()` method is called on the `dog2` instance.

Instance methods provide a way to define the behavior associated with objects of a class. They can access and modify attributes, perform calculations, interact with other objects, and more. When designing classes, you encapsulate both the data (attributes) and the behavior (methods) that are specific to the objects of that class.


**Inheritance:**

Python supports inheritance, allowing you to create a new class that inherits attributes and methods from an existing class. This promotes code reuse and allows you to override or extend the behavior of the parent class.

Inheritance is a fundamental concept in object-oriented programming that allows you to create a new class based on an existing class. The new class inherits attributes and methods from the existing class, and you can also add new attributes and methods or modify the existing ones in the new class. This promotes code reuse and enhances the organization and structure of your code.

Let's explore inheritance using an example of a base class `Animal` and a derived class `Dog`:

```python
class Animal:
    def __init__(self, species):
        self.species = species

    def speak(self):
        print("Some generic animal sound.")

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__("Dog")  # Call the constructor of the parent class
        self.name = name
        self.age = age

    def speak(self):
        print(f"{self.name} says woof!")

# Creating instances of the Dog class
dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)

# Calling methods of the Dog class
dog1.speak()  # Output: Buddy says woof!
dog2.speak()  # Output: Charlie says woof!
```

In this example:

- The `Animal` class is the base class, and it has an `__init__()` method to initialize the `species` attribute and a `speak()` method that provides a generic animal sound.
- The `Dog` class is the derived class. It inherits from the `Animal` class using parentheses `class Dog(Animal):`. It overrides the `speak()` method to provide a specific bark sound for dogs.
- The `super().__init__("Dog")` line in the `Dog` class constructor calls the constructor of the parent class `Animal`, passing `"Dog"` as the species.
- Instances of the `Dog` class can call both the inherited `speak()` method from the `Animal` class and the overridden `speak()` method from the `Dog` class.

Inheritance allows you to create more specialized classes that inherit properties and behaviors from a more general base class. This helps in creating a hierarchical structure of classes that represents the relationships between different objects in your program.

**Encapsulation:**

Classes provide a way to encapsulate data and methods, meaning you can bundle data (attributes) and functions (methods) together, reducing code duplication and improving code organization.

Encapsulation is one of the fundamental principles of object-oriented programming that focuses on bundling data (attributes) and the methods (functions) that operate on that data into a single unit, known as a class. The primary goal of encapsulation is to hide the internal details of how an object works and provide a controlled interface for interacting with the object. It helps in creating well-organized, modular, and maintainable code.

Let's explore encapsulation using an example of a `Person` class:

```python
class Person:
    def __init__(self, name, age):
        self._name = name     # Protected attribute
        self._age = age       # Protected attribute

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        if new_age >= 0:
            self._age = new_age
        else:
            print("Age cannot be negative.")

# Creating an instance of the Person class
person = Person("Alice", 30)

# Accessing attributes using methods
print("Name:", person.get_name())  # Output: Name: Alice
print("Age:", person.get_age())    # Output: Age: 30

# Modifying attributes using methods
person.set_name("Alicia")
person.set_age(32)
print("Updated Name:", person.get_name())  # Output: Updated Name: Alicia
print("Updated Age:", person.get_age())    # Output: Updated Age: 32
```

In this example:

- The `Person` class encapsulates the attributes `_name` and `_age` using the `_` prefix to indicate that they are protected attributes.
- Public methods (`get_name()`, `set_name()`, `get_age()`, and `set_age()`) are provided to interact with the encapsulated attributes. These methods allow controlled access to the attributes while enforcing data validation (for example, preventing negative ages).
- By encapsulating the attributes and providing methods to access and modify them, we can ensure that the object's internal state is manipulated in a controlled and consistent manner.

Encapsulation helps in achieving data hiding, preventing unauthorized access, and providing a clear interface for interacting with objects. It's an important concept for building robust and maintainable object-oriented code.

**Polymorphism:**

Polymorphism in Python allows objects of different classes to be treated as if they are objects of a common parent class. This helps achieve more flexible and reusable code.

By using classes and objects, you can model real-world entities, organize code, and build more structured and maintainable programs.

Polymorphism is another key concept in object-oriented programming that allows objects of different classes to be treated as objects of a common parent class. It enables you to write code that can work with objects of different types in a consistent way. Polymorphism promotes code reusability, flexibility, and modularity.

There are two main types of polymorphism: compile-time (or static) polymorphism and runtime (or dynamic) polymorphism.

**1. Compile-Time Polymorphism:**
Also known as static polymorphism, this involves method overloading and operator overloading. It occurs at compile time, where the compiler determines the appropriate function or operator to be called based on the arguments or operands.

**2. Runtime Polymorphism:**
Also known as dynamic polymorphism, this involves method overriding. It occurs at runtime, where the appropriate method is determined and executed based on the actual object type. This is achieved through inheritance and method overriding.

Here's an example of runtime polymorphism using method overriding:

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

# Polymorphic function
def animal_sound(animal):
    animal.speak()

# Creating instances of different classes
dog = Dog()
cat = Cat()

# Calling the polymorphic function with different objects
animal_sound(dog)  # Output: Dog barks
animal_sound(cat)  # Output: Cat meows
```

In this example:

- The `Animal` class defines an abstract `speak()` method that is overridden by its subclasses `Dog` and `Cat`.
- The `animal_sound()` function takes an object of type `Animal` and calls its `speak()` method. It doesn't matter whether the actual object is of type `Dog` or `Cat`, as long as it's a subclass of `Animal`.
- Polymorphism allows the same function (`animal_sound()`) to work with objects of different classes (`Dog` and `Cat`) in a seamless way.

Polymorphism simplifies code and allows you to write more flexible and extensible programs, as you can add new subclasses without modifying existing code that relies on polymorphic behavior.
