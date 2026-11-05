# Python Encapsulation

## Detailed Tutorial on Python Encapsulation

Welcome to [codeswithpankaj.com](https://codeswithpankaj.com)! In this tutorial, we will explore the concept of encapsulation in Python. We'll cover what encapsulation is, how it works in Python, and provide detailed examples to illustrate its application.

### Table of Contents

1. Introduction to Encapsulation
2. Benefits of Encapsulation
3. Private and Public Members
4. Getter and Setter Methods
5. Property Decorators
6. Implementing Encapsulation in Python
7. Practical Examples
8. Advantages of Encapsulation
9. Summary

### 1. Introduction to Encapsulation

#### What is Encapsulation?

Encapsulation is an object-oriented programming concept that restricts access to certain components of an object. It bundles the data (attributes) and methods (functions) that operate on the data into a single unit, called a class. Encapsulation helps in protecting the data from unauthorized access and modification.

#### Key Points

* Encapsulation involves hiding the internal state of an object and requiring all interactions to be performed through an object's methods.
* It is a way of restricting direct access to some of an object's components, which can prevent the accidental modification of data.

### 2. Benefits of Encapsulation

* **Data Protection:** Encapsulation helps in protecting the data from unintended or unauthorized access.
* **Modularity:** It allows the implementation details of a class to be hidden, promoting modularity.
* **Maintainability:** Encapsulation makes the code more maintainable and flexible by isolating changes to a specific part of the code.
* **Ease of Use:** It simplifies the interface to the object by providing a controlled way to access and modify the object's data.

### 3. Private and Public Members

#### Public Members

Public members are accessible from outside the class. In Python, all members are public by default.

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car = Car("Toyota", "Corolla")
print(car.brand)  # Accessing public member
print(car.model)  # Accessing public member
```

#### Private Members

Private members are accessible only within the class. In Python, private members are indicated by a prefixing the member name with double underscores (`__`).

```python
class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model

car = Car("Toyota", "Corolla")
print(car.__brand)  # Error: AttributeError
print(car.__model)  # Error: AttributeError
```

### 4. Getter and Setter Methods

#### Getter Methods

Getter methods are used to access the value of private attributes from outside the class.

```python
class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model

    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

car = Car("Toyota", "Corolla")
print(car.get_brand())
print(car.get_model())
```

#### Setter Methods

Setter methods are used to modify the value of private attributes from outside the class.

```python
class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model

    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    def set_brand(self, brand):
        self.__brand = brand

    def set_model(self, model):
        self.__model = model

car = Car("Toyota", "Corolla")
car.set_brand("Honda")
car.set_model("Civic")
print(car.get_brand())
print(car.get_model())
```

### 5. Property Decorators

Property decorators in Python provide a pythonic way to define getters and setters. The `@property` decorator is used to define a getter method, and the `@<property_name>.setter` decorator is used to define a setter method.

#### Using Property Decorators

```python
class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        self.__brand = brand

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = model

car = Car("Toyota", "Corolla")
print(car.brand)
print(car.model)

car.brand = "Honda"
car.model = "Civic"
print(car.brand)
print(car.model)
```

### 6. Implementing Encapsulation in Python

#### Example: Encapsulating Bank Account Information

```python
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    @property
    def account_number(self):
        return self.__account_number

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdraw amount")

account = BankAccount("123456789", 1000)
print(account.account_number)
print(account.balance)

account.deposit(500)
print(account.balance)

account.withdraw(200)
print(account.balance)
```

### 7. Practical Examples

#### Example 1: Encapsulating Employee Information

```python
class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    @property
    def name(self):
        return self.__name

    @property
    def salary(self):
        return self.__salary

    def give_raise(self, amount):
        if amount > 0:
            self.__salary += amount
        else:
            print("Invalid raise amount")

employee = Employee("John Doe", 50000)
print(employee.name)
print(employee.salary)

employee.give_raise(5000)
print(employee.salary)
```

#### Example 2: Encapsulating Product Information

```python
class Product:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    def apply_discount(self, discount):
        if 0 < discount < 1:
            self.__price -= self.__price * discount
        else:
            print("Invalid discount value")

product = Product("Laptop", 1000)
print(product.name)
print(product.price)

product.apply_discount(0.1)
print(product.price)
```

### 8. Advantages of Encapsulation

* **Encapsulation helps in protecting the data from unauthorized access.**
* **It improves code maintainability by isolating changes to a specific part of the code.**
* **Encapsulation makes the code more modular and easier to manage.**
* **It allows for controlled access to the data, providing getter and setter methods.**

### 9. Summary

In this tutorial, we explored the concept of encapsulation in Python, its importance, and how to implement it using private members, getter and setter methods, and property decorators. We also covered practical examples to illustrate the application of encapsulation. Encapsulation is a powerful feature that enhances code flexibility, readability, and maintainability.

For more tutorials and in-depth explanations, visit [codeswithpankaj.com](https://codeswithpankaj.com)!

***

This tutorial provides a comprehensive overview of Python encapsulation, detailing each topic and subtopic with examples and explanations. For more such tutorials, keep following [codeswithpankaj.com](https://codeswithpankaj.com)!
