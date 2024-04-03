"""
Write a Python program to convert a month name to a number of days.
Expected Output:

List of months: January, February, March, April, May, June, July, August, September, October, November,
December
Input the name of Month: February
No. of days: 28/29 days
"""

s = input("Enter month: ")
month_name = s.lower()
if month_name in ["january", "march", "may", "july", "August", "October", "December"]:
    print("Number of days: 31 days")
elif month_name == "february":
    print("Number of days: 28/29 days")
else:
    print("Number of days: 30 days")