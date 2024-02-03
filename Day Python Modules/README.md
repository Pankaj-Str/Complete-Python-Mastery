# Python Modules

Python modules are a way to organize and structure Python code into separate files. Modules provide a means to reuse code, encapsulate functionality, and keep the codebase maintainable. Let's explore each of the topics you mentioned:

1. **Python Import:**

   Python `import` statement is used to bring code from one module into another. It allows you to use functions, classes, and variables defined in other modules within your code. For example:

   ```python
   import math

   result = math.sqrt(25)
   print(result)  # Output: 5.0
   ```

##  Python Math Module

The Python `math` module is a standard library module that provides mathematical functions and constants. You can use it for a wide range of mathematical operations, including basic arithmetic, trigonometry, logarithmic, and exponential functions. Here's an overview of some commonly used functions and constants in the `math` module:

**Common Mathematical Functions:**

1. `math.sqrt(x)`: Returns the square root of x.
2. `math.pow(x, y)`: Returns x raised to the power of y.
3. `math.exp(x)`: Returns e raised to the power of x, where e is the base of the natural logarithm (approximately 2.71828).
4. `math.log(x)`: Returns the natural logarithm (base e) of x.
5. `math.log10(x)`: Returns the base-10 logarithm of x.
6. `math.sin(x)`, `math.cos(x)`, `math.tan(x)`: Trigonometric functions to calculate sine, cosine, and tangent, respectively.
7. `math.degrees(x)`: Converts radians to degrees.
8. `math.radians(x)`: Converts degrees to radians.
9. `math.ceil(x)`: Returns the smallest integer greater than or equal to x.
10. `math.floor(x)`: Returns the largest integer less than or equal to x.
11. `math.fabs(x)`: Returns the absolute value of x.
12. `math.factorial(x)`: Returns the factorial of x.

**Common Mathematical Constants:**

1. `math.pi`: Represents the mathematical constant π (pi), which is approximately 3.14159.
2. `math.e`: Represents the base of the natural logarithm, approximately 2.71828.

**Example Usage:**

Here's a Python script that demonstrates the use of some `math` module functions:

```python
import math

# Calculate the square root of a number
result_sqrt = math.sqrt(25)
print("Square root of 25:", result_sqrt)

# Calculate e raised to the power of 2
result_exp = math.exp(2)
print("e raised to the power of 2:", result_exp)

# Calculate the sine of 45 degrees
result_sin = math.sin(math.radians(45))
print("Sine of 45 degrees:", result_sin)

# Calculate the factorial of 5
result_factorial = math.factorial(5)
print("Factorial of 5:", result_factorial)
```

This script imports the `math` module and uses various functions to perform mathematical calculations. You can explore more mathematical functions and constants provided by the `math` module in the Python documentation to suit your specific needs.



2. **Python Module Internally:**

   Python modules can be created internally within your project by defining a Python file (e.g., `my_module.py`) with functions, classes, or variables. You can then import and use them in other parts of your code. Here's a simple example of an internally defined module:

   ```python
   # my_module.py
   def greet(name):
       return f"Hello, {name}!"

   # main.py
   import my_module

   message = my_module.greet("Alice")
   print(message)  # Output: Hello, Alice!
   ```

3. **Python Module Externally:**

   Python also has a standard library with many built-in modules that are maintained by the Python community. These external modules are distributed with Python and can be imported and used in your code. Examples include the `math` module for mathematical operations, the `datetime` module for working with dates and times, and the `calendar` module for calendar-related operations.

4. **Python Math Module:**

   The `math` module is a standard Python module that provides mathematical functions and constants. You can use it for various mathematical operations like square root, trigonometry, and more. Here's an example of using the `math` module:

   ```python
   import math

   result = math.sqrt(25)
   print(result)  # Output: 5.0
   ```

5. **Python Date Time Module:**

   The `datetime` module is a standard Python module for working with dates, times, and time intervals. It provides classes and functions to manipulate and format dates and times. Here's an example of using the `datetime` module:

   ```python
   import datetime

   current_time = datetime.datetime.now()
   print(current_time)  # Output: Current date and time
   ```
##  Python Date Time Module

The Python `datetime` module is a standard library module that provides classes and functions for working with dates, times, and time intervals. It allows you to perform a wide range of operations related to date and time, including date and time arithmetic, formatting and parsing, and working with time zones. Here's an overview of some commonly used classes and functions in the `datetime` module:

**Common `datetime` Classes:**

1. `datetime.date`: Represents a date (year, month, day).
2. `datetime.time`: Represents a time of day (hour, minute, second, microsecond).
3. `datetime.datetime`: Represents both a date and a time.
4. `datetime.timedelta`: Represents a duration or difference between two dates or times.
5. `datetime.tzinfo`: An abstract base class for dealing with time zones.

