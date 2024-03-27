"""
Write a Python program to find the least common multiple (LCM) of two positive integers.
"""

# method 1

import math

a = int(input("Enter a: "))
b = int(input("Enter b: "))

l_cm = math.lcm(a, b)
print(l_cm)

# method 2

y = a * b

for i in range(1, y + 1):
    if (i % a == 0) & (i % b == 0):
        print(i)
        break