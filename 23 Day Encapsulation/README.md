# **Encapsulation in Python**

**Introduction to Encapsulation**

Encapsulation is one of the fundamental concepts in object-oriented programming (OOP). It refers to the bundling of data (variables) and methods (functions) that operate on the data into a single unit, typically a class in Python. Encapsulation also restricts direct access to some of the object's components, which is a way of preventing the accidental modification of data.

In simple terms, encapsulation is like a protective shield that prevents the data from being accessed directly. It controls the access to methods and variables by encapsulating them within a class and making them private or protected.

**Key Concepts:**
1. **Public Members**
2. **Protected Members**
3. **Private Members**
4. **Getters and Setters**

### **1. Public Members**

In Python, public members are accessible from outside the class. Any attribute or method that is defined without a leading underscore (`_`) is considered a public member.

#### **Example:**

```python
class Student:
    def __init__(self, name, age):
        self.name = name  # Public attribute
        self.age = age    # Public attribute

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating an object
student1 = Student("John", 20)

# Accessing public attributes and methods
print(student1.name)  # Output: John
print(student1.age)   # Output: 20
student1.display()    # Output: Name: John, Age: 20
```

In this example, both `name` and `age` are public attributes, and they can be accessed directly from outside the class.

### **2. Protected Members**

Protected members in Python are those whose names begin with a single underscore (`_`). These members are intended to be accessed within the class and its subclasses but not from outside.

#### **Example:**

```python
class Student:
    def __init__(self, name, age):
        self._name = name  # Protected attribute
        self._age = age    # Protected attribute

    def _display(self):
        print(f"Name: {self._name}, Age: {self._age}")

# Creating an object
student1 = Student("John", 20)

# Accessing protected attributes and methods (not recommended)
print(student1._name)  # Output: John
print(student1._age)   # Output: 20
student1._display()    # Output: Name: John, Age: 20
```

Although Python does not enforce access restrictions strictly, the convention of using a single underscore is a way to indicate that these members are intended for internal use within the class or its subclasses.

### **3. Private Members**

Private members are those whose names begin with a double underscore (`__`). These members are not accessible from outside the class and are intended to be used only within the class itself.

#### **Example:**

```python
class Student:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age    # Private attribute

    def __display(self):
        print(f"Name: {self.__name}, Age: {self.__age}")

# Creating an object
student1 = Student("John", 20)

# Accessing private attributes and methods (will raise an error)
# print(student1.__name)  # AttributeError
# print(student1.__age)   # AttributeError
# student1.__display()    # AttributeError
```

In this example, attempting to access `__name`, `__age`, or `__display()` from outside the class will raise an `AttributeError`. These members are meant to be hidden from external access.

### **4. Getters and Setters**

To access private members outside the class, we can use getter and setter methods. These methods provide a controlled way to access and modify the private attributes of a class.

#### **Example:**

```python
class Student:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age    # Private attribute

    # Getter method for name
    def get_name(self):
        return self.__name

    # Setter method for name
    def set_name(self, name):
        self.__name = name

    # Getter method for age
    def get_age(self):
        return self.__age

    # Setter method for age
    def set_age(self, age):
        self.__age = age

# Creating an object
student1 = Student("John", 20)

# Accessing private attributes using getter methods
print(student1.get_name())  # Output: John
print(student1.get_age())   # Output: 20

# Modifying private attributes using setter methods
student1.set_name("Mike")
student1.set_age(22)

print(student1.get_name())  # Output: Mike
print(student1.get_age())   # Output: 22
```

Here, `get_name`, `set_name`, `get_age`, and `set_age` are used to access and modify the private attributes `__name` and `__age`. This approach ensures that the internal state of the object is accessed in a controlled manner.

### **Advantages of Encapsulation**

1. **Data Hiding:** Encapsulation provides a way to hide the internal representation of an object from the outside world.
2. **Improved Security:** By restricting access to certain components of an object, encapsulation ensures that sensitive data is protected.
3. **Controlled Access:** Through the use of getters and setters, encapsulation provides a controlled way of accessing and modifying the data.
4. **Flexibility and Maintainability:** Encapsulation makes it easier to change the implementation details of a class without affecting other parts of the code.
5. **Prevention of Invalid Data:** By controlling how data is accessed and modified, encapsulation helps in preventing invalid data from being assigned to attributes.

### **Encapsulation in Real-World Scenarios**

Encapsulation is widely used in real-world applications. For example, consider a banking system where the balance of a customer should not be directly modified by external entities. Encapsulation allows the balance to be accessed and modified through specific methods that ensure the correctness and security of the operation.

#### **Example:**

```python
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private attribute
        self.__balance = balance                # Private attribute

    # Getter for balance
    def get_balance(self):
        return self.__balance

    # Setter for balance with validation
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid amount. Deposit failed.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid amount or insufficient balance. Withdrawal failed.")

# Creating a BankAccount object
account = BankAccount("1234567890", 1000)

# Accessing balance using the getter method
print("Initial Balance:", account.get_balance())  # Output: Initial Balance: 1000

# Depositing money
account.deposit(500)
print("Balance after deposit:", account.get_balance())  # Output: Balance after deposit: 1500

# Withdrawing money
account.withdraw(300)
print("Balance after withdrawal:", account.get_balance())  # Output: Balance after withdrawal: 1200
```

In this example, the `BankAccount` class encapsulates the `__account_number` and `__balance` attributes. The balance can only be modified through the `deposit` and `withdraw` methods, which include validation to ensure that the operations are performed correctly.

### **Conclusion**

Encapsulation is a powerful feature of object-oriented programming that promotes data hiding, security, and maintainability. By encapsulating data and methods within a class and controlling access through public, protected, and private members, developers can create robust and secure applications.

Understanding encapsulation is essential for mastering object-oriented programming in Python. It not only helps in writing cleaner code but also in designing systems that are easier to maintain and extend.

---

*This tutorial on Encapsulation in Python is brought to you by [codeswithpankaj.com](https://codeswithpankaj.com), your go-to resource for mastering Python programming and more.*

