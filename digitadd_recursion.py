"""
Write a Python program to get the sum of a non-negative integer using recursion.
Test Data:
sumDigits(345) -> 12
sumDigits(45) -> 9
"""

n = int(input("Enter n: "))

if n > 0:
    def digit_add(n):
        if n < 10:
            return n
        else:
            r = n % 10
            return r + digit_add(n//10)

    print(digit_add(n))
else:
    print(f"{n} is negative integer.")

