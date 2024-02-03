class Animal:
    def speak(self):
        pass

class Dog(Animal):
    @classmethod
    def speak(cls):
        return "Woof!"

class Cat(Animal):
    @classmethod
    def speak(cls):
        return "Meow!"

class Cow(Animal):
    @classmethod
    def speak(cls):
        return "Moo!"

# Create instances of different animals
dog = Dog()
cat = Cat()
cow = Cow()

# Store them in a list
animals = [dog, cat, cow]

# Polymorphic behavior
for animal in animals:
    print(f"{animal.__class__.__name__} says: {animal.speak()}")
