"""
Write a  Python program to sort three integers without using conditional statements and loops.
"""

a = 10
b = 5
c = 8

maximum = max(a, b, c)
minimum = min(a, b, c)
middle = (a + b + c) - maximum - minimum

print(f"maximum: {maximum}, minimum: {minimum}, middle: {middle}")