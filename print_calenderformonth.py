"""
Write a Python program that prints the calendar for a given month and year.
"""

import calendar

month = int(input("Enter month: "))
year = int(input("Enter year: "))

if (month >= 1 and month <= 12):
    n = calendar.month(year, month)
    print(n)
else:
    print("invalid month")

