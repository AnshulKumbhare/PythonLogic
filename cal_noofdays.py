"""
Write a Python program to calculate the number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
"""

import datetime

d1 = datetime.date(2014, 7, 2)
d2 = datetime.date(2014, 7, 11)

d = d2 - d1
print(d.days)