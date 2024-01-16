# Python Inheritance


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