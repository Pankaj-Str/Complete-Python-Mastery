# Python Datetime

## Python Datetime

Welcome to [codeswithpankaj.com](https://codeswithpankaj.com)! In this tutorial, we will explore the `datetime` module in Python. We'll cover how to work with dates and times, how to format and manipulate them, and provide detailed examples to illustrate their application.

### Table of Contents

1. Introduction to `datetime`
2. Getting the Current Date and Time
3. Creating Date and Time Objects
4. Formatting Dates and Times
5. Parsing Dates from Strings
6. Calculating Time Differences
7. Working with Time Zones
8. Practical Examples
9. Summary

### 1. Introduction to `datetime`

#### What is the `datetime` Module?

The `datetime` module in Python provides classes for manipulating dates and times. It allows you to work with date and time objects, format them, and perform arithmetic operations on them.

#### Key Classes

* `datetime.date`: Represents a date (year, month, day).
* `datetime.time`: Represents a time (hour, minute, second, microsecond).
* `datetime.datetime`: Combines date and time.
* `datetime.timedelta`: Represents the difference between two dates or times.
* `datetime.timezone`: Represents a time zone.

### 2. Getting the Current Date and Time

#### Example: Getting the Current Date and Time

```python
import datetime

# Get the current date and time
now = datetime.datetime.now()
print("Current date and time:", now)

# Get the current date
today = datetime.date.today()
print("Current date:", today)

# Get the current time
current_time = datetime.datetime.now().time()
print("Current time:", current_time)
```

### 3. Creating Date and Time Objects

#### Example: Creating a Date Object

```python
import datetime

# Create a date object
date_obj = datetime.date(2024, 8, 5)
print("Date object:", date_obj)
```

#### Example: Creating a Time Object

```python
import datetime

# Create a time object
time_obj = datetime.time(14, 30, 45)
print("Time object:", time_obj)
```

#### Example: Creating a Datetime Object

```python
import datetime

# Create a datetime object
datetime_obj = datetime.datetime(2024, 8, 5, 14, 30, 45)
print("Datetime object:", datetime_obj)
```

### 4. Formatting Dates and Times

#### Example: Formatting a Date

```python
import datetime

# Create a date object
date_obj = datetime.date(2024, 8, 5)

# Format the date
formatted_date = date_obj.strftime("%B %d, %Y")
print("Formatted date:", formatted_date)
```

#### Example: Formatting a Time

```python
import datetime

# Create a time object
time_obj = datetime.time(14, 30, 45)

# Format the time
formatted_time = time_obj.strftime("%H:%M:%S")
print("Formatted time:", formatted_time)
```

#### Example: Formatting a Datetime

```python
import datetime

# Create a datetime object
datetime_obj = datetime.datetime(2024, 8, 5, 14, 30, 45)

# Format the datetime
formatted_datetime = datetime_obj.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted datetime:", formatted_datetime)
```

### 5. Parsing Dates from Strings

#### Example: Parsing a Date from a String

```python
import datetime

# Parse a date from a string
date_str = "August 5, 2024"
date_obj = datetime.datetime.strptime(date_str, "%B %d, %Y").date()
print("Parsed date:", date_obj)
```

#### Example: Parsing a Datetime from a String

```python
import datetime

# Parse a datetime from a string
datetime_str = "2024-08-05 14:30:45"
datetime_obj = datetime.datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
print("Parsed datetime:", datetime_obj)
```

### 6. Calculating Time Differences

#### Example: Calculating the Difference Between Two Dates

```python
import datetime

# Create two date objects
date1 = datetime.date(2024, 8, 5)
date2 = datetime.date(2023, 8, 5)

# Calculate the difference
difference = date1 - date2
print("Difference between dates:", difference)
```

#### Example: Calculating the Difference Between Two Datetimes

```python
import datetime

# Create two datetime objects
datetime1 = datetime.datetime(2024, 8, 5, 14, 30, 45)
datetime2 = datetime.datetime(2023, 8, 5, 12, 15, 30)

# Calculate the difference
difference = datetime1 - datetime2
print("Difference between datetimes:", difference)
```

### 7. Working with Time Zones

#### Example: Adding Time Zone Information

```python
import datetime

# Create a datetime object
datetime_obj = datetime.datetime(2024, 8, 5, 14, 30, 45)

# Create a time zone object
timezone_obj = datetime.timezone(datetime.timedelta(hours=-5))

# Add the time zone information to the datetime object
datetime_with_timezone = datetime_obj.replace(tzinfo=timezone_obj)
print("Datetime with time zone:", datetime_with_timezone)
```

#### Example: Converting Between Time Zones

```python
import datetime

# Create a datetime object with time zone information
datetime_obj = datetime.datetime(2024, 8, 5, 14, 30, 45, tzinfo=datetime.timezone.utc)

# Convert to another time zone
new_timezone = datetime.timezone(datetime.timedelta(hours=-5))
converted_datetime = datetime_obj.astimezone(new_timezone)
print("Converted datetime:", converted_datetime)
```

### 8. Practical Examples

#### Example 1: Getting the Weekday of a Date

```python
import datetime

# Get the weekday of a date
date_obj = datetime.date(2024, 8, 5)
weekday = date_obj.strftime("%A")
print("Weekday:", weekday)
```

#### Example 2: Adding Days to a Date

```python
import datetime

# Create a date object
date_obj = datetime.date(2024, 8, 5)

# Add 10 days to the date
new_date = date_obj + datetime.timedelta(days=10)
print("New date:", new_date)
```

#### Example 3: Calculating Age

```python
import datetime

# Define the birthdate
birthdate = datetime.date(1990, 8, 5)

# Get the current date
today = datetime.date.today()

# Calculate the age
age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
print("Age:", age)
```

### 9. Summary

In this tutorial, we explored the `datetime` module in Python, its importance, and how to work with dates and times. We covered getting the current date and time, creating date and time objects, formatting and parsing dates, calculating time differences, and working with time zones. We also provided practical examples to illustrate the application of the `datetime` module. The `datetime` module is a powerful tool for handling dates and times in Python.

For more tutorials and in-depth explanations, visit [codeswithpankaj.com](https://codeswithpankaj.com)!

***

This tutorial provides a comprehensive overview of Python's `datetime` module, detailing each topic and subtopic with examples and explanations. For more such tutorials, keep following [codeswithpankaj.com](https://codeswithpankaj.com)!
