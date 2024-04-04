"""
Write a Python program to count the number of characters (character frequency) in a string.
"""

s = input("Enter s: ")

d = {}
for i in s:
    if i not in d.keys():
        c = s.count(i)
        d.update([(i, c)])

print(d)