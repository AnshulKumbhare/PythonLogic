"""
Write a Python program to count the occurrences of each word in a given sentence.
"""

s = input("Enter s: ")
l = s.split(" ")
d= {}

for i in l:
    if i not in d.keys():
        d.update([(i, l.count(i))])

print(d)