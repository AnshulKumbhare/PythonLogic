"""
Write a python program to get the volume of sphere with radius.
"""
import math

# volume of sphere fomula = 4 / 3 *  3.14 ** 3

r = float(input("Enter radius: "))
volume = 4 / 3 * math.pi * r ** 3

print(f"Volume of sphere with radius {r} is {volume}.")