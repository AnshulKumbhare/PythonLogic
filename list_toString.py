"""
Write a Python program that concatenates all elements in a list into a string and returns it.
"""

l = [2, 5, 'a', "Jack", 3.2, 8.695]

s = ""
for i in l:
    s += str(i)

print(s)