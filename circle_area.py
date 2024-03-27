"""
Write a Python program that calculates the area of a circle based on the radius entered by the user.
"""
import math as m

r = float(input("Enter radius: "))

area = m.pi * r ** 2
print(f" Area of Circle is {area}")