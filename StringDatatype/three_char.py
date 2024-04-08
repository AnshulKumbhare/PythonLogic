"""
Write a Python function to get a string made of the first three characters of a specified string.
If the length of the string is less than 3, return the original string.
Sample function and result :
first_three('ipy') -> ipy
first_three('python') -> pyt
"""

s = input("Enter s: ")


def first_three(s):
    if len(s) < 3:
        return s
    else:
        return s[0:3:]

print(first_three(s))