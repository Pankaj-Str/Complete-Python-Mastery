
---

# **Python Inheritance Tutorial**

**Tutorial Name:** Codes With Pankaj  
**Website:** [www.codeswithpankaj.com](http://www.codeswithpankaj.com)

---

### **Table of Contents**

1. [Introduction to Python Inheritance](#introduction-to-python-inheritance)
2. [Understanding the Basics of Inheritance](#understanding-the-basics-of-inheritance)
   - [What is Inheritance?](#what-is-inheritance)
   - [Benefits of Inheritance](#benefits-of-inheritance)
   - [Terminology: Parent and Child Classes](#terminology-parent-and-child-classes)
3. [Creating a Simple Inheritance Example](#creating-a-simple-inheritance-example)
4. [Types of Inheritance in Python](#types-of-inheritance-in-python)
   - [Single Inheritance](#single-inheritance)
   - [Multiple Inheritance](#multiple-inheritance)
   - [Multilevel Inheritance](#multilevel-inheritance)
   - [Hierarchical Inheritance](#hierarchical-inheritance)
   - [Hybrid Inheritance](#hybrid-inheritance)
5. [Method Overriding](#method-overriding)
   - [Concept of Method Overriding](#concept-of-method-overriding)
   - [Example of Method Overriding](#example-of-method-overriding)
6. [Using super() Function](#using-super-function)
7. [Inheritance and Encapsulation](#inheritance-and-encapsulation)
8. [Practical Examples of Inheritance](#practical-examples-of-inheritance)
   - [Example 1: Inheritance in a Bank System](#example-1-inheritance-in-a-bank-system)
   - [Example 2: Inheritance in an Employee Management System](#example-2-inheritance-in-an-employee-management-system)
9. [Best Practices for Using Inheritance](#best-practices-for-using-inheritance)
10. [Conclusion](#conclusion)

---

### **1. Introduction to Python Inheritance**

Inheritance is one of the fundamental concepts of Object-Oriented Programming (OOP) in Python. It allows you to create a new class (child class) that inherits attributes and methods from an existing class (parent class). This promotes code reusability and helps to maintain a clean and organized codebase.

In this tutorial, we'll explore the concept of inheritance in detail, understand different types of inheritance, learn about method overriding, and see how the `super()` function is used in inheritance. We'll also look at practical examples and best practices for implementing inheritance in Python.

[Back to Top](#table-of-contents)

---

### **2. Understanding the Basics of Inheritance**

#### **What is Inheritance?**

Inheritance in Python is a mechanism that allows one class to inherit attributes and methods from another class. The class that inherits is called the child class or subclass, and the class from which it inherits is called the parent class or superclass.

**Example:**
```python
class Parent:
    def parent_method(self):
        print("This is a parent class method.")

class Child(Parent):
    pass

# Creating an object of the Child class
child_obj = Child()
child_obj.parent_method()
```

**Explanation:**
- In this example, the `Child` class inherits the `parent_method()` from the `Parent` class.

#### **Benefits of Inheritance**

- **Code Reusability:** You can reuse the code from the parent class in the child class.
- **Simplifies Code Maintenance:** Changes made in the parent class are automatically reflected in the child class.
- **Extensibility:** You can add new features to a child class without modifying the parent class.

#### **Terminology: Parent and Child Classes**

- **Parent Class (Superclass):** The class whose properties and methods are inherited by another class.
- **Child Class (Subclass):** The class that inherits properties and methods from the parent class.

[Back to Top](#table-of-contents)

---

### **3. Creating a Simple Inheritance Example**

Let's create a simple example to demonstrate inheritance.

**Example:**
```python
class Animal:
    def sound(self):
        print("This is an animal sound.")

class Dog(Animal):
    def bark(self):
        print("Woof! Woof!")

# Creating an object of the Dog class
dog = Dog()
dog.sound()  # Inherited from Animal class
dog.bark()   # Defined in Dog class
```

**Explanation:**
- The `Dog` class inherits the `sound()` method from the `Animal` class.
- Additionally, the `Dog` class defines its own method, `bark()`.

[Back to Top](#table-of-contents)

---

### **4. Types of Inheritance in Python**

Python supports different types of inheritance, allowing you to design complex class hierarchies. Let's explore the main types of inheritance.

#### **4.1 Single Inheritance**

In single inheritance, a child class inherits from one parent class.

**Example:**
```python
class Parent:
    def method(self):
        print("Parent class method.")

class Child(Parent):
    def method(self):
        print("Child class method.")

child = Child()
child.method()  # Output: Child class method.
```

#### **4.2 Multiple Inheritance**

In multiple inheritance, a child class inherits from more than one parent class.

**Example:**
```python
class Parent1:
    def method1(self):
        print("Parent1 class method.")

class Parent2:
    def method2(self):
        print("Parent2 class method.")

class Child(Parent1, Parent2):
    pass

child = Child()
child.method1()  # Output: Parent1 class method.
child.method2()  # Output: Parent2 class method.
```

**Explanation:**
- The `Child` class inherits methods from both `Parent1` and `Parent2`.

#### **4.3 Multilevel Inheritance**

In multilevel inheritance, a child class inherits from a parent class, and another child class inherits from that child class.

**Example:**
```python
class Grandparent:
    def grandparent_method(self):
        print("Grandparent class method.")

class Parent(Grandparent):
    def parent_method(self):
        print("Parent class method.")

class Child(Parent):
    pass

child = Child()
child.grandparent_method()  # Inherited from Grandparent class
child.parent_method()       # Inherited from Parent class
```

**Explanation:**
- The `Child` class inherits methods from both `Parent` and `Grandparent`.

#### **4.4 Hierarchical Inheritance**

In hierarchical inheritance, multiple child classes inherit from a single parent class.

**Example:**
```python
class Parent:
    def parent_method(self):
        print("Parent class method.")

class Child1(Parent):
    pass

class Child2(Parent):
    pass

child1 = Child1()
child2 = Child2()
child1.parent_method()  # Inherited from Parent class
child2.parent_method()  # Inherited from Parent class
```

#### **4.5 Hybrid Inheritance**

Hybrid inheritance is a combination of two or more types of inheritance.

**Example:**
```python
class Base:
    def base_method(self):
        print("Base class method.")

class Parent1(Base):
    pass

class Parent2(Base):
    pass

class Child(Parent1, Parent2):
    pass

child = Child()
child.base_method()  # Inherited from Base class
```

**Explanation:**
- The `Child` class inherits from `Parent1` and `Parent2`, both of which inherit from the `Base` class.

[Back to Top](#table-of-contents)

---

### **5. Method Overriding**

#### **Concept of Method Overriding**

Method overriding occurs when a child class provides a specific implementation of a method that is already defined in its parent class. This allows the child class to modify or enhance the behavior of the inherited method.

**Example:**
```python
class Parent:
    def method(self):
        print("Parent class method.")

class Child(Parent):
    def method(self):
        print("Child class method (overridden).")

child = Child()
child.method()  # Output: Child class method (overridden).
```

**Explanation:**
- The `Child` class overrides the `method()` from the `Parent` class, providing its own implementation.

[Back to Top](#table-of-contents)

---

### **6. Using `super()` Function**

The `super()` function in Python is used to call a method from the parent class in the child class. This is useful when you want to extend the functionality of a parent class method in the child class.

**Example:**
```python
class Parent:
    def method(self):
        print("Parent class method.")

class Child(Parent):
    def method(self):
        super().method()  # Call the parent class method
        print("Child class method (extended).")

child = Child()
child.method()
```

**Output:**
```plaintext
Parent class method.
Child class method (extended).
```

**Explanation:**
- The `super().method()` calls the method from the parent class, and the child class adds additional functionality.

[Back to Top](#table-of-contents)

---

### **7. Inheritance and Encapsulation**

Inheritance works seamlessly with encapsulation in Python. Enc

apsulation is the practice of hiding internal details of a class and restricting access to them.

**Example:**
```python
class Parent:
    def __init__(self):
        self._protected_var = "Protected Variable"

    def method(self):
        print("Parent class method.")

class Child(Parent):
    def display(self):
        print("Accessing:", self._protected_var)

child = Child()
child.display()
```

**Explanation:**
- The `_protected_var` is a protected variable, but it can still be accessed in the child class.

[Back to Top](#table-of-contents)

---

### **8. Practical Examples of Inheritance**

#### **Example 1: Inheritance in a Bank System**

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}, New Balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount}, New Balance: {self.balance}")
        else:
            print("Insufficient funds")

class SavingsAccount(BankAccount):
    def add_interest(self, rate):
        interest = self.balance * rate
        self.deposit(interest)
        print(f"Interest Added: {interest}")

# Example usage
account = SavingsAccount("John Doe", 1000)
account.deposit(500)
account.add_interest(0.05)
```

**Explanation:**
- The `SavingsAccount` class inherits from `BankAccount` and adds a new method `add_interest()`.

#### **Example 2: Inheritance in an Employee Management System**

```python
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def show_details(self):
        print(f"Employee: {self.name}, Position: {self.position}")

class Manager(Employee):
    def __init__(self, name, position, team_size):
        super().__init__(name, position)
        self.team_size = team_size

    def show_details(self):
        super().show_details()
        print(f"Team Size: {self.team_size}")

# Example usage
manager = Manager("Alice", "Project Manager", 10)
manager.show_details()
```

**Explanation:**
- The `Manager` class inherits from `Employee` and extends the `show_details()` method to include team size.

[Back to Top](#table-of-contents)

---

### **9. Best Practices for Using Inheritance**

- **Use Inheritance When It Makes Sense:** Inheritance should represent an "is-a" relationship. For example, a `Dog` is a type of `Animal`, so inheritance is appropriate.
- **Avoid Deep Inheritance Hierarchies:** Deep hierarchies can make code difficult to understand and maintain. Favor composition over inheritance when appropriate.
- **Override Methods Carefully:** When overriding methods, ensure that the new implementation is consistent with the original method's purpose.
- **Use `super()` to Extend Parent Methods:** When you need to extend the behavior of a parent method, use `super()` to avoid code duplication.

[Back to Top](#table-of-contents)

---

### **10. Conclusion**

Inheritance is a powerful feature in Python that allows you to reuse code, extend functionality, and create organized class hierarchies. By understanding different types of inheritance, method overriding, and the use of `super()`, you can effectively implement inheritance in your Python projects.

For more tutorials and resources, visit **Codes With Pankaj** at [www.codeswithpankaj.com](http://www.codeswithpankaj.com).

**End of Tutorial**

[Back to Top](#table-of-contents)

---

This comprehensive tutorial on Python inheritance covers everything from basic concepts to advanced topics like method overriding and the `super()` function. With practical examples and best practices, you'll be able to implement inheritance in your Python projects efficiently.

---

