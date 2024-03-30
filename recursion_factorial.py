"""
finding factorial of a number using recursion
"""

n = int(input("Enter n: "))

def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)

print(factorial(n))