**Common `datetime` Functions:**

1. `datetime.datetime.now()`: Returns the current date and time.
2. `datetime.date.today()`: Returns the current date.
3. `datetime.datetime(year, month, day, hour=0, minute=0, second=0)`: Creates a `datetime` object with the specified components.
4. `datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)`: Creates a time duration or difference.
5. `datetime.strftime(format)`: Converts a `datetime` object to a string using a specified format.
6. `datetime.strptime(date_string, format)`: Parses a string into a `datetime` object using a specified format.
7. `datetime.timedelta(days=0)`: Represents the number of days between two dates.
8. `datetime.timedelta(hours=0)`: Represents the number of hours between two times.
9. `datetime.timedelta(minutes=0)`: Represents the number of minutes between two times.
10. `datetime.timedelta(seconds=0)`: Represents the number of seconds between two times.

**Example Usage:**

Here's a Python script that demonstrates the use of the `datetime` module:

```python
import datetime

# Current date and time
current_datetime = datetime.datetime.now()
print("Current Date and Time:", current_datetime)

# Current date
current_date = datetime.date.today()
print("Current Date:", current_date)

# Creating a custom datetime
custom_datetime = datetime.datetime(2023, 9, 15, 12, 0, 0)
print("Custom Datetime:", custom_datetime)

# Formatting a datetime as a string
formatted_date = custom_datetime.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted Date:", formatted_date)

# Parsing a string into a datetime
parsed_date = datetime.datetime.strptime("2023-09-15 12:00:00", "%Y-%m-%d %H:%M:%S")
print("Parsed Date:", parsed_date)

# Date arithmetic using timedelta
one_week = datetime.timedelta(weeks=1)
one_week_later = current_date + one_week
print("One Week Later:", one_week_later)
```

This script imports the `datetime` module and demonstrates various operations such as obtaining the current date and time, creating custom date and time objects, formatting and parsing date strings, and performing date arithmetic using `timedelta`. The `datetime` module is a powerful tool for working with dates and times in Python applications.


6. **Python Calendar Module:**

   The `calendar` module is a standard Python module for working with calendars and dates. It provides functions and classes to display calendars, work with dates, and calculate dates. Here's an example of using the `calendar` module:

   ```python
   import calendar

   # Print a calendar for a specific month and year
   cal = calendar.month(2023, 9)
   print(cal)
   ```

# Python Calendar Module


The Python `calendar` module is a standard library module that provides functions and classes for working with calendars and dates. It allows you to perform operations related to calendars, such as displaying calendars, determining weekday names, and calculating dates. Here's an overview of some commonly used functions and classes in the `calendar` module:

**Common `calendar` Functions:**

1. `calendar.calendar(year, w=2, l=1, c=6)`: Returns a multi-line text calendar for a specified year.
   - `year`: The year for which you want to generate the calendar.
   - `w`: Width of date columns.
   - `l`: Number of lines for each week.
   - `c`: Number of spaces between month columns.

2. `calendar.month(year, month, w=2, l=1)`: Returns a multi-line text calendar for a specified month.
   - `year`: The year of the month.
   - `month`: The month for which you want to generate the calendar (1-12).
   - `w`: Width of date columns.
   - `l`: Number of lines for each week.

3. `calendar.weekday(year, month, day)`: Returns the weekday as an integer (0-6), where Monday is 0 and Sunday is 6, for a given date.
   - `year`: The year of the date.
   - `month`: The month of the date (1-12).
   - `day`: The day of the date (1-31).

4. `calendar.month_name`: A list of month names.
   - Example: `calendar.month_name[1]` returns `'January'`.

5. `calendar.day_name`: A list of weekday names.
   - Example: `calendar.day_name[0]` returns `'Monday'`.

**Example Usage:**

Here's a Python script that demonstrates the use of the `calendar` module:

```python
import calendar

# Display a calendar for a specific year
year_calendar = calendar.calendar(2023)
print("Calendar for 2023:")
print(year_calendar)

# Display a calendar for a specific month
month_calendar = calendar.month(2023, 9)
print("Calendar for September 2023:")
print(month_calendar)

# Determine the weekday of a specific date
weekday = calendar.weekday(2023, 9, 15)
print("Weekday of September 15, 2023:", calendar.day_name[weekday])
```

This script imports the `calendar` module and demonstrates various operations such as generating calendars for a specific year and month and determining the weekday of a specific date.

The `calendar` module is useful when you need to work with dates and calendars in your Python programs, especially when you want to display calendars or perform date-related calculations.