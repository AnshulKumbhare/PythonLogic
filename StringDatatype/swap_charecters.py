"""
Write a Python program to get a single string from two given strings,
separated by a space and swap the first two characters of each string.
"""

s1 = input("Enter s1: ")
s2 = input("Enter s2: ")

new_s = s1.replace(s1[0:2:], s2[0:2:]) + " " + s2.replace(s2[0:2:], s1[0:2:])
print(new_s)