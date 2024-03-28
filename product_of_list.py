"""
Write a Python program to compute the product of a list of integers (without using a for loop).
"""
import functools

l = [1, 2, 5, 10, 15, 4]

prod_l = functools.reduce(lambda x, y: x * y, l)
print(prod_l)