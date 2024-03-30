"""
Write a Python program that accepts an integer and
determines whether it is greater than 4^4 and which is 4 mod 34.
"""

n = int(input("Enter n: "))

if (n > 4 ** 4) and (n % 34 == 4):
    print(True)
else:
    print(False)