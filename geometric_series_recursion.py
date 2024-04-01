"""
Write a Python program to calculate the geometric sum up to 'n' terms.
"""

n = int(input("Enter n: "))

def geometricseries_recursion(n):
    if n == 0:
        return 1 * 2 ** n
    else:
        return 1 / 2 ** n + geometricseries_recursion(n - 1)

print(geometricseries_recursion(n))