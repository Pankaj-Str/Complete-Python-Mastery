# Data Abstraction with a very simple and relatable example that students can easily understand.

Think of data abstraction like a TV remote control. You just need to know which buttons to press, but you don't need to know how it works inside!

Here's a simple example using a Student Report Card:

```python
class StudentReport:
    def __init__(self, name):
        # Private variables (hidden from outside)
        self.__name = name
        self.__marks = []
    
    # Public methods (can be used by anyone)
    def add_mark(self, mark):
        if 0 <= mark <= 100:  # Making sure mark is valid
            self.__marks.append(mark)
            print("Mark added successfully!")
        else:
            print("Invalid mark! Please enter between 0 and 100")
    
    def get_average(self):
        if len(self.__marks) > 0:
            return sum(self.__marks) / len(self.__marks)
        return 0
    
    def show_report(self):
        print(f"Student Name: {self.__name}")
        print(f"Marks: {self.__marks}")
        print(f"Average: {self.get_average()}")

# Let's use our StudentReport class
john = StudentReport("John")

# Adding marks
john.add_mark(85)  # Output: Mark added successfully!
john.add_mark(90)  # Output: Mark added successfully!
john.add_mark(75)  # Output: Mark added successfully!

# Show the report
john.show_report()
# Output:
# Student Name: John
# Marks: [85, 90, 75]
# Average: 83.33
```

Let's break down why this is abstraction:

1. Hidden Data (Private):
   - `__name` and `__marks` are hidden inside the class
   - You can't directly change them from outside
   - Just like you can't see inside a TV remote!

2. Simple Interface (Public Methods):
   - `add_mark()`: to add a new mark
   - `get_average()`: to calculate average
   - `show_report()`: to display results
   - These are like the buttons on your remote control!

Here's what happens if you try to access private variables directly:

```python
# These won't work:
print(john.__marks)      # Error!
john.__name = "Jimmy"    # Won't change the name

# You must use the provided methods:
john.add_mark(95)        # This works!
john.show_report()       # This works!
```

Another simple example using a Mobile Phone:

```python
class MobilePhone:
    def __init__(self):
        self.__battery_level = 100
        self.__is_on = False
    
    def switch_on(self):
        self.__is_on = True
        print("Phone is switched ON")
    
    def switch_off(self):
        self.__is_on = False
        print("Phone is switched OFF")
    
    def check_battery(self):
        return f"Battery level: {self.__battery_level}%"

# Using the phone
my_phone = MobilePhone()
my_phone.switch_on()     # Output: Phone is switched ON
print(my_phone.check_battery())  # Output: Battery level: 100%
```

Think of it this way:
- When you use your real mobile phone, you just press the power button
- You don't need to know how the battery works inside
- You just need to know how to check battery level

This is exactly what abstraction does:
1. Hides complicated stuff inside (using `__`)
2. Gives you simple methods to use (like `switch_on()`)
3. Protects the data from accidental changes
4. Makes the code easier to use

