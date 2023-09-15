class Person:
    # Constructor (the __init__ method)
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    # A method to display information about the person
    def display_info(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")

# Creating instances of the Person class using the constructor
person1 = Person("Alice", "Johnson", 30)
person2 = Person("Bob", "Smith", 25)

# Accessing object attributes and calling a method
person1.display_info()
person2.display_info()
