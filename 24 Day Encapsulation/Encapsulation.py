class Person:
    def __init__(self, name, age):
        self._name = name     # Protected attribute
        self._age = age       # Protected attribute

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        if new_age >= 0:
            self._age = new_age
        else:
            print("Age cannot be negative.")

# Creating an instance of the Person class
person = Person("Alice", 30)

# Accessing attributes using methods
print("Name:", person.get_name())  # Output: Name: Alice
print("Age:", person.get_age())    # Output: Age: 30

# Modifying attributes using methods
person.set_name("Alicia")
person.set_age(32)
print("Updated Name:", person.get_name())  # Output: Updated Name: Alicia
print("Updated Age:", person.get_age())    # Output: Updated Age: 32