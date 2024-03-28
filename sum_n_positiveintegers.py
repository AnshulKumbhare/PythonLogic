"""
Write a Python program to sum the first n positive integers.
"""

n = int(input("Enter n: "))

s = 0
for i in range(n, 0, -1):
    s += i

print(s)