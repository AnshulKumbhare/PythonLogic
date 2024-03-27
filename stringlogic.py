"""
Write a Python program to get a newly-generated string from a given string where "Is" has
been added to the front. Return the string unchanged if the given string already begins with "Is".
"""

s = input("Enter a string: ")

is_contains = "Is"

if s[:2].count(is_contains):
    print(s)
else:
    s = "Is " + s
    print(s)

