"""
Write a Python program that prompts the user to input an integer and raises a ValueError exception
if the input is not a valid integer.
"""

try:
    n = int(input("Enter n: "))
    m = int(input("Enter m: "))
    print(n, m)
except ValueError:
    print("Value Error")