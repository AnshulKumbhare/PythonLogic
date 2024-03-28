"""
Write a Python program to filter positive numbers from a list.
"""

li = [10, -2, 3, 5, -4, -5, 8, -9]

pos_l = list(filter(lambda i: i > 0, li))
print(pos_l)