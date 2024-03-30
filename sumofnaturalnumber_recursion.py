"""
Finding sum of n natural numbers using recursion
"""

n = int(input("Enter n: "))

def sum_of_n(n):
    if n == 1:
        return 1
    else:
        return n + sum_of_n(n - 1)

print(sum_of_n(n))