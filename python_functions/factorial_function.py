"""
Write a Python function to calculate the factorial of a number (a non-negative integer).
The function accepts the number as an argument.
"""

n = int(input("Enter n: "))

def factorial_func(n):
    if n == 1:
        return 1
    else:
        return n * factorial_func(n - 1)

print(factorial_func(n))