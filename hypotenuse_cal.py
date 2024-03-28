"""
Write a Python program to calculate the hypotenuse of a right-angled triangle.
"""
import math

# Using Pythagoras Theorem: a^2 + b^2 = c^2 where c will be hypotenuse

a = int(input("Enter a: "))
b = int(input("Enter b: "))

c = math.sqrt(a ** 2 + b ** 2)
print(f"The length of hypotenuse is {c}")