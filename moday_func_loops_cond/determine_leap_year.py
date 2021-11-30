"""
Problem: Determining Leap Year

The following program checks whether a year is a leap year.
A year is a leap year if:
it is divisible by 4
but not by 100, or
it is divisible by 400.

(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
"""

year = int(input("enter a year: \n"))

is_leap_year = ("leap year" if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else "not a leap year")
print(is_leap_year)