"""
Write a Python program to remove the nth index character from a nonempty string.
"""

s = input("Enter s: ")
index = int(input("Enter the character index you want to remove: "))

if index < len(s):
    c = s[index]
    s = s.replace(c, "")
    print(s)
else:
    print("Index out of Bounds")