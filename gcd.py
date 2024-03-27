"""
Write a Python program that computes the greatest common divisor (GCD) of two positive integers.
"""

import math

# Method 1
a = int(input("Enter a: "))
b = int(input("Enter b: "))

ans = math.gcd(a, b)
print(ans)

# Method 2

min_ab = min(a, b)
y = a * b

greatest_gcd = 0
for i in range(1, min_ab + 1):
    if (a % i == 0) & (b % i == 0):
        if i > greatest_gcd:
            greatest_gcd = i


print(greatest_gcd)

