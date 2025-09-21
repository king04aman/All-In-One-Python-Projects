import time
from calendar import isleap

# Check if a year is a leap year
def judge_leap(year: int) -> bool:
    return isleap(year)

# Return number of days in a month, considering leap years
def month_days(month: int, leap_year: bool) -> int:
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2 and leap_year:
        return 29
    else:
        return 28

# User input
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

localtime = time.localtime(time.time())

year = int(age)
month = year * 12 + localtime.tm_mon
day = 0

begin_year = int(localtime.tm_year) - year
end_year = begin_year + year

# Count days in past years
for y in range(begin_year, end_year):
    if judge_leap(y):
        day += 366
    else:
        day += 365

# Add days from current year
leap_year = judge_leap(localtime.tm_year)
for m in range(1, localtime.tm_mon):
    day += month_days(m, leap_year)

# Approximate breakdown (ignores time of day)
hours = day * 24
minutes = hours * 60
seconds = minutes * 60

print(f"\nHello {name}, you are approximately:")
print(f"  {day:,} days")
print(f"  {hours:,} hours")
print(f"  {minutes:,} minutes")
print(f"  {seconds:,} seconds old!")
