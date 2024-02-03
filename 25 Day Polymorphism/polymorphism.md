
# Polymorphism in Python 

#### 1. **Understanding Polymorphism:**
   Polymorphism is a fundamental concept in object-oriented programming, allowing objects to be treated as instances of their parent class. It can be achieved through method overloading and overriding.

#### 2. **Method Overloading:**
   - **Definition:**
     Method overloading involves defining multiple methods with the same name but different parameters.
   - **Example:**
     ```python
     class Calculator:
         def add(self, a, b):
             return a + b

         def add_three(self, a, b, c):
             return a + b + c

     calc = Calculator()
     print(calc.add(2, 3))        # Output: 5
     print(calc.add_three(2, 3, 4))  # Output: 9
     ```

#### 3. **Method Overriding:**
   - **Definition:**
     Method overriding occurs when a subclass provides a specific implementation for a method already defined in its superclass.
   - **Example:**
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

     dog = Dog()
     cat = Cat()
     print(dog.speak())  # Output: Woof!
     print(cat.speak())  # Output: Meow!
     ```

#### 4. **Polymorphism with Common Interface:**
   - **Definition:**
     Polymorphism allows different classes to be treated as instances of a common interface or superclass.
   - **Example:**
     ```python
     class Shape:
         def area(self):
             pass

     class Square(Shape):
         def __init__(self, side):
             self.side = side

         def area(self):
             return self.side * self.side

     class Circle(Shape):
         def __init__(self, radius):
             self.radius = radius

         def area(self):
             return 3.14 * self.radius * self.radius

     square = Square(5)
     circle = Circle(3)
     print(square.area())  # Output: 25
     print(circle.area())  # Output: 28.26

#### 5. **Advantages of Polymorphism:**
   - Code Reusability: Write generic code that works with multiple classes.
   - Flexibility: Easily extend functionality by adding new classes.
   - Maintainability: Changes to one class don't affect others if they adhere to the same interface.

#### Conclusion:
   Polymorphism enhances the adaptability and extensibility of your code by allowing different objects to be treated uniformly. Whether through method overloading or overriding, polymorphism is a powerful tool in creating flexible and maintainable software.