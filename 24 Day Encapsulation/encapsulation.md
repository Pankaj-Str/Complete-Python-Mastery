# Encapsulation in Python

## Introduction
Encapsulation is a fundamental concept in Object-Oriented Programming (OOP) that involves bundling data and the methods that operate on that data within a single unit. This helps in controlling access to variables and methods, preventing accidental modifications. In Python, encapsulation is achieved by using private variables within classes.

## Real-Life Example
Consider a company with different sections like finance, accounts, and sales. Each section encapsulates its data and operations. For instance, if someone from the finance section needs sales data, they can't directly access it but must request it through the appropriate channel. This encapsulation ensures data security and maintains the integrity of each section.

## Private Variables
In Python, private variables are used to encapsulate data within a class. These variables are accessible only within the class itself. Conventionally, private variables are denoted by a double underscore "__" prefix. For example:

```python
class Example:
    def __init__(self):
        # Private variable
        self.__private_var = 42
```

## Protected Members
Protected members, similar to those in languages like C++ and Java, can be accessed within the class and its subclasses. In Python, the convention for achieving this is to prefix the member name with a single underscore "_". Here's an example:

```python
class Base:
    def __init__(self):
        # Protected member
        self._a = 2

class Derived(Base):
    def __init__(self):
        # Accessing protected member of the base class
        Base.__init__(self)
        print("Calling protected member of base class:", self._a)

        # Modifying the protected variable
        self._a = 3
        print("Calling modified protected member outside class:", self._a)

# Example usage
obj1 = Derived()
obj2 = Base()

# Accessing protected member (though not recommended due to convention)
print("Accessing protected member of obj1:", obj1._a)

# Accessing protected variable outside
print("Accessing protected member of obj2:", obj2._a)
```

Output:
```
Calling protected member of base class: 2
Calling modified protected member outside class: 3
Accessing protected member of obj1: 3
Accessing protected member of obj2: 2
```

Remember, although it's possible to access protected members outside the class, it's generally discouraged as a matter of convention. Encapsulation enhances code readability, maintainability, and security.