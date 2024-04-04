"""
Write a Python program to change a given string to a new string where the first and
last chars have been exchanged.
"""

s = input("Enter s: ")

temp = s[0]
s = s.replace(s[0], s[-1])
t = s[-1]
s = t + s[1::].replace(s[-1], temp)

print(s)