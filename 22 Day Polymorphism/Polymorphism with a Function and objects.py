class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says Woof!"

class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says Meow!"

class Cow:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says Moo!"

# A function that works with objects of various classes
def animal_speak(animal):
    if isinstance(animal, (Dog, Cat, Cow)):
        return animal.speak()
    else:
        return "Unknown animal"

# Create instances of different animals
dog = Dog("Buddy")
cat = Cat("Whiskers")
cow = Cow("Bessie")

# Use the function to make animals speak
animals = [dog, cat, cow]

for animal in animals:
    print(animal_speak(animal))

 
