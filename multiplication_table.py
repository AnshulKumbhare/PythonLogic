"""
Write a Python program to create the multiplication table (from 1 to 10) of a number.
"""

n = int(input("Enter n: "))

for i in range(1, 11):
    m = n * i
    print("{} * {} = {}".format(n, i, m))