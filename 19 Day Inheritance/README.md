# Python Inheritance

In Python, inheritance allows a class to inherit attributes and methods from another class. You can create a subclass by specifying the parent class in parentheses after the subclass name. For example:

```python
class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def bark(self):
        return "Dog barks"

# Create an instance of Dog
my_dog = Dog()

# Access methods from both Animal and Dog
print(my_dog.speak())  # Output: Animal speaks
print(my_dog.bark())   # Output: Dog barks
```

Here, `Dog` is a subclass of `Animal`, inheriting the `speak` method. You can extend or override methods in the subclass as needed.

1. **Single Inheritance:**

   ```python
   class Animal:
       def speak(self):
           return "Animal speaks"

   class Dog(Animal):
       def bark(self):
           return "Dog barks"
   ```

2. **Multiple Inheritance:**

   ```python
   class Bird:
       def fly(self):
           return "Bird flies"

   class Dog(Animal, Bird):
       def bark(self):
           return "Dog barks"
   ```

3. **Multilevel Inheritance:**

   ```python
   class Animal:
       def speak(self):
           return "Animal speaks"

   class Dog(Animal):
       def bark(self):
           return "Dog barks"

   class GermanShepherd(Dog):
       def guard(self):
           return "German Shepherd guards"
   ```

4. **Hierarchical Inheritance:**

   ```python
   class Animal:
       def speak(self):
           return "Animal speaks"

   class Dog(Animal):
       def bark(self):
           return "Dog barks"

   class Cat(Animal):
       def meow(self):
           return "Cat meows"
   ```

5. **Hybrid Inheritance:**

   ```python
   class Animal:
       def speak(self):
           return "Animal speaks"

   class Bird:
       def fly(self):
           return "Bird flies"

   class Parrot(Animal, Bird):
       def mimic(self):
           return "Parrot mimics"
   ```