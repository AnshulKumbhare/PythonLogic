"""
Binary to Decimal
"""
import math

b = input("Enter binary format: ")

p = len(b) - 1
d = 0

for i in b:
    d += int(math.pow(2, p) * int(i))
    p -= 1

print(d)