"""
Write a python program to display the current date and time
"""

import datetime as d

cur_datetime = d.datetime.now()
print(cur_datetime.strftime("%Y/%M/%D  %H:%M:%S"))
