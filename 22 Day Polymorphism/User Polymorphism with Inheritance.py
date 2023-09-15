class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

class Cow(Animal):
    def speak(self):
        return f"{self.name} says Moo!"

# Create instances of different animals
dog = Dog("Buddy")
cat = Cat("Whiskers")
cow = Cow("Bessie")

# Polymorphic behavior
animals = [dog, cat, cow]

for animal in animals:
    print(animal.speak())


