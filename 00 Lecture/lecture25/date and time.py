# Python Date and Time

import datetime

# 1. Current Date and Time
now = datetime.datetime.now()
print(now)

# 2. Current Date
today = datetime.date.today()
print(today)

# 3. Current Time
current_time = datetime.datetime.now().time()
print(current_time)

# 4. Create Specific Date
my_date = datetime.date(2026, 11, 13)
print(my_date)

# 5. Create Specific Time
my_time = datetime.time(10, 30, 45)
print(my_time)

# 6. Create Date and Time
my_datetime = datetime.datetime(2026, 11, 13, 10, 30, 45)
print(my_datetime)

# 7. Extract Year, Month and Day
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)

# 8. Extract Hour, Minute and Second
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)

# 9. Format Date Using strftime()
print(now.strftime("%d-%m-%Y"))
print(now.strftime("%d/%m/%Y"))
print(now.strftime("%B %d, %Y"))

# 10. Format Time
print(now.strftime("%H:%M:%S"))
print(now.strftime("%I:%M:%S %p"))

# 11. Day Name
print(now.strftime("%A"))

# 12. Month Name
print(now.strftime("%B"))

# 13. Weekday
print(today.weekday())

# 14. ISO Weekday
print(today.isoweekday())

# 15. Add Days
new_date = today + datetime.timedelta(days=10)
print(new_date)

# 16. Subtract Days
previous_date = today - datetime.timedelta(days=5)
print(previous_date)

# 17. Add Hours
new_time = now + datetime.timedelta(hours=5)
print(new_time)

# 18. Date Difference
date1 = datetime.date(2026, 11, 13)
date2 = datetime.date(2026, 12, 25)

difference = date2 - date1
print("Difference:", difference.days, "Days")

# 19. Check Leap Year
year = 2024

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

# 20. Convert String into Date
date_string = "13-11-2026"

converted_date = datetime.datetime.strptime(
    date_string, "%d-%m-%Y"
)

print(converted_date)

# 21. Timestamp
timestamp = now.timestamp()
print(timestamp)

# 22. Convert Timestamp into Date
converted = datetime.datetime.fromtimestamp(timestamp)
print(converted)

# 23. Compare Two Dates
date1 = datetime.date(2026, 11, 13)
date2 = datetime.date(2026, 12, 25)

if date1 < date2:
    print("Date1 is Earlier")
else:
    print("Date2 is Earlier")

# 24. Min and Max Date
dates = [
    datetime.date(2026, 11, 13),
    datetime.date(2026, 12, 25),
    datetime.date(2026, 10, 15)
]

print("Minimum Date:", min(dates))
print("Maximum Date:", max(dates